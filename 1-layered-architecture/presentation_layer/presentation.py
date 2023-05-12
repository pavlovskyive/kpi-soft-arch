import sys
from os.path import dirname, abspath

# Add the project root directory to the Python path
project_dir = dirname(dirname(abspath(__file__)))
sys.path.append(project_dir)

from business_logic_layer.business_logic import BusinessLogicLayer


class PresentationLayer:
    def __init__(self):
        self.business_logic = BusinessLogicLayer()

    def run(self):
        while True:
            user_input = input("Enter a number: ")
            if user_input == 'exit':
                break

            result = self.business_logic.square_number(int(user_input))
            print(f"The square of {user_input} is {result}.")


if __name__ == "__main__":
    presentation = PresentationLayer()
    presentation.run()