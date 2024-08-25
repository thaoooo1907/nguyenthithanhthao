# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:22:18 2024

@author: ADMIN
"""


a = int(input("Nhập hệ số a: "))
b = int(input("Nhập hệ số b: "))
c = int(input("Nhập hệ số c: "))


def format_coefficient(coeff, variable, first_term):
    if coeff > 0 and not first_term:
        return f"+ {coeff}{variable}"
    elif coeff > 0:
        return f"{coeff}{variable}"
    elif coeff < 0:
        return f"- {abs(coeff)}{variable}"
    return ""


equation = f"{format_coefficient(a, 'X^2', True)} {format_coefficient(b, 'X', False)} {format_coefficient(c, '', False)} = 0"


print(equation.strip())
