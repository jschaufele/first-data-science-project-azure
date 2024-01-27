from azureml.core import Workspace, Experiment, Environment, ScriptRunConfig
from azureml.core.compute import ComputeTarget, AmlCompute
from azureml.core.compute_target import ComputeTargetException

ws = Workspace.from_config()

### START IMPORTANT NOTE###
### THIS CODE IS TO CREATE A CLUSTER FROM THE SDK, IT IS NOT KEY TO THE VIDEO###
cpu_cluster_name = "cpu-cluster"

try:
    cpu_cluster = ComputeTarget(workspace=ws, name=cpu_cluster_name)
    print('Found existing cluster, use it.')
except ComputeTargetException:
    compute_config = AmlCompute.provisioning_configuration(vm_size='STANDARD_D2_V2',
                                                            max_nodes=4, 
                                                            idle_seconds_before_scaledown=2400)
    cpu_cluster = ComputeTarget.create(ws, cpu_cluster_name, compute_config)

cpu_cluster.wait_for_completion(show_output=True)

### END IMPORTANT NOTE###
######

# Create an experiment
experiment = Experiment(ws,name='first-experiment')
# Create a run configuration to run a script
source_directory=""
config = ScriptRunConfig(source_directory==".",script="module3/hello.py",compute_target=cpu_cluster_name)

#Submit the run to the experiment
run = experiment.submit(config)

aml_url = run.get_portal_url()
print(aml_url)