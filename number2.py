import random
a = []
summ = 0
mult = 1
maxx = -2e9
pos_max = -1
minn = 2e9
pos_min = -1
povt = dict()
for i in range(0, 100):
    n = random.randint(-1e3, 1e3)
    try:
        povt[n] += 1
    except KeyError:
        povt[n] = 1

    a.append(n)
    summ += n
    mult *= n
    if n > maxx:
        maxx = n
        pos_max = i
    if n < minn:
        minn = n
        pos_min = i
print("Сумма = ", summ)
print("Произведение = ", mult)
print("Максимум = ", maxx)
print("Повторения:")
for i in povt:
    if povt[i] > 1:
        print(i, povt[i])
print("Список, в котором поменяны местами самый большой и самый маленький элементы:")
t = a[pos_max]
a[pos_max] = a[pos_min]
a[pos_min] = t
print(a)

#Задание 4
f = open('text.txt', 'w')
f.write("Сумма = " + str(summ))
f.write("\nПроизведение = " + str(mult))
f.write("\nМаксимум = " + str(maxx))
f.write("\nПовторения:")
for i in povt:
    if povt[i] > 1:
        f.write("\n" + str(i) + " " + str(povt[i]))
f.write("\nСписок, в котором поменяны местами самый большой и самый маленький элементы:\n")
f.write(str(a))