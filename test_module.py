import pytest

from time_calculator import add_time


class TestAddTime:
    def test_1(self):
        assert 0 == 0

    def test_2(self):
        assert add_time("3:00 PM", "3:10") == "6:10 PM"

    def test_3(self):
        assert add_time("11:30 AM", "2:32", "Monday") == "2:02 PM, Monday"

    def test_4(self):
        assert add_time("11:43 AM", "00:20") == "12:03 PM"

    def test_5(self):
        assert add_time("10:10 PM", "3:30") == "1:40 AM (next day)"

    def test_6(self):
        assert add_time("11:43 PM", "24:20", "tueSday") == "12:03 AM, Thursday (2 days later)"

    def test_7(self):
        assert add_time("6:30 PM", "205:12") == "7:42 AM (9 days later)"



