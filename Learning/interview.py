def is_valid(route_number):
    if len(route_number) < 9:
        return False
    try:
        digits = [int(c) for c in list(route_number)]
    except ValueError:
        return False

    weights = [3, 7, 1]
    sum = 0
    for i, d in enumerate(digits):
        sum += d * weights[i % 3]
    return sum % 10 == 0


tests = [
    '00000',
    'aoei',
    '000000001',
    '333333333',
    
    '000000000',
    '990000000',
    '111000025',
]

results = [is_valid(t) for t in tests]
print results
