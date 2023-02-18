def int_to_roman(num):
    roman_numerals = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M"
    }
    result = ""
    for value, numeral in sorted(roman_numerals.items(), reverse=True):
        while num >= value:
            result += numeral
            num -= value
    return result

# Get input from user
number = int(input("Enter an integer: "))

# Convert integer to Roman numeral
roman_numeral = int_to_roman(number)

# Print the result
print(f"The Roman numeral for {number} is {roman_numeral}")
