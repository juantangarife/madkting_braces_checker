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
            return 0
    else:
        opener = s[0]
        if opener in dict_openers:
            next_char = s[1]
            if next_char == dict_openers[opener]:
                return _check_string(s[2:])
            else:
                closer_char = dict_openers[opener]
                last_closer_index = s.rfind(closer_char)
                if last_closer_index >= 0:
                    prov = list(s)
                    prov[0] = ''
                    prov[last_closer_index] = ''
                    return _check_string(''.join(prov))
                else:
                    return 0
        else:
            return 0


if __name__ == '__main__':
    test_input = [
        '{(})([]}',
        '{}()[]{}',
        '{({}[])}',
        '{()}[]'
    ]
    braces_checker(test_input)
