from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



list = ['a','b','c']

s1 = pd.Series(list)

print(s1[0])

out=['LEB','LEB','LEB','FRA','FRA','FRA','USA','USA','USA']
inside=['MORNING','MIDDAY','EVENING','MORNING','MIDDAY','EVENING','MORNING','MIDDAY','EVENING']
ind=['1','2','3','4','5','6','7','8','9']
indexRows=zip(out,inside)
df2=pd.DataFrame(out,inside)

indexRows=pd.MultiIndex.from_tuples(indexRows)
df3=pd.DataFrame(np.random.rand(9,9), indexRows,ind)

df4=pd.DataFrame(np.random.rand(9,9), indexRows)

print(df2)
print(df3)
print(df4)

print(df3.loc['LEB'].loc['EVENING'].loc['9'])

print(df3 >0.5)

dictionary= {'country':['IND','USA','UK'], 'Price':['80','47','98']}
df5=pd.DataFrame(dictionary,['1','2','3'])
print(df5)
print(df5.groupby('country').describe())
print(df5.groupby('country').min())

# concatenation 
df6 = pd.DataFrame({'A':[1,2,3,4], 'B':[10,20,30,40], 'C':[100,200,300,400]})
df7 = pd.DataFrame({'A':[5,6,7,8], 'B':[50,60,70,80], 'C':[500,600,700,800]})
df8 = pd.concat([df6,df7]) # by default axis is 0 in df8 = pd.concat([df6,df7],axis=0) which means to concatenate data frame top of each other
print(df8)
df9=pd.concat([df6,df7],axis=1) # to concatenate side by side use axis=1
print(df9)


# merging when you have common multiple columns 
print('======== Merging module ========')
df10 = pd.DataFrame({'A':[1,2,2,4], 'B':[10,20,30,40], 'C':[100,200,300,400]})
df11 = pd.DataFrame({'D':[5,6,7,8], 'B':[10,20,30,40], 'E':[500,600,700,800]})

df12 = pd.merge(df10,df11)
print(df12)

# unique 
print('======== Unique module ========')
print(df10['A'].unique())
print(df10['A'].nunique())
print(df10['A'].value_counts())

# creating function
print('======== Creating functions =======')
def abc(x):
    return x*3
print(abc(df10))
# another way of applying function to dataframe
print(df10.apply(abc))

# to drop the row (does not save it. To save it use inplace argu)
print('======== To drop row =======')
print(df10.drop(2))

print('======== To drop column =======')
print(df10.drop('B',axis=1))

# to drop and take the affect 
print('======== To drop column and take affect =======')

df10.drop('B', axis=1, inplace=True)
print(df10)

# work with file (csv, excel and html)
print('work with file (csv, excel and html)')
print('CSV file read and write')
df13=pd.read_csv('AMC.csv')
print(df13)
print('writing to another csv file')
df13.to_csv('fromAMC.csv')

print('Excel file read and write')
df13=pd.read_excel('AMC.xlsx')
print(df13)
print('writing to another xlsx file')
df13.to_excel('fromAMC.xlsx')

# Visualization 
print('Visualization')
# if you want to graph just open column
df13['Open'].plot()
plt.show()





