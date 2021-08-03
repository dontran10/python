import labs.lab1 as lab1


class TestLab1:
    def test_is_leap_year_if_evenly_divided_for_400(self):
        assert lab1.is_leap(2000) is True

    def test_is_not_leap_year_if_evenly_divided_for_100_but_not_400(self):
        assert lab1.is_leap(1900) is False

    def test_is_leap_year_if_evenly_divided_for_4_but_not_100(self):
        assert lab1.is_leap(2004) is True
