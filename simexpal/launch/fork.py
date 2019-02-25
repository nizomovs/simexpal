
from . import common

class ForkLauncher(common.Launcher):
	def submit(self, config, run):
		if not common.lock_run(run):
			return
		common.create_run_file(run)

		print("Launching experiment '{}', instance '{}' on local machine".format(
				run.experiment.name, run.instance.filename))
		common.invoke_run(run)

