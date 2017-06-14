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

array = []
array.append("1")
array.append("2")
for a in array:
    print(a)

i = re.finditer(r"dd", "1111")
k = next(i, "")
print(k)
