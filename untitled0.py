# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 14:56:51 2024

@author: MicaiahTakudzwaNhamb
"""

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('C://Users//MicaiahTakudzwaNhamb//Downloads//TIRED AND HUNGRY STUDENT')
plt.plot(df['name'],df['score'],color='red')
plt.bar(df['name'],df['score'],color='green')
#C:/Users/MicaiahTakudzwaNhamb/Downloads/TIRED AND HUNGRY STUDENT