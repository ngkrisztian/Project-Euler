# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
sum_1 = 0
sum_2 = 0

for i in range(1,101):
    sum_1 = sum_1 + i

sum_1 = sum_1 ** 2

for j in range(1,101):
    sum_2 =sum_2 + j ** 2

sum_3 = sum_1 - sum_2

print(sum_3)