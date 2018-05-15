import unittest
from exercises import beginner


class BeginnerExercises(unittest.TestCase):

    def test_flatten_level1(self):
        l1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(beginner.flatten_list(l1, 1), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_flatten_level2(self):
        l2 = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]
        flattened_lvl2 = beginner.flatten_list(l2, 2)
        flatten_lvl0 = beginner.flatten_list(flattened_lvl2, 1)
        self.assertEqual(flatten_lvl0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_merge_dicts(self):
        a = {'x': [1, 2, 3], 'y': 1, 'z': set([1, 2, 3]), 'w': 'qweqwe', 't': {'a': [1, 2]}, 'm': [1]}
        b = {'x': [4, 5, 6], 'y': 4, 'z': set([4, 2, 3]), 'w': 'asdf', 't': {'a': [3, 2]}, 'm': "wer"}
        res = {'x': [1, 2, 3, 4, 5, 6], 'y': 5, 'z': set([1, 2, 3, 4]), 'w': 'qweqweasdf', 't': {'a': [1, 2, 3, 2]},
               'm': ([1], "wer")}
        m_dicts = beginner.merge_dicts(a, b)
        self.assertEqual(m_dicts, res)
