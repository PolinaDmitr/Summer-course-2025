def f(n):
    c = 0
    while n != 0:
        char = n % 36
        #xor как вариант
        if int(char % 3 == 0) + int(char % 5 == 0) == 1:
            c += 1
        n //= 36
    return c



#30⋅36231+18⋅6101−3⋅3645−2357
numb = 30 * 36 ** 231 + 18 * 6 ** 101 - 3 * 36 ** 45 - 2357
print(f(numb))