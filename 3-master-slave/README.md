# Master-Slave Pattern

This repository demonstrates a simple implementation of the Master-Slave pattern in Python. The Master-Slave pattern involves a master component that delegates tasks to one or more slave components, which perform the assigned tasks and return the results to the master.

## Implementation

The implementation consists of two main files: `master.py` and `slave.py`.

## `master.py`

The `master.py` file represents the master component. It contains the `start_master()` function, which is responsible for managing the tasks and coordinating with the slave components. In this example, the master component has a list of tasks and delegates each task to a slave component using the `process_task()` function.

To start the master component, run the following command:

```bash
python3 master.py
```

The master component prints the results received from the slave components and indicates the completion of the process.

## `slave.py`

The `slave.py` file represents the slave component. It contains the `process_task()` function, which takes a task as input, simulates the task processing, and returns the result. In this example, the `process_task()` function simply adds a prefix to the task string to indicate that it has been processed by the slave.

## Usage

1. Run the master component by executing `python3 master.py`.
2. Observe the master component delegating tasks to the slave component and printing the results received.
3. Customize the tasks in the tasks list in `master.py` or modify the task processing logic in `slave.py` to suit your needs.
4. Experiment with different tasks and observe how the master-slave coordination works.
   
## Conclusion

The Master-Slave pattern provides a way to distribute and delegate tasks across multiple components, enabling parallel processing and improving overall system performance. This implementation demonstrates a basic example of the pattern using a master component to delegate tasks to a slave component. You can extend and customize this implementation to suit your specific requirements.