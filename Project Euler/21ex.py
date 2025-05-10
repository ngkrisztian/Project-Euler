def list_of_divisors(n):
    divisors = [1]
    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            divisors.append(i)
            divisors.append(n // i)
        i = i + 1
    return divisors

def sum_of_divisors(n):
    local_divisors = list_of_divisors(n)
    s = 0
    for divisor in local_divisors:
        s = s + divisor
    return s



def is_amicable_number(a, b):
    if sum_of_divisors(a) == b and sum_of_divisors(b) == a:
        return True


result = 0
for a in range(1,10000):
    b = sum_of_divisors(a)
    if sum_of_divisors(b) == a and a != b:
        result = result + a + b


print(result // 2)
