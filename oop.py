class RomanConverter:
    def __init__(self, number):
        if not isinstance(number, int):
            raise TypeError("Input must be an integer.")
        if number <= 0 or number > 3999:
            raise ValueError("Number must be between 1 and 3999.")
        self.number = number

    def to_roman(self):
        values = [
            (1000, "M"), (900, "CM"),
            (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"),
            (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"),
            (5, "V"), (4, "IV"),
            (1, "I")
        ]

        num = self.number
        roman = ""

        for value, symbol in values:
            while num >= value:
                roman += symbol
                num -= value

        return roman

try:
    n = int(input("Enter an integer (1–3999): "))
    converter = RomanConverter(n)
    print("Roman numeral:", converter.to_roman())
except Exception as e:
    print("Error:", e)