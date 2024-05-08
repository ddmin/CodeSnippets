#!/usr/bin/python

HIRAGANA = "hiragana.txt"
KATAKANA = "katakana.txt"


def get_kana(file):
    dictionary = {}

    with open(file, "r") as f:
        filtered = filter(lambda x: x, f.read().split("\n"))
        pairs = map(lambda x: x.split(), filtered)
        for a, b in pairs:
            dictionary[a] = b

    return dictionary


def main():
    hiragana = get_kana(HIRAGANA)
    katakana = get_kana(KATAKANA)


if __name__ == "__main__":
    main()
