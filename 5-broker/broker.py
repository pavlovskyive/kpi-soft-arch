class Broker:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, topic, callback):
        if topic not in self.subscribers:
            self.subscribers[topic] = []
        self.subscribers[topic].append(callback)

    def publish(self, topic, message):
        if topic in self.subscribers:
            for callback in self.subscribers[topic]:
                callback(message)


if __name__ == '__main__':
    # Create an instance of the Broker
    broker = Broker()

    # Define callback functions
    def callback1(message):
        print("Received message in callback 1:", message)

    def callback2(message):
        print("Received message in callback 2:", message)

    # Subscribe callback functions to topics
    broker.subscribe("topic1", callback1)
    broker.subscribe("topic2", callback2)

    # Publish messages on topics
    broker.publish("topic1", "Hello from topic 1")
    broker.publish("topic2", "Hello from topic 2")
