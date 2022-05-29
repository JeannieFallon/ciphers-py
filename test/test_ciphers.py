import sys

import pytest

import src.ciphers

class TestCiphers:
    def test_ciphers(self):
        rc = src.ciphers.main()
        assert rc == 0
