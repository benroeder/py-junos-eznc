from os.path import dirname,join,basename
from .yaml import loadyaml

# import the definitions from the YAML file in this directory and
# make them part of this module, yo!

_yml_file = 'routes.yml'
globals().update( loadyaml(join(dirname(__file__),_yml_file)) )
