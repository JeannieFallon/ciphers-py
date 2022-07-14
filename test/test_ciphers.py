import sys
import errno
import subprocess

import pytest

import src.ciphers
import src.util


"""Tuples contain 4 items: message, ROT13 ciphertext, Caesar ciphertext using keyval20, and Vigenere ciphertext
using keyword "Alice"
"""
TEST_MESSAGES = [
    (
        "Curiouser and curiouser!",
        "Phevbhfre naq phevbhfre!",
        "Wolciomyl uhx wolciomyl",
        "Cfzksudmt eno kwvizcuir!",
    ),
    ("xyzabc XYZABC", "klmnop KLMNOP", "rstuvw RSTUVW", "xjhcfc IGBEBN"),
    ("l! M@ n#", "y! Z@ a#", "f! G@ h#", "l! X@ v#"),
    ("1 2 3 4 5", "1 2 3 4 5", "1 2 3 4 5", "1 2 3 4 5"),
]
# TODO block keyval % 26 = 0
TEST_KEYVALS = [
    (1, "bCd YzA"),
    (10, "kLm HiJ"),
    (25, "zAb WxY"),
    (26, "aBc XyZ"),
    (42, "qRs NoP"),
]

DEFAULT_MESSAGE = "aBc XyZ"
DEFAULT_ROT13 = 13
DEFAULT_CAESAR = 20
DEFAULT_VIGENERE = "Alice"

INVALID_KEYVALS = [-1, 0]
INVALID_KEYWORDS = ["a bc", "123abc", "abc!@#"]

# FIXME
TOOL = "bin/ciphers"


class Args:
    def __init__(self, *, message=None, keyval=None, keyword=None):
        self.message = message
        self.keyval = keyval
        self.keyword = keyword


class TestCiphers:
    def test_noarg(self):
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            rc = src.ciphers.main()
        assert pytest_wrapped_e.type == SystemExit
        assert pytest_wrapped_e.value.code == errno.ENOENT


# Use full executable to test validation and error handling
class TestValidation:
    @pytest.mark.parametrize("keyval", INVALID_KEYVALS)
    def test_invalid_keyvals(self, capsys, keyval):
        pass
        # rc = subprocess.call(f'{TOOL} -m "{DEFAULT_MESSAGE}" -k {keyval}', shell=True)
        # assert rc == errno.EINVAL

        # output = capsys.readouterr()
        # assert "Key value must be greater than 0" in output.out

    def test_invalid_keywords(self):
        pass
        # try:
        #    subprocess.check_output("dir /f",shell=True,stderr=subprocess.STDOUT)
        # except subprocess.CalledProcessError as e:
        #    assert "Key word" in output


class TestRot13:
    @pytest.mark.parametrize("message,rot13,caesar,vigenere", TEST_MESSAGES)
    def test_messages(self, capsys, message, rot13, caesar, vigenere):
        args = Args(message=message)

        rc = src.ciphers.rot13(args)
        assert rc == 0

        output = capsys.readouterr()
        assert message in output.out
        assert rot13 in output.out


class TestCaesar:
    @pytest.mark.parametrize("message,rot13,caesar,vigenere", TEST_MESSAGES)
    def test_messages(self, capsys, message, rot13, caesar, vigenere):
        args = Args(message=message, keyval=DEFAULT_CAESAR)

        rc = src.ciphers.caesar(args)
        assert rc == 0

        output = capsys.readouterr()
        assert message in output.out
        assert f"{DEFAULT_CAESAR}" in output.out
        assert caesar in output.out

    @pytest.mark.parametrize("keyval,cipher", TEST_KEYVALS)
    def test_keyvals(self, capsys, keyval, cipher):
        args = Args(message=DEFAULT_MESSAGE, keyval=keyval)

        rc = src.ciphers.caesar(args)
        assert rc == 0

        output = capsys.readouterr()
        assert DEFAULT_MESSAGE in output.out
        assert f"{keyval}" in output.out
        assert cipher in output.out


class TestVigenere:
    @pytest.mark.parametrize("message,rot13,caesar,vigenere", TEST_MESSAGES)
    def test_messages(self, capsys, message, rot13, caesar, vigenere):
        args = Args(message=message, keyword=DEFAULT_VIGENERE)

        rc = src.ciphers.vigenere(args)
        assert rc == 0

        output = capsys.readouterr()
        assert message in output.out
        assert vigenere in output.out
