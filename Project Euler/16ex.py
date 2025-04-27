# What is the sum of the digits of the number 2^1000

def sum_of_digit(n):
    n = str(n)
    digit_sum = 0
    for digit in n:
        digit_sum = digit_sum + int(digit)
    return digit_sum

print(sum_of_digit(2 ** 1000))

