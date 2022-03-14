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


from functools import cache
from importlib import resources
from threading import Lock

import yaml
from pydantic import BaseModel

import latinoslav


config_lock = Lock()


class Method(BaseModel):
    word_pattern: str
    steps: list[dict[str, str]]


class Config(BaseModel):
    methods: dict[str, Method]


@cache
def _config():
    config_str = resources.read_text(latinoslav, "config.yaml")
    d = yaml.safe_load(config_str)
    return Config(**d)


def config():
    with config_lock:
        return _config()
