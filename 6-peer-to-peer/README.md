# Peer-to-Peer Pattern

The Peer-to-Peer pattern is a decentralized communication model where all participants (peers) have the same capabilities and can act both as clients and servers. Peers establish direct connections with each other to exchange data or perform distributed tasks without relying on a central server.

## Implementation

The codebase demonstrates the Peer-to-Peer pattern using the `Peer` class. Each instance of the Peer class represents a peer in the network. Peers can connect to each other, send messages, and receive messages.

The `Peer` class provides the following methods:

- `connect(peer)`: Establishes a connection between the current peer and the specified peer.
- `disconnect(peer)`: Terminates the connection between the current peer and the specified peer.
- `send_message(message)`: Sends a message to all connected peers.
- `receive_message(message)`: Receives a message from a connected peer.

## Usage

To use the Peer-to-Peer pattern, create instances of the `Peer` class and establish connections between them. Peers can then send messages to all connected peers, which will receive and process the messages.

Here's an example usage (`p2p.py`):

```python
if __name__ == '__main__':
    # Create peers
    peer1 = Peer(name="Peer 1")
    peer2 = Peer(name="Peer 2")
    peer3 = Peer(name="Peer 3")

    # Establish connections
    peer1.connect(peer2)
    peer1.connect(peer3)

    # Send messages
    peer1.send_message("Hello, everyone!")
    peer2.send_message("Hi, Peer 1!")
    peer3.send_message("Greetings from Peer 3!")

    # Disconnect peers
    peer1.disconnect(peer2)
    peer2.disconnect(peer3)

    # Send another message
    peer1.send_message("Goodbye!")
```
In this example, three peers (`peer1`, `peer2`, `peer3`) are created and connections are established between them. Messages are sent between peers using the `send_message` method. Peers can also be disconnected using the `disconnect` method.

## Running tests

```bash
sudo chmod +x ./run_tests.sh
./run_tests.sh
```

## Advantages

- Decentralization: The Peer-to-Peer pattern eliminates the need for a central server, enabling peers to communicate directly with each other.
- Scalability: The pattern allows for easy scalability as new peers can join the network without affecting the overall architecture.
- Redundancy: The distributed nature of the pattern provides redundancy, as the failure of one peer does not disrupt the entire network.

## Considerations

- Network Topology: The topology of the peer network can affect the performance and efficiency of communication. Various approaches, such as fully connected, overlay networks, or structured/unstructured networks, can be considered based on the specific requirements.