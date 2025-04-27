# Triangle

with open('triangle.txt', 'r') as file:
    triangle = file.readlines()

triangle = [line.strip('\n') for line in triangle]

triangle = [line.split(" ") for line in triangle]

triangle_with_numbers = []

for line in triangle:
    line = [int(text) for text in line]
    triangle_with_numbers.append(line)



def max_sum(row, col):
   if row == len(triangle_with_numbers) - 1:
       return triangle_with_numbers[row][col]
   left = max_sum(row + 1, col)
   right = max_sum(row + 1, col + 1)
   return triangle_with_numbers[row][col] + max(left, right)

print(max_sum(0, 0))
