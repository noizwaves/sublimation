#!/usr/bin/python
"""
Generates a CloudFormation compatible JSON declaration for a particular stack.

Result is written to std out.

Usage: python bash-bootstrapped-ec2.py <bootstrap_script_path.sh>
"""

import os
import sys

from sublimation.s9n import *


# Configuration
description = 'A simple BASH script bootstrapped EBS backed Ubuntu Precise (12.04.2 LTS amd64) EC2 instance. Nothing fancier than that.'
alert_email_address = 'alerts@noizwaves.com'
user_data_script_path = os.path.expanduser(sys.argv[1])

# Load template and transform
Template(description,
         KeyPairParameter(), InstanceTypeParamater(), SecurityGroupParameter(name='WebServerSecurityGroupName'),
         Parameter('WebServerPort', 'WebServer serves via this port', default='8000'),
         InstanceTypeToArch64BitOnlyMapping(), RegionToAmiUbuntu12042Mapping(),
         AutoScalingGroup('WebServerAutoScalingGroup', ref('WebServerLaunchConfig'), get_azs(), '1', '1', '1', [ref('WebServerElasticLoadBalancer')]),
         LaunchConfiguration('WebServerLaunchConfig',
                             find_in_map('AWSRegionArch2AMI', 'AWS::Region', find_in_map('AWSInstanceType2Arch', 'AWSInstanceType2Arch', 'Arch')),
                             ref('InstanceType'),
                             [ref('WebServerSecurityGroupName')],
                             as_joined_base64(load_script(user_data_script_path, keep_if=is_bash_useful))),
         SecurityGroup('WebServerSecurityGroup', 'SSH access to web servers and custom HTTP via ELB', [{
                'IpProtocol': 'tcp',
                'FromPort': ref('WebServerPort'),
                'ToPort': ref('WebServerPort'),
                'SourceSecurityGroupOwnerId': get_attr('WebServerElasticLoadBalancer', 'SourceSecurityGroup.OwnerAlias'),
                'SourceSecurityGroupName': get_attr('WebServerElasticLoadBalancer', 'SourceSecurityGroup.GroupName'),
            }, {
                'IpProtocol': 'tcp',
                'FromPort': '22',
                'ToPort': '22',
                'CidrIp': '0.0.0.0/0'
            }
         ]),
         LoadBalancer('WebServerElasticLoadBalancer', get_azs(), [{
                'LoadBalancerPort': '80',
                'InstancePort': ref('WebServerPort'),
                'Protocol': 'HTTP'
            }],
                      target=join('HTTP:', ref('WebServerPort'), '/healthcheck.html'),
                      healthy_threshold=3, unhealthy_threshold=5, interval=12),
         Distribution('StaticAssetsCloudFrontDistribution', 'Caches static files served through the ELB.', True, [{
                'Id': 'Custom Origin',
                'DomainName': get_attr('WebServerElasticLoadBalancer', 'DNSName'),
                'CustomOriginConfig': {
                    'HTTPPort': '80',
                    'HTTPSPort': '443',
                    'OriginProtocolPolicy': 'http-only'
                }
            }],
                      {
                        'TargetOriginId': 'Custom Origin',
                        'ForwardedValues': {
                            'QueryString': 'false'
                        },
                        'ViewerProtocolPolicy': 'allow-all'
                      }),
         Topic('SendWarningTopic', 'Warning - Web Servers', alert_email_address),
         Topic('SendOkTopic', 'Ok - Web Servers', alert_email_address),
         AutoscaleCpuHighAlarm('CpuHighAlarm', 'WebServerAutoScalingGroup', 'SendWarningTopic', 'SendOkTopic'),
         ElbUrlOutput('WebServerElasticLoadBalancer'),
         CfUrlOutput('StaticAssetsCloudFrontDistribution')
         ).print_stdout()
