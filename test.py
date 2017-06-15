#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/13 21:57
# @Author  : Aries
# @Site    : 
# @File    : test.py
# @Software: PyCharm Community Edition
import sys
import re
import os

line = "08:40:30 LM_INFO    proxy_server_thread.cpp:410 business_id:49426 client_send_packet_num:4394, size:821852  druggist_send_packet_num:3959, size:760638, c_audio:1571,frame:9034, p_audio:904,frame:8848"
dd = re.match(r".*business_id:\d+.*client_send_packet_num:\d+.*c_audio:\d+.*p_audio:\d+.*", line)

line = "sdfsf p_audio:904,sdfsdf"
dd = re.match(r".*p_audio:\d+.*", line)


array = []
array.append("1")
array.append("2")
for a in array:
    print(a)

i = re.finditer(r"dd", "1111")
k = next(i, "")
print(k)
