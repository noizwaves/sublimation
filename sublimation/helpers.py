"""
Short helper methods that wrap specific CF short functions.
"""


def find_in_map(name, key, value_name):
    return {'Fn::FindInMap': [name, ref(name), value_name]}


def get_azs():
    return {"Fn::GetAZs": ""}


def get_attr(name, attribute):
    return {"Fn::GetAtt": [name, attribute]}


def base64(value):
    return {"Fn::Base64": value}


def join(*parts):
    return {'Fn::Join': ['', parts]}


def ref(value):
    return {'Ref': value}


def as_joined_base64(lines):
    """Turns a list of string 'lines' into a base64 joined string"""

    return base64(join(*lines))
