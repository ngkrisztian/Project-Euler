for a in range (1,999):
    for b in range(1,999):
        c = 1000 - a - b
        if a ** 2 + b ** 2 == c ** 2 and c > 0:
            print(a * b * c)
