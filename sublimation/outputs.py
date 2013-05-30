"""
Useful outputs.
"""

__all__ = ['output', 'output_elb_url', 'output_cf_url']


from .helpers import join, get_attr


def output(name, description, value):
    """
    Defines an output called `name` with description `description` of value `value`.
    """

    return {
        name: {
            'Description': description,
            'Value': value,
        }
    }


def output_elb_url(elb_name):
    return output('ELB_Url', 'The public url of %s' % elb_name, join('http://', get_attr(elb_name, 'DNSName')))


def output_cf_url(cf_name):
    return output('CloudFront_Url', 'The public url of %s' % cf_name, join('//', get_attr(cf_name, 'Domain')))
