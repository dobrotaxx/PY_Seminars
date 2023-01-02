import view
import calc_rational
import calc_complex

def calc():
    mode = view.get_mode()
    num1, sign, num2 = view.get_data()
    if mode == 1:
        result = calc_rational.calc_value(num1, num2, sign)
    else:
        result = calc_complex.calc_value(num1, num2, sign)
    view.view_data(result)