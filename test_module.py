import pytest

from time_calculator import add_time


class TestAddTime:
    def test_probate(self):
        assert 0 == 0

    def test_2(self):
        assert add_time("3:00 PM", "3:10") == f'6:10 PM'

