"""
Useful preset mappings for various things.
"""

__all__ = ['map_instance_type_to_arch_64bit', 'map_region_to_ami_ubuntu_12_04_2']


def map_instance_type_to_arch_64bit():
    """Use only 64 bit instance types"""

    return {
        'AWSInstanceType2Arch':  {
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
        },
    }


def map_region_to_ami_ubuntu_12_04_2():
    """Use Ubuntu 12.04.2 in all regions"""

    return {
        'AWSRegionArch2AMI': {
            'us-east-1': {'64': 'ami-79c0ae10'},
            'us-west-2': {'64': 'ami-773caa47'},
            'us-west-1': {'64': 'ami-69b59a2c'},
            'eu-west-1': {'64': 'ami-7b62730f'},
            'ap-southeast-1': {'64': 'ami-e40846b6'},
            'ap-southeast-2': {'64': 'ami-b30e9e89'},
            'ap-northeast-1': {'64': 'ami-7d43cd7c'},
            'sa-east-1': {'64': 'ami-0c76ac11'},
        }
    }
