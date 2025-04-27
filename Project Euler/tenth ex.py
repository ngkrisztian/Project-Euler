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

s = 2
i = 3
while j < 2000000:
    if is_prime(j):
        s = s + j
    j = j + 2
print(s)