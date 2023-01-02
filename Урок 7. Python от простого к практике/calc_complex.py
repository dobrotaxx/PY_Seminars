def calc_value(real, real1, oper):
    if oper == '+':
        res = complex(real.replace(' ', '')) + complex(real1.replace(' ', ''))
    elif oper == '-':
        res = complex(real.replace(' ', '')) - complex(real1.replace(' ', ''))
    elif oper == '*':
        res = complex(real.replace(' ', '')) * complex(real1.replace(' ', ''))
    else:
        res = complex(real.replace(' ', '')) / complex(real1.replace(' ', ''))
    return res
