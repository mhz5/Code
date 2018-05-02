def fibonacci(n):
    arr = [0, 1]

    while len(arr) <= n + 1:
        arr.append(arr[-1] + arr[-2])

    return arr[n]


for i in range(20):
    print fibonacci(i)
