s = '1234567'
print(s[0], type(s[0]))
print(s[0], s[1], s[2])
l = s[0:3]
print(s, l)
print(s[::])
print(s[0:7:2])
print(s[-1])
print(s[::-1])
l = '123' + '456'
print(len(l))
print(l * 2)
print(1 + int(l))

a = '1234'
b = '456'
print(a > b)
print(ord('1'), ord('4'))
print('123' < '1234')
print('123' == '123')

print('1' in a, '1' in b)

print(a.count('1'))
a = 'aa09aaa8aap89'
print(a.count('aa'))
print(max(1, 5, 8))
print(min(5, 4, 8))
print(max('12347yh'))
print(ord('y'), ord('Y'))
print(ord(' '))
print(chr(89))

print(a.index('09', 1, 9))
print(a.split('a'))

