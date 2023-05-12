import unittest

from data_access_layer.data_access import DataAccessLayer


class DataAccessLayerTests(unittest.TestCase):
    def setUp(self):
        self.data_access = DataAccessLayer()

    def test_get_square(self):
        result = self.data_access.get_square(4)
        self.assertEqual(result, 16)


if __name__ == "__main__":
    unittest.main()