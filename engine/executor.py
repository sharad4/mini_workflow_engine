import time

class Executor:

    def execute(self, task):

        attempts = 0

        while attempts <= task.retries:

            try:

                print(f"Running task: {task.name}")

                task.run()

                print(f"Task finished: {task.name}")

                return True

            except Exception as e:

                attempts += 1

                print(f"Retry {attempts} for {task.name}")

                time.sleep(1)

        print(f"Task failed: {task.name}")

        return False
