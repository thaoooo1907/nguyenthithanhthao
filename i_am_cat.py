# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 19:06:02 2024

@author: ADMIN
"""

str_input = "i’m a cat"

result_title = str_input.title()
print(result_title)

result_upper = str_input.upper()
print(result_upper)

result_swapcase = str_input[0].upper() + str_input[1:].swapcase()
print(result_swapcase)

result_capitalize = str_input.capitalize()
print(result_capitalize)