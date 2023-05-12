import unittest
from unittest.mock import patch
from master import Master


class MasterTests(unittest.TestCase):
    @patch('master.Slave')
    def test_process(self, mock_slave):
        mock_slave_instance = mock_slave.return_value
        mock_slave_instance.process_task.side_effect = lambda task: f"Processed {task}"
        tasks = ["Task 1", "Task 2", "Task 3"]

        master = Master()
        results = master.process(tasks)

        expected_results = ["Processed Task 1", "Processed Task 2", "Processed Task 3"]
        self.assertEqual(results, expected_results)
        self.assertEqual(mock_slave_instance.process_task.call_count, 3)


if __name__ == '__main__':
    unittest.main()
