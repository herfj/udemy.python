def rec(i):
    if i < 1:
        return i
    print(i)
    rec(i - 1)
rec(6)