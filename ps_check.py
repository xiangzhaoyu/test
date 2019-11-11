#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/5 下午3:43
# @Author  : zhaoyu
# @Site    : 
# @File    : ps_check.py
# @Software: PyCharm

import sys
import os

rootPath = os.path.abspath(os.path.dirname(__file__))
sys.path.append(rootPath)
import psutil

for proc in psutil.process_iter():
    # print("pid-%d,name:%s,cwd:%s,exe:%s" % (proc.pid, proc.name(), proc.cwd(), proc.exe()))
    if 'python' in proc.name() and os.path.join(rootPath, 'scheduler') in proc.cwd():
        cmds = proc.cmdline()
        for cmd in cmds:
            if './sche_process.py' in cmd:
                print("pid-%d,name:%s,cwd:%s,exe:%s" % (proc.pid, proc.name(), proc.cwd(), proc.exe()))
                print(cmds)