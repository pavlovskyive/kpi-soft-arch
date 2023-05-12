from slave import Slave


class Master:
    def process(self, tasks):
        print("Master started.")

        results = []
        for task in tasks:
            # Create a new instance of the Slave class for each task
            slave = Slave()
            result = slave.process_task(task)
            results.append(result)

        print("Master finished.")
        return results
