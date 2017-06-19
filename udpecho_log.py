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

# 2017-06-19 16:59:12: DEBUG: ip:121.41.108.248,port:45005,tag:11837,id:0
re_head = re.compile(r".*ip:.*,port:\d+,tag:\d+,id:\d+.*")
# 2017-06-19 17:00:17: DEBUG: 发送包数:4062,发送流量:120091,发送包平均大小:29.56
re_send = re.compile(r".*发送包数:\d+,发送流量:\d+.*")
# 2017-06-19 17:00:17: DEBUG: 接收包数:4062,接收流量:120091,接收包平均大小:29.56
re_recv = re.compile(r".*接收包数:\d+,接收流量:\d+.*")
# 2017-06-19 17:00:17: DEBUG: 丢包数量百分比:0.00%,丢包流量百分比:0.00%
re_percent = re.compile(r".*丢包数量百分比:\d{1,3}\.\d{1,2}%.*丢包流量百分比:\d{1,3}\.\d{1,2}%.*")

tag = ""
_id = ""
sendCount = ""
recvCount = ""
time = ""
lastCountPercent = ""
for line in file:
    if re_head.match(line):
        s = re.findall(r"tag:\d+", line)[0]
        tag = s.split(":")[1]

        s = re.findall(r"id:\d+", line)[0]
        _id = s.split(":")[1]
    elif re_send.match(line):
        s = re.findall(r"发送包数:\d+", line)[0]
        sendCount = s.split(":")[1]
    elif re_recv.match(line):
        s = re.findall(r"接收包数:\d+", line)[0]
        recvCount = s.split(":")[1]
    elif re_percent.match(line):
        time = re.findall(r"\d{4}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}:\d{1,2}", line)[0]
        s = re.findall(r"丢包数量百分比:\d{1,3}\.\d{1,2}", line)[0]
        lastCountPercent = s.split(":")[1]
        if tag != "":
            infos.append((time, tag, _id, sendCount, recvCount, lastCountPercent))
            tag = ""

file.close()

file = open(os.path.splitext(filePath)[0] + ".csv", mode="w", encoding="GBK")
file.writelines("time,tag,id,sendCount,recvCount,lastCountPercent\n")


def get_diff(x, y):
    d = 0
    if x > y:
        d = (x - y) / x
    elif y > x:
        d = (y - x) / y
    return d


for info in infos:
    f = float(info[5])
    diff = (100.0 - f) / 100
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
        "%s,%s,%s,%s,%s,%s,%s\n" % (info[0], info[1], info[2], info[3], info[4], info[5], e))

file.close()
