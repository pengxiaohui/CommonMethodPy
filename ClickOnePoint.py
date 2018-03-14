# -*- coding:utf-8 -*-

import time


"""
    本方法适用任何手机，已根据比例做适配
    :Usage:
        myclick(driver, x=100, y=200)
"""
def myclick(driver,x=0, y=0, duration=500):
    time.sleep(3)

    # 按这个手机大小来计算的（开发者当前使用的手机）
    a = 1440.0
    b = 2560.0

    # 当前手机大小（可能不是开发者当时使用的手机，即拿另外一个手机来测试）
    x1 = driver.get_window_size()['width']
    y1 = driver.get_window_size()['height']
    # print('---x1--', x1, '----y1---', y1)

    # 比例（注意类型）
    x2 = float(x1 / a)
    y2 = float(y1 / b)
    # print('---x2--', x2, '----y2---', y2)

    # 实际点击的坐标
    x3 = x2 * x
    y3 = y2 * y
    print('---x3--', x3, '----y3---', y3)
    try:
        driver.tap([(x3, y3)], duration)
    except:
        assert False,'can''t click one piont'
    time.sleep(3)






