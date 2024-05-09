#!/usr/bin/env python3
# (it's not really diceware)

import random
import click


@click.command()
@click.option(
    "-n", "--words", "words", type=int, default=7, help="Number of words to generate."
)
@click.option(
    "-v",
    "--verbose",
    "verbose",
    is_flag=True,
    default=False,
    help="Display original, un-romanized word.",
)
@click.option(
    "-k",
    "--kanji",
    "kanji",
    is_flag=True,
    default=False,
    help="Use only words derived from Kanji (or English)",
)
@click.argument("wordlist", type=click.File("r"))
def main(words, verbose, kanji, wordlist):
    wl = wordlist.read().split("\n")
    lines = [line.split() for line in wl]

    # Filtering Words
    # --kanji
    if kanji:
        lines = list(filter(lambda line: len(line) == 3, lines))

    diceware = random.choices(lines, k=words)

    for word_tuple in diceware:
        click.echo(click.style(word_tuple[0], fg="bright_white"), nl=False)
        if verbose:
            click.echo(
                click.style(f" ({word_tuple[-1]})", fg="bright_magenta"), nl=False
            )
        click.echo(" ", nl=False)


if __name__ == "__main__":
    main()
