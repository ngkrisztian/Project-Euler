# What is the value of the first triangle number to have over five hundred divisors?

def triangular(n):
    return (n * (n + 1)) / 2

def counting_divisors(n):
    count = 2
    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            count = count + 2
        i = i + 1
    return count

j = 1

while True:
    triangle = triangular(j)
    if counting_divisors(triangle) <= 500:
        j = j + 1
    else:
        break

print(triangle)