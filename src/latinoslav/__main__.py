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


from latinoslav.config import config
from latinoslav.convert import convert
import click


@click.command()
@click.option(
    "-m",
    "--method",
    prompt="Enter method, please",
    help="Transliteration method (see methods.yaml).",
    type=click.Choice(list(config().methods.keys()), case_sensitive=False),
)
def main(method: str) -> None:
    while True:
        print(convert(input(), method))


main()
