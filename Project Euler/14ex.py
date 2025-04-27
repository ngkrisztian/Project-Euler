def collatz_iter(n):
    count = 0
    while n >= 1:
        if n == 1:
            count = count + 1
            return count
        elif n % 2 == 0:
            n = n / 2
            count = count + 1
        elif n % 2 == 1:
            n = 3 * n + 1
            count = count + 1

longest_chain = [0, 0]

for i in range (1, 1000001):
    if collatz_iter(i) > longest_chain[0]:
        longest_chain[0] = collatz_iter(i)
        longest_chain[1] = i

print(longest_chain)


