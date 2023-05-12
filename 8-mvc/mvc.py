import time

# Model
class Model:
    def __init__(self):
        self.data = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data


# View
class View:
    def get_user_input(self):
        return input("Enter data (or 'q' to quit): ")

    def display_data(self, data):
        print("Displaying data:", data)


# Controller
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def update_data(self, user_input):
        if user_input.lower() == 'q':
            return False
        self.model.set_data(user_input)
        self.view.display_data(self.model.get_data())
        return True


# Main program
if __name__ == '__main__':
    # Create instances of the Model, View, and Controller
    model = Model()
    view = View()
    controller = Controller(model, view)

    # Event loop
    running = True
    while running:
        user_input = view.get_user_input()
        running = controller.update_data(user_input)
        time.sleep(1)  # Delay between iterations for better user experience
