class Scheduler:

    def __init__(self, dag, executor):
        self.dag = dag
        self.executor = executor
        self.completed = set()

    def run(self):

        tasks = self.dag.get_tasks()

        while len(self.completed) < len(tasks):

            for task in tasks:

                if task.name in self.completed:
                    continue

                if all(
                    dep.name in self.completed
                    for dep in task.dependencies
                ):

                    success = self.executor.execute(task)

                    if success:
                        self.completed.add(task.name)
