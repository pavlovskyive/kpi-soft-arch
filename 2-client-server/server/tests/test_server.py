import unittest
from server.server import generate_response

class ServerTests(unittest.TestCase):
    def test_generate_response_hello(self):
        # Test for valid request 'hello'
        request = 'hello'
        expected_response = 'Hello, client!'
        response = generate_response(request)
        self.assertEqual(response, expected_response)

    def test_generate_response_invalid(self):
        # Test for invalid request
        request = 'invalid'
        expected_response = 'Invalid request'
        response = generate_response(request)
        self.assertEqual(response, expected_response)

if __name__ == '__main__':
    unittest.main()
