#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/6 上午9:16
# @Author  : zhaoyu
# @Site    : 
# @File    : qq_boom.py
# @Software: PyCharm

import win32gui
import win32con
import win32clipboard as w

# 发送的消息
msg = "测试代码"
# 窗口名字
name = "不知"
# 将测试消息复制到剪切板中
w.OpenClipboard()
w.EmptyClipboard()
w.SetClipboardData(win32con.CF_UNICODETEXT, msg)
w.CloseClipboard()
# 获取窗口句柄
handle = win32gui.FindWindow(None, name)
print(handle)
# while True:
i = 5
if i > 0:
    # 填充消息
    win32gui.SendMessage(handle, 770, 0, 0)
    # 回车发送消息
    win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    i -= 1
    print('send {}'.format(i))