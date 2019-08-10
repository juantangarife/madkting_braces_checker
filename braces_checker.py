dict_openers = {
    '(': ')',
    '[': ']',
    '{': '}'
}


def braces_checker(strings_array):
    for s in strings_array:
        print(_check_string(s))


def _check_string(s):
    len_s = len(s)
    if len_s < 2 or len_s % 2 != 0:
        return 0
    elif len(s) == 2:
        if s in ['()', '{}', '[]']:
            return 1
    else:
        pass


if __name__ == '__main__':
    test_input = [
        '{(})([]}',
        '{}()[]',
        '{({}[])}'
    ]
    braces_checker(test_input)
