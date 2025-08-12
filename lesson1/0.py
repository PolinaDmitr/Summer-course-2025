import sys

print('Hello')
a = 500
b = a
print(id(a), id(b))
print(sys.getrefcount(b))
print(a is b)
a = '7'
print(id(a), id(b))
print(a is b)
print(a, b)
print(sys.getrefcount(b))
print(sys.getrefcount(500))
print(b is 500)
print('-')
x = 500
x = x - 200
y = 300
print(id(x), id(y))
print(x is y, x == y)

x = 200
y = x
x = x - 5
print(x, y)
print('----')
x = 500
x = x - 300
y = 200
print(id(x), id(y))
print(x is y, x == y)
print(sys.getrefcount(y))

a = "nwnk"
n = 'njwhewh'
m = -68738
l = 64784.837
print(type(a), type(n), type(m), type(l))
a = a + "befe"
print(id("nwnk"), id(a))
print('----')
l = []
print(l, id(l))
l.append('7')
print(l, id(l))



