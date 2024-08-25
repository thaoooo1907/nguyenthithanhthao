# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:45:35 2024

@author: ADMIN
"""

def tinh_bieu_thuc_A():
  """Hàm tính giá trị biểu thức A và làm tròn kết quả đến 3 chữ số thập phân"""
  A = (32**0.2-(1/64)**(-0.25)+(8/27)**(1/3))
  A_rounded = round(A, 3)
  return A_rounded


ket_qua = tinh_bieu_thuc_A()
print("Kết quả của biểu thức A là:", ket_qua) 