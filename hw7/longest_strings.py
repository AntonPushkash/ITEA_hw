"""
    Написать функцию, которая принимает список строк,
    и возвращает другой список, содержащий все самые длинные строки.

    Например:
    [in] ['a', 'asd', 'bd', 'q', 'dsq']
    [out] ['asd', 'dsq']
"""
input_list = ['a', 'asd', 'bd', 'q', 'dsq']


def longest_strings(input_list):
    sort_list = sorted(input_list, key=len)
    longest = sort_list[-1]
    out_list = []
    for word in sort_list:
        if len(word) == len(longest):
            out_list.append(word)
    return out_list


tmp = longest_strings(input_list)
print(tmp)

t_1 = ['x']
assert longest_strings(t_1) == ['x']

t_2 = ['abc',  'eeee',  'abcd', 'dcd']
assert longest_strings(t_2) == ['eeee', 'abcd']

t_3 = ['a', 'abc', 'cbd', 'zzzzzz', 'a', 'abcdef', 'asasa', 'aaaaaa']
assert longest_strings(t_3) == ['zzzzzz', 'abcdef', 'aaaaaa']

t_4 = ['enyky', 'benyky', 'yely', 'varennyky']
assert longest_strings(t_4) == ['varennyky']

t_5 = ['abacaba', 'abacab', 'abac', 'xxxxxx']
assert longest_strings(t_5) == ['abacaba']

print('All right!')
