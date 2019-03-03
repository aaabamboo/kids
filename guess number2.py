#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 输入数字，并猜到它，在一定的数字整数范围内。
# 解题办法：先输入这个数字范围内的中间数试错，再取余下中间数字，试错少于六次。

import random
secret = random.randint(1, 99)
guess = 0
# tries = 0
tries = 6

# print("ahoy! I'm Dread Pirate Robers,and I have a secret!")
# print("It is a number from 1 to 99. I'll give you 6 tries")

while guess != secret and tries > 0:    # tries < 6:
    guess = int(input("What's yer guess?enter number: "))
    if guess < secret:
        print("Too low,ye scurvy dog!")
    elif guess > secret:
        print("Too high,landlubber!")

    # tries = tries + 1
    tries = tries - 1
    print("还有", tries, "一次机会哟")


if guess == secret:
    print("Avast !Ye got it ! Found my secret ,ye did !")
else:
    print("No more guesses! Better luck next time,matey!")
    print("The secret number was", secret)
