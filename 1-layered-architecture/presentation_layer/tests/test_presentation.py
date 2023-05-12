import unittest
from unittest.mock import patch
from io import StringIO

from presentation_layer.presentation import PresentationLayer


class PresentationLayerTests(unittest.TestCase):
    def test_run(self):
        # Mocking user input and capturing the output
        with patch('builtins.input', side_effect=['2', '3', 'exit']):
            output = StringIO()
            with patch('sys.stdout', new=output):
                presentation = PresentationLayer()
                presentation.run()
        
        # Check the output
        self.assertEqual(output.getvalue().strip(), "The square of 2 is 4.\nThe square of 3 is 9.")


if __name__ == "__main__":
    unittest.main()