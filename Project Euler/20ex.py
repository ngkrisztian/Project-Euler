def factorial_function(n):
    product = 1
    i = 1
    while i <= n:
        product = product * i
        i = i + 1
    return product


number = str(factorial_function(100))

s = 0
for digit in number:
    s = s + int(digit)

print(s)

