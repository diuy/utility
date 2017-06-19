#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/19 10:02
# @Author  : Aries
# @Site    : 
# @File    : udpecho_log.py
# @Software: PyCharm Community Edition


import sys
import re
import os

filePath = ""

if len(sys.argv) < 2:
    filePath = input("请输入文件:\n")
else:
    filePath = sys.argv[1]

file = open(filePath, mode="r", encoding="GBK")
infos = []
line_re = re.compile(r".*丢包数量百分比:\d{1,3}\.\d{1,2}%.*丢包流量百分比:\d{1,3}\.\d{1,2}%.*")
for line in file:
    if line_re.match(line):
        time = re.findall(r"\d{4}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}:\d{1,2}", line)[0]
        s = re.findall(r"丢包数量百分比:\d{1,3}\.\d{1,2}", line)[0]
        lastCount = s.split(":")[1]
        s = re.findall(r"丢包流量百分比:\d{1,3}\.\d{1,2}", line)[0]
        lastFlow = s.split(":")[1]

        infos.append((time, lastCount, lastFlow))
file.close()

file = open(os.path.splitext(filePath)[0] + ".csv", mode="w", encoding="GBK")
file.writelines("time,lastCount,lastFlow\n")


def get_diff(x, y):
    d = 0
    if x > y:
        d = (x - y) / x
    elif y > x:
        d = (y - x) / y
    return d


for info in infos:
    f = float(info[1])
    diff = (100.0-f)/100
    if diff < 0.6:
        e = "****"
    elif diff < 0.7:
        e = "***"
    elif diff < 0.8:
        e = "**"
    elif diff < 0.9:
        e = "*"
    else:
        e = ""
    file.writelines(
        "%s,%s,%s,%s\n" % (info[0], info[1], info[2], e))

file.close()
