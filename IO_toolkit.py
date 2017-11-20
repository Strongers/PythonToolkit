#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 11:29:48 2017

@author: stronger
@tiltle: IO toolkit
"""

import os
import pandas as pd

class IOToolkit:
    def __init__(self):
        pass
    
    def read_csv_folder(folder_path):
        '''
        Read all csv file in the target folder. Return a dataframe.
        '''
        os.chdir(folder_path)
        files = os.listdir()
        data = pd.read_csv(files[0], sep=',')
        if(len(files)>1):
            for file_i in files[1:]:
                dataTemp = pd.read_csv(file_i, sep=',')
                data = pd.concat([data,dataTemp], ignore_index=True)
        print('Folder contains %s file' % len(files))
        return data
        
