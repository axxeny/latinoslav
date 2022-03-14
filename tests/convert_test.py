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


sample_ru_text = """\
Съешь же ещё этих мягких французских булок, да выпей чаю.
Кстати, отличная квартирка для экзамена на карантине!
Въезд, выезд.
Сходящаяся.
English text in hotel hyatt.
"""


sample_uk_text = """\
В Бахчисараї фельд'єґер зумів одягнути ящірці жовтий капюшон!
Українська абетка має 33 літери:
а, б, в, г, ґ, д, е, є, ж, з, и, і, ї, й, к, л, м, н, о, п, р, с, т, у, ф,
х, ц, ч, ш, щ, ь, ю, я.
Інколи також до неї зараховують апостроф ('), що має фонетичне значення
і є обов'язковим знаком на письмі,
але літерою не вважається та формально до абетки не входить.
English text in hotel Hyatt.
"""


sample_uk_out = """\
V Bakhchysarayi feljdyeger zumiv odjahnuty yashchirci zhovtyy kapjushon!
Ukrayinsjka abetka maye 33 litery:
a, b, v, h, g, d, e, ye, zh, z, y, i, yi, y, k, l, m, n, o, p, r, s, t, u, f,
kh, c, ch, sh, shch, j, yu, ya.
Inkoly takozh do neyi zarakhovuyutj apostrof ('), shcho maye fonetychne znachennja
i ye obovyazkovym znakom na pysjmi,
ale literoyu ne vvazhayetjsja ta formaljno do abetky ne vkhodytj.
English text in hotel Hyatt.
"""


@pytest.fixture
def sample_ru_out():
    with Path("tests", "sample_out.yaml").open() as f:
        return yaml.safe_load(f)


@pytest.mark.parametrize(
    "method",
    ["vjezd_vyezd_shodyaschayasya", "vyezd_vyyezd_shodjaschayasja", "ето_вьезд_выезд"],
)
def test_convert_ru(method, sample_ru_out):
    actual = convert.convert(sample_ru_text, method)
    expected = sample_ru_out[method]
    assert expected == actual


def test_convert_uk():
    actual = convert.convert(sample_uk_text, "uk1")
    expected = sample_uk_out
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
