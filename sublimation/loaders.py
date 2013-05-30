"""
Methods for loading data.
"""

__all__ = ['is_bash_useful', 'load_template', 'load_script']


from json import loads


def is_bash_useful(line):
    """
    Returns True if a line is important in a bash file, false otherwise.
    """

    if line.startswith('#!'):
        return True
    elif line.startswith('#'):
        return False
    elif line.startswith(('\n', '\r')):
        return False
    else:
        return True


def load_template(path):
    """Loads a CF template JSON file"""

    with open(path, 'r') as cf_template:
        return loads(cf_template.read())


def load_script(path, keep_if=None):
    """Loads a script from disk ready into a series of lines"""

    if keep_if is None:
        keep_if = lambda x: True

    with open(path, 'r') as script_file:
        return [l for l in script_file.readlines() if keep_if(l)]
