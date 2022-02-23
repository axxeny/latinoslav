from convert import convert
import click


@click.command()
@click.option(
    "-m",
    "--method",
    prompt="Enter method, please",
    help="Transliteration method (see methods.yaml).",
)
def main(method: str) -> None:
    while True:
        print(convert(input(), method))


main()
