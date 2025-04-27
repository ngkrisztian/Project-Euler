# What is the smallest positive number that is evenly divisible by all the numbers from 1 to 20?

def factorial(m):
    fac = 1
    for l in range (1, m+1):
        fac = fac * l
    return fac



def is_divisible(k):
    i=1
    while i <= 20:
        if k % i ==0:
            i = i + 1
        else:
            break
    if i == 21:
        return True
    else:
        return False


def smallest_multiple(n):
    j = 3
    while is_divisible(n):
        n = n / 2
    n = n * 2

    while j <= 19:
        while is_divisible(n):
            n = n / j
        n = n * j
        j = j + 2
    return n

a = factorial(20)
print(a)
print(smallest_multiple(a))