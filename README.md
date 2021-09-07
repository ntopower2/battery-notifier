# battery-service

A python script that periodically checks the battery level and displays a system notification if any of the following conditions is true:
- `battery_level > upper` and `isPluggedIn`
- `battery_level < lower` and `!isPluggedIn`

## Dependencies

Make sure that `psutil`, `plyer` are installed in your system!