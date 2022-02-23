from pyrulatin.config import config
from pyrulatin.convert import convert
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
