from copy import deepcopy


def flatten_list(list_a, max_depth):
    if (max_depth == 0) | (not (type(list_a[0]) is list)):
        return list_a
    else:
        return flatten_list([inner_element for inner_list in list_a for inner_element in inner_list], max_depth - 1)


def _list_merge_op(l1, l2):
    l1_copy = deepcopy(l1)
    l1_copy.extend(l2)
    return l1_copy


def _set_merge_op(s1, s2):
    return s1 | s2


def _str_merge_op(str1,str2):
    return str1 + str2


def _number_merge_op(num1,num2):
    return num1 + num2


def _misc_merge_op(elem1, elem2):
    return elem1, elem2


def merge_dicts(dict1, dict2):

    merge_op = {
        list: _list_merge_op,
        set: _set_merge_op,
        str: _str_merge_op,
        int: _number_merge_op,
        float: _number_merge_op,
        dict: merge_dicts
    }

    result = {}

    for key in dict1:
        elem1 = dict1.get(key)
        elem2 = dict2.get(key)
        operator = merge_op.get(type(elem1))
        if type(elem1) is not type(elem2):
            operator = _misc_merge_op

        result[key] = operator(elem1, elem2)

    return result


_path_of_files = '../static'


def _read_dicts_from_file(file_path=_path_of_files + '/input.txt'):
    dicts = []
    with open(file_path, 'r') as in_file:
        for line in in_file:
            keys = line.split()[::2]
            values = list(map(lambda s: int(s), line.split()[1::2]))
            dict_from_line = dict(zip(keys, values))
            dicts.append(dict_from_line)
    return dicts


def _get_value_for_lowest_key(dict_a):
    return dict_a.get(min(dict_a.keys()))


def _compare_dicts(dict1, dict2):
    if len(dict1) == 0:
        return True
    else:
        val1 = _get_value_for_lowest_key(dict1)
        val2 = _get_value_for_lowest_key(dict2)
        if val1 == val2:
            new_dict1 = {k: v for (k, v) in dict1 if v != val1}
            new_dict2 = {k: v for (k, v) in dict1.items() if v != val2}
            return _compare_dicts(new_dict1, new_dict2)
        else:
            return val1 > val2


def _write_to_output(unsorted_list,sorted_list,file_path = _path_of_files + '/output.txt'):
    with open(file_path,'w') as out_file:
        for dict1 in sorted_list:
            out_file.write(str(unsorted_list.index(dict1))+' ')


def _bubble_sort(list_of_dicts):
    for i in range(0, len(list_of_dicts)):
        for j in range(0, i):
            if _compare_dicts(list_of_dicts[j], list_of_dicts[i]):
                list_of_dicts[i], list_of_dicts[j] = list_of_dicts[j], list_of_dicts[i]


def sort_dicts_and_write_to_out():
    list_of_dicts = _read_dicts_from_file()
    sorted_list = deepcopy(list_of_dicts)
    _bubble_sort(sorted_list)
    _write_to_output(list_of_dicts, sorted_list)


if __name__ == '__main__':
    list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    list2 = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]
    print(flatten_list(list1, 1))
    print(flatten_list(list2, 1))

    a = {'x': [1, 2, 3], 'y': 1, 'z': set([1, 2, 3]), 'w': 'qweqwe', 't': {'a': [1, 2]}, 'm': [1]}
    b = {'x': [4, 5, 6], 'y': 4, 'z': set([4, 2, 3]), 'w': 'asdf', 't': {'a': [3, 2]}, 'm': "wer"}
    res = {'x': [1, 2, 3, 4, 5, 6], 'y': 5, 'z': {1, 2, 3, 4}, 'w': 'qweqweasdf', 't': {'a': [1, 2, 3, 2]}, 'm': ([1], "wer")}
    m_dicts = merge_dicts(a, b)
    print(m_dicts)
    print(m_dicts == res)

    dictionaries = _read_dicts_from_file()
    print(dictionaries)
    print(_get_value_for_lowest_key(dictionaries[2]))
    print(_compare_dicts(dictionaries[1], dictionaries[2]))

    sort_dicts_and_write_to_out()

    pass
