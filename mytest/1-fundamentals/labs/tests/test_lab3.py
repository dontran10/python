import labs.lab3 as lab3


class TestLab3:
    def test_find_champion_and_runner_up_normal_case(self):
        assert lab3.find_champion_and_runner_up([15, 67, 12, 86, 75]) == [86, 75]

    def test_find_champion_and_runner_up_when_all_scores_are_the_same(self):
        assert lab3.find_champion_and_runner_up([80, 80, 80, 80]) == [80]
