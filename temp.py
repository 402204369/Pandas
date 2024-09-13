# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd

name=['John','Peter','Mark','Jmaes','Tkay','Micaiah','Glen','Leo']
stId=[22,22,26,56,89,89,78,45]
age=[12,18,23,22,24,25,25,26]
module=['maths','prog','data science','web tech','networks','INS','Bcom','aiii']
score=[60,70,80,98,78,67,78,78]
student={'name':name,'studentID':stId,'age':age,'module':module,'score':score}

df=pd.DataFrame(student)
grade=('distinction','Credit','Pass','Pass','distinction','Credit','distinction','Pass')
df.insert(5,"Grades",grade)
print(df)
df.to_csv("TIRED AND HUNGRY STUDENT")