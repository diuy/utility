#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/16 14:19
# @Author  : Aries
# @Site    : 
# @File    : dispatch_log.py
# @Software: PyCharm Community Edition


import sys
import re
import os

filePath = ""

if len(sys.argv) < 2:
    filePath = input("请输入文件:\n")
else:
    filePath = sys.argv[1]

file = open(filePath, mode="r", encoding="GB2312", errors="ignore")
infos = []
line_re = re.compile(r".*business_id:\d+.*user:\S+.*pharmacist:\S+.*proxy_sever:\S+.*")
for line in file:
    if line_re.match(line):
        s = re.findall(r"business_id:\d+", line)[0]
        bid = s.split(":")[1]

        time = re.findall(r"\d{2}:\d{2}:\d{2}", line)[0]

        s = re.findall(r"user:\S+", line)[0]
        user = s.split(":")[1]

        s = re.findall(r"pharmacist:\S+", line)[0]
        pharmacist = s.split(":")[1]

        s = re.findall(r"proxy_sever:\S+", line)[0]
        proxy_sever = s[s.index(":") + 1:]

        infos.append((time, bid, user, pharmacist, proxy_sever))
file.close()

file = open(os.path.splitext(filePath)[0] + ".csv", mode="w", encoding="GBK")
file.writelines("time,bid,user,pharmacist,proxy_sever\n")

for info in infos:
    file.writelines(
        "%s,%s,%s,%s,%s\n" % (info[0], info[1], info[2], info[3], info[4]))

file.close()
