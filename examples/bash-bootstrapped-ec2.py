#!/usr/bin/python
"""
Generates a CloudFormation compatible JSON declaration for a particular stack.

Result is written to std out.

Usage: python bash-bootstrapped-ec2.py <bootstrap_script_path.sh>
"""

import os
import sys

from sublimation.s9n import *


# CF Template configuration
description = 'A simple BASH script bootstrapped EBS backed Ubuntu Precise (12.04.2 LTS amd64) EC2 instance. Nothing fancier than that.'
user_data_script_path = os.path.expanduser(sys.argv[1])

Template(description,
         KeyPairParameter(), SecurityGroupParameter(), InstanceTypeParamater(),
         InstanceTypeToArch64BitOnlyMapping(), RegionToAmiUbuntu12042Mapping(),
         Instance('NewInstance',
                  find_in_map('AWSRegionArch2AMI', ref('AWS::Region'), find_in_map('AWSInstanceType2Arch', ref('InstanceType'), 'Arch')),
                  ref('InstanceType'),
                  ref('KeyName'),
                  [ref('SecurityGroupName')],
                  as_joined_base64(load_script(user_data_script_path, keep_if=is_bash_useful)))
         ).print_stdout()
