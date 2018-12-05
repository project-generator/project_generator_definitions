# Copyright 2015 0xc0170
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import pip

from setuptools import setup, find_packages

setup(
    name='project_generator_definitions',
    version='0.2.38',
    author_email='c0170@rocketmail.com',
    keywords="definitions mcu uvision iar coide",
    url="https://github.com/project-generator/project_generator_definitions",
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development"
    ],

    entry_points={
        'console_scripts': [
            "progendef=project_generator_definitions.main:main",
        ]
    },
    packages=find_packages(),
    install_requires = [
        'pyYAML',
        'xmltodict'
    ],
    include_package_data = True,
)
