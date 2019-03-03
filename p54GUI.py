#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import easygui

# easygui.msgbox("hello there!")
#
# user_response = easygui.msgbox("hello there!")
# print(user_response)

# 第一种方法
# flavor = easygui.buttonbox("What is your favorite ice cream flavor?",
#                            choices=['Vanilla', 'Chocolate', 'strawberry'])
#
# easygui.msgbox("You picked " + flavor)


# 第二种方法
flavor = easygui.choicebox("What is your favorite ice cream flavor?",
                           choices=['Vanilla', 'Chocolate', 'strawberry'])

easygui.msgbox("You picked " + flavor)
