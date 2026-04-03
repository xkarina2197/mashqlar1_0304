# 1-misol
func = lambda a, b: max(a, b)
print(func(219, 36))

# 2-misol
func = lambda x: x if x < 0 else -x
print(func(7))


# 3-misol
func = lambda a, b, x:  (a + b + x)
print(func(8, 3, 9))

# 4-misol
func = lambda a, b: a % b
print(func(17, 5))


# 5-misol
func = lambda x: x * 9/5 +32

t = 100
res = func(t)
print(res)


# 6-misol
func = lambda k, x: 0 if k == x else min(k, x)
print(func(18, 15))

# 7-misol
func = lambda x: 'juft' if x % 2 == 0 else 'toq'
print(func(83))

# 8-misol
func = lambda k, x: k * x
print(func(17, 8))

# 9-misol
func = lambda k, m, x: max(k, m, x)
print(func(17, 7, 33))

# 10-misol
func = lambda x: len(str(x))
print(func(27))

# 11-misol
func = lambda k,x: True if k % x == 0 else False
print(func(97, 23))

# 12-misol
func = lambda k, x: k * x
print(func(7, 3.14))

# 13-misol
func = lambda k, x: (k - x) ** 2
print(func(26,7))


# 15-misol
func = lambda k, m, x: 'teng tomonli' if k == m and m == x else 'teng yonli' if k == m or k == x or m == x else 'oddiy'

res = func(1, 1, 1)
print(res)

res = func(10, 10, 5)
print(res)

res = func(12, 11, 11)
print(res)

