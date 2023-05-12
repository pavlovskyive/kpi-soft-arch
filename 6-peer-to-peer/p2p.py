class Peer:
    def __init__(self, name):
        self.name = name
        self.peers = []

    def connect(self, peer):
        if peer not in self.peers:
            self.peers.append(peer)
            peer.connect(self)

    def disconnect(self, peer):
        if peer in self.peers:
            self.peers.remove(peer)
            peer.disconnect(self)

    def send_message(self, message):
        print(f"{self.name} sent message: {message}")
        for peer in self.peers:
            peer.receive_message(message)

    def receive_message(self, message):
        print(f"{self.name} received message: {message}")


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