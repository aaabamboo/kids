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

# letters = ['a', 'b', 'c', 'd', 'e']
# for i in letters:
#     print(i)

#  动手试一试
name = input('Enter 5 names:')
print(type(name))
print("The names are: ", name)
sort_name = name.sort()
print(sort_name)
