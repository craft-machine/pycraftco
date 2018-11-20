#/usr/bin/env python
from setuptools import setup, find_packages


with open("README.md", "r") as f:
    long_description = f.read()


setup(
    name="pycraftco",
    version="0.1",
    description="pycraftco is a Python library that serves as a convenient wrapper for Craft API (https://api.craft.co/docs/v1)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Craft Machine Inc",
    url="https://github.com/craft-machine/pycraftco",
    packages=find_packages(),
    include_package_data=True,
    keywords=['SDK', 'API'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities'],
    install_requires=[
        'sgqlc==1',
    ],
)
