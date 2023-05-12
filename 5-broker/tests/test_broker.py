import unittest
from unittest.mock import patch
from broker import Broker, Subscriber


class BrokerTests(unittest.TestCase):
    def test_publish_with_subscribers(self):
        broker = Broker()

        # Create subscribers
        subscriber1 = Subscriber(name="subscriber1")
        subscriber2 = Subscriber(name="subscriber2")

        # Subscribe subscribers to topics
        broker.subscribe('topic1', subscriber1)
        broker.subscribe('topic2', subscriber2)
        broker.subscribe('topic2', subscriber1)

        # Publish messages to topics
        broker.publish('topic1', 'Message for topic 1')
        broker.publish('topic2', 'Message for topic 2')

        # Check if the subscribers received the messages
        self.assertEqual(subscriber1.received_messages, ['Message for topic 1', 'Message for topic 2'])
        self.assertEqual(subscriber2.received_messages, ['Message for topic 2'])

    def test_unsubscribe(self):
        broker = Broker()

        # Create subscribers
        subscriber1 = Subscriber(name="subscriber1")
        subscriber2 = Subscriber(name="subscriber2")

        # Subscribe subscribers to topics
        broker.subscribe('topic1', subscriber1)
        broker.subscribe('topic2', subscriber2)
        broker.subscribe('topic2', subscriber1)

        # Unsubscribe a subscriber
        broker.unsubscribe('topic2', subscriber1)

        # Publish a message to the topic
        broker.publish('topic2', 'Another message for topic 2')

        # Check if the unsubscribed subscriber did not receive the message
        self.assertEqual(subscriber1.received_messages, [])
        self.assertEqual(subscriber2.received_messages, ['Another message for topic 2'])


if __name__ == '__main__':
    unittest.main()
