# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 20:44:14 2016

@author: amylo
"""

import os
import requests

print(os.getcwd())

r = requests.get("http://www.nwu.edu.cn")

print(r.url)
print(r.encoding)
print(r.text)