# Inventory Management System

## Overview
This Inventory Management System is designed for a hypothetical scenario as part of an assignment task. The system manages the production, stocking, and handling of items using robots in a warehouse scenario. It demonstrates the use of threading for concurrent operations and ensures thread safety for shared resources.

## Components

### 1. `main.py`
- **Description**: Entry point for the program.
- **Functionality**:
  - Contains the main logic for production, stocking, and task assignment to robots.
  - Orchestrates the overall system behavior.
  
### 2. `production.py`
- **Description**: Defines the `Production` class responsible for tracking produced and remaining items.
- **Functionality**:
  - Keeps track of the number of items produced.
  - Calculates the remaining items to be processed.

### 3. `robot.py`
- **Description**: Defines the `Robot` class responsible for picking up and transferring items.
- **Functionality**:
  - Manages robot actions such as item pickup and transfer.
  - Ensures efficient movement within the warehouse.

### 4. `container.py`
- **Description**: Defines the `Container` class responsible for managing the container's capacity and current items.
- **Functionality**:
  - Tracks the capacity of each container.
  - Manages the items stored in the container.

## How to Use

1. Run `main.py` to start the system.
2. Input the following parameters:
   - Number of items to produce.
   - Capacity of the container.
3. Example inputs:
   - Produce 35 items.
   - Container capacity: 8.
4. The system will calculate the number of containers required and initiate production and stocking.
5. Robots will pick up and transfer items until all items are processed.
6. At the end, summary of the task will be printed. 


## Purpose
This project serves as an example of using thread pools and ensuring thread safety in a concurrent programming scenario. It is intended to demonstrate the ability to design and implement a multithreaded system with proper synchronization mechanisms.