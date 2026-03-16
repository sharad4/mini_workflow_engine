from engine.task import Task

class StoreTask(Task):

	def run(self):
		print("Storing data into database...")
