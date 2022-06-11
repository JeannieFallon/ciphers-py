import sys
import errno

import pytest

import src.ciphers
import src.util


class Args:
    def __init__(self, *, message=None):
        self.message = message


class TestCiphers:
    def test_noarg(self):
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            rc = src.ciphers.main()
        assert pytest_wrapped_e.type == SystemExit
        assert pytest_wrapped_e.value.code == errno.ENOENT

    def test_rot13(self):
        plain = "This is a test message"
        args = Args(message=plain)
        rc = src.ciphers.rot13(args)
        assert rc == 0
        # TODO get console output

    def test_caesar(self):
        plain = "This is a test message"
        args = Args(message=plain)
        rc = src.ciphers.caesar(args)
        assert rc == 0

    def test_vigenere(self):
        plain = "This is a test message"
        args = Args(message=plain)
        rc = src.ciphers.vigenere(args)
        assert rc == 0
