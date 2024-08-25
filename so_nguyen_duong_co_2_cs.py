# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:07:53 2024

@author: ADMIN
"""


N = int(input("Nhập số nguyên dương có 2 chữ số: "))


if 10 <= N <= 99:
   
    tens_digit = N // 10  
    ones_digit = N % 10   
    total_sum = tens_digit + ones_digit
    
    
    print(f"Tổng các chữ số của {N} là: {tens_digit} + {ones_digit} = {total_sum}")
else:
    print("Số nhập vào không phải là số nguyên dương có 2 chữ số.")
