class Context:
    def __init__(self, expression):
        self.expression = expression


class Expression:
    def interpret(self, context):
        pass


class NumberExpression(Expression):
    def __init__(self, value):
        self.value = value

    def interpret(self, context):
        return self.value


class AdditionExpression(Expression):
    def __init__(self, left_expression, right_expression):
        self.left_expression = left_expression
        self.right_expression = right_expression

    def interpret(self, context):
        return self.left_expression.interpret(context) + self.right_expression.interpret(context)


if __name__ == '__main__':
    # Prompt the user to enter an arithmetic expression
    expression = input("Enter an arithmetic expression: ")

    # Create the expression tree based on the input
    stack = []
    operators = {"+": AdditionExpression}

    for token in expression.split():
        if token.isdigit():
            stack.append(NumberExpression(int(token)))
        elif token in operators:
            if len(stack) < 2:
                print("Invalid expression: Not enough operands")
                break
            right_expression = stack.pop()
            left_expression = stack.pop()
            operator = operators[token]
            stack.append(operator(left_expression, right_expression))
        else:
            print("Invalid token:", token)
            break
    else:
        # Check if there is exactly one expression left in the stack
        if len(stack) != 1:
            print("Invalid expression: Too many operands")
        else:
            # Interpret the expression tree and display the result
            context = Context(expression)
            result = stack[0].interpret(context)
            print("Result:", result)
