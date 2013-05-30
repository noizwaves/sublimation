"""
A shortened namespace for referencing Sublimation Cf wrappers.
"""

__all__ = ['template', 'parameter', 'key_pair_existing', 'security_group_existing', 'security_group_new',
           'instance_type_any', 'map_instance_type_to_arch_64bit', 'map_region_to_ami_ubuntu_12_04_2', 'resource',
           'topic', 'alert_autoscale_cpu_high', 'output', 'output_elb_url', 'output_cf_url', 'find_in_map',
           'get_azs', 'get_attr', 'base64', 'join', 'ref', 'as_joined_base64', 'is_bash_useful', 'load_template', 'load_script',
           'instance']

from ..templates import template
from ..parameters import parameter, key_pair_existing, security_group_existing, security_group_new, instance_type_any
from ..mappings import map_instance_type_to_arch_64bit, map_region_to_ami_ubuntu_12_04_2
from ..resources import resource, topic, alert_autoscale_cpu_high, instance
from ..outputs import output, output_elb_url, output_cf_url
from ..helpers import find_in_map, get_azs, get_attr, base64, join, ref, as_joined_base64
from ..loaders import is_bash_useful, load_template, load_script
