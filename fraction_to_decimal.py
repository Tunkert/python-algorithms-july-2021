class FractionToDecimal:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def decimal_value(self):
        decimal = self.numerator / self.denominator
        return decimal
