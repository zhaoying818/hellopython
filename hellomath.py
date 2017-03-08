#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

def quadratic(a, b, c):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
        raise TypeError('Wrong Input Type!')
    if a == 0:
        raise TypeError('Not quadratic!')
    delta = pow(b,2) - 4 * a * c
    if delta < 0:
        raise TypeError('No root!')
    elif delta == 0:
        #print('Two equal roots: %f' % -b/(2 * a))
        return -b/(2 * a)
    elif delta > 0:
        #print('Two unequal roots: %f and %f' % ((-b - math.sqrt(delta))/(2*a), (-b + math.sqrt(delta))/(2*a)))
        return (-b - math.sqrt(delta))/(2*a), (-b + math.sqrt(delta))/(2*a)
print(quadratic(2, 3, 1))
