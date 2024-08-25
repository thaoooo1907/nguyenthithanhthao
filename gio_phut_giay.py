# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:15:52 2024

@author: ADMIN
"""


hours = int(input("Nhập số giờ: "))
minutes = int(input("Nhập số phút: "))
seconds = int(input("Nhập số giây: "))


total_seconds = (hours * 3600) + (minutes * 60) + seconds


print(f"Tổng số giây là: {total_seconds}")
