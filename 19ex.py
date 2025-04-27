# Sundays

# Creating a list which contains every first day of every year
# 0 means Monday, ..., 6 means Sunday

first_days = []
starting_point = 0
for i in range(1900, 2000):
    if i % 4 == 0 and i % 100 != 0:
        first_day = (starting_point + 366) % 7
        first_days.append(first_day)
        starting_point = first_day
    elif i % 400 == 0:
        first_day = (starting_point + 366) % 7
        first_days.append(first_day)
        starting_point = first_day
    else:
        first_day = (starting_point + 365) % 7
        first_days.append(first_day)
        starting_point = first_day

print(first_days)


# x is the starting point
def sundays_in_in_normal_year(x):
    count = 0
    if x == 6:
        count = count + 1
    x = (x + 31) % 7
    if x == 6:
        count = count + 1
    x = (x + 28) % 7
    if x == 6:
        count = count + 1
    x = (x + 31) % 7
    if x == 6:
        count = count + 1
    x = (x + 30) % 7
    if x == 6:
        count = count + 1
    x = (x + 31) % 7
    if x == 6:
        count = count + 1
    x = (x + 30) % 7
    if x == 6:
        count = count + 1
    x = (x + 31) % 7
    if x == 6:
        count = count + 1
    x = (x + 31) % 7
    if x == 6:
        count = count + 1
    x = (x + 30) % 7
    if x == 6:
        count = count + 1
    x = (x + 31) % 7
    if x == 6:
        count = count + 1
    x = (x + 30) % 7
    if x == 6:
        count = count + 1
    return count

def sundays_in_in_leap_year(x):
    count = 0
    if x == 6:
        count = count + 1
    x = (x + 31) % 7
    if x == 6:
        count = count + 1
    x = (x + 29) % 7
    if x == 6:
        count = count + 1
    x = (x + 31) % 7
    if x == 6:
        count = count + 1
    x = (x + 30) % 7
    if x == 6:
        count = count + 1
    x = (x + 31) % 7
    if x == 6:
        count = count + 1
    x = (x + 30) % 7
    if x == 6:
        count = count + 1
    x = (x + 31) % 7
    if x == 6:
        count = count + 1
    x = (x + 31) % 7
    if x == 6:
        count = count + 1
    x = (x + 30) % 7
    if x == 6:
        count = count + 1
    x = (x + 31) % 7
    if x == 6:
        count = count + 1
    x = (x + 30) % 7
    if x == 6:
        count = count + 1
    return count

sundays = 0
for index, first_day in enumerate(first_days):
    if (index + 1901) % 4 == 0 and (index + 1901) % 100 != 0:
        sundays = sundays + sundays_in_in_leap_year(first_day)
    elif (index + 1901) % 400 == 0:
        sundays = sundays + sundays_in_in_leap_year(first_day)
    else:
        sundays = sundays + sundays_in_in_normal_year(first_day)
print(sundays)