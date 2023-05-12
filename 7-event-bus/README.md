# Event-bus Pattern

The Event-bus pattern facilitates communication between components in a decoupled manner by introducing a central event bus. Components can publish events to the event bus, and other components can subscribe to specific event types and handle those events accordingly.

## Implementation

The implementation of the Event-bus pattern consists of the following classes:

- `EventBus`: Represents the central event bus that manages event subscriptions and publications.
- `EventSource`: Represents a source or producer of events that can publish events to the event bus.
- `EventListener`: Represents a listener or subscriber of events that can subscribe to specific event types and handle the received events.

## Usage Example

Here's an example that demonstrates the usage of the Event-bus pattern (`event-bus.py`):

```python
from event_bus import EventBus, EventSource, EventListener

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
```

In this example, an `EventBus` instance is created as the central event bus. An `EventSource` instance is used to generate events and publish them to the event bus. `EventListener` instances are created to subscribe to specific event types and handle the received events. The example showcases the flow of generating events, starting and stopping the listeners, and generating events without listeners for that event type.

## Running tests

```bash
sudo chmod +x ./run_tests.sh
./run_tests.sh
```

# Benefits
- Loose coupling: Components communicate through events without directly depending on each other, leading to more modular and decoupled systems.
- Scalability: New components can easily subscribe to existing event types or introduce new event types without impacting the existing components.
- Extensibility: The pattern supports adding new event sources and listeners without modifying the core event bus implementation.
- Flexibility: Components can selectively subscribe to events they are interested in, reducing unnecessary event processing.

By using the Event-bus pattern, you can establish a flexible and scalable communication mechanism between components in your application.