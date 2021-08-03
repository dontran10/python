import labs.lab4 as lab4


class TestLab4:
    def test_find_student_average_mark_normal_case(self):
        assert lab4.find_student_average_mark({'Tom': [45, 54, 51]}, 'Tom') == 50.00

    def test_find_student_average_mark_round_down_case(self):
        assert lab4.find_student_average_mark({'Tom': [46, 54.5, 53.5]}, 'Tom') == 51.33

    def test_find_student_average_mark_round_up_case(self):
        assert lab4.find_student_average_mark({'Tom': [45.5, 54.5, 52]}, 'Tom') == 50.67
