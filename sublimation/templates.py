"""
Template object construction.
"""

import sys
from json import dumps, loads

PARAMETERS_FIELD = 'Parameters'
MAPPINGS_FILED = 'Mappings'
RESOURCES_FIELD = 'Resources'
OUTPUTS_FIELD = 'Outputs'


class Template(object):
    def __init__(self, data):
        self.data = data

    def parameter(self, parameter):
        self.data[PARAMETERS_FIELD] = self.data.get(PARAMETERS_FIELD, dict())
        self.data[PARAMETERS_FIELD].update(parameter)
        return self

    def mapping(self, mapping):
        self.data[MAPPINGS_FILED] = self.data.get(MAPPINGS_FILED, dict())
        self.data[MAPPINGS_FILED].update(mapping)
        return self

    def resource(self, resource):
        self.data[RESOURCES_FIELD] = self.data.get(RESOURCES_FIELD, dict())
        self.data[RESOURCES_FIELD].update(resource)
        return self

    def output(self, output):
        self.data[OUTPUTS_FIELD] = self.data.get(OUTPUTS_FIELD, dict())
        self.data[OUTPUTS_FIELD].update(output)
        return self

    def value(self, location, value):
        d = self.data
        while len(location) > 1:
            d = d[location[0]]
            location = location[1:]
        d[location[0]] = value
        return self

    def print_stdout(self):
        """Prints a template as JSON to std out"""

        sys.stdout.write(dumps(self.data, indent=4) + '\n')


def load_template(data=None, path=None):
    if data is not None:
        return Template(data)
    elif path is not None:
        with open(path, 'r') as cf_template:
            data = loads(cf_template.read())
        return Template(data)
    else:
        return Template(dict())


def template(description, version='2010-09-09'):
    return load_template(data={
        'Description': description,
        'AWSTemplateFormatVersion': version,
    })
