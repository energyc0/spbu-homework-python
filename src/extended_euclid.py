def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    d, y, x = extended_gcd(b, a % b)
    return d, x, (d - a * x) // b


a = int(input("a: "))
b = int(input("b: "))
print(extended_gcd(a, b))
