#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# friends = []
# friends.append("David")
# print(friends)
#
# friends.append("Mary")
# print(friends)

# friends.pop()
# print(friends)

# letters = ['a', 'b', 'c', 'd', 'e']
# print(type(letters))
# print(letters[3])
# a = ['("北京",126),("上海",48),("天津",73),("重庆",92),("广州",86)']
# a[0] = eval(a[0])
# print(type(a[0]))

# print(letters[1:4])
# print(letters[1:5])
# print(letters[0:4])
# print(letters[0:5])
# print(letters[:])    #  以下为分片简写
# print(letters[0:5])
# print(letters[:5])
# print(letters[1:2])
# print(letters[2:0])   # 错误为空none
# print(letters[2:])

# 12.8修改元素
# letters = ['a', 'b', 'c', 'd', 'e']
# print(letters)
# letters[2] = 'z'
# print(letters)

# 12.9增加的元素的方法
# letters = ['a', 'b', 'c', 'd', 'e']
# print(letters)
# letters.append(5)
# letters.append('z')   # 增加至末尾
# print(letters)

# letters = ['a', 'b', 'c', 'd', 'e']
# print(letters)
# letters.extend(['p', 'q', 'r'])   # 扩展列表
# print(letters)

# insert()插入元素
# letters = ['a', 'b', 'c', 'd', 'e']
# print(letters)
# letters.insert(2, 'z')
# print(letters)

# letters = ['a', 'b', 'c', 'd', 'e']
# print(letters[2])
# print(letters.index('e'))   # 获取元素索引的下标值
# print(letters)

# 12.10从列表删除元素
# letters = ['a', 'b', 'c', 'd', 'e']
# letters.remove("c")
# print(letters)
# letters.remove("f")  # 删除列表中不存在的一个值时报错
# print(letters)

# letters = ['a', 'b', 'c', 'd', 'e']
# print(letters)
# del letters[3]    # 注意用del删除的特别之处
# print(letters)


# letters = ['a', 'b', 'c', 'd', 'e']
# print(letters)
# lastletter = letters.pop()
# print(lastletter)
#
# second = letters.pop(1)
# print(second)

# 12.11 搜索列表
# in关键字
# letters = ['a', 'b', 'c', 'd', 'e']
# if 'a' in letters:
#     print("found 'a' in letters")
# else:
#     print("didn't find 'a' in letters")

# letters = ['a', 'b', 'c', 'd', 'e']
# yuanshu = input("pleaes enter a yuanshu:")
# if yuanshu in letters:
#     print("found it in letters,it is:", yuanshu)
# else:
#     print("didn't find it in letters,you enter is:", yuanshu)

# str1 = "this is string example....wow!!!"
# str2 = "exam"
# print(str1.index(str2))
# print(str1.index(str2, 10))
# print(str1.index(str2, 15))

# 12.12循环处理列表
# letters = ['a', 'b', 'c', 'd', 'e']
# for i in letters:
#     print(i)

# 12.13列表排序
# letters = ['d', 'a', 'e', 'c', 'b']
# print(letters)  # 打印原始序列
# # print(letters.sort())  不能这样做，必须分丙步来完成，如下：
# letters.sort()  # 按正序排序
# print(letters)
#
# letters.reverse()   # 按逆序排序，第一种方法。
# print(letters)

# 按逆序排序，第二种方法
# letters = ['d', 'a', 'e', 'c', 'b']
# print(letters)  # 打印原始序列
#
# letters.sort()  # 按正序排序
# print(letters)
#
# letters.sort(reverse=True)   # 按逆序排序，第一种方法。
# print(letters)

# original = [5, 2, 3, 1, 4]
# print(original)
# new = original
#
# new.sort()
# print(new)
# print(original)

# new = original[:]
# print(new)
# new.sort()
# print(new)
# print(original)

# sorted()
# original = [5, 2, 3, 1, 4]
# print(original)
# newer = sorted(original)
# print(original)
# print(newer)

# 12.14 可变和不可变
# my_tuple = ("red", "green", "blue")
# print(type(my_tuple))
# print(my_tuple)

# 12.15 双重列表：数据表。
# joemarks = [55, 63, 77, 81]
# tommarks = [65, 61, 67, 72]
# betmarks = [97, 95, 92, 88]
#
# classmarks = [joemarks, tommarks, betmarks]
# print(classmarks)
#
# print(classmarks[0][0])
# print(classmarks[2][3])
# print(classmarks[2][1])

# 12.6字典
# phonenumbers = {}  # 首先建立一个空字典，准备用于存储数据。
# phonenumbers["John"] = "555-1234"
# phonenumbers["Mary"] = "555-6789"
# phonenumbers["Bobz"] = "444-4321"
# phonenumbers["Jeny"] = "867-5309"
# print(phonenumbers)
# print(phonenumbers["Mary"])
# print(phonenumbers.keys())    # 列出字典中所有的键
# print(phonenumbers.values())  # 列出字典中所有的值
# for key in sorted(phonenumbers.keys()):
#     print(key, phonenumbers[key])

#  动手试一试
# 1.写一个程序：让用户提供5个名字，程序要把这5个名字保存在一个列表中，最后打印出来。
names = ["tom", "jack", "peter", "mark", "john"]
# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])
# print(names[4])
# print("The names are:", names[0], names[1], names[2], names[3], names[4])  # 最笨的办法

for i in names:
    print(i)
print("The names are:", end=', ')
for i in names:
    print(i, end=', ')

# 2.修改第一题的程序，要求不仅显示原来的名字列表，还要显示出排序后的列表。
print('\n')
print(names)
names.sort()
print(names)

# 3.修改第一题的程序，要求只显示用户键入的第3个名字。




# 4.修改第一题的程序，让用户替换其中一个名字。用户应该能选择要替换那个名字，然后键入新名字。最后显示这个新列表：
# 5.编写一个字典程序，让用户可以添加单词和定义，然后可以查找这些单词。确保当要查找的单词不存在时，用户能够知晓。
    # 运行的时候，经应该是像这样的：
    # Add or look up a word (a/1)? a
    # Type the word: computer
    # Type the definition: A machine that does very fast math
    # Word added!
    # Add or look up a word (a/1)? 1
    # Type the word: computer
    # A machine that does very fast math
    # Add or look up a word (a/1)? 1
    # Type the word : qwerty
    # That word isn't in the dictionary yet.
