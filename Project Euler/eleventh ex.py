# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20 x 20 grid?

def list_rotation_left(list_local, n):
    new_list = list_local[n:] + list_local[:n]
    return new_list

def list_rotation_right(list_local, n):
    new_list = list_local[len(list_local)-n:] + list_local[:len(list_local)-n]
    return new_list


with open("numbers", "r") as file:
    grid = file.readlines()

grid = [line.strip("\n") for line in grid]

grid = [line.split(" ") for line in grid]

grid_with_numbers = []
for line in grid:
    line = [int(text) for text in line]
    grid_with_numbers.append(line) # Transforming the grid

print(grid_with_numbers)

product_ups = []

for index, line in enumerate(grid_with_numbers):
    if index < 17:
        line = [a * b * c * d for a, b, c, d in zip(grid_with_numbers[index], grid_with_numbers[index + 1], grid_with_numbers[index + 2], grid_with_numbers[index + 3])]
        product_ups.append(line)

max_product_up = []
for line in product_ups:
    product = max(line)
    max_product_up.append(product)

first_product = max(max_product_up) # Maximum of the products in direction up

product_verticals = []

for line in grid_with_numbers:
    line = [line[i] * line[i+1] * line[i + 2] * line[i + 3] for i in range(0, 16)]
    product_verticals.append(line)


max_product_verticals = []
for line in product_verticals:
    product = max(line)
    max_product_verticals.append(product)

second_product = max(max_product_verticals) # Maximum of the products in direction right


product_diagonals_right = []

for index, line in enumerate(grid_with_numbers):
    if index < 17:
        line = [
            a * b * c * d
            for a, b, c, d in zip(
                grid_with_numbers[index][:17],
                list_rotation_left(grid_with_numbers[index + 1], n=1)[:17],
                list_rotation_left(grid_with_numbers[index + 2], n=2)[:17],
                list_rotation_left(grid_with_numbers[index + 3], n=3)[:17]
            )
        ]
        product_diagonals_right.append(line)

max_product_diagonals_right = []
for line in product_diagonals_right:
    product = max(line)
    max_product_diagonals_right.append(product)

third_product = max(max_product_diagonals_right) # Maximum of the products diagonally right



product_diagonals_left = []

for index, line in enumerate(grid_with_numbers):
    if index < 17:
        line = [
            a * b * c * d
            for a, b, c, d in zip(
                grid_with_numbers[index][3:],
                list_rotation_right(grid_with_numbers[index + 1], n=1)[3:],
                list_rotation_right(grid_with_numbers[index + 2], n=2)[3:],
                list_rotation_right(grid_with_numbers[index + 3], n=3)[3:]
            )
        ]
        product_diagonals_left.append(line)

print(product_diagonals_left)

max_product_diagonals_left = []
for line in product_diagonals_left:
    product = max(line)
    max_product_diagonals_left.append(product)

fourth_product = max(max_product_diagonals_left) # Maximum of the products diagonally right

print(first_product)
print(second_product)
print(third_product)
print(fourth_product)
result = max([first_product, second_product, third_product, fourth_product])

print(result)