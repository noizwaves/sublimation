"""
Template object construction.
"""

import sys
from json import dumps

PARAMETERS_FIELD = 'Parameters'
MAPPINGS_FILED = 'Mappings'
RESOURCES_FIELD = 'Resources'
OUTPUTS_FIELD = 'Outputs'


class Template(object):
    version = '2010-09-09'

    def __init__(self, description, *nodes):
        self.description = description
        self.nodes = list(nodes)

    def print_stdout(self):
        """Prints a template as JSON to std out"""

        output = {
            'Description': self.description,
            'AWSTemplateFormatVersion': self.version,
        }

        for node in self.nodes:
            output[node.belongs_in] = output.get(node.belongs_in, dict())
            output[node.belongs_in].update(node.data)

        sys.stdout.write(dumps(output, indent=4) + '\n')


class TemplateNode(object):
    belongs_in = None
    data = dict()

    def __init__(self):
        raise NotImplementedError
