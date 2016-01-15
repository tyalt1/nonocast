# Copyright 2016 Tyler Alterio, YuetLong Leung, Matthew Wolf, Allison Ober
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

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("README.md") as f:
    readme = f.read();

setup(
    name='nonocast',
    version='0.0.0',
    description='Web server for universal media casting.',
    long_description=readme,
    author='Tyler Alterio',
    scripts=['bin/nonocast'],
    packages=['nonocast'],
    install_requires=['livestreamer'],
    license='Apache 2.0',
    include_package_data=True,
    package_data={'nonocast' : ['bg.jpg']},
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Web Environment",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Multimedia :: Video",
        "Topic :: Utilities"
    ],
)
