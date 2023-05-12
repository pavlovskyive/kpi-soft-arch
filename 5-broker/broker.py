class Subscriber:
    def __init__(self, name):
        self.name = name
        self.received_messages = []

    def receive(self, message):
        self.received_messages.append(message)


class Broker:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, topic, subscriber):
        if topic not in self.subscribers:
            self.subscribers[topic] = []
        self.subscribers[topic].append(subscriber)

    def unsubscribe(self, topic, subscriber):
        if topic in self.subscribers:
            self.subscribers[topic].remove(subscriber)

    def publish(self, topic, message):
        if topic in self.subscribers:
            for subscriber in self.subscribers[topic]:
                subscriber.receive(message)


if __name__ == '__main__':
    # Create a broker instance
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

    # Unsubscribe a subscriber
    broker.unsubscribe('topic2', subscriber1)

    # Publish another message
    broker.publish('topic2', 'Another message for topic 2')

    # Check messages
    print('subscriber1 messages', subscriber1.received_messages)
    print('subscriber2 messages', subscriber2.received_messages)
