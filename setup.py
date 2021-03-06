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


setup(
    author="Arseniy Poroshin",
    name="latinoslav",
    version="0.1.0",
    description=(
        "Transliterate Russian or Ukrainian language to latin script. Now: CLI."
        " Planning: an HTTP microservice, as well."
    ),
    url="https://github.com/axxeny/latinoslav",
    include_package_data=True,
    install_requires=["click", "pygtrie", "pydantic", "PyYAML"],
    packages=find_packages(where="src"),
    package_dir={
        "": "src",
        "latinoslav": "src/latinoslav",
    },
    package_data={
        "latinoslav": ["config.yaml"],
    },
    python_requires=">=3.9",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Education",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: Russian",
        "Natural Language :: Ukrainian",
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
