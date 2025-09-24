# Python script for automation. First argument is the path to the environment.yaml you want to edit. The second argument is the PYTHONPATH you want to set.

from ruamel.yaml import YAML
import sys

environemnt_yaml_path:str  = sys.argv[1]
python_path:str = sys.argv[2] # The python path is the same as the codon_path


yaml = YAML()
yaml.preserve_quotes = True

# load the environment.yaml file
data = None # Not necessary with python scope, but I just like the way it looks more


with open(environemnt_yaml_path, 'r') as fh:
    data = yaml.load(fh)
    data['variables']['PYTHONPATH'] = python_path
    data['variables']['CODON_PATH'] = python_path

with open(environemnt_yaml_path, 'w') as fh:
    data = yaml.dump(data, fh)