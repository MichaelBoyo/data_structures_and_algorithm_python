from unittest import TestCase

from max_sum_of_sub_arr import max_sum


class Test(TestCase):
    def test_max_sum(self):
        self.assertEqual(max_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(max_sum([5, 4, -1, 7, 8]), 23)
        self.assertEqual(max_sum([1]), 1)
        self.assertEqual(max_sum([-2, -1]), -1)
