#!/usr/bin/python

import re


KANA_DIR = "kana"
HIRAGANA = f"{KANA_DIR}/hiragana.txt"
KATAKANA = f"{KANA_DIR}/katakana.txt"

SMALL_HIRAGANA = f"{KANA_DIR}/small-hiragana.txt"
SMALL_KATAKANA = f"{KANA_DIR}/small-katakana.txt"

TXT_DIR = "txt"
JMdict = "JMdict_e"
savefile = f"{TXT_DIR}/JP_JMDICT_WORDLIST.txt"


def get_kana(file):
    """Store kana and readings from file in dictionary"""
    dictionary = {}

    with open(file, "r") as f:
        filtered = filter(lambda x: x, f.read().split("\n"))
        pairs = map(lambda x: x.split(), filtered)
        for a, b in pairs:
            dictionary[a] = b

    return dictionary


def read_jmdict(file):
    """Extract only the kanji and readings from JMdict"""

    readings = []
    keb_pattern = r"<keb>(.*)</keb>"
    reb_pattern = r"<reb>(.*)</reb>"
    with open(file, "r") as f:
        kanji = []
        for line in f.read().split("\n"):
            keb = re.match(keb_pattern, line)
            reb = re.match(reb_pattern, line)
            if keb:
                kanji.append(keb.group(1))
            if reb:
                if len(kanji) > 0:
                    readings.append((reb.group(1), kanji.pop()))
                    kanji[:] = []
                else:
                    readings.append((reb.group(1), ""))

    return readings


def get_mora(word, hiragana, katakana, small_hiragana, small_katakana):
    mora = []
    for c in word:
        if c in small_hiragana:
            combined = mora[-1] + c
            if combined in hiragana:
                mora[-1] = combined
            else:
                mora.append(c)
        elif c in small_katakana:
            combined = mora[-1] + c
            if combined in katakana:
                mora[-1] = combined
            else:
                mora.append(c)
        else:
            mora.append(c)

    return mora


def get_reading_singular(moras, hiragana, katakana):
    reading = ""
    special = {"ー": "-", "〜": "~", "、": ",", "・": "."}

    tsu = False
    for mora in moras:
        if mora in hiragana:
            if tsu:
                r = hiragana[mora]
                reading += r[0] + r
                tsu = False
            else:
                reading += hiragana[mora]
        elif mora in katakana:
            if tsu:
                r = katakana[mora].upper()
                reading += r[0] + r
                tsu = False
            else:
                reading += katakana[mora].upper()
        elif mora in special:
            reading += special[mora]
        elif mora in ["っ", "ッ"]:
            tsu = True
        else:
            pass
    return reading


def get_readings(jmdict, hiragana, katakana, small_hiragana, small_katakana):
    readings = []
    for word, kanji in jmdict:
        moras = get_mora(word, hiragana, katakana, small_hiragana, small_katakana)

        reading = get_reading_singular(moras, hiragana, katakana)
        readings.append((reading, word, kanji))

    return readings


def main():
    hiragana = get_kana(HIRAGANA)
    katakana = get_kana(KATAKANA)

    small_hiragana = get_kana(SMALL_HIRAGANA)
    small_katakana = get_kana(SMALL_KATAKANA)

    jmdict_all = read_jmdict(JMdict)
    readings = get_readings(
        jmdict_all, hiragana, katakana, small_hiragana, small_katakana
    )

    readings = filter(lambda x: len(x[0]) > 2, readings)
    readings = sorted(set(readings))

    with open(savefile, "w") as f:
        for reading, word, kanji in readings:
            f.write(f"{reading}\t{word}")
            if kanji:
                f.write(f"\t{kanji}")
            f.write("\n")


if __name__ == "__main__":
    main()
