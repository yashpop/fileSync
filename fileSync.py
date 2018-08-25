# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 21:48:41 2018

@author: Yashwanth
"""

import shutil
import os

while True:
    src_files = os.listdir('./test1')
    dest_files = os.listdir('./test2')
    
    for file in src_files:
        #if file in src_files:
        #shutil.copytree('./test1','./test2/')
        shutil.copy2('./test1/'+file,'./test2/'+file)