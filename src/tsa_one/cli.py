#!/usr/bin/env python3
from argparse import ArgumentParser

from tsa_one.duplicate import detect_duplicates


def main():
    """The main CLI entrypoint."""
    parser = ArgumentParser(prog="tsa_one-cli")
    parser.add_argument(
        "lst", nargs="*", default=[], help="Space-delimited list of items to parse"
    )
    args = parser.parse_args()

    res = detect_duplicates(args.lst)
    print(res)


if __name__ == "__main__":
    main()
