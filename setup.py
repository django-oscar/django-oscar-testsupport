#!/usr/bin/env python
import os
from setuptools import setup, find_packages

PROJECT_ROOT = os.path.dirname(__file__)

setup(
    name='django-oscar-testsupport',
    version='0.3.1',
    url='https://github.com/tangentlabs/django-oscar-testsupport',
    author="David Winterbottom",
    author_email="david.winterbottom@tangentlabs.co.uk",
    description="Testing utilities for Oscar",
    long_description=open(os.path.join(PROJECT_ROOT, 'README.rst')).read(),
    license=open(os.path.join(PROJECT_ROOT, 'LICENSE')).read(),
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django-oscar>=0.4,<0.6',
        'WebTest>=1.3,<2.1',
        'django-webtest>=1.5.7,<1.6',
        'purl>=0.4',
    ])
