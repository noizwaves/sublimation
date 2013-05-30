"""
Useful preset mappings for various things.
"""

from .templates import TemplateNode, MAPPINGS_FILED


class Mapping(TemplateNode):
    belongs_in = MAPPINGS_FILED

    def __init__(self, name, mapping):
        self.data = {
            name: mapping,
        }


class InstanceTypeToArch64BitOnlyMapping(Mapping):
    """Use only 64 bit architectures for all instance types"""

    def __init__(self):
        mapping = {
            't1.micro': {'Arch': '64'},
            'm1.small': {'Arch': '64'},
            'm1.medium': {'Arch': '64'},
            'm1.large': {'Arch': '64'},
            'm1.xlarge': {'Arch': '64'},
            'm2.xlarge': {'Arch': '64'},
            'm2.2xlarge': {'Arch': '64'},
            'm2.4xlarge': {'Arch': '64'},
            'm3.xlarge': {'Arch': '64'},
            'm3.2xlarge': {'Arch': '64'},
            'c1.medium': {'Arch': '64'},
            'c1.xlarge': {'Arch': '64'},
            'cc1.4xlarge': {'Arch': '64'},
            'cc2.8xlarge': {'Arch': '64'},
            'cg1.4xlarge': {'Arch': '64'},
        }

        super(InstanceTypeToArch64BitOnlyMapping, self).__init__('AWSInstanceType2Arch', mapping)


class RegionToAmiUbuntu12042Mapping(Mapping):
    """Use Ubuntu 12.04.2 in all regions"""

    def __init__(self):
        mapping = {
            'us-east-1': {'64': 'ami-79c0ae10'},
            'us-west-2': {'64': 'ami-773caa47'},
            'us-west-1': {'64': 'ami-69b59a2c'},
            'eu-west-1': {'64': 'ami-7b62730f'},
            'ap-southeast-1': {'64': 'ami-e40846b6'},
            'ap-southeast-2': {'64': 'ami-b30e9e89'},
            'ap-northeast-1': {'64': 'ami-7d43cd7c'},
            'sa-east-1': {'64': 'ami-0c76ac11'},
        }

        super(RegionToAmiUbuntu12042Mapping, self).__init__('AWSRegionArch2AMI', mapping)
