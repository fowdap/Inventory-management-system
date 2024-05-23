from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import math
from production import Production
from robot import Robot
from container import Container


#tasks for the thread pool

# Production and stocking the produced items

def Stocking(total_production, production):
    print("Production has been started")
    while production.total_produced < total_production:
        production.produce()
        production.add_to_stock()
        time.sleep(0.5)
    return "Production and Stocking has been completed"

# pickup and transfer of items by the robots

def task(robot):
    counter = 0
    while True:
        if robot.production.get_total_remaining() > 0:
            time.sleep(0.5)
            robot.pick_up()
            time.sleep(1)
            robot.transferred()
            time.sleep(0.5)
        else:
            time.sleep(1)
            counter += 1
            if counter >= 5:
                print("Nothing to do.")
                return f"{robot.name} completed the task"
            
def main():
    # Input the required no of production and the capacity of a contaniner

    total_production = int(input("Enter the number of items to produce:\n"))
    container_capacity = int(input("Enter the capacity of the container:\n"))
    required_no_of_container = math.ceil(total_production/container_capacity)
    print(f"{required_no_of_container} container will be required.")

    # Classes initialization

    production = Production()
    container = Container(container_capacity)
    robot1 = Robot("Robot1", production, container)
    robot2 = Robot("Robot2", production, container)

    # Use ThreadPoolExecutor to manage the threads

    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = []
        futures.append(executor.submit(Stocking, total_production, production))
        futures.append(executor.submit(task, robot1))
        futures.append(executor.submit(task, robot2))

        for future in as_completed(futures):
            print(future.result())

    # Printing final status
    print("Production completed.")
    print(f"Total produced: {production.total_produced}")
    print(f"Robot1 handled: Item picked: {robot1.items_picked}, Items transferred:{robot1.items_transferred}")
    print(f"Robot2 handled: Item picked: {robot2.items_picked}, Items transferred: {robot2.items_transferred}")
    print(f"Container used: {container.container_number}")


if __name__ == "__main__":
    main()