#  Copyright 2022 Arseniy Poroshin
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


from setuptools import setup, find_packages

import os.path


setup(
    author="Arseniy Poroshin",
    name="pyrulatin",
    version="0.1.0",
    description="Transliterate Russian language to latin script. CLI. In the future: http microservice",
    url="https://github.com/axxeny/pyrulatin",
    include_package_data=True,
    install_requires=["click", "pygtrie", "pydantic", "PyYAML"],
    packages=["pyrulatin"],
    package_dir={"pyrulatin": "src/pyrulatin"},
    package_data={"pyrulatin": ["config.yaml"]},
    python_requires=">=3.9",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Education",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: Russian",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Text Processing :: Linguistic",
        "Typing :: Typed",
    ],
)
