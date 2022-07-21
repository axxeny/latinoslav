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


import pytest

from pathlib import Path

import yaml

import latinoslav.convert as convert


ru_sample_text = """\
Съешь же ещё этих мягких французских булок, да выпей чаю.
Кстати, отличная квартирка для экзамена на карантине!
Въезд, выезд.
Третьи.
Сходящаяся.
English text in hotel hyatt.
"""


uk_sample_text = """\
В Бахчисараї фельд'єґер зумів одягнути ящірці жовтий капюшон!
Українська абетка має 33 літери:
а, б, в, г, ґ, д, е, є, ж, з, и, і, ї, й, к, л, м, н, о, п, р, с, т, у, ф,
х, ц, ч, ш, щ, ь, ю, я.
Інколи також до неї зараховують апостроф ('), що має фонетичне значення
і є обов'язковим знаком на письмі,
але літерою не вважається та формально до абетки не входить.
English text in hotel Hyatt.
"""


def ru_transform_names():
    with Path("tests", "ru_sample_out.yaml").open() as f:
        return yaml.safe_load(f).keys()


def uk_transform_names():
    with Path("tests", "uk_sample_out.yaml").open() as f:
        return yaml.safe_load(f).keys()


@pytest.fixture
def ru_sample_out():
    with Path("tests", "ru_sample_out.yaml").open() as f:
        return yaml.safe_load(f)


@pytest.fixture
def uk_sample_out():
    with Path("tests", "uk_sample_out.yaml").open() as f:
        return yaml.safe_load(f)


@pytest.mark.parametrize(
    "method",
    ru_transform_names(),
)
def test_convert_ru(method, ru_sample_out):
    actual = convert.convert(ru_sample_text, method)
    expected = ru_sample_out[method]
    assert expected == actual


@pytest.mark.parametrize(
    "method",
    ["uk1", "uk2", "uk3"],
)
def test_convert_uk(method, uk_sample_out):
    actual = convert.convert(uk_sample_text, method)
    expected = uk_sample_out[method]
    assert expected == actual


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("", ""),
        ("a", "n"),
        ("b", "b"),
        ("ba", "bn"),
        ("c", "c"),
        ("g", "p"),
        ("e", "e"),
        ("bcg", "op"),
        ("bfbcf", "rof"),
        ("abcgefd", "noqfd"),
    ],
)
def test_step(text, expected):
    method = {
        "a": "n",
        "bc": "o",
        "bf": "r",
        "g": "p",
        "ge": "q",
    }

    assert expected == convert._convert_step(text, method)
