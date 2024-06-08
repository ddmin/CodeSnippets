#!/usr/bin/env python3

from bs4 import BeautifulSoup
import click
import os
import requests
import time
import tqdm


DELAY = 1
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"
}


def read_links(file):
    return list(filter(lambda x: x, file.read().split("\n")))


def fix_link(full_link, link):
    if 'https://' not in link:
        if full_link[-1] != '/':
            full_link += '/'

        if len(link) > 1 and link[0] == '/':
            link = link[1:]

        return full_link + link

    return link

def get_href(link):
    if 'href' in link.attrs:
        return link['href']
    return ''

def get_src(img):
    if 'src' in img.attrs:
        return img['src']
    return ''

@click.command()
@click.option(
    "-d",
    "--no-delay",
    "no_delay",
    is_flag=True,
    help="Disable delay between image downloads.",
)
@click.argument("file", type=click.File("r"), nargs=1)
def main(file, no_delay):
    links = read_links(file)

    count = 0
    site_imgs = {}
    for link in links:
        images = []
        html = requests.get(link, headers=HEADERS).text
        soup = BeautifulSoup(html, "lxml")

        # find all anchors
        link_images = soup.find_all("a")

        link_images = list(map(lambda url: get_href(url), link_images))
        link_images = list(map(lambda image: fix_link(link, image), link_images))

        # filter anchors with images
        link_images = list(filter(lambda url: url.endswith(('jpg', 'jpeg', 'png', 'webp')), link_images))

        # find all images
        img_images = soup.find_all("img")

        img_images = list(map(lambda url: get_src(url), img_images))
        img_images = list(map(lambda image: fix_link(link, image), img_images))

        images.extend(link_images)
        images.extend(img_images)

        count += len(images)

        site_imgs[link] = images

        if not no_delay:
            time.sleep(DELAY)

    image_string = click.style(
        f"IMAGES TO DOWNLOAD ({count})\n\n", fg="bright_red"
    )

    for nn, site in enumerate(site_imgs):
        image_string += click.style(f'{nn+1}. {site}',fg="bright_green") + '\n'
        for n, image in enumerate(site_imgs[site]):
            image_string += (
                        click.style(f"\t{n+1}. ", fg="bright_yellow")
                        + click.style(image, fg="bright_blue")
                        + "\n\n"
                    )

    click.echo_via_pager(image_string)
    click.confirm(click.style("Continue?", fg="bright_red"), abort=True)

    for nn, site in enumerate(site_imgs):

        save_dir = str(nn+1).zfill(3)
        if not os.path.exists(save_dir):
            os.mkdir(save_dir)

        progress = tqdm.tqdm(total=len(images), desc=f"[{save_dir}] Downloading Images...")
        for n, image in enumerate(site_imgs[site]):
            img_response = requests.get(image, headers=HEADERS)
            with open(f"{save_dir}/{str(n+1).zfill(3)}", "wb") as img:
                img.write(img_response.content)

            if not no_delay:
                time.sleep(DELAY)

            progress.update(n=1)

if __name__ == "__main__":
    main()
