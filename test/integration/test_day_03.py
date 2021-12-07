from unittest import TestCase
from unittest.mock import MagicMock

from save_christmas import q3
from save_christmas.q3 import q3_p1, q3_p2


class TestDay3(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sample_data = ['00100',
                           '11110',
                           '10110',
                           '10111',
                           '10101',
                           '01111',
                           '00111',
                           '11100',
                           '10000',
                           '11001',
                           '00010',
                           '01010', ]
        cls.input_data = q3.parse_input('../../inputs/input_03.txt')

    def test_part_1_sample(self):
        q3.parse_input = MagicMock(return_value=self.sample_data)
        self.assertEqual(q3_p1(), 198)

    def test_part_1(self):
        q3.parse_input = MagicMock(return_value=self.input_data)
        self.assertEqual(q3_p1(), 2743844)

    def test_part_2_sample(self):
        q3.parse_input = MagicMock(return_value=self.sample_data)
        self.assertEqual(q3_p2(), -1)

    def test_part_2(self):
        q3.parse_input = MagicMock(return_value=self.input_data)
        self.assertEqual(q3_p2(), -1)
