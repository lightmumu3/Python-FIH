#!/usr/bin/env python
# -*- coding:utf-8 -*-

import math


def translate(p_list, dx, dy):
    """平移

    :param p_list: (list of list of int: [[x0, y0], [x1, y1], [x2, y2], ...]) 图元参数
    :param dx: (int) 水平方向平移量
    :param dy: (int) 垂直方向平移量
    :return: (list of list of int: [[x_0, y_0], [x_1, y_1], [x_2, y_2], ...]) 变换后的图元参数
    """
    result = []
    for x, y in p_list:
        x = x + dx
        y = y + dy
        result.append([x, y])
    return result


def rotate(p_list, x, y, r):
    """旋转

    :param p_list: (list of list of int: [[x0, y0], [x1, y1], [x2, y2], ...]) 图元参数
    :param x: (int) 旋转中心x坐标
    :param y: (int) 旋转中心y坐标
    :param r: (int) 顺时针旋转角度（°）
    :return: (list of list of int: [[x_0, y_0], [x_1, y_1], [x_2, y_2], ...]) 变换后的图元参数
    """
    result = []
    r = math.radians(r)
    sinr = math.sin(r)
    cosr = math.cos(r)
    for xi, yi in p_list:
        dx = xi - x
        dy = yi - y
        result.append([int(x + dx * cosr - dy * sinr), int(y + dx * sinr + dy * cosr)])
    return result


def scale(p_list, x, y, s):
    """缩放变换

    :param p_list: (list of list of int: [[x0, y0], [x1, y1], [x2, y2], ...]) 图元参数
    :param x: (int) 缩放中心x坐标
    :param y: (int) 缩放中心y坐标
    :param s: (float) 缩放倍数
    :return: (list of list of int: [[x_0, y_0], [x_1, y_1], [x_2, y_2], ...]) 变换后的图元参数
    """
    result = []
    for xi, yi in p_list:
        dx = xi - x
        dy = yi - y
        result.append([int(x + s * dx), int(y + s * dy)])
    return result





