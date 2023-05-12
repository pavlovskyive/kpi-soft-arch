# Pipe-Filter Pattern

The Pipe-Filter pattern is a software design pattern that allows you to process data sequentially through a series of components, known as filters, connected by pipes. Each filter performs a specific transformation or computation on the data, and the pipes facilitate the flow of data between filters.

## Implementation

The implementation of the Pipe-Filter pattern consists of the following elements:

1. **Filter:** A filter is a component that performs a specific operation on the data. It accepts input from the previous filter in the pipeline, processes the data, and produces output that is passed to the next filter. Each filter has a defined interface or contract that specifies the input and output data formats.
2. **Pipe:** A pipe connects filters together and enables the flow of data between them. It serves as a communication channel for passing data from one filter to the next. The pipe ensures that the output of one filter becomes the input of the next filter in the pipeline.
3. **Pipeline:** The pipeline represents the overall structure of connected filters and pipes. It defines the sequence and arrangement of filters to process the data.

## Usage

To use the Pipe-Filter pattern, follow these steps:

1. Define the filters: Create individual filter classes that implement the desired operations or transformations on the data. Each filter should have a `process` method that takes input data and produces output data.
2. reate the pipes: Define pipes to connect the filters together. Pipes can be implemented as simple data structures or objects that facilitate the flow of data between filters.
3. Build the pipeline: Create an instance of the pipeline and connect the filters using the pipes. Specify the order in which the filters should be executed.
4. Process the data: Invoke the pipeline's `process` method, passing the input data. The pipeline will internally handle the data flow between the filters, executing them in the defined order.
5. Retrieve the output: Once the data has been processed by all the filters in the pipeline, retrieve the final output from the pipeline.

## Example

Here's a simple example (`pipe_filter.py`) to illustrate the usage of the Pipe-Filter pattern:

```python
# Implementation of the Pipe-Filter pattern

class Filter:
    def process(self, data):
        raise NotImplementedError("Subclasses must implement the 'process' method.")

class UppercaseFilter(Filter):
    def process(self, data):
        return data.upper()

class ReverseFilter(Filter):
    def process(self, data):
        return data[::-1]

class Pipeline:
    def __init__(self, filters):
        self.filters = filters

    def process(self, data):
        for filter in self.filters:
            data = filter.process(data)
        return data

# Usage example
def main():
    # Create the filters
    uppercase_filter = UppercaseFilter()
    reverse_filter = ReverseFilter()

    # Build the pipeline
    pipeline = Pipeline([uppercase_filter, reverse_filter])

    # Process the data
    data = "Hello, world!"
    result = pipeline.process(data)

    # Print the output
    print("Result:", result)

if __name__ == '__main__':
    main()
```

In this example, we define two filters: `UppercaseFilter`, which converts the input data to uppercase, and `ReverseFilter`, which reverses the input data. We create a Pipeline with these filters and invoke the `process` method to pass the data through the pipeline. The final result is then printed.

By using the Pipe-Filter pattern, we can easily extend and modify the pipeline by adding or removing filters, enabling flexible data processing and transformation pipelines.

## Running tests

```bash
sudo chmod +x ./run_tests.sh
./run_tests.sh
```

## Conclusion

The Pipe-Filter pattern provides a flexible and modular approach to data processing by breaking down complex operations into a series of simple filters connected by pipes.