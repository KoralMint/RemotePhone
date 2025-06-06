from app.client.interactables import volume_controller as vc
import time

from logging import getLogger
logger = getLogger(__name__)

last_time = time.time()

def handle_event(event_type, data):
    global last_time
    current_time = time.time()
    if current_time - last_time > 0.5:
        vc.refresh_volume_controller_if_needed()
    last_time = current_time

    if event_type == "volume_up": # no args
        vc.change_volume(+0.05)
    elif event_type == "volume_down": # no args
        vc.change_volume(-0.05)
    elif event_type == "volume_change": # delta
        vc.change_volume(float(data["delta"])/100)
    elif event_type == "volume_set": # volume
        vc.set_volume(float(data["volume"]))
    else:
        logger.error(f"Unknown volume event: {event_type}")
        return "Unknown"
    
    current_volume = f"{vc.get_volume() * 100:.1f}"
    return current_volume
        