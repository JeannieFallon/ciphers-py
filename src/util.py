import sys


UPPER_MAP = 65
LOWER_MAP = 97
ALPHA_LEN = 26


def get_cipher(msg, *, keyval=None, keyword=None) -> str:
    # FIXME validate keyval > 0
    if keyval or keyval == 0:
        # ROT13 and Caesar
        return get_single_shift_cipher(msg, keyval)
    elif keyword:
        # Vigenere
        return get_multi_shift_cipher(msg, keyword)
    else:
        raise


def get_single_shift_cipher(msg, keyval) -> str:
    ciphertext = ""

    for c in msg:
        if c.isalpha():
            c = get_cipher_letter(c, shift=keyval)
        ciphertext += c

    return ciphertext


def get_multi_shift_cipher(msg, keyword) -> str:
    ciphertext = ""
    shift_vals = get_shift_vals(keyword)
    len_vals = len(shift_vals)

    i = 0
    for c in msg:
        if c.isalpha():
            shift_val = shift_vals[i % len_vals]
            c = get_cipher_letter(c, shift=shift_val)
            i += 1
        ciphertext += c

    return ciphertext


def get_shift_vals(keyword) -> list:
    shift_vals = []

    for c in keyword:
        shift_vals.append(get_alpha_idx(c))

    return shift_vals


def get_cipher_letter(c, *, shift) -> chr:
    # Get zero-based index in English alphabet
    alpha_idx = get_alpha_idx(c)
    # Shift index by key value, and wrap around alphabet
    shift_idx = (alpha_idx + shift) % ALPHA_LEN
    # Get shifted alphabet character
    return get_alpha_char(c, shift_idx)


def get_alpha_idx(c) -> int:
    # Map ASCII value onto zero-based indices
    return ord(c) - (UPPER_MAP if c.isupper() else LOWER_MAP)


def get_alpha_char(c, idx) -> chr:
    # Map zero-based index onto ASCII value
    return chr(idx + (UPPER_MAP if c.isupper() else LOWER_MAP))
