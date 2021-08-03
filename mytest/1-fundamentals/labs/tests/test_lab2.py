import labs.lab2 as lab2


class TestLab2:
    def test_find_angle_MBC_with_a_equal_b(self):
        assert lab2.find_angle_MBC(10, 10) == 45

    def test_find_angle_MBC_in_round_up_case(self):
        assert lab2.find_angle_MBC(3, 4) == 37

    def test_find_angle_MBC_in_round_down_case(self):
        assert lab2.find_angle_MBC(2, 11) == 10
