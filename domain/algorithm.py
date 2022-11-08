integer_roman = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

def decimal_to_roman(number):
    roman = ''
    if number > 0 and number < 3999:
        for i, r in integer_roman:
            while number >= i:
                roman += r
                number -= i
    else:
        if number > 3999:
            return ""
    
    print(characters_uniques(roman))
    return roman


def characters_uniques(nRoman):
    arrayLetters = []
    for char in nRoman:
        if char not in arrayLetters:
            arrayLetters.append(char)
        
    return arrayLetters