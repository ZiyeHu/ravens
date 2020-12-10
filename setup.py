# coding=utf-8
# Copyright 2020 The Ravens Authors.
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

"""Setup."""

from distutils import core
from setuptools import find_packages

# Bare-bones setup file so we can import ravens.
core.setup(
    name='ravens',
    version='0.0.1',
    author='Andy Zeng, Pete Florence, Daniel Seita, Jonathan Tompson',
    packages=find_packages(),
)