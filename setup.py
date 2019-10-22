#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# Note: To use the 'upload' functionality of this file, you must:
#   $ pipenv install twine --dev

from setuptools import setup, find_packages, find_namespace_packages, Command
import sys, re, os, io
from shutil import rmtree

# Package meta-data.
NAME = 'pyTemplate'
DESCRIPTION = ('Template of python3 project.')
URL = 'https://github.com/StephenRicher/pyTemplate'
EMAIL = 'sr467@bath.ac.uk'
AUTHOR = 'Stephen Richer'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = '0.1.0'
SCRIPTS = []
REQUIRED = []

# Import the README and use it as the long-description.
try:
    with open('README.md') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Import the LICENSE
try:
    with open('LICENSE') as f:
        license = '\n' + f.read()
except FileNotFoundError:
    license = 'MIT'

class UploadCommand(Command):
    """Support setup.py upload."""

    here = os.path.abspath(os.path.dirname(__file__))

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPI via Twine…')
        os.system('twine upload dist/*')

        self.status('Pushing git tags…')
        os.system(f'git tag v{get_version()}')
        os.system('git push --tags')

        sys.exit()

setup(name = NAME,
    version = VERSION,
    description = DESCRIPTION,
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    author = AUTHOR,
    author_email = EMAIL,
    python_requires = REQUIRES_PYTHON,
    url = URL,
    license = license,
    packages = find_namespace_packages(where = 'src'),
    package_dir={'': 'src'},
    install_requires = REQUIRED,
    scripts = SCRIPTS,
    setup_requires = ['pytest-runner'],
    tests_require = ['pytest'],
    zip_safe = False,
    # $ python setup.py upload
    cmdclass={
        'upload': UploadCommand,
    }
)
