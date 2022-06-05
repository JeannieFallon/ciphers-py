import sys
import errno

import pytest

import src.ciphers


class Args:
    def __init__(self, *, plaintext=None):
        self.plaintext = plaintext


class TestCiphers:
    def test_noarg(self):
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            rc = src.ciphers.main()
        assert pytest_wrapped_e.type == SystemExit
        assert pytest_wrapped_e.value.code == errno.ENOENT

    def test_rot13(self):
        plain = "This is test plaintext"
        args = Args(plaintext=plain)
        rc = src.ciphers.rot13(args)
        assert rc == 0
        # TODO get console output
