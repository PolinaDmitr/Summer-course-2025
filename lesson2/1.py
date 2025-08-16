l = list()
print(id(l))
l.append(1)
print(l, id(l))
l.append(2)
print(l)
m = [1, 2, 3, 4]
print(m)
a = m.pop()
print(m, a)
m.remove(2)
print(m)
b = m
print(id(m), id(b))
b = m.copy()
print(id(m), id(b))

l.insert(0, '7859')
print(l)
l[0] = '567'
print(l)
s = '567'
s = '9' + s[1:]
print(s)
l.reverse()
print(l)
l[-1] = 89
l.sort()
print(l)
print(l[1])
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix)
print(matrix[0][1])

k = tuple()
print(k)
k = (1, 3, 5, 7, 8, 9, 1)
print(k)
print(len(k), k.count(1))

s = set()
s.add(1)
s.add(1)
s.add(2)
print(s)
print(2 in s)
print({4, 5, 6})

d = dict(a=3, b=4)
print(d)
print(d['a'])
print(d.values())
print(d.keys())
d = { 1 : (1, 2, 3), 2 : (4, 5, 6)}
print(d[1])
print(d.get(3))

print('1234567'[2:6])
print('123456'[-1])
print('123456'[:-5:-1])
print(matrix)
print(matrix[0])
print(matrix[1])
