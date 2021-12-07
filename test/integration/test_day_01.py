from unittest import TestCase
from unittest.mock import MagicMock

from save_christmas import q1
from save_christmas.q1 import q1_p1, q1_p2


class TestDay1(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sample_data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        cls.input_data = q1.parse_input('../../inputs/input_01.txt')

    def test_part_1_with_sample(self):
        q1.parse_input = MagicMock(return_value=self.sample_data)
        self.assertEqual(q1_p1(), 7)

    def test_part_1(self):
        q1.parse_input = MagicMock(return_value=self.input_data)
        self.assertEqual(q1_p1(), 1548)

    def test_part_2_with_sample(self):
        q1.parse_input = MagicMock(return_value=self.sample_data)
        self.assertEqual(q1_p2(), 5)

    def test_part_2(self):
        q1.parse_input = MagicMock(return_value=self.input_data)
        self.assertEqual(q1_p2(), 1589)
