"""
Sublimation is an early stage pythonic DSL for declaring CloudFormation templates.
"""

__all__ = ['template', 's9n']

from sublimation.templates import template
from sublimation import s9n
