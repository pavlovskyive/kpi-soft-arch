import unittest
from unittest.mock import patch

from p2p import Peer


class PeerTests(unittest.TestCase):
    def test_send_message(self):
        peer1 = Peer(name="Peer1")
        peer2 = Peer(name="Peer2")

        with patch('builtins.print') as mock_print:
            peer1.send_message("Hello peer2!")

        mock_print.assert_called_with("Peer1 sent message: Hello peer2!")

    def test_receive_message(self):
        peer1 = Peer(name="Peer1")
        peer2 = Peer(name="Peer2")

        with patch('builtins.print') as mock_print:
            peer2.receive_message("Hi peer1!")

        mock_print.assert_called_with("Peer2 received message: Hi peer1!")


if __name__ == '__main__':
    unittest.main()
