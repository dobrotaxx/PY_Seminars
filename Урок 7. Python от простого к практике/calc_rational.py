from fractions import Fraction

def calc_value(frac1, frac2, sign):
    if sign == '+':
        result = Fraction(frac1) + Fraction(frac2)
    elif sign == '-':
        result = Fraction(frac1) - Fraction(frac2)
    elif sign == '*':
        result = Fraction(frac1) * Fraction(frac2)
    else:
        result = Fraction(frac1) / Fraction(frac2)  
    return result