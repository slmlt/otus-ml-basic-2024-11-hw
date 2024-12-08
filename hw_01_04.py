mapper = [
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I')
]


def to_roman(number: int, roman: str = "") -> str:
    next_decimal, next_roman = next(((decimal, roman) for (decimal, roman) in mapper if number - decimal >= 0), (0, ""))
    return roman if next_decimal == 0 else to_roman(number - next_decimal, roman + next_roman)


result = to_roman(int(input()))
print(result if result else '0')
