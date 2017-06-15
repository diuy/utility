#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/13 18:46
# @Author  : Aries
# @Site    : 
# @File    : pc_log.py
# @Software: PyCharm Community Edition


import sys
import re
import os

filePath = ""

if len(sys.argv) < 2:
    filePath = input("请输入文件:\n")
else:
    filePath = sys.argv[1]

file = open(filePath, mode="r", encoding="UTF-8")
infos = []
line_re = re.compile(
    r".*business_id:\d+.*client_send_packet_num:\d+.*druggist_send_packet_num:\d+.*c_audio:\d+.*frame:\d+.*"
    r"p_audio:\d+.*frame:\d+.*")
for line in file:
    if line_re.match(line):
        # if r"business_id:\d+.*client_send_packet_num:\d+.*c_audio\d+.*p_audio:\d+.*" in line:
        s = re.findall(r"business_id:\d+", line)[0]
        bid = s.split(":")[1]
        time = re.findall(r"\d{2}:\d{2}:\d{2}", line)[0]
        s = re.findall(r"client_send_packet_num:\d+", line)[0]
        client_send_packet_num = s.split(":")[1]
        s = re.findall(r"druggist_send_packet_num:\d+", line)[0]
        druggist_send_packet_num = s.split(":")[1]
        s = re.findall(r"c_audio:\d+", line)[0]
        c_audio = s.split(":")[1]
        s = re.findall(r"c_audio:\d+,frame:\d+", line)[0]
        c_frame = s.split(":")[2]
        s = re.findall(r"p_audio:\d+", line)[0]
        p_audio = s.split(":")[1]
        s = re.findall(r"p_audio:\d+,frame:\d+", line)[0]
        p_frame = s.split(":")[2]
        infos.append((time, bid, client_send_packet_num, druggist_send_packet_num, c_audio, c_frame, p_audio, p_frame))
file.close()

file = open(os.path.splitext(filePath)[0] + ".csv", mode="w", encoding="GBK")
file.writelines("time,id,client_send,druggist_send,c_audio,c_frame,p_audio,p_frame\n")
for info in infos:
    c_audio = int(info[4])
    p_audio = int(info[5])
    diff = 0
    if c_audio > p_audio:
        diff = (c_audio - p_audio) / c_audio
    elif p_audio > c_audio:
        diff = (p_audio - c_audio) / p_audio
    diff = 1 - diff
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
        "%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7], e))

file.close()
