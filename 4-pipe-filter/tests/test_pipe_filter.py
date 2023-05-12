import unittest
from pipe_filter import UppercaseFilter, ReverseFilter, Pipe


class PipeFilterTests(unittest.TestCase):
    def test_uppercase_filter(self):
        filter = UppercaseFilter()
        data = "hello, world!"
        expected_result = "HELLO, WORLD!"
        result = filter.process(data)
        self.assertEqual(result, expected_result)

    def test_reverse_filter(self):
        filter = ReverseFilter()
        data = "hello, world!"
        expected_result = "!dlrow ,olleh"
        result = filter.process(data)
        self.assertEqual(result, expected_result)

    def test_pipe_with_filters(self):
        data = "hello, world!"
        expected_result = "!DLROW ,OLLEH"
        filter1 = UppercaseFilter()
        filter2 = ReverseFilter()
        pipe = Pipe([filter1, filter2])
        result = pipe.process(data)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
