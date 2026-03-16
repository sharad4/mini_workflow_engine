from engine.dag import DAG
from engine.executor import Executor
from engine.scheduler import Scheduler

from tasks.download_task import DownloadTask
from tasks.clean_task import CleanTask
from tasks.validate_task import ValidateTask
from tasks.store_task import StoreTask


dag = DAG("data_pipeline")

download = DownloadTask("download")
clean = CleanTask("clean")
validate = ValidateTask("validate")
store = StoreTask("store")

clean.depends_on(download)
validate.depends_on(clean)
store.depends_on(validate)

dag.add_task(download)
dag.add_task(clean)
dag.add_task(validate)
dag.add_task(store)

executor = Executor()

scheduler = Scheduler(dag, executor)

scheduler.run()
