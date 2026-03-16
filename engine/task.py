class Task:

	def __init__(self, name, retries=2):
		self.name = name
		self.retries = retries
		self.dependencies = []

	def depends_on(self, task):
		self.dependencies.append(task)


	def run(self):
		raise NotImplementedError
