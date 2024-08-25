# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 20:03:56 2024

@author: ADMIN
"""

import math


a = float(input("Nhập giá trị của a: "))
b = float(input("Nhập giá trị của b: "))


if b == 0:
    print("Lỗi: b không thể bằng 0.")
else:
    
    sqrt_a = math.sqrt(a)
    sqrt_b = math.sqrt(b)
    fourth_root_a = a ** 0.25
    fourth_root_b = b ** 0.25
    
    
    numerator1 = sqrt_a - sqrt_b
    denominator1 = fourth_root_a - fourth_root_b
    part1 = numerator1 / denominator1 if denominator1 != 0 else float('inf')  # Tránh chia cho 0
    
    sqrt_ab = (a * b) ** 0.25
    numerator2 = sqrt_a + sqrt_ab
    denominator2 = fourth_root_a + fourth_root_b
    part2 = numerator2 / denominator2 if denominator2 != 0 else float('inf')  # Tránh chia cho 0
    
    expression = part1 - part2
    
    
    result = fourth_root_b
    
    print(f"Kết quả của biểu thức là: {expression}")
    print(f"Kết quả của căn bậc 4 của b là: {result}")