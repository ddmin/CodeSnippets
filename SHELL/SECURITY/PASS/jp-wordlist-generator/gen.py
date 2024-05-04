#!/usr/bin/python

import re
import itertools

dice = [i for i in range(1, 7)]
rolls = [''.join(map(lambda x: str(x), p)) for p in itertools.product(dice, repeat=7)]

JMdict = "JMdict_e"
helper = "JP_EFF_LARGE_WORDLIST.txt"
savefile = "JP_JMDICT_WORDLIST.txt"
exceptions = ["・", "＝", "。", "ゐ", "ゑ", "ヰ", "ヱ", "々", "ゞ", "ゝ", "ゝ", "、", "ヶ", "ﾀ", "ﾋ", "ヮ", "ゎ"]

jp_to_en = {
    "あ": "a",
    "い": "i",
    "え": "e",
    "う": "u",
    "お": "o",
    "ア": "a",
    "イ": "i",
    "ウ": "u",
    "エ": "e",
    "オ": "o",
    "か": "ka",
    "き": "ki",
    "く": "ku",
    "け": "ke",
    "こ": "ko",
    "カ": "ka",
    "キ": "ki",
    "ケ": "ke",
    "ク": "ku",
    "コ": "ko",
    "さ": "sa",
    "し": "shi",
    "す": "su",
    "せ": "se",
    "そ": "so",
    "サ": "sa",
    "シ": "shi",
    "ス": "su",
    "セ": "se",
    "ソ": "so",
    "は": "ha",
    "ひ": "hi",
    "ふ": "hu",
    "へ": "he",
    "ほ": "ho",
    "ハ": "ha",
    "ヒ": "hi",
    "フ": "hu",
    "ヘ": "he",
    "ホ": "ho",
    "ら": "ra",
    "り": "ri",
    "る": "ru",
    "れ": "re",
    "ろ": "ro",
    "ラ": "ra",
    "リ": "ri",
    "ル": "ru",
    "レ": "re",
    "ロ": "ro",
    "た": "ta",
    "ち": "chi",
    "つ": "tsu",
    "て": "te",
    "と": "to",
    "タ": "ta",
    "チ": "chi",
    "ツ": "tsu",
    "テ": "te",
    "ト": "to",
    "な": "na",
    "に": "ni",
    "ぬ": "nu",
    "ね": "ne",
    "の": "no",
    "ナ": "na",
    "ニ": "ni",
    "ヌ": "nu",
    "ネ": "ne",
    "ノ": "no",
    "ま": "ma",
    "み": "mi",
    "む": "mu",
    "め": "me",
    "も": "mo",
    "マ": "ma",
    "ミ": "mi",
    "ム": "mu",
    "メ": "me",
    "モ": "mo",
    "や": "ya",
    "ゆ": "yu",
    "よ": "yo",
    "ヤ": "ya",
    "ユ": "yu",
    "ヨ": "yo",
    "わ": "wa",
    "を": "wo",
    "ワ": "wa",
    "ヲ": "wo",
    "ん": "n",
    "ン": "n",

    "が": "ga",
    "ぎ": "gi",
    "ぐ": "gu",
    "げ": "ge",
    "ご": "go",
    "ざ": "za",
    "じ": "ji",
    "ず": "zu",
    "ぜ": "ze",
    "ぞ": "zo",
    "だ": "da",
    "ぢ": "di",
    "づ": "dzu",
    "で": "de",
    "ど": "do",
    "ば": "ba",
    "び": "bi",
    "ぶ": "bu",
    "べ": "be",
    "ぼ": "bo",
    "ぱ": "pa",
    "ぴ": "pi",
    "ぷ": "pu",
    "ぺ": "pe",
    "ぽ": "po",

    "ガ": "ga",
    "ギ": "gi",
    "グ": "gu",
    "ゲ": "ge",
    "ゴ": "go",
    "ザ": "za",
    "ジ": "ji",
    "ズ": "zu",
    "ゼ": "ze",
    "ゾ": "zo",
    "ダ": "da",
    "ヂ": "di",
    "ヅ": "dzu",
    "デ": "de",
    "ド": "do",
    "バ": "ba",
    "ビ": "bi",
    "ブ": "bu",
    "ベ": "be",
    "ボ": "bo",
    "パ": "pa",
    "ピ": "pi",
    "プ": "pu",
    "ペ": "pe",
    "ポ": "po",

    "きゃ": "gya",
    "きゅ": "gyu",
    "きょ": "gyo",
    "しゃ": "sha",
    "しゅ": "shu",
    "しょ": "sho",
    "ちゃ": "cha",
    "ちゅ": "chu",
    "ちょ": "cho",
    "にゃ": "nya",
    "にゅ": "nyu",
    "にょ": "nyo",
    "ひゃ": "hya",
    "ひゅ": "hyu",
    "ひょ": "hyo",
    "みゃ": "mya",
    "みゅ": "myu",
    "みょ": "myo",
    "りゃ": "rya",
    "りゅ": "ryu",
    "りょ": "ryo",
    "じゃ": "ja",
    "じゅ": "ju",
    "じょ": "jo",
    "びゃ": "bya",
    "びゅ": "byu",
    "びょ": "byo",
    "ぴゃ": "pya",
    "ぴゅ": "pyu",
    "ぴょ": "pyo",

    "キャ": "gya",
    "キュ": "gyu",
    "キョ": "gyo",
    "シャ": "sha",
    "シュ": "shu",
    "ショ": "sho",
    "チャ": "cha",
    "チュ": "chu",
    "チョ": "cho",
    "ニャ": "nya",
    "ニュ": "nyu",
    "ニョ": "nyo",
    "ビャ": "hya",
    "ビュ": "hyu",
    "ビョ": "hyo",
    "ミャ": "mya",
    "ミュ": "myu",
    "ミョ": "myo",
    "リャ": "rya",
    "リュ": "ryu",
    "リョ": "ryo",
    "ジャ": "ja",
    "ジュ": "ju",
    "ジョ": "jo",
    "ビャ": "bya",
    "ビュ": "byu",
    "ビョ": "byo",
    "ピャ": "pya",
    "ピュ": "pyu",
    "ピョ": "pyo",

    "ヴァ": "va",
    "ヴィ": "vi",
    "ヴ": "vu",
    "ヴェ": "ve",
    "ヴォ": "vo",
    "ウィ": "wi",
    "ウェ": "we",
    "ウォ": "uo",
    "ファ": "fa",
    "フィ": "fi",
    "フェ": "fe",
    "フォ": "fo",
    "チェ": "che",
    "ディ": "di",
    "ドゥ": "dou",
    "ティ": "ti",
    "トゥ": "tou",
    "ジェ": "je",
    "シェ": "she",

    "ぁ": "a",
    "ぃ": "i",
    "ぅ": "u",
    "ぇ": "e",
    "ぉ": "o",
    "ァ": "a",
    "ィ": "i",
    "ゥ": "u",
    "ェ": "e",
    "ォ": "o",
    "ゃ": "ya",
    "ゅ": "yu",
    "ょ": "yo",
    "ャ": "ya",
    "ュ": "yu",
    "ョ": "yo",
}

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
            small = ["ょ", "ゅ", "ゃ", "ョ", "ュ", "ャ", "ぁ", "ぃ", "ぅ", "ぇ", "ぉ", "ァ", "ィ", "ゥ", "ェ", "ォ"]
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
                elif m in ['ー', '〜']:
                    if roman:
                        roman += roman[-1]
                else:
                    en = jp_to_en[m]
                    roman += en

            words.append(roman)

    with open(helper, 'r') as f:
        lines = f.read().split('\n')
        lines = list(filter(lambda x: not x.startswith('#') and len(x) > 0, lines))
        helper_words = list(map(lambda x: x.split()[1], lines))

    with open(savefile, 'w') as f:
        n = -1
        for roll, word, japanese in zip(rolls, words, jp):
            n += 1
            f.write(f'{roll}\t{word}\t{japanese}\n')

        for n, roll in enumerate(rolls[n+1:]):
            helper_word = helper_words[n % len(helper_words)]
            f.write(f'{roll}\t{helper_word}\n')



if __name__ == "__main__":
    main()
