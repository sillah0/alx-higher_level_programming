#!/usr/bin/python3
import sys


def print_arguments():
    num_args = len(sys.argv) - 1
    print(f"{''if num_args != 1 else ''} {num_args} arguments", end='')
    if num_args == 0:
        print(".")
    else:
        print(":")
    for i in range(1, num_args + 1):
        print(f"{i}: {sys.argv[i]}")


if __name__ == "__main__":

    print_arguments()
