def reverse(s):
    return recurse_reverse(s, '')


def recurse_reverse(s, final_s):
    if s == '':
        return final_s

    return recurse_reverse(s[:-1], final_s + s[-1])


s = 'aoeihtns'
assert reverse(s) == 'snthieoa'
