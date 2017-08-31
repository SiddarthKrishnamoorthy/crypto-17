#!/bin/env python3

from itertools import cycle
import string

in1 = cycle(string.ascii_lowercase[:26]); in2 = cycle(string.ascii_lowercase[:26]); in3 = cycle(string.ascii_lowercase[:26]);
ki = {}

for i in range(0, 26):
    a = next(in1)
    ki[a] = {}
    for j in range(0, 26):
        ki[a][next(in2)] = next(in3)
    next(in3)

def encode(text_from_a_great_book, txt):
    txt = txt.lower()
    cipher = [ b for b in text_from_a_great_book.lower() if b in string.ascii_lowercase[:26] ]
    cipher_text = [x for x in txt]
    for i in range(len(txt)):
        if txt[i] in ki.keys():
            cipher_text[i] = ki[txt[i]][cipher[i]]
    return "".join(cipher_text)
