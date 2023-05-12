from slave import process_task


def start_master():
    tasks = ["Task 1", "Task 2", "Task 3"]
    results = []

    print("Master started.")

    for task in tasks:
        # Delegate task to a slave
        result = process_task(task)
        results.append(result)

    print("Results:", results)
    print("Master finished.")


if __name__ == '__main__':
    start_master()
