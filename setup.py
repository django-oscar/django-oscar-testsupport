#!/usr/bin/env python
import os
from setuptools import setup, find_packages

PROJECT_ROOT = os.path.dirname(__file__)

setup(
    name='django-oscar-testsupport',
    version='0.1',
    url='https://github.com/tangentlabs/django-oscar-testsupport',
    author="David Winterbottom",
    author_email="david.winterbottom@tangentlabs.co.uk",
    description="Testing utilities for Oscar",
    long_description=open(os.path.join(PROJECT_ROOT, 'README.rst')).read(),
    license=open(os.path.join(PROJECT_ROOT, 'LICENSE')).read(),
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django-oscar',
        'WebTest>=1.3',
        'django-webtest>=1.5',
        'purl>=0.4',
    ])
