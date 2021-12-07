from save_christmas.q1 import count_increased, q1_p1, q1_p2


def day_1_sample():
    return [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def test_day_01_part_01_sample():
    assert count_increased(day_1_sample()) == 7


def test_day_01_part_01():
    assert q1_p1() == 1548


def test_day_01_part_02():
    assert q1_p2() == 1589
