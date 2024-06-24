#!/usr/bin/python3
""" prints the ASCII alphabet"""

for i in range(ord('a'), ord('z') +1):
    print("{}".format(chr(i)), end="")
