from save_christmas.q2 import q2_p1, q2_p2


def day_02_sample():
    return ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']


def test_day_02_part_01():
    assert q2_p1() == 2322630


def test_day_02_part_02():
    assert q2_p2() == 2105273490
