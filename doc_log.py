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
ips = {}
infos = {}

for line in file:
    if "druggist match succeed" in line:
        s = re.findall(r"business_id:\d+", line)[0]
        bid = s.split(":")[1]
        time = re.findall(r"\d{4}/\d{1,2}/\d{1,2} \d{1,2}:\d{1,2}:\d{1,2}", line)[0]
        s = re.findall(r"proxy_server_ip:\S+", line)[0]
        ip = s.split(":")[1]
        s = re.findall(r"proxy_server_port:\d+", line)[0]
        port = s.split(":")[1]
        ips[bid] = (time, ip, port)
    elif "video_send_packet" in line:
        s = re.findall(r"business_id:\d+", line)[0]
        bid = s.split(":")[1]
        s = re.findall(r"video_send_packet:\d+", line)[0]
        video_send = s.split(":")[1]
        s = re.findall(r"video_recv_packet:\d+", line)[0]
        video_recv = s.split(":")[1]
        s = re.findall(r"audio_send_packet:\d+", line)[0]
        audio_send = s.split(":")[1]
        s = re.findall(r"audio_recv_packet:\d+", line)[0]
        audio_recv = s.split(":")[1]
        infos[bid] = (video_send, video_recv, audio_send, audio_recv)

file.close()

file = open(os.path.splitext(filePath)[0] + ".csv", mode="w", encoding="GBK")
file.writelines("time,id,ip,port,video_send,video_recv,audio_send,audio_recv\n")
for key in infos:
    if key in ips:
        ip = ips[key]
        info = infos[key]
        send = int(info[2])
        recv = int(info[3])

        if recv / send < 0.6:
            e = "****"
        elif recv / send < 0.7:
            e = "***"
        elif recv / send < 0.8:
            e = "**"
        elif recv / send < 0.9:
            e = "*"
        else:
            e = ""
        file.writelines(
            "%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (ip[0], key, ip[1], ip[2], info[0], info[1], info[2], info[3], e))

file.close()
