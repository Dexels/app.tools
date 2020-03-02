#!/usr/bin/env python3

from argparse import ArgumentParser
from sys import exit

from apptools.image.core.parser import spec_parser
from apptools.image.image.distribute import distribute


def main():
    parser = ArgumentParser(allow_abbrev=False, parents=[spec_parser])
    parser.add_argument('-t',
                        '--target',
                        help='only build for a specific target')
    args = parser.parse_args()

    distribute(args.spec, args.target)

    exit()


if __name__ == "__main__":
    main()
