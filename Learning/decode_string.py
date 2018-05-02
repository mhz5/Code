def decode_string(s):
    opp_brack = {}
    brack_stack = []
    for i, c in enumerate(s):
        if c == '[':
            brack_stack.append(i)
        elif c == ']':
            idx = brack_stack.pop()
            opp_brack[idx] = i

    return decode(s, 0, len(s), opp_brack)


def decode(s, start, end, opp_brack):
    res = ''
    i = start
    while i < end:
        c = s[i]
        k = 0
        while '0' <= c <= '9':
            k = 10 * k + int(c)
            i += 1
            c = s[i]

        if c == '[':
            opp_i = opp_brack[i]
            res += k * decode(s, i + 1, opp_i, opp_brack)
            i = opp_i + 1
        else:
            res += c
            i += 1

    return res

s1 = "3[a]2[bc]"
print decode_string(s1)
