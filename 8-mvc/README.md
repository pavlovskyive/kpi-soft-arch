# Model-View-Controller (MVC) Pattern

The Model-View-Controller (MVC) pattern is a software architectural pattern commonly used in user interface design. It separates the application into three interconnected components: the Model, the View, and the Controller. This pattern promotes separation of concerns and enhances maintainability and reusability of code.

## Implementation

### Model

The Model represents the application's data and business logic. It encapsulates the state of the application and provides methods to manipulate and access the data. In our implementation, the `Model` class is responsible for storing and retrieving the data.

### View

The View is responsible for presenting the data to the user and receiving input from them. It provides a visual representation of the data and interacts with the user. In our implementation, the `View` class handles user input and displays the data.

### Controller

The Controller acts as an intermediary between the Model and the View. It receives input from the user via the View, updates the Model based on the input, and notifies the View to update the display. In our implementation, the `Controller` class manages the interaction between the Model and the View.

### Event Loop

We have introduced an event loop in the main program to create an interactive experience. The event loop continuously prompts the user for input and updates the data based on their responses. It utilizes the Controller to handle the input and updates.

## Usage

To run the program, execute the script in a Python environment:

```bash
python mvc.py
```

The program will prompt you to enter data. Enter any value you like, and it will update and display the data. To quit the program, simply enter 'q'.

## Running tests

```bash
sudo chmod +x ./run_tests.sh
./run_tests.sh
```

## Benefits of MVC

- Separation of concerns: The separation of Model, View, and Controller components enables independent development and maintenance of each component.
- Code reusability: With well-defined interfaces between components, individual components can be reused in different contexts or scenarios.
- Testability: Each component can be tested independently, making it easier to write unit tests and ensure code correctness.
- Scalability: The MVC pattern allows for easier scaling of the application as each component can be modified or extended without affecting others.
