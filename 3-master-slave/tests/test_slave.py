import unittest
from slave import Slave


class SlaveTests(unittest.TestCase):
    def test_process_task(self):
        slave = Slave()
        task = "Test Task"

        result = slave.process_task(task)

        expected_result = f"Task '{task}' processed by slave"
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
