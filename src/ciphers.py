import sys
import argparse


def rot13(args) -> int:
    plain = args.plaintext
    print(f'Running ROT13 cipher on plaintext: {plain}')

    return 0


def main() -> int:
    parser = argparse.ArgumentParser('main parser')
    cipher_parsers = parser.add_subparsers(dest='cipher', required=True, help='ciphers parsers')

    rot13_parser = cipher_parsers.add_parser('rot13', help='rot13 help')
    rot13_parser.add_argument('plaintext', help='plain text to be enciphered')
    rot13_parser.set_defaults(func=rot13)

    args = parser.parse_args()
    args.func(args)

    return 0


if __name__ == '__main__':
    sys.exit(main())
