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


import logging
import re
from enum import Enum

from pygtrie import CharTrie

from pyrulatin.config import config


logger = logging.getLogger(__name__)


class Case(str, Enum):
    LOWER = "lower"
    UPPER = "upper"


def convert(text: str, method_name: str) -> str:
    if method_name not in config().methods:
        return ValueError(f"{method_name=} not in {config()=}")
    if not text:
        return text
    method = config().methods[method_name]

    word_pattern = re.compile(rf"({method.word_pattern}+)")
    words = word_pattern.split(text)

    for i, word in enumerate(words):
        if i % 2 == 0:
            continue
        if word.islower():
            restore_case = _restore_lower_case
        elif word.isupper():
            restore_case = _restore_upper_case
        else:
            # case_mask = [c.isupper() for c in word]
            # todo maybe letter apply the mask
            restore_case = _restore_title_case
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

    text = f"{text}<rlend>"

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
    text = text.replace("<rlend>", "")

    return text


def _restore_lower_case(lower_word: str) -> str:
    return lower_word


def _restore_upper_case(lower_word: str) -> str:
    return lower_word.upper()


def _restore_title_case(lower_word: str) -> str:
    return lower_word.title()
