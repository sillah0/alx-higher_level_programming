#!/usr/bin/python3
""" prints the ASCII alphabet expect  q and e"""

for letter in range(97, 123):
    if chr(letter) != 'q' and chr(letter) != 'e':
        print("{}".format(chr(letter)).lower(), end="")