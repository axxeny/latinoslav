from functools import cache
import logging
from pathlib import Path
from threading import Lock

import yaml
from pydantic import BaseModel


logger = logging.getLogger(__name__)


methods_lock = Lock()


Pass = dict[str, str]


class Method(BaseModel):
    passes: list[Pass]


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


def convert(text: str, method_name: str) -> str:
    if method_name not in methods().methods:
        return ValueError(f"{method_name=} not in {methods()=}")
    if not text:
        return text
    method = methods().methods[method_name]
    passes = method.passes
    for p in passes:
        # logging
        substrs: list[str] = []
        logger.debug(f'{p = }')
        i, j = 0, 1
        candidate = None
        out: str = []
        while j < len(text):

            substr = str(text[i:j])

            # logging
            substrs.append(substr)
            # logger.debug(f'{substr = }')

            if substr in p:
                candidate = substr
                logger.debug(f'{candidate = }')
                j += 1
                continue

            if substr not in p:
                if candidate is not None:
                    out.append(p[candidate])
                    logger.debug(f'{out = }')
                    candidate = None
                    i = j - 1
                    continue

                if candidate is None:
                    out.append(substr)
                    i += 1
                    j = i + 1
                    continue

                assert False

            assert False

        if candidate is not None:
            out.append(p[candidate])
            logger.debug(f'{out = }')

        logger.debug(f'{substrs = }')

        text = "".join(out)

        logger.debug(f'{text = }')

    return text
