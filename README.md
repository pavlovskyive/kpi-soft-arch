## KPI -- Software Architecture Course

This repository contains an implementation of various software architecture patterns in Python. It serves as a practical demonstration of these patterns and their application in building robust and scalable software systems.

## Patterns Implemented

1. [**Layered Architecture Pattern:**](1-layered-architecture/) The codebase follows the Layered Architecture pattern, where the application is divided into layers such as presentation, business logic, and data access. Each layer has a specific responsibility and communicates with adjacent layers through well-defined interfaces.
2. [**Client-Server Pattern:**](2-client-server) The codebase demonstrates the Client-Server pattern, enabling communication and data exchange between clients and a central server.
3. [**Master-Slave Pattern:**](3-master-slave) A pattern where a master component delegates tasks to one or more slave components for parallel processing.
4. [**Pipe-Filter Pattern:**](4-pipe-filter) A pattern, which processes data sequentially through a series of filters connected by pipes, allowing for modular and reusable data transformations.
5. [**Broker Pattern:**](5-broker) A pattern, which involves a central broker acting as an intermediary for communication and coordination between components. It allows publishers to send messages to specific topics and delivers those messages to subscribers interested in those topics.
6. [**Peer-to-Peer Pattern:**](6-peer-to-peer) The codebase demonstrates the Peer-to-Peer pattern, a decentralized communication model where all participants (peers) have the same capabilities and can act both as clients and servers. Peers establish direct connections with each other to exchange data or perform distributed tasks without relying on a central server.
7. [**Event-bus Pattern:**](7-event-bus) The codebase demonstrates the Event-bus pattern, which facilitates communication between components in a decoupled manner through a central event bus. Components can publish events to the event bus, and other components can subscribe to specific event types and handle those events accordingly.
8. [**Model-View-Controller (MVC) Pattern:**](8-mvc) The codebase showcases the Model-View-Controller pattern, a widely used architectural pattern for developing user interfaces. It separates the application into three interconnected components: the Model, the View, and the Controller. This pattern promotes separation of concerns and enhances maintainability and reusability of code.

## Usage

Each pattern implementation resides within its corresponding directory. To run an example or test a pattern, navigate to the respective directory and follow the instructions provided in the `README.md` within that directory.


