import unittest
from unittest.mock import patch
from client.client import start_client

class ClientTests(unittest.TestCase):
    @patch('builtins.input', return_value='hello')
    @patch('builtins.print')
    @patch('socket.socket')
    def test_start_client(self, mock_socket, mock_print, mock_input):
        # Mock the socket and server response
        mock_recv = mock_socket.return_value.recv
        mock_recv.return_value = b'Hello, client!'

        # Test for valid request 'hello'
        start_client()

        # Verify the expected server response is printed
        mock_print.assert_called_with('Server response:', 'Hello, client!')

    @patch('builtins.input', return_value='invalid')
    @patch('builtins.print')
    @patch('socket.socket')
    def test_start_client_invalid(self, mock_socket, mock_print, mock_input):
        # Mock the socket and server response
        mock_recv = mock_socket.return_value.recv
        mock_recv.return_value = b'Invalid request'

        # Test for invalid request
        start_client()

        # Verify the expected server response is printed
        mock_print.assert_called_with('Server response:', 'Invalid request')

if __name__ == '__main__':
    unittest.main()
