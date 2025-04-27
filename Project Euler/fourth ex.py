# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009=99*91.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(n):
    n = str(n)
    list_forward = []
    for digit in n:
        list_forward.append(digit)
    l = len(list_forward) - 1
    list_backward = []
    while l >= 0:
        list_backward.append(list_forward[l])
        l = l - 1
    if list_forward == list_backward:
        return True
    else:
        return False

i = 999
largest_palindrome = 0

while i >= 100:
    j = 999
    while j >= 100:
        palindrome = i * j
        if palindrome <= largest_palindrome:
            break
        if is_palindrome(palindrome):
            largest_palindrome = palindrome
        j = j -1
    i = i -1


print(largest_palindrome)
