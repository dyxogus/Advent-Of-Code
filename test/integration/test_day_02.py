from unittest import TestCase
from unittest.mock import MagicMock

from save_christmas import q2
from save_christmas.q2 import q2_p1, q2_p2


class TestDay2(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sample_data = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']
        cls.input_data = q2.parse_input('../../inputs/input_02.txt')

    def test_part_1_sample(self):
        q2.parse_input = MagicMock(return_value=self.sample_data)
        self.assertEqual(q2_p1(), 150)

    def test_part_1(self):
        q2.parse_input = MagicMock(return_value=self.input_data)
        self.assertEqual(q2_p1(), 2322630)

    def test_part_2_sample(self):
        q2.parse_input = MagicMock(return_value=self.sample_data)
        self.assertEqual(q2_p2(), 900)

    def test_part_2(self):
        q2.parse_input = MagicMock(return_value=self.input_data)
        self.assertEqual(q2_p2(), 2105273490)
