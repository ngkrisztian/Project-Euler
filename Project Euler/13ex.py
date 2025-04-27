with open('summing', 'r') as file:
    numbers = file.readlines()


numbers = [line.strip('\n') for line in numbers]
numbers = [int(line) for line in numbers]

sum_numbers = sum(numbers)

result = str(sum_numbers)[:10]

print(result)
