# What is the 10001 st prime number?

def is_prime(n):
    if n == 1:
        return False
    if n == 1:
        return True
    if n % 2 == 0 and n != 2:
        return False
    else:
        i = 3
        while i ** 2 <= n:
            if n % i == 0:
                return False
            else:
                i = i + 2
        if i ** 2  > n:
            return True

index = 0
j = 1
while True:
    if is_prime(j):
        index = index + 1
    j = j + 1
    if index == 10001:
        break

print(j - 1)