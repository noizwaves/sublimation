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
            'SecurityGroups': security_groups,  # TODO: ensure a list
        }

        if user_data is not None:
            properties['UserData'] = user_data

        super(Instance, self).__init__(name, self.cf_type, properties)


class AutoScalingGroup(Resource):
    cf_type = 'AWS::AutoScaling::AutoScalingGroup'

    def __init__(self, name, launch_config, azs, min_size, max_size, desired_capacity, load_balancers):
        properties = {
            'AvailabilityZones': azs,
            'LaunchConfigurationName': launch_config,
            'MinSize': min_size,  # TODO: ensure a string
            'MaxSize': max_size,  # TODO: ensure a string
            'DesiredCapacity': desired_capacity,  # TODO: ensure a string
            'LoadBalancerName': load_balancers,  # TODO: ensure a list
        }

        super(AutoScalingGroup, self).__init__(name, self.cf_type, properties)


class LaunchConfiguration(Resource):
    cf_type = 'AWS::AutoScaling::LaunchConfiguration'

    def __init__(self, name, image_id, instance_type, security_groups, user_data=None):
        properties = {
            'ImageId': image_id,
            'SecurityGroups': security_groups,  # TODO: ensure a list
            'InstanceType': instance_type,
        }

        if user_data is not None:
            properties['UserData'] = user_data

        super(LaunchConfiguration, self).__init__(name, self.cf_type, properties)


class SecurityGroup(Resource):
    cf_type = 'AWS::EC2::SecurityGroup'

    def __init__(self, name, description, ingress):
        properties = {
            'GroupDescription': description,
            'SecurityGroupIngress': ingress,  # TODO: ensure a list
        }

        super(SecurityGroup, self).__init__(name, self.cf_type, properties)


class LoadBalancer(Resource):
    cf_type = 'AWS::ElasticLoadBalancing::LoadBalancer'

    def __init__(self, name, azs, listeners, target, healthy_threshold=10, unhealthy_threshold=2,
                 interval=30, timeout=5):
        properties = {
            'AvailabilityZones': azs,
            'Listeners': listeners,  # TODO: ensure list
            'HealthCheck': {
                'Target': target,
                'HealthyThreshold': healthy_threshold,  # TODO: ensure string
                'UnhealthyThreshold': unhealthy_threshold,  # TODO: ensure string
                'Interval': interval,  # TODO: ensure string
                'Timeout': timeout,  # TODO: ensure string
            }
        }

        super(LoadBalancer, self).__init__(name, self.cf_type, properties)


class Distribution(Resource):
    cf_type = 'AWS::CloudFront::Distribution'

    def __init__(self, name, comment, enabled, origins, default_cache_behavior):
        distribution_config = {
            'Comment': 'Caches static files served through the ELB.',
            'Enabled': True,
            'Origins': origins,  # TODO: ensure list
            'DefaultCacheBehavior': default_cache_behavior,
        }

        properties = {
            'DistributionConfig': distribution_config,
        }

        super(Distribution, self).__init__(name, self.cf_type, properties)


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
