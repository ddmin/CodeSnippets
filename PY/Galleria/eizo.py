#!/usr/bin/env python3

import click
import tqdm
import requests
from bs4 import BeautifulSoup
import time


FILEFORMAT = "jpg"
DELAY = 1
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"
}


def read_links(file):
    return list(filter(lambda x: x, file.read().split("\n")))


@click.command()
@click.option(
    "-d",
    "--delay",
    "is_delay",
    is_flag=True,
    help="Enable delay between image downloads.",
)
@click.argument("file", type=click.File("r"), nargs=1)
def main(file, is_delay):
    links = read_links(file)

    images = []
    for link in links:
        html = requests.get(link, headers=HEADERS).text
        soup = BeautifulSoup(html, "lxml")
        images.extend(soup.find_all("img"))

        if is_delay:
            time.sleep(DELAY)

    images = list(map(lambda url: url["src"], images))
    image_string = click.style(
        f"IMAGES TO DOWNLOAD ({len(images)})\n\n", fg="bright_red"
    )
    for n, image in enumerate(images):
        image_string += (
            click.style(f"{n+1}. ", fg="bright_yellow")
            + click.style(image, fg="bright_blue")
            + "\n\n"
        )

    click.echo_via_pager(image_string)
    click.confirm(click.style("Continue?", fg="bright_red"), abort=True)

    progress = tqdm.tqdm(total=len(images), desc="Downloading Images...")
    for n, image in enumerate(images):
        img_response = requests.get(image, headers=HEADERS)
        with open(f"{str(n+1).zfill(3)}.{FILEFORMAT}", "wb") as img:
            img.write(img_response.content)

        if is_delay:
            time.sleep(DELAY)

        progress.update(n=1)


if __name__ == "__main__":
    main()
