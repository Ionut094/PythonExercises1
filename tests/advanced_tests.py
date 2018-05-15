import unittest
import advanced


class AdvancedExercises(unittest.TestCase):

    def test_get_nodes(self):
        tree = ('b', ('a', None, None), ('z', ('c', None, None), ('zz', None, None)))
        res = ['b', 'a', 'z', 'c', 'zz']
        self.assertEqual(list(advanced.get_nodes(tree)), res)

    def test_subsets(self):
        s1 = {1, 2, 3}
        res = [{1, 2, 3}, {2, 3}, {1, 3}, {3}, {1, 2}, {2}, {1}, set()]
        subsets = list(advanced.subsets(s1))
        self.assertTrue(all(elem in subsets for elem in res))

    def test_singleto(self):
        singletons = [advanced.Singleton() for i in range(0, 99)]
        singleton = advanced.Singleton()
        self.assertTrue(all(elem is singleton for elem in singletons))

