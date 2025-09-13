def extended_gcd(a,b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = extended_gcd(b, a % b)
        return d, y, x - y * (a // b)

a = int(input("a: "))
b = int(input("b: "))
print(extended_gcd(a, b))
