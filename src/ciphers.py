import sys
import argparse


def rot13(args) -> int:
    plain = args.message
    print(f"Running ROT13 cipher on message: {plain}")

    return 0


def caesar(args) -> int:
    plain = args.message
    print(f"Running Caesar cipher on message: {plain}")

    return 0


def vigenere(args) -> int:
    plain = args.message
    print(f"Running Vigenere cipher on message: {plain}")

    return 0


def main() -> int:
    parser = argparse.ArgumentParser("main parser")
    cipher_parsers = parser.add_subparsers(
        dest="cipher", required=True, help="ciphers parsers"
    )

    msg_parser = argparse.ArgumentParser(add_help=False)
    msg_parser.add_argument('--message', '-m', required=True)

    rot13_parser = cipher_parsers.add_parser("rot13", parents=[msg_parser], help="rot13 help")
    rot13_parser.set_defaults(func=rot13)

    args = parser.parse_args()
    args.func(args)

    return 0


if __name__ == "__main__":
    sys.exit(main())
