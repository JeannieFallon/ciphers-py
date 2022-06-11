import sys


UPPER_MAP = 65
LOWER_MAP = 97
ALPHA_LEN = 26


def get_cipher(msg, *, key) -> str:
    cipher = ""

    for c in msg:
        if c.isalpha():
            # Map ASCII value onto zero-based indices
            map_val = UPPER_MAP if c.isupper() else LOWER_MAP
            alpha_idx = ord(c) - map_val
            # Shift index by key value, and wrap around alphabet
            shift_idx = (alpha_idx + key) % ALPHA_LEN
            c = chr(shift_idx + map_val)
        cipher += c

    return cipher
