import json
import pygame
from pathlib import Path

def export_radar_data(radar):
    data = {
        "timestamp": pygame.time.get_ticks(),
        "radar": {
            "distance": radar.distance if radar.distance else 0.0,
            "valid": radar.valid
        }
    }
    with open(Path(__file__).parent / "output" / "sensor.json", "w") as f:
        json.dump(data, f)
