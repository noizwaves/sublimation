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


class Topic(Resource):
    cf_type = 'AWS::SNS::Topic'

    def __init__(self, name, display_name, email_address):
        properties = {
            'DisplayName': display_name,
            'Subscription': [{
                'Protocol': 'email',
                'Endpoint': email_address,
            }],
        }

        super(Topic, self).__init__(name, self.cf_type, properties)


class Instance(Resource):
    cf_type = 'AWS::EC2::Instance'

    def __init__(self, name, image_id, instance_type, key_name, security_groups, user_data=None):
        properties = {
            'ImageId': image_id,
            'InstanceType': instance_type,
            'KeyName': key_name,
            'SecurityGroups': security_groups,
        }

        if user_data is not None:
            properties['UserData'] = user_data

        super(Instance, self).__init__(name, self.cf_type, properties)


class AutoscaleCpuHighAlarm(Resource):
    cf_type = 'AWS::CloudWatch::Alarm'

    def __init__(self, name, as_group, alarm_topic, ok_topic):
        """
        Defines a new alert for an AutoScaling group hitting high CPU usage.

        Arguments:
        - as_group: the name of the AutoScaling group
        - alarm_topic: the name of the SNS topic to send alarm message to
        - ok_topic: the name of the SNS topic to send ok message to
        """

        properties = {
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

        super(AutoscaleCpuHighAlarm, self).__init__(name, self.cf_type, properties)
