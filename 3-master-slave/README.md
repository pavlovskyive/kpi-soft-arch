# Master-Slave Pattern

This repository demonstrates a simple implementation of the Master-Slave pattern in Python. The Master-Slave pattern involves a master component that delegates tasks to one or more slave components, which perform the assigned tasks and return the results to the master.

## Getting Started

To use the Master-Slave pattern in your project, follow these steps:

1. Import the `Master` class from master.py and the `Slave` class from `slave.py` into your project.
2. Create an instance of the `Master` class and configure the tasks to be processed.
3. Start the master by calling the `process` method, which delegates the tasks to the individual slaves for processing.
4. Retrieve the results from the master once the processing is complete.

## Example Usage

Here's an example usage of the Master-Slave pattern:

```python

from master import Master

# Create a master instance
master = Master()

# Configure the tasks to be processed
tasks = ["Task 1", "Task 2", "Task 3"]

# Process the tasks using the master
results = master.process(tasks)

# Print the results
for result in results:
    print(result)

# Example output:
# Processed Task 1
# Processed Task 2
# Processed Task 3
```

In this example, we create a `Master` instance and configure the tasks to be processed. We then call the `process` method on the master, which delegates the tasks to individual slaves for processing. The results are collected and returned as a list, which we can then iterate over and process further as needed.

## Running tests

```bash
sudo chmod +x ./run_tests.sh
./run_tests.sh
```

## Conclusion

The Master-Slave pattern is a useful approach for distributing computational tasks and achieving parallel processing. By delegating tasks to individual slaves, the master can efficiently manage the workload and collect the results. This repository provides a basic implementation of the Master-Slave pattern in Python, which can serve as a starting point for more complex distributed computing scenarios.