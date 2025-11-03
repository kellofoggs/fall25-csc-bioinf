from decimal import Decimal, ROUND_HALF_UP

class Rounding:

    @staticmethod
    def round_decimal(value: Decimal, digits: int=3) -> Decimal:
        # Used because for whatever reason python defaults to nearest even when a 5 is after the cutoff decimal
        precision = Decimal('1.' + '0' * digits)
        return value.quantize(precision, rounding=ROUND_HALF_UP)
