import sys
import argparse

import util


def rot13(args) -> int:
    msg = args.message
    print(f"Running ROT13 cipher on message:\n{msg}")

    cipher = ""
    for c in msg:
        if c.isalpha():
            map_val = util.UPPER_MAP if c.isupper() else util.LOWER_MAP
            alpha_idx = ord(c) - map_val
            shift_idx = (alpha_idx + 13) % util.ALPHA_LEN
            c = chr(shift_idx + map_val)

        cipher += c

    print(f"Ciphertext is:\n{cipher}")
    return 0


def caesar(args) -> int:
    msg = args.message
    print(f"Running Caesar cipher on message: {msg}")
    return 0


def vigenere(args) -> int:
    msg = args.message
    print(f"Running Vigenere cipher on message: {msg}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser("main parser")
    cipher_parsers = parser.add_subparsers(
        dest="cipher", required=True, help="ciphers parsers"
    )

    msg_parser = argparse.ArgumentParser(add_help=False)
    msg_parser.add_argument("--message", "-m", required=True)

    rot13_parser = cipher_parsers.add_parser(
        "rot13", parents=[msg_parser], help="rot13 help"
    )
    rot13_parser.set_defaults(func=rot13)

    caesar_parser = cipher_parsers.add_parser(
        "caesar", parents=[msg_parser], help="caesar help"
    )
    caesar_parser.set_defaults(func=caesar)

    vigenere_parser = cipher_parsers.add_parser(
        "vigenere", parents=[msg_parser], help="vigenere help"
    )
    vigenere_parser.set_defaults(func=vigenere)

    args = parser.parse_args()
    args.func(args)

    return 0


if __name__ == "__main__":
    sys.exit(main())
