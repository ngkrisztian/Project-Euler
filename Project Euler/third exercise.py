# Third exercise: What is the largest prime factor of the number 600851475143

def largest_factor(n):
    while n % 2 == 0:
        n = n / 2
    i = 3
    while i ** 2 <= n:
        while n % i ==0:
            n = n / i
        i = i+2
    return n

lp_factor = largest_factor(600851475143)
print(lp_factor)

