#5150+598−x
def f(n):
    c = 0
    while n != 0:
        if n % 5 == 0:
            c += 1
        n //= 5
    return c


x_max = -1
zero_max = -1
numb = 5 ** 150 + 5 ** 98
for x in range(1, 2006):
    zero = f(numb - x)
    if zero >= zero_max:
        x_max = x
        zero_max = zero
print(x_max)
