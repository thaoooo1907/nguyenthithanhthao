# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 19:33:12 2024

@author: ADMIN
"""

import random

def generate_random_number(start, end):
    """
    Sinh số nguyên ngẫu nhiên trong khoảng từ start đến end (bao gồm start và end).
    """
    if start > end:
        raise ValueError("Giá trị bắt đầu phải nhỏ hơn hoặc bằng giá trị kết thúc.")
    
    return random.randint(start, end)

def main():
   
    try:
        start = int(input("Nhập giá trị bắt đầu của đoạn số: "))
        end = int(input("Nhập giá trị kết thúc của đoạn số: "))
        
        
        random_number = generate_random_number(start, end)
        print(f"Số ngẫu nhiên trong đoạn [{start}, {end}] là: {random_number}")
    
    except ValueError as ve:
        print(f"Đã xảy ra lỗi: {ve}")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

if __name__ == "__main__":
    main()
