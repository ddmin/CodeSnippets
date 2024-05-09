#!/usr/bin/env sh

TXT="txt"
JP_WORDLIST="JP_JMDICT_WORDLIST.txt"
TRIMMED_SAVE_FILE="JP_TRIMMED_JMDICT_WORDLIST.txt"
HIRAGANA_SAVE="JP_HIRAGANA_WORDLIST.txt"

# Remove Duplicates
# 1) reverse line order (to prioritize kanji)
# 2) remove first column duplicates (awk)
# 3) reverse line order back

# Remove Duplicate Readings
tac "$TXT/$JP_WORDLIST" | awk '!_[$1]++' | tac > "$TXT/$TRIMMED_SAVE_FILE"

# Hiragana Wordlist
# 1) Remove lines containing uppercase letters

# Only Hiragana Words
sed '/[[:upper:]]/d' "$TXT/$TRIMMED_SAVE_FILE" > "$TXT/$HIRAGANA_SAVE"
