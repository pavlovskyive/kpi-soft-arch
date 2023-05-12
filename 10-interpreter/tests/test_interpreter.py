import unittest
from interpreter import *

class InterpreterTests(unittest.TestCase):
    def test_arithmetic_expression(self):
        left_expression = NumberExpression(5)
        right_expression = NumberExpression(3)
        expression = AdditionExpression(left_expression, right_expression)
        context = Context(expression)

        result = expression.interpret(context)

        self.assertEqual(result, 8)

if __name__ == "__main__":
    unittest.main()
