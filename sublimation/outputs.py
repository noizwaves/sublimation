"""
Useful outputs.
"""

from .helpers import join, get_attr
from .templates import TemplateNode, OUTPUTS_FIELD


class Output(TemplateNode):
    belongs_in = OUTPUTS_FIELD

    def __init__(self, name, description, value):
        self.data = {
            name: {
                'Description': description,
                'Value': value,
            }
        }


class ElbUrlOutput(Output):
    def __init__(self, elb_name):
        value = join('http://', get_attr(elb_name, 'DNSName'))
        description = 'The public url of %s' % elb_name
        super(ElbUrlOutput, self).__init__('ELB_Url', description, value)


class CfUrlOutput(Output):
    def __init__(self, cf_name):
        value = join('//', get_attr(cf_name, 'Domain'))
        description = 'The public url of %s' % cf_name
        super(CfUrlOutput, self).__init__('CloudFront_Url', description, value)
