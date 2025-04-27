def number_to_text(n):
    texts_1_to_19 = {
        1: 'one', 2: 'two', 3: 'three', 4: 'four',
        5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
        9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
        13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
        16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
    }

    tens = {
        20: 'twenty', 30: 'thirty', 40: 'forty',
        50: 'fifty', 60: 'sixty', 70: 'seventy',
        80: 'eighty', 90: 'ninety'
    }

    if 1 <= n < 20:
        return texts_1_to_19[n]
    elif 20 <= n < 100:
        return tens[n - n % 10] + texts_1_to_19.get(n % 10, '')
    elif 100 <= n < 1000:
        hundreds = texts_1_to_19[n // 100] + ' hundred'
        remainder = n % 100
        if remainder == 0:
            return hundreds
        else:
            return hundreds + ' and ' + number_to_text(remainder)
    elif n == 1000:
        return 'one thousand'
    else:
        return ''

# Main loop to count letters
result = ''
for i in range(1, 1001):
    words = number_to_text(i)
    result += words.replace(' ', '').replace('-', '')  # strip spaces and hyphens

print(result)
print(len(result))