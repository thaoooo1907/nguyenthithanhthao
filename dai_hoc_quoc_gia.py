# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 18:16:31 2024

@author: ADMIN
"""


str_input = "Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"


sub_strings = [part.strip() for part in str_input.split(',')]


print("Yêu cầu 1: Tách thành các sub-string")
for sub_str in sub_strings:
    print(sub_str)


filtered_sub_strings = []
for sub_str in sub_strings:
    if sub_str.startswith("P. "):
        filtered_sub_strings.append(sub_str[3:])
    elif sub_str.startswith("Q. "):
        filtered_sub_strings.append(sub_str[3:])
    elif sub_str.startswith("Tp. "):
        filtered_sub_strings.append(sub_str[4:])
    else:
        filtered_sub_strings.append(sub_str)

print("\nYêu cầu 2: Tách và lọc các sub-string")
for sub_str in filtered_sub_strings:
    print(sub_str)