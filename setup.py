from setuptools import setup

setup(
    name="sublimation",
    version="0.0.1dev",
    author="Adam Neumann",
    author_email="adam@noizwaves.com",
    description=("Efficient and modular CloudFormation template declaration via a Python internal DSL"),
    license="Apache License, Version 2.0",
    keywords="aws cloudformation dsl",
    url="https://github.com/noizwaves/sublimation",
    packages=['sublimation'],
    long_description='TODO',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: System :: Systems Administration",
    ],
)
