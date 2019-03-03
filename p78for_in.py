#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# for looper in [1, 2, 3, 4, 5]:
#     print("hello")
#
# for looper in [1, 2, 3, 4, 5]:
#     print(looper)
#
# for looper in [1, 2, 3, 4, 5]:
#     print(looper, "times 8 =", looper * 8)
#
# for looper in range(1, 5):
#     print(looper, "times 8 =", looper * 8)
#
# for looper in range(1, 11):
#     print(looper, "times 8 =", looper * 8)
#
# for i in range(1, 5):
#     print(i, "times 8 =", i * 8)   # iteration use i j k  循环变量常用习惯i j k
#
#
# for i in range(5):   # range(5) == range(0,5)
#     print(i, "times 8 =", i * 8)
#
# print("-------------------------------")
#
# for letter in "Hi there":
#     print(letter)
#
#
# for i in range(1, 10, 2):
#     print(i)

# import time
# for i in range(10, 0, -1):   # 反向计数
#     print(i)
#     time.sleep(1)    # 等待1秒
# print("Blast off!")

# 8-7
# import time
# for cool_guy in ["Spongebob", "Spiderman", "Justin Timberlake", "My Dad"]:
#     print(cool_guy, "is the coolest guy ever!")
#     time.sleep(1)

# text = ["Spongebob", "Spiderman", "Justin Timberlake", "My Dad"]
# import time
# for cool_guy in text:
#     print(cool_guy, "is the coolest guy ever!")
#     time.sleep(1)

# 8-8
# print("Type 3 to continue anything else to quit.")
# someinput = input()
# while someinput == '3':    # 只要someinput = '3'就一直循环
#     print("Thank you for the 3. Very kind of you .")
#     print("Type 3 to continue,anything else to quit.")
#     someinput = input()
# print("That's not 3, So I'm quitting now.")

# 8-9

# for i in range(1, 6):
#     print()
#     print('i =', i, end=' ')   # python3 中采用end=' '保持不换行打印显示。
#     print('Hello,how', end=' ')
#     if i == 3:
#         continue
#     print("are you today?")

# 动手试一试

# print("Which multiplication table would you like?")
# number = int(input("enter a number:"))
# for i in range(1, 11):
#     print(number, 'X', i, '=', i*number)

# i = int(input("enter number:"))
# number = 1
# while number <= 10:
#     print(i, 'X', number, '=', i*number)
#     number += 1

# 由客户决定的乘法表
i = int(input("enter first number:"))
number = int(input("Enter scend number:"))
while number <= 10:
    print(i, 'X', number, '=', i*number)
    number += 1
