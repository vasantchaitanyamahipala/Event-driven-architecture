from typing import Dict, Callable, List

# Simulated in-memory event queue
event_queue: List[Dict] = []

# Register event handlers
event_handlers: Dict[str, Callable] = {}

def register_event(event_type: str):
    """Decorator to register an event handler."""
    def wrapper(func: Callable):
        event_handlers[event_type] = func
        return func
    return wrapper

def trigger_event(event_type: str, payload: Dict):
    """Trigger an event and enqueue it."""
    event_queue.append({"type": event_type, "payload": payload})

def process_events():
    """Process events from the queue."""
    while event_queue:
        event = event_queue.pop(0)
        event_type = event["type"]
        payload = event["payload"]

        if event_type in event_handlers:
            event_handlers[event_type](payload)

@register_event("ticket_created")
def handle_ticket_created(payload: Dict):
    print(f"Ticket Created Event Received: {payload}")

@register_event("user_updated")
def handle_user_updated(payload: Dict):
    print(f"User Updated Event Received: {payload}")
