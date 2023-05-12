import unittest

from business_logic_layer.business_logic import BusinessLogicLayer


class BusinessLogicLayerTests(unittest.TestCase):
    def setUp(self):
        self.business_logic = BusinessLogicLayer()

    def test_square_number(self):
        result = self.business_logic.square_number(5)
        self.assertEqual(result, 25)


if __name__ == "__main__":
    unittest.main()