# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:27:15 2024

@author: ADMIN
"""


print("=" * 30)
print("============ MENU ============")
print("1. Hu tieu")
print("2. Chao long")
print("3. Banh canh")
print("4. Bun rieu")
print("5. Pho bo")
print("=" * 30)


choice = input("Moi nhap lua chon: ")


print("=" * 30)


menu = {
    "1": "Hu tieu",
    "2": "Chao long",
    "3": "Banh canh",
    "4": "Bun rieu",
    "5": "Pho bo"
}

if choice in menu:
    print(f"Ban da chon: {menu[choice]}")
else:
    print("Lua chon khong hop le.")
