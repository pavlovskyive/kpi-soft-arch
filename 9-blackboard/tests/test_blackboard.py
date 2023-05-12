import unittest
from unittest.mock import patch
from blackboard import Blackboard, KnowledgeSource, Monitor


class BlackboardTests(unittest.TestCase):
    def test_add_knowledge(self):
        blackboard = Blackboard()
        blackboard.add_knowledge("Knowledge 1")
        blackboard.add_knowledge("Knowledge 2")
        knowledge = blackboard.get_knowledge()
        self.assertEqual(len(knowledge), 2)
        self.assertIn("Knowledge 1", knowledge)
        self.assertIn("Knowledge 2", knowledge)


class KnowledgeSourceTests(unittest.TestCase):
    def test_update_knowledge(self):
        blackboard = Blackboard()
        knowledge_source = KnowledgeSource(blackboard)
        knowledge_source.update_knowledge("Knowledge 1")
        knowledge_source.update_knowledge("Knowledge 2")
        knowledge = blackboard.get_knowledge()
        self.assertEqual(len(knowledge), 2)
        self.assertIn("Knowledge 1", knowledge)
        self.assertIn("Knowledge 2", knowledge)


class MonitorTests(unittest.TestCase):
    @patch('builtins.print')
    def test_display_knowledge(self, mock_print):
        blackboard = Blackboard()
        monitor = Monitor(blackboard)
        blackboard.add_knowledge("Knowledge 1")
        blackboard.add_knowledge("Knowledge 2")
        monitor.display_knowledge()
        mock_print.assert_called_once_with("Displaying knowledge:", ["Knowledge 1", "Knowledge 2"])


if __name__ == '__main__':
    unittest.main()
