import sys
import errno

import pytest

import src.ciphers
import src.util

TEST_MESSAGES = [
    ("Curiouser and curiouser!", "Phevbhfre naq phevbhfre!"),
    ("xyzabc XYZABC", "klmnop KLMNOP"),
    ("l! M@ n#", "y! Z@ a#"),
    ("1 2 3 4 5", "1 2 3 4 5"),
]
# TODO block keyval % 26 = 0
TEST_KEYVALS = [
    (0, "aBc XyZ"),
    (1, "bCd YzA"),
    (10, "kLm HiJ"),
    (25, "zAb WxY"),
    (26, "aBc XyZ"),
    (42, "qRs NoP"),
]

DEFAULT_MESSAGE = "aBc XyZ"
DEFAULT_KEYVAL = 13


class Args:
    def __init__(self, *, message=None, keyval=None):
        self.message = message
        self.keyval = keyval


class TestCiphers:
    def test_noarg(self):
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            rc = src.ciphers.main()
        assert pytest_wrapped_e.type == SystemExit
        assert pytest_wrapped_e.value.code == errno.ENOENT


class TestRot13:
    @pytest.mark.parametrize("message,cipher", TEST_MESSAGES)
    def test_messages(self, capsys, message, cipher):
        args = Args(message=message)

        rc = src.ciphers.rot13(args)
        assert rc == 0

        output = capsys.readouterr()
        assert message in output.out
        assert cipher in output.out


class TestCaesar:
    @pytest.mark.parametrize("message,cipher", TEST_MESSAGES)
    def test_messages(self, capsys, message, cipher):
        args = Args(message=message, keyval=DEFAULT_KEYVAL)

        rc = src.ciphers.caesar(args)
        assert rc == 0

        output = capsys.readouterr()
        assert message in output.out
        assert f"{DEFAULT_KEYVAL}" in output.out
        assert cipher in output.out

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
    @pytest.mark.parametrize("message,cipher", TEST_MESSAGES)
    def test_messages(self, capsys, message, cipher):
        args = Args(message=message)

        rc = src.ciphers.vigenere(args)
        assert rc == 0

        output = capsys.readouterr()
        assert message in output.out
        # TODO
        # assert cipher in output.out
