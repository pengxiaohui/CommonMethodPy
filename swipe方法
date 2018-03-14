# -*- coding:utf-8 -*-
'''
Created on 2018年03月14日

@author: Administrator
'''


def getSize(mydriver):
    x = mydriver.get_window_size()['width']
    y = mydriver.get_window_size()['height']
    #     print('x,y----',x,y)
    return (x, y)


def scrollOption(mydriver, ax, by, cx, dy, t):
    l = getSize(mydriver)
    x1 = int(l[0] * ax)  # x坐标    t代表的是毫秒
    y1 = int(l[1] * by)  # y坐标
    x2 = int(l[0] * cx)  # 移动x坐标
    y2 = int(l[1] * dy)  # 移动y坐标
    time = t * 1000  # 单位是秒
    mydriver.swipe(x1, y1, x2, y2, time)

