import sys
import errno

import pytest

import src.ciphers
import src.util

TEST_MESSAGES = ["Curiouser and curiouser!", "xyzabc XYZABC", "a! B@ c#", "1 2 3 4 5"]


class Args:
    def __init__(self, *, message=None):
        self.message = message


class TestCiphers:
    def test_noarg(self):
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            rc = src.ciphers.main()
        assert pytest_wrapped_e.type == SystemExit
        assert pytest_wrapped_e.value.code == errno.ENOENT


class TestRot13:
    @pytest.mark.parametrize("message", TEST_MESSAGES)
    def test_messages(self, capsys, message):
        args = Args(message=message)

        rc = src.ciphers.rot13(args)
        assert rc == 0

        output = capsys.readouterr()
        assert message in output.out


class TestCaesar:
    @pytest.mark.parametrize("message", TEST_MESSAGES)
    def test_messages(self, capsys, message):
        args = Args(message=message)

        rc = src.ciphers.caesar(args)
        assert rc == 0

        output = capsys.readouterr()
        assert message in output.out


class TestVigenere:
    @pytest.mark.parametrize("message", TEST_MESSAGES)
    def test_messages(self, capsys, message):
        args = Args(message=message)

        rc = src.ciphers.vigenere(args)
        assert rc == 0

        output = capsys.readouterr()
        assert message in output.out
