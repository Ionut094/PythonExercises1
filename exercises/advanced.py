from itertools import combinations


def get_nodes(tree):
    if tree is not None:
        yield tree[0]
    left = tree[1]
    right = tree[2]
    if left is not None:
        yield from get_nodes(left)
    if right is not None:
        yield from get_nodes(right)


def subsets(set_of_ints):
    for i in range(0, len(set_of_ints) + 1):
        for subset in combinations(set_of_ints, i):
            yield set(subset)


class SingletonMeta(type):
    def __call__(cls, *args, **kwargs):
        try:
            return cls.instance
        except AttributeError:
            instance = type.__call__(cls, *args, **kwargs)
            cls.instance = instance
            return instance


class Singleton(metaclass=SingletonMeta):
    pass


if __name__ == '__main__':
    for node in get_nodes(('b', ('a', None, None), ('z', ('c', None, None), ('zz', None, None)))):
        print(node)

    print(list(subsets({1, 2, 3})))

    singletons = [Singleton() for i in range(0, 99)]
    singleton = Singleton()
    print(all(elem is singleton for elem in singletons))
