"""
Useful parameters.
"""

from .templates import TemplateNode, PARAMETERS_FIELD


class Parameter(TemplateNode):
    belongs_in = PARAMETERS_FIELD

    def __init__(self, name, description, type='String', default=None, allowed_values=None, constraint_description=None):
        self.data = {
            name: {
                'Description': description,
                'Type': type,
            }
        }

        if default is not None:
            self.data[name]['Default'] = default
        if allowed_values is not None:
            self.data[name]['AllowedValues'] = allowed_values
        if constraint_description is not None:
            self.data[name]['ConstraintDescription'] = constraint_description


class KeyPairParameter(Parameter):
    def __init__(self, name=None):
        name = name if name is not None else 'KeyName'
        super(KeyPairParameter, self).__init__(name, 'Name of the EC2 KeyPair to enable SSH access to the instances.')


class SecurityGroupParameter(Parameter):
    def __init__(self, name=None):
        name = name if name is not None else 'SecurityGroupName'
        super(SecurityGroupParameter, self).__init__(name, 'Name of the EC2 Security Group to include the instance in.')


class InstanceTypeParamater(Parameter):
    def __init__(self, name=None, default='m1.small'):
        name = name if name is not None else 'InstanceType'
        all_instance_types = [
            "t1.micro",
            "m1.small",
            "m1.medium",
            "m1.large",
            "m1.xlarge",
            "m2.xlarge",
            "m2.2xlarge",
            "m2.4xlarge",
            "m3.xlarge",
            "m3.2xlarge",
            "c1.medium",
            "c1.xlarge",
            "cc1.4xlarge",
            "cc2.8xlarge",
            "cg1.4xlarge",
        ]

        super(InstanceTypeParamater, self).__init__(name, 'The EC2 instance type',
                                                    default=default,
                                                    allowed_values=all_instance_types,
                                                    constraint_description='Must be a valid EC2 instance type')
