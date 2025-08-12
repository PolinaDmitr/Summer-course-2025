a = 11
b = 6
print(a + b)
print(a / b)
c = a // b
o = a % b
print(c)   #целочисленное
print(o)
# делимое = делитель * частное + остаток
print(a == c * b + o)
a = -a
c = a // b
o = a % b
print(c)   #целочисленное
print(o)
print(a == c * b + o)
#-11 = -2 * 6 + 1
a1 = -a % 10
a2 = a % 10
a3 = abs(a) % 10
print(a1, a2, a3)
print(a ** 3)
print((-a) ** 0.5)
print(2 != 3)
print('-----')
a = True
b = False
print('not', not a)
print('and', a and b)
print('or', a or b)
a = 5   #101
b = 1   #001
print(bin(~a))
print(bin(a & b))
print(bin(a | b))
print(bin(a ^ b))
print('----')
s = 'bwui'
b = s.isnumeric() and int(s)
c = not s.isnumeric() or int(s)
print(bool(0), bool(5))
print(b, c)

print('---')
b = 10 / 3
print(b)
c = 3.333333333335
print(b == c)
d = 0.000001
print(d > abs(b - c))
