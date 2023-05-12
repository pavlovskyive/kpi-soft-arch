# Layered Architecture Pattern

The Layered Architecture pattern promotes modularization and separation of concerns in software applications. It organizes the codebase into distinct layers, each with a specific responsibility and clear interfaces for communication. This pattern improves maintainability, scalability, and testability of the application.

## Implementation Details

This implementation of the Layered Architecture pattern consists of three layers:

1. **Presentation Layer:** Handles user interaction and input/output presentation. It communicates with the business logic layer.
2. **Business Logic Layer:** Contains the core logic and rules of the application. It processes requests from the presentation layer and interacts with the data access layer.
3. **Data Access Layer:** Provides data access and manipulation. It interacts with data storage or external systems.

## Key Benefits

- **Separation of Concerns:** Each layer focuses on specific functionalities, improving code organization and understanding.
- **Modularity:** The layers can be developed or replaced independently, promoting reusability and flexibility.
- **Testability:** The layer boundaries enable independent testing, enhancing the quality and reliability of the application.
- **Scalability:** Additional layers can be added to accommodate changing requirements without affecting other layers.

## Example Application

The current implementation demonstrates a simple application where the presentation layer takes user input, passes it to the business logic layer, and displays the result. The business logic layer performs the requested operations and communicates with the data access layer for data retrieval.

## Usage

To run the application, execute `python3 ./presentation_layer/presentation.py` from the command line, while in `1-layered-architecture` subfolder. 

Enter a number when prompted, and the application will display the square of that number.

## Running tests

```bash
sudo chmod +x ./run_tests.sh
./run_tests.sh
```

## Conclusion

The Layered Architecture pattern provides a structured approach to software development, ensuring separation of concerns and improving code maintainability, scalability, and testability. The current implementation showcases this pattern with the distinct layers and their respective responsibilities.