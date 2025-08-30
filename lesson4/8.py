from string import digits, ascii_uppercase

#0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ
a = digits + ascii_uppercase
print(a)

#11Hx05+3Fx54x8+Gxxx9
for x in range(18):
    n1 = 5 * 1 + x * 18 ** 2 + 17 * 18 ** 3 + 1 * 18 ** 4 + 1 * 18 ** 5
    n2 = 8 + x * 18 + 4 * 18 ** 2 + 5 * 18 ** 3 + x * 18 ** 4 + 15 * 18 ** 5 + 3 * 18 ** 6
    n3 = 9 + x * 18 + x * 18 ** 2 + x * 18 ** 3 + 16 * 18 ** 4
    n = n1 + n2 + n3
    if n % 14 == 0:
        print(x, n // 14)
        break

for x in range(18):
    n = int(f'11H{a[x]}05', 18) + int(f'3F{a[x]}54{a[x]}8', 18) + int(f'G{a[x]}{a[x]}{a[x]}9', 18)
    if n % 14 == 0:
        print(x, n // 14)
        break


