# Interpreter Pattern

The Interpreter pattern is a behavioral design pattern that provides a way to evaluate language grammar or expressions. It defines a representation for grammar rules and uses this representation to interpret and evaluate expressions.

## Concept

The pattern involves several key components:

- Abstract Expression: This is an abstract base class or interface that defines the common methods for interpreting expressions.
- Terminal Expressions: These are concrete implementations of the Abstract Expression that represent the lowest level of the grammar. They handle specific parts of the language and provide the interpretation logic for those parts.
- Non-Terminal Expressions: These are concrete implementations of the Abstract Expression that represent complex expressions composed of one or more subexpressions. They interpret and evaluate the subexpressions based on the grammar rules.
- Context: This represents the context or input in which the expressions are evaluated. It provides any necessary data or state required for the interpretation.

## Usage

In our example implementation, the program prompts the user to enter an arithmetic expression in Reverse Polish Notation (RPN) format. It then evaluates the expression using the Interpreter pattern and displays the result.

To run the program, execute the following command:

```bash
python3 interpreter.py
```

Enter an arithmetic expression in RPN format when prompted. For example, you can enter "`1 2 +`" to perform addition. The program will evaluate the expression and display the result.

## Example

Consider the following example:

```bash
Copy code
Enter an arithmetic expression: 1 2 + 5 +
Result: 8
```

In this example, the expression `"1 2 + 5 +"` is interpreted as adding the numbers 1 and 2, and then 5. The result of the expression is 8.

This example showcases how the Interpreter pattern can be used to evaluate expressions in different formats, such as Reverse Polish Notation.

## Running tests

```bash
sudo chmod +x ./run_tests.sh
./run_tests.sh
```