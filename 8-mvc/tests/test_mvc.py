import unittest
from unittest.mock import MagicMock
from mvc import Model, View, Controller

class ModelTests(unittest.TestCase):
    def test_set_data(self):
        model = Model()
        data = "Hello"
        model.set_data(data)
        self.assertEqual(model.get_data(), data)

class ViewTests(unittest.TestCase):
    def test_display_data(self):
        view = View()
        view_output = MagicMock()
        view.display_data = view_output
        data = "Hello"
        view.display_data(data)
        view_output.assert_called_once_with(data)

class ControllerTests(unittest.TestCase):
    def test_update_data(self):
        model = Model()
        view = View()
        controller = Controller(model, view)
        user_input = "Hello"
        expected_output = "Hello"
        
        view_output = MagicMock()
        view.display_data = view_output
        
        controller.update_data(user_input)
        view_output.assert_called_once_with(expected_output)
        self.assertEqual(model.get_data(), user_input)

if __name__ == '__main__':
    unittest.main()
