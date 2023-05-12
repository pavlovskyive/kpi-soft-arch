import unittest
from unittest.mock import patch, MagicMock

from event_bus import EventBus, EventSource, EventListener


class EventBusTests(unittest.TestCase):
    def test_subscribe_and_publish(self):
        event_bus = EventBus()

        # Define event handler
        handler = MagicMock()

        # Subscribe handler to event type
        event_bus.subscribe("EventType", handler)

        # Publish event
        event_bus.publish("EventType", "Event Data")

        # Assert that handler was called
        handler.assert_called_with("Event Data")

    def test_unsubscribe(self):
        event_bus = EventBus()

        # Define event handler
        handler = MagicMock()

        # Subscribe handler to event type
        event_bus.subscribe("EventType", handler)

        # Unsubscribe handler from event type
        event_bus.unsubscribe("EventType", handler)

        # Publish event
        event_bus.publish("EventType", "Event Data")

        # Assert that handler was not called
        handler.assert_not_called()


class EventSourceTests(unittest.TestCase):
    def test_generate_event(self):
        event_bus = EventBus()
        event_source = EventSource(event_bus)

        # Create a mock handler for testing
        mock_handler = MagicMock()

        # Subscribe the mock handler to the event type
        event_bus.subscribe("EventType", mock_handler)

        # Generate event
        event_source.generate_event("EventType", "Event Data")

        # Assert that the mock handler was called with the correct arguments
        mock_handler.assert_called_once_with("Event Data")




class EventListenerTests(unittest.TestCase):
    def test_handle_event(self):
        event_bus = EventBus()
        listener = EventListener(event_bus, "EventType")

        # Create a mock handler for testing
        mock_handler = MagicMock()

        with patch("event_bus.print", mock_handler):
            # Start listening
            listener.start_listening()

            # Publish event
            event_bus.publish("EventType", "Event Data")

            # Assert that event was handled
            mock_handler.assert_called_with("Received event of type 'EventType': Event Data")

            # Stop listening
            listener.stop_listening()

            # Publish another event
            event_bus.publish("EventType", "Another Event Data")

            # Assert that event was not handled again
            mock_handler.assert_called_once()


if __name__ == "__main__":
    unittest.main()
