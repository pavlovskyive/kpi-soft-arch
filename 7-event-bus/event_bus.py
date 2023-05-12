class EventBus:
    def __init__(self):
        self.event_handlers = {}

    def subscribe(self, event_type, handler):
        if event_type not in self.event_handlers:
            self.event_handlers[event_type] = []
        self.event_handlers[event_type].append(handler)

    def unsubscribe(self, event_type, handler):
        if event_type in self.event_handlers:
            self.event_handlers[event_type].remove(handler)

    def publish(self, event_type, event_data):
        if event_type in self.event_handlers:
            handlers = self.event_handlers[event_type]
            for handler in handlers:
                handler(event_data)


class EventSource:
    def __init__(self, event_bus):
        self.event_bus = event_bus

    def generate_event(self, event_type, event_data):
        self.event_bus.publish(event_type, event_data)


class EventListener:
    def __init__(self, event_bus, event_type):
        self.event_bus = event_bus
        self.event_type = event_type

    def start_listening(self):
        self.event_bus.subscribe(self.event_type, self.handle_event)

    def stop_listening(self):
        self.event_bus.unsubscribe(self.event_type, self.handle_event)

    def handle_event(self, event_data):
        print(f"Received event of type '{self.event_type}': {event_data}")

if __name__ == '__main__':
        # Create an event bus
    event_bus = EventBus()

    # Create an event source
    event_source = EventSource(event_bus)

    # Create event listeners
    listener1 = EventListener(event_bus, "EventType1")
    listener2 = EventListener(event_bus, "EventType2")

    # Start event listeners
    listener1.start_listening()
    listener2.start_listening()

    # Generate events
    event_source.generate_event("EventType1", "Event 1 Data")
    event_source.generate_event("EventType2", "Event 2 Data")

    # Stop event listeners
    listener1.stop_listening()
    listener2.stop_listening()

    # Generate another event (no listeners for this event type)
    event_source.generate_event("EventType3", "Event 3 Data")
