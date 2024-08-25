# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:05:13 2024

@author: ADMIN
"""


a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))


tong = a + b
hieu = a - b
tich = a * b


if b != 0:
    thuong = a / b
    chia_lay_du = a % b
    chia_lay_nguyen = a // b
    
    thuong_lam_tron = round(thuong, 3)
else:
    thuong = chia_lay_du = chia_lay_nguyen = None
    thuong_lam_tron = None
    print("Lỗi: Không thể chia cho số 0!")


print(f"Tổng của {a} và {b} là: {tong}")
print(f"Hiệu của {a} và {b} là: {hieu}")
print(f"Tích của {a} và {b} là: {tich}")

if thuong_lam_tron is not None:
    print(f"Thương của {a} chia cho {b} là: {thuong_lam_tron}")
    print(f"Chia lấy dư của {a} chia cho {b} là: {chia_lay_du}")
    print(f"Chia lấy nguyên của {a} chia cho {b} là: {chia_lay_nguyen}")
