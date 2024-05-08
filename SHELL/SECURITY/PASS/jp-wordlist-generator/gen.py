#!/usr/bin/python

# TODO: separate hiragana / katakana words
# TODO: remove repeated words

import re
import itertools
from random import shuffle


dice = [i for i in range(1, 7)]
rolls = ["".join(map(lambda x: str(x), p)) for p in itertools.product(dice, repeat=7)]

JMdict = "JMdict_e"
savefile = "JP_JMDICT_WORDLIST.txt"

hiragana = "hiragana.txt"
katakana = "katakana.txt"

exceptions = [
    "・",
    "＝",
    "。",
    "ゐ",
    "ゑ",
    "ヰ",
    "ヱ",
    "々",
    "ゞ",
    "ゝ",
    "ゝ",
    "、",
    "ヶ",
    "ﾀ",
    "ﾋ",
    "ヮ",
    "ゎ",
]


def main():

    # read file
    with open(JMdict, "r") as f:
        file = f.read()

    jp = []
    words = []
    inner_html_regex = r"<.*>(.*?)<.*>"
    for line in file.split("\n"):
        if line.startswith("<reb>"):
            word = re.match(inner_html_regex, line).group(1)
            jp.append(word)

            mora = [""]
            small = [
                "ょ",
                "ゅ",
                "ゃ",
                "ョ",
                "ュ",
                "ャ",
                "ぁ",
                "ぃ",
                "ぅ",
                "ぇ",
                "ぉ",
                "ァ",
                "ィ",
                "ゥ",
                "ェ",
                "ォ",
            ]
            for c in word:
                if c in small:
                    combined = mora[-1] + c
                    if combined in jp_to_en:
                        mora[-1] = combined
                    else:
                        mora.append(c)
                else:
                    mora.append(c)

            tsu = False
            roman = ""

            mora = list(filter(lambda x: x, mora))
            for m in mora:
                if m in exceptions:
                    pass
                elif tsu:
                    en = jp_to_en[m]
                    roman += en[0] + en
                    tsu = False
                elif m in ["っ", "ッ"]:
                    tsu = True
                elif m in ["ー", "〜"]:
                    if roman:
                        roman += roman[-1]
                else:
                    en = jp_to_en[m]
                    roman += en

            words.append(roman)

    with open(savefile, "w") as f:
        n = -1
        for roll, word, japanese in zip(rolls, words, jp):
            n += 1
            f.write(f"{roll}\t{word}\t{japanese}\n")

        # it's not "non-deterministic", baby
        matching = list(
            filter(lambda x: len(x[0]) > 2 and len(x[0]) < 10, zip(words, jp))
        )
        shuffle(matching)

        for roll, zipped in zip(rolls[n + 1 :], matching):
            word, japanese = zipped
            f.write(f"{roll}\t{word.upper()}\t{japanese}\n")


if __name__ == "__main__":
    main()
