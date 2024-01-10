#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    argc = len(argv) - 1

    if argc == 0:
        print("{} arguments.".format(argc))
    elif argc == 1:
        print("{} argument:".format(argc))
    else:
        print("{} arguments:".format(argc))

    if argc >= 1:
        argc = 0
        for arg in argv:
            if argc != 0:
                print("{}: {}".format(argc, arg))
            argc += 1
