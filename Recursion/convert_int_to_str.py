"""
Convert an integer to a string in some base between binary and hexadecimal.

- Base case: n < 10
- Reduce the original number to a series of single-digit number
- Look up the corresponding str of the single digit to convert the number to a string
- Concatenate the single digit together to form the final result
"""


def convert_int_to_str(num: int, base: int)->str:
    str_digits = "0123456789ABCDEF"
    if num < base:
        return str_digits[num]
    else:
        return convert_int_to_str(num // 2, base) + str_digits[num % base]

