<h1>Python API Reference</h1>

!!! important
    Versions prior to 0.9.0 have a very different API. For the documentation of
    the stable version please switch to the
    [stable branch](https://carla.readthedocs.io/en/stable/).

## `carla.Client`

- `Client(host, port, worker_threads=0)`
- `set_timeout(float_seconds)`
- `get_client_version()`
- `get_server_version()`
- `get_world()`

## `carla.World`

- `id`
- `map_name`
- `get_blueprint_library()`
- `get_spectator()`
- `get_weather()`
- `set_weather(weather_parameters)`
- `get_actors()`
- `spawn_actor(blueprint, transform, attach_to=None)`
- `try_spawn_actor(blueprint, transform, attach_to=None)`
- `wait_for_tick(seconds=1.0)`
- `on_tick(callback)`

## `carla.BlueprintLibrary`

- `find(id)`
- `filter(wildcard_pattern)`
- `__getitem__(pos)`
- `__len__()`
- `__iter__()`

## `carla.ActorBlueprint`

- `id`
- `tags`
- `has_tag(tag)`
- `match_tags(wildcard_pattern)`
- `has_attribute(key)`
- `get_attribute(key)`
- `set_attribute(key, value)`
- `__len__()`
- `__iter__()`

## `carla.ActorAttribute`

- `id`
- `type`
- `recommended_values`
- `is_modifiable`
- `as_bool()`
- `as_int()`
- `as_float()`
- `as_str()`
- `as_color()`
- `__eq__(other)`
- `__ne__(other)`
- `__nonzero__()`
- `__bool__()`
- `__int__()`
- `__float__()`
- `__str__()`

## `carla.ActorList`

- `filter(wildcard_pattern)`
- `__getitem__(pos)`
- `__len__()`
- `__iter__()`

## `carla.Actor`

- `id`
- `type_id`
- `semantic_tags`
- `is_alive`
- `get_world()`
- `get_location()`
- `get_transform()`
- `get_velocity()`
- `get_acceleration()`
- `set_location(location)`
- `set_transform(transform)`
- `set_simulate_physics(enabled=True)`
- `destroy()`

## `carla.Vehicle(carla.Actor)`

- `bounding_box`
- `control`
- `apply_control(vehicle_control)`
- `set_autopilot(enabled=True)`

## `carla.TrafficLight(carla.Actor)`

- `state`

## `carla.Sensor(carla.Actor)`

- `is_listening`
- `listen(callback_function)`
- `stop()`

## `carla.SensorData`

- `frame_number`
- `transform`

## `carla.Image(carla.SensorData)`

- `width`
- `height`
- `fov`
- `raw_data`
- `convert(color_converter)`
- `save_to_disk(path, color_converter=None)`
- `__len__()`
- `__iter__()`
- `__getitem__(pos)`
- `__setitem__(pos, color)`

## `carla.LidarMeasurement(carla.SensorData)`

- `horizontal_angle`
- `channels`
- `raw_data`
- `get_point_count(channel)`
- `save_to_disk(path)`
- `__len__()`
- `__iter__()`
- `__getitem__(pos)`
- `__setitem__(pos, location)`

## `carla.CollisionEvent(carla.SensorData)`

- `actor`
- `other_actor`
- `normal_impulse`

## `carla.VehicleControl`

- `throttle`
- `steer`
- `brake`
- `hand_brake`
- `reverse`
- `__eq__(other)`
- `__ne__(other)`

## `carla.WeatherParameters`

- `cloudyness`
- `precipitation`
- `precipitation_deposits`
- `wind_intensity`
- `sun_azimuth_angle`
- `sun_altitude_angle`
- `__eq__(other)`
- `__ne__(other)`

Static presets

- `carla.WeatherParameters.ClearNoon`
- `carla.WeatherParameters.CloudyNoon`
- `carla.WeatherParameters.WetNoon`
- `carla.WeatherParameters.WetCloudyNoon`
- `carla.WeatherParameters.MidRainyNoon`
- `carla.WeatherParameters.HardRainNoon`
- `carla.WeatherParameters.SoftRainNoon`
- `carla.WeatherParameters.ClearSunset`
- `carla.WeatherParameters.CloudySunset`
- `carla.WeatherParameters.WetSunset`
- `carla.WeatherParameters.WetCloudySunset`
- `carla.WeatherParameters.MidRainSunset`
- `carla.WeatherParameters.HardRainSunset`
- `carla.WeatherParameters.SoftRainSunset`

## `carla.Vector3D`

- `x`
- `y`
- `z`
- `__add__(other)`
- `__sub__(other)`
- `__eq__(other)`
- `__ne__(other)`

## `carla.Location`

- `x`
- `y`
- `z`
- `__add__(other)`
- `__sub__(other)`
- `__eq__(other)`
- `__ne__(other)`

## `carla.Rotation`

- `pitch`
- `yaw`
- `roll`
- `__eq__(other)`
- `__ne__(other)`

## `carla.Transform`

- `location`
- `rotation`
- `__eq__(other)`
- `__ne__(other)`

## `carla.Timestamp`

- `frame_count`
- `elapsed_seconds`
- `delta_seconds`
- `platform_timestamp`
- `__eq__(other)`
- `__ne__(other)`

## `carla.Color`

- `r`
- `g`
- `b`
- `a`
- `__eq__(other)`
- `__ne__(other)`

## `carla.ColorConverter`

- `Raw`
- `Depth`
- `LogarithmicDepth`
- `CityScapesPalette`

## `carla.ActorAttributeType`

- `Bool`
- `Int`
- `Float`
- `RGBColor`

## `carla.TrafficLightState`

- `Unknown`
- `Red`
- `Yellow`
- `Green`
