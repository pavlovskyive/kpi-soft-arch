## KPI -- Software Architecture Course

This repository contains an implementation of various software architecture patterns in Python. It serves as a practical demonstration of these patterns and their application in building robust and scalable software systems.

## Patterns Implemented

1. [**Layered Architecture Pattern:**](1-layered-architecture/) The codebase follows the Layered Architecture pattern, where the application is divided into layers such as presentation, business logic, and data access. Each layer has a specific responsibility and communicates with adjacent layers through well-defined interfaces.
2. [**Client-Server Pattern:**](2-client-server) The codebase demonstrates the Client-Server pattern, enabling communication and data exchange between clients and a central server.
3. [**Master-Slave Pattern:**](3-master-slave) A pattern where a master component delegates tasks to one or more slave components for parallel processing.
4. [**Pipe-Filter Pattern:**](4-pipe-filter) A pattern, which processes data sequentially through a series of filters connected by pipes, allowing for modular and reusable data transformations.
5. [**Broker Pattern:**](5-broker) A pattern, which involves a central broker acting as an intermediary for communication and coordination between components. It allows publishers to send messages to specific topics and delivers those messages to subscribers interested in those topics.

## Usage

Each pattern implementation resides within its corresponding directory. To run an example or test a pattern, navigate to the respective directory and follow the instructions provided in the `README.md` within that directory.


