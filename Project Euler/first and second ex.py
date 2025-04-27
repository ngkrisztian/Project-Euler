# First exercise: Find the sum of all the multiples of 3 or 5 below 1000
s = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        s += i
print(s)


# Second exercise: By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

    # fibonacci_list = [1, 1]
    # number = 0
    # while True:
        # n = len(fibonacci_list)
        # number = fibonacci_list[n-2] + fibonacci_list[n-1]
        # if number <= 4000000:
            # fibonacci_list.append(number)
        # else:
            # break
    # print(fibonacci_list)

    # result = 0
    # for i in fibonacci_list:
        # if i % 2 == 0:
            # result = result + i

    # print(result)

def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n >= 3:
        return fibonacci(n-1) + fibonacci(n-2)

s = 0
k = 1
while fibonacci(k) <= 4000000:
    if fibonacci(k) % 2 == 0:
        s = s + fibonacci(k)
    k = k + 1

print(s)




