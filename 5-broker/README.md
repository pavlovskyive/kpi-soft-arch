# Broker Pattern

The Broker pattern is a messaging pattern that facilitates communication between components by using a central broker or mediator. Components can subscribe to specific topics of interest and receive messages published to those topics.

##Implementation

The implementation consists of two main components: `Subscriber` and `Broker`. The `Subscriber` class represents the components that can receive messages, while the `Broker` class acts as the central message broker.

The `Subscriber` class has a receive method that stores received messages in a list. The `Broker` class maintains a dictionary of subscribers for each topic. It provides methods to subscribe, unsubscribe, and publish messages to the appropriate subscribers based on the topic.

To showcase the functionality of the Broker pattern, you can run the `broker.py` script. It creates a `Broker` instance, subscribes `Subscriber` objects to topics, publishes messages to topics, and demonstrates the process of subscribing, unsubscribing, and receiving messages.

## Usage
1. Run the `broker.py` script: `python3 broker.py`
2. The script will create a `Broker` instance and perform the following steps:
   - Create subscribers (Subscriber objects) with unique names.
   - Subscribe subscribers to topics of interest using the subscribe method of the Broker.
   - Publish messages to specific topics using the publish method of the Broker.
   - Unsubscribe a subscriber from a topic using the unsubscribe method of the Broker.
   - Check if subscribers receive the messages correctly.

## Running tests

```bash
sudo chmod +x ./run_tests.sh
./run_tests.sh
```

## Conclusion

The Broker pattern provides a flexible and decoupled approach to handle communication and messaging between components. By centralizing the message exchange in a broker, it enables components to subscribe to specific topics of interest and receive relevant messages. This pattern promotes loose coupling, reusability, and scalability in complex systems.