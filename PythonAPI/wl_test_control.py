#!/usr/bin/env python

# Copyright (c) 2017 Computer Vision Center (CVC) at the Universitat Autonoma de
# Barcelona (UAB).
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.


from __future__ import print_function

import sys

sys.path.append(
    'dist\carla-0.9.0-py%d.%d-win-amd64.egg' % (sys.version_info.major,
                                                        sys.version_info.minor))

import carla

import argparse
import logging
import random
import time

try:
    import pygame
    from pygame.locals import K_DOWN
    from pygame.locals import K_LEFT
    from pygame.locals import K_RIGHT
    from pygame.locals import K_SPACE
    from pygame.locals import K_UP
    from pygame.locals import K_a
    from pygame.locals import K_d
    from pygame.locals import K_p
    from pygame.locals import K_q
    from pygame.locals import K_r
    from pygame.locals import K_s
    from pygame.locals import K_w
except ImportError:
    raise RuntimeError('cannot import pygame, make sure pygame package is installed')

try:
    import numpy as np
except ImportError:
    raise RuntimeError('cannot import numpy, make sure numpy package is installed')


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
START_POSITION = carla.Transform(carla.Location(x=180.0, y=199.0, z=40.0))
CAMERA_POSITION = carla.Transform(carla.Location(x=0.5, z=1.40))


class CarlaGame(object):
    def __init__(self, args):
        self._client = carla.Client(args.host, args.port)
        self._client.set_timeout(2.0)
        self._display = None
        self._surface = None
        self._camera = None
        self._vehicle = None

    def execute(self):
        pygame.init()
        try:
            self._display = pygame.display.set_mode(
                (WINDOW_WIDTH, WINDOW_HEIGHT),
                pygame.HWSURFACE | pygame.DOUBLEBUF)
            logging.debug('pygame started')

            world = self._client.get_world()
            blueprint = random.choice(world.get_blueprint_library().filter('vehicle'))
            self._vehicle = world.spawn_actor(blueprint, START_POSITION)
            self._vehicle.set_autopilot(True)
            cam_blueprint = world.get_blueprint_library().find('sensor.camera')
            self._camera = world.spawn_actor(cam_blueprint, CAMERA_POSITION, attach_to=self._vehicle)

            self._camera.listen(self._parse_image)

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return
                self._on_render()
                print(self._vehicle.get_control())
                time.sleep(1)
        finally:
            pygame.quit()
            if self._camera is not None:
                self._camera.destroy()
                self._camera = None
            if self._vehicle is not None:
                self._vehicle.destroy()
                self._vehicle = None

    def _parse_image(self, image):
        array = np.frombuffer(image.raw_data, dtype=np.dtype("uint8"))
        array = np.reshape(array, (image.height, image.width, 4))
        array = array[:, :, :3]
        array = array[:, :, ::-1]
        self._surface = pygame.surfarray.make_surface(array.swapaxes(0, 1))

    def _on_render(self):
        if self._surface is not None:
            self._display.blit(self._surface, (0, 0))
        pygame.display.flip()


def main():
    argparser = argparse.ArgumentParser(
        description='CARLA Test Control Client by Wangli')
    argparser.add_argument(
        '-v', '--verbose',
        action='store_true',
        dest='debug',
        help='print debug information')
    argparser.add_argument(
        '--host',
        metavar='H',
        default='localhost',
        help='IP of the host server (default: localhost)')
    argparser.add_argument(
        '-p', '--port',
        metavar='P',
        default=2000,
        type=int,
        help='TCP port to listen to (default: 2000)')
    
    args = argparser.parse_args()
    
    log_level = logging.DEBUG if args.debug else logging.INFO
    logging.basicConfig(format='%(levelname)s: %(message)s', level=log_level)

    logging.info('listening to server %s:%s', args.host, args.port)

    print(__doc__)

    while True:
        try:

            game = CarlaGame(args)
            game.execute()
            break

        except Exception as error:
            logging.error(error)
            time.sleep(1)


if __name__ == '__main__':

    try:
        main()
    except KeyboardInterrupt:
        print('\nCancelled by user. Bye!')
