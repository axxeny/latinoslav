from functools import cache
import logging
import re
from enum import Enum
from pathlib import Path
from threading import Lock
from typing import overload

import yaml
from pydantic import BaseModel, validator
from pygtrie import CharTrie


logger = logging.getLogger(__name__)


methods_lock = Lock()


class Method(BaseModel):
    word_pattern: str
    steps: list[dict[str, str]]


class Methods(BaseModel):
    methods: dict[str, Method]


@cache
def _methods():
    with Path("methods.yaml").open() as f:
        d = yaml.safe_load(f)
        return Methods(**d)


def methods():
    with methods_lock:
        return _methods()


class Case(str, Enum):
    LOWER = "lower"
    UPPER = "upper"


def convert(text: str, method_name: str) -> str:
    if method_name not in methods().methods:
        return ValueError(f"{method_name=} not in {methods()=}")
    if not text:
        return text
    method = methods().methods[method_name]

    word_pattern = re.compile(rf"({method.word_pattern}+)")
    words = word_pattern.split(text)

    for i, word in enumerate(words):
        if i % 2 == 0:
            continue
        restore_case = lambda word: word
        if word.isupper():
            restore_case = lambda word: word.upper()
        if not word.islower() and not word.isupper():
            # case_mask = [c.isupper() for c in word]
            restore_case = lambda word: word.title()  # todo maybe letter apply the mask
        word = word.lower()
        for step_dict in method.steps:
            word = _convert_step(word, step=step_dict)
        word = restore_case(word)
        words[i] = word
    return "".join(words)


def _convert_step(text: str, step: dict[str, str]) -> str:

    step = CharTrie(**step)

    # logging
    substrs: list[str] = []
    logger.debug(f"{step = }")

    text = f'{text}<rlend>'

    i, j = 0, 1
    candidate = None
    out: str = []
    while j <= len(text):

        substr = str(text[i:j])

        # logging
        substrs.append(substr)
        # logger.debug(f'{substr = }')

        if substr in step:
            candidate = substr
            logger.debug(f"{candidate = }")
            j += 1
            continue

        elif step.has_subtrie(substr):
            j += 1
            continue

        else:
            if candidate is not None:
                out.append(step[candidate])
                logger.debug(f"{out = }")
                candidate = None
                i = j - 1
                continue

            if candidate is None:
                out.append(text[i])
                i += 1
                j = i + 1
                continue

            assert False


    if candidate is not None:
        out.append(step[candidate])
        logger.debug(f"{out = }")

    else:
        out.append(text[i:])
        logger.debug(f"{out = }")

    text = "".join(out)
    text = text.replace('<rlend>', '')

    return text
