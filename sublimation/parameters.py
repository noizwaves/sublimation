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



def parameter(name, type, description, default=None):
    """
    Creates a new parameter named `name` of type `type` described by `description`.
    """

    output = {
        "Description": description,
        "Type": type,
    }

    if default is not None:
        output['Default'] = default

    return {
        name: output,
    }


def key_pair_existing():
    """
    Parameter named 'KeyName' that references an existing EC2 Key Pair.
    """

    return {
        "KeyName": {
            "Description": "Name of an existing EC2 KeyPair to enable SSH access to the instances",
            "Type": "String",
        }
    }


def security_group_existing(name=None):
    """
    Parameter named `name` (default is 'SecurityGroupName') that references an existing EC2 Security Group.
    """

    name = name if name is not None else 'SecurityGroupName'

    return {
        name: {
            "Description": "Name of an existing EC2 Security Group to include the instance in",
            "Type": "String",
        },
    }


def security_group_new(name=None):
    """
    Parameter named `name` (default is 'SecurityGroupName') used to create a new EC2 Security Group.
    """

    name = name if name is not None else 'SecurityGroupName'

    return {
        name: {
            "Description": "Name of a new EC2 Security Group to create instances in",
            "Type": "String",
        },
    }


def instance_type_any(name=None, description=None):
    """
    Parameter named `name` (default is 'InstanceType') that can be any EC2 instance type.
    """

    name = name if name is not None else 'InstanceType'
    description = description if description is not None else 'The EC2 instance type'

    return {
        name: {
            "Description": description,
            "Type": "String",
            "Default": "m1.small",
            "AllowedValues": [
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
                "cg1.4xlarge"
            ],
            "ConstraintDescription": "Must be a valid EC2 instance type."
        }
    }
