from cmath import exp
import pytest

from pathlib import Path

import yaml

import rulatin.convert as convert


sample_text = """\
Съешь же ещё этих мягких французских булок, да выпей чаю.
Кстати, отличная квартирка для экзамена на карантине!
Въезд, выезд.
Сходящаяся.
English text in hotel hyatt.
"""


@pytest.fixture
def sample_out():
    with Path("tests", "sample_out.yaml").open() as f:
        return yaml.safe_load(f)


@pytest.mark.parametrize(
    "method",
    ["vjezd_vyezd_shodyaschayasya", "vyezd_vyyezd_shodjaschayasja", "ето_вьезд_выезд"],
)
def test_convert(method, sample_out):
    actual = convert.convert(sample_text, method)
    expected = sample_out[method]
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
