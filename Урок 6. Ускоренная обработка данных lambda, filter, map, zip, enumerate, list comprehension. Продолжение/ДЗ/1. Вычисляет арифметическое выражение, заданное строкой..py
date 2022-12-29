# 1. Напишите программу, которая вычисляет арифметическое выражение заданное строкой. Используйте
# операции +, -, /, *. Приоритет операций - стандартный.
# Пример:
# 2 + 2 = > 4;
# 1 + 1 * 3 = > 4;
# 1 - 2 * 3 = > -5.

# print(eval('2 + 2 * 2'))
# print(eval('2 * 3 / 6'))

expression = '2 + 2'
exprsn_lst = expression.split()
print(exprsn_lst)
while len(exprsn_lst) > 1:
    while '*' in exprsn_lst or '/' in exprsn_lst:
        if exprsn_lst.count('*') > 0 and exprsn_lst.count('/') > 0:
            if exprsn_lst.index('/') > exprsn_lst.index('*'):
                exprsn_lst[exprsn_lst.index('*') - 1] = \
                    int(exprsn_lst[exprsn_lst.index('*') - 1]) * int(exprsn_lst[exprsn_lst.index('*') + 1])
                exprsn_lst.pop(exprsn_lst.index('*') + 1)
                exprsn_lst.pop(exprsn_lst.index('*'))
            else:
                exprsn_lst[exprsn_lst.index('/') - 1] = \
                    int(exprsn_lst[exprsn_lst.index('/') - 1]) / int(exprsn_lst[exprsn_lst.index('/') + 1])
                exprsn_lst.pop(exprsn_lst.index('/') + 1)
                exprsn_lst.pop(exprsn_lst.index('/'))
        else:
            if '*' in exprsn_lst:
                exprsn_lst[exprsn_lst.index('*') - 1] = \
                    int(exprsn_lst[exprsn_lst.index('*') - 1]) * int(exprsn_lst[exprsn_lst.index('*') + 1])
                exprsn_lst.pop(exprsn_lst.index('*') + 1)
                exprsn_lst.pop(exprsn_lst.index('*'))
            else:
                exprsn_lst[exprsn_lst.index('/') - 1] = \
                    int(exprsn_lst[exprsn_lst.index('/') - 1]) / int(exprsn_lst[exprsn_lst.index('/') + 1])
                exprsn_lst.pop(exprsn_lst.index('/') + 1)
                exprsn_lst.pop(exprsn_lst.index('/'))
    while '+' in exprsn_lst or '-' in exprsn_lst:
        if exprsn_lst.count('+') > 0 and exprsn_lst.count('-') > 0:
            if exprsn_lst.index('-') > exprsn_lst.index('+'):
                exprsn_lst[exprsn_lst.index('+') - 1] = \
                    int(exprsn_lst[exprsn_lst.index('+') - 1]) + int(exprsn_lst[exprsn_lst.index('+') + 1])
                exprsn_lst.pop(exprsn_lst.index('+') + 1)
                exprsn_lst.pop(exprsn_lst.index('+'))
            else:
                exprsn_lst[exprsn_lst.index('-') - 1] = \
                    int(exprsn_lst[exprsn_lst.index('-') - 1]) - int(exprsn_lst[exprsn_lst.index('-') + 1])
                exprsn_lst.pop(exprsn_lst.index('-') + 1)
                exprsn_lst.pop(exprsn_lst.index('-'))
        else:
            if '+' in exprsn_lst:
                exprsn_lst[exprsn_lst.index('+') - 1] = \
                    int(exprsn_lst[exprsn_lst.index('+') - 1]) + int(exprsn_lst[exprsn_lst.index('+') + 1])
                exprsn_lst.pop(exprsn_lst.index('+') + 1)
                exprsn_lst.pop(exprsn_lst.index('+'))
            else:
                exprsn_lst[exprsn_lst.index('-') - 1] = \
                    int(exprsn_lst[exprsn_lst.index('-') - 1]) - int(exprsn_lst[exprsn_lst.index('-') + 1])
                exprsn_lst.pop(exprsn_lst.index('-') + 1)
                exprsn_lst.pop(exprsn_lst.index('-'))
print(exprsn_lst)