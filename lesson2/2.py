for i in '1234':
    print(i)
print('-----')
a = range(8)
print(type(a))
for i in a:
    print(i)
print('------')
for a in range(1, 11, 2):
    print(a)

l = [1, 4, 5, 6, 7, 8]
for i in l:
    print(i, i ** 2)

for _ in range(3):
    print('****')

a = 0
while a < 10:
    print(a)
    a += 2

s = 0
a = int(input())
while a != 0:
    s += a
    a = int(input())
print(s)

a = 0
while a < 3:
    print('***')
    a += 1

l = [3, 4, 5]
a = 0
while a < len(l):
    print(l[a])
    a += 1

ss = {4, 5, 6, 7, 8}
for i in ss:
    print(i)

