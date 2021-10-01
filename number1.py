#тут b является ссылкой на a
a = [4, 8, 6, 1]
b = a
a.sort()
print(a)
print(b)

#тут b является отдельным списком
a = [4, 8, 6, 1]
b = a[:]
a.sort()
print(a)
print(b)