# CAN Sensor Simulation (Ceedling Starter)

This project simulates sensor data for an ADAS system and sends it over a virtual CAN interface.

## Project Structure
- `inc/` - Header files
- `src/` - Source files
- `test/` - Unit tests using Ceedling/Unity
- `config/` - CAN configurations

## Test Setup
Run unit tests using Ceedling:
```sh
ceedling test:all
```

## MISRA Integration
Use static analyzers (e.g., Cppcheck or PC-lint Plus) to validate compliance with MISRA C:2012.
