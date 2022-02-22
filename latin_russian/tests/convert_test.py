import pytest

from pathlib import Path

import yaml

import rulatin.convert as convert


sample_text = """\
Съешь же ещё этих мягких французских булок, да выпей чаю.
Въезд, выезд.
Сходящаяся.
English text in hotel hyatt.
"""


@pytest.fixture
def sample_out():
    with Path("tests", "sample_out.yaml").open() as f:
        return yaml.safe_load(f)


@pytest.mark.parametrize(
    "method", ["vjezd_vyezd_shodyaschayasya", "vyezd_vyyezd_shodjaschayasja"]
)
def test_convert(method, sample_out):
    actual = convert.convert(sample_text, method)
    expected = sample_out[method]
    assert expected == actual
