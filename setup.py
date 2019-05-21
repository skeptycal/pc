#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pylint: disable=missing-docstring
# Note: To use the 'upload' functionality of this file, you must:
#   $ pipenv install twine --dev

import io
import os
import sys
from shutil import rmtree
from typing import Dict, List

from setuptools import Command, find_packages, setup

# Package meta-data.
NAME: str = 'skeptycal.github.io'
DESCRIPTION: str = 'A portfolio of various creative projects.'
URL: str = 'https://github.com/skeptycal/skeptycal.github.io'
EMAIL: str = 'skeptycal@gmail.com'
AUTHOR: str = 'Michael Treanor'
REQUIRES_PYTHON: str = '>=3.6.0'
VERSION: str = '0.1.0'

# What packages are required for this module to be executed?
REQUIRED: List[str] = [
    'requests'
]

# What packages are optional?
EXTRAS: Dict = {
    'testgui': ['flask']
}

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the
#   Trove Classifier for that!

here: str = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description: str = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about: Dict = {}
if not VERSION:
    project_slug: str = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(here, project_slug, '__version__.py')) as f:
        exec(f.read(), about)  # pylint: disable=exec-used
else:
    about['__version__'] = VERSION


class UploadCommand(Command):
    """Support setup.py upload."""

    description: str = 'Build and publish the package.'
    user_options: List = []

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
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(
            sys.executable))

        self.status('Uploading the package to PyPI via Twine…')
        os.system('twine upload dist/*')

        self.status('Pushing git tags…')
        os.system('git tag v{0}'.format(about['__version__']))
        os.system('git push --tags')

        sys.exit()


# Where the magic happens:
setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(
        exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],

    # entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    # $ setup.py publish support.
    cmdclass={
        'upload': UploadCommand,
    },
)
