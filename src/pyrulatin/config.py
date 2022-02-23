from functools import cache
from importlib import resources
from threading import Lock

import yaml
from pydantic import BaseModel

import pyrulatin


config_lock = Lock()


class Method(BaseModel):
    word_pattern: str
    steps: list[dict[str, str]]


class Config(BaseModel):
    methods: dict[str, Method]


@cache
def _config():
    config_str = resources.read_text(pyrulatin, "config.yaml")
    d = yaml.safe_load(config_str)
    return Config(**d)


def config():
    with config_lock:
        return _config()
