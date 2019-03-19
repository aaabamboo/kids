#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 13.1 create function and use it
# def printMyAddress():
#     print("Warren Sanda")
#     print("123 Main street")
#     print("ottawa,ontario,canada")
#     print("K2M 2E9")
#     print()
# printMyAddress()

# 13.2 调用函数
# printMyAddress()

# 13.3 向function 传递参数
# def printMyAddress(myname):
#     print(myname)
#     print("123 Main street")
#     print("ottawa,ontario,canada")
#     print("K2M 2E9")
#     print()
# printMyAddress("Carter Sande")
# printMyAddress("kyra sande")
# printMyAddress("patricia sande")
# printMyAddress("龙马精神")
# printMyAddress("the usa ")

# 13.4 有多个参数的函数
# def printMyAddress(somename, housenum):
#     print(somename)
#     print(housenum, end=',')
#     print("main street")
#     print("ottawa,ontario,canada")
#     print("K2M 2E9")
#     print()
# printMyAddress("Carter Sande", '45')
# printMyAddress("kyra sande", '64')
# printMyAddress("patricia sande", '22')
# printMyAddress("龙马精神", '36')

# 13.5 返回值的函数
# def calculatetax(price, tax_rate):
#     taxtotal = price + (price * tax_rate)
#     return taxtotal
# calculatetax(7.99, 0.06)
# print(calculatetax(7.99, 0.06))

# 13-4 代码清单
# def calculatetax(price, tax_rate):
#     total = price + (price * tax_rate)
#     return total
#
# my_price = float(input("enter a price:"))   # total = lxl(float(input("enter a num:")),float(input("enter a tax:")))
#
# totalprice =calculatetax(my_price, 0.06)
# print("price =", my_price, "total price =", totalprice)


# calculatetax(7.99, 0.06)
# print(calculatetax(7.99, 0.06))  8.4694

# 13.-5
# def calculatetax(price, tax_rate):
#     total = price + (price * tax_rate)
#     return total
#
# my_price = float(input("enter a price:"))   # total = lxl(float(input("enter a num:")),float(input("enter a tax:")))
#
# totalprice =calculatetax(my_price, 0.06)
# print("price =", my_price, "total price =", totalprice)
# print(price)   # NameError:name 'price' is not defined 局部变量price报错

# 13-6
# def calculatetax(price, tax_rate):
#     total = price + (price * tax_rate)
#     print(my_price)   # my_price 在此处为全局变量
#     return total
#
# my_price = float(input("enter a price:"))   # total = lxl(float(input("enter a num:")),float(input("enter a tax:")))
#
# totalprice =calculatetax(my_price, 0.06)
# print("price =", my_price, "total price =", totalprice)

# 13-7
def calculatetax(price, tax_rate):
    total = price + (price * tax_rate)

    my_price = 10000   # 在函数内部修改my_price
    print("my_price(inside function) = ", my_price)  # 打印局部版本的my_price
    return total

my_price = float(input("enter a price:"))   # total = lxl(float(input("enter a num:")),float(input("enter a tax:")))

totalprice =calculatetax(my_price, 0.06)
print("price =", my_price, "total price =", totalprice)
print("my_price (outside functin) = ", my_price)  # 打印全局版本的my_price


### use tow weeks of time finish it , because boy sick
