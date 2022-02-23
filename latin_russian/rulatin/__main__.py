from convert import convert, methods
import click


@click.command()
@click.option(
    "-m",
    "--method",
    prompt="Enter method, please",
    help="Transliteration method (see methods.yaml).",
    type=click.Choice(list(methods().methods.keys()), case_sensitive=False)
)
def main(method: str) -> None:
    while True:
        print(convert(input(), method))


main()
