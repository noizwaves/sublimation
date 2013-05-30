"""
A shortened namespace for referencing Sublimation Cf wrappers.
"""

__all__ = ['Template',
           'Parameter', 'KeyPairParameter', 'SecurityGroupParameter', 'InstanceTypeParamater',
           'Mapping', 'InstanceTypeToArch64BitOnlyMapping', 'RegionToAmiUbuntu12042Mapping',
           'Resource', 'Topic', 'Instance', 'AutoscaleCpuHighAlarm', 'AutoScalingGroup',
           'LaunchConfiguration', 'SecurityGroup', 'LoadBalancer', 'Distribution',
           'Output', 'ElbUrlOutput', 'CfUrlOutput',
           'find_in_map', 'get_azs', 'get_attr', 'base64', 'join', 'ref', 'as_joined_base64',
           'is_bash_useful', 'load_template', 'load_script']

from ..templates import Template
from ..parameters import Parameter, KeyPairParameter, SecurityGroupParameter, InstanceTypeParamater
from ..mappings import Mapping, InstanceTypeToArch64BitOnlyMapping, RegionToAmiUbuntu12042Mapping
from ..resources import Resource, Topic, Instance, AutoscaleCpuHighAlarm, AutoScalingGroup, LaunchConfiguration
from ..resources import SecurityGroup, LoadBalancer, Distribution
from ..outputs import Output, ElbUrlOutput, CfUrlOutput

from ..helpers import find_in_map, get_azs, get_attr, base64, join, ref, as_joined_base64
from ..loaders import is_bash_useful, load_template, load_script
