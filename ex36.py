#!/usr/bin/python 
# -*- coding: utf-8 -*-
from sys import exit

def phantom_blood():
    jojo = "Jonathan"
    print("")

def battle_tendency():
    return

def stardust_crusaders():
    jojo = "Joutaro"
    print("承太郎一行来到了埃及吊魔馆，与迪奥之间展开了最终决斗")
    print("dio的世界可以暂停时间，承太郎陷入了苦战")
    print("dio: 木大木大")
    print("承太郎: ......\n1. 欧拉欧拉欧拉欧拉欧拉！\n2. ヤレヤレダゼ")

    choice = int(input("> "))
    if choice == 1:
        clear(jojo)
    elif choice == 2:
        dead("不好意思，说错台词了诶嘿~。")

def clear(jojo):
    print(f"{jojo}打败了dio")
    exit(0)

def dead(why):
    print(why, "YOU DEAD!")
    print("oh no,你做出了错误的选择。想要重新开始吗？")
    print("1. 怎么能在这里倒下！？")
    print("2. 是个不错提案，だが断る！")
    choice = int(input("> "))

    if choice == 1:
        start()
    elif choice == 2:
        print("goodbye")
        exit(0)
    else:
        print("搞毛啊，滚")
        exit(0)

def start():
    print("接下来您将作为主角体验JOJO的故事")
    print("眼前有三个房间，您希望进入第几个呢？")
    room = int(input("> "))
    
    if room == 1:
        phantom_blood()
    elif room == 2:
        battle_tendency()
    elif room == 3:
        stardust_crusaders()
    else:
        dead("")

start()
