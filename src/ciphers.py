import sys
import errno
import argparse

import util


ROT13_KEYVAL = 13


def rot13(args) -> int:
    msg = args.message

    print(f"Running ROT13 cipher on message:\n{msg}")
    cipher = util.get_cipher(msg, keyval=ROT13_KEYVAL)
    print(f"Ciphertext is:\n{cipher}")

    return 0


def caesar(args) -> int:
    msg = args.message
    keyval = args.keyval

    if keyval <= 0 or keyval % 26 == 0:
        raise ValueError("Key value must not be zero or divisible by 26")

    print(f"Running Caesar cipher with shift value {keyval} on message:\n{msg}")
    cipher = util.get_cipher(msg, keyval=keyval)
    print(f"Ciphertext is:\n{cipher}")

    return 0


def vigenere(args) -> int:
    msg = args.message
    keyword = args.keyword

    if not keyword.isalpha():
        raise ValueError("Key word must contain alphabet letters only")

    print(f"Running Vigenere cipher with keyword {keyword} on message:\n{msg}")
    cipher = util.get_cipher(msg, keyword=keyword)
    print(f"Ciphertext is:\n{cipher}")

    return 0


def main():
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
    caesar_parser.add_argument(
        "--keyval",
        "-k",
        required=True,
        type=int,
        help="the shift value for each letter",
    )
    caesar_parser.set_defaults(func=caesar)

    vigenere_parser = cipher_parsers.add_parser(
        "vigenere", parents=[msg_parser], help="vigenere help"
    )
    vigenere_parser.add_argument(
        "--keyword",
        "-k",
        required=True,
        help="the keyword used to generate sequence of shift values",
    )
    vigenere_parser.set_defaults(func=vigenere)

    args = parser.parse_args()

    try:
        args.func(args)
    except ValueError as e:
        print(e)
        sys.exit(errno.EINVAL)
    except BaseException as e:
        print(e)
        sys.exit(errno.ESRCH)


if __name__ == "__main__":
    main()
