"""
Constructors for various possible resources.
"""

from .helpers import join, ref
from .templates import TemplateNode, RESOURCES_FIELD


class Resource(TemplateNode):
    belongs_in = RESOURCES_FIELD

    def __init__(self, name, cf_type, properties):
        self.data = {
            name: {
                'Type': cf_type,
                'Properties': properties,
            }
        }


def resource(name, cf_type, properties):
    return {
        name: {
            'Type': cf_type,
            'Properties': properties,
        }
    }


def topic(name, display_name, email_address):
    return {
        name: {
            'Type': 'AWS::SNS::Topic',
            'Properties': {
                'DisplayName': display_name,
                'Subscription': [{
                    'Protocol': 'email',
                    'Endpoint': email_address,
                }],
            },
        },
    }


def instance(name, image_id, instance_type, key_name, security_groups, user_data=None):
    properties = {
        'ImageId': image_id,
        'InstanceType': instance_type,
        'KeyName': key_name,
        'SecurityGroups': security_groups,
    }

    if user_data is not None:
        properties['UserData'] = user_data

    return resource(name, 'AWS::EC2::Instance', properties)


def alert_autoscale_cpu_high(name, as_group, alarm_topic, ok_topic):
    """
    Defines a new alert for an AutoScaling group hitting high CPU usage.

    Arguments:
    - as_group: the name of the AutoScaling group
    - alarm_topic: the name of the SNS topic to send alarm message to
    - ok_topic: the name of the SNS topic to send ok message to
    """

    return {
        name: {
            'Type': 'AWS::CloudWatch::Alarm',
            'Properties': {
                'AlarmDescription': join('Alarm if', ref(as_group), 'CPU > 70% for 5 minutes'),
                'Dimensions': [{
                    'Name': 'AutoScalingGroupName',
                    'Value': ref(as_group),
                }],
                'Namespace': 'EC2',
                'Statistic': 'Average',
                'MetricName': 'CPUUtilization',
                'ComparisonOperator': 'GreaterThanOrEqualToThreshold',
                'Threshold': '70',
                'Period': '60',
                'EvaluationPeriods': '5',
                'AlarmActions': [ref(alarm_topic)],
                'OkActions': [ref(ok_topic)],
            }
        }
    }
