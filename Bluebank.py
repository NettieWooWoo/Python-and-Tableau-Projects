# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 20:23:44 2022

@author: shaga
"""

import pandas as pd
import json
import numpy as np
import matplotlib.pyplot as plt

#method 1 to read json data
json_file = open('loan_data_json (2).json')
data = json.load(json_file)

#method 2 to read json data
with open('loan_data_json (2).json') as json_file:
    data = json.load(json_file)
    
#transform to dataframe
loandata = pd.DataFrame(data)

#finding unique values for Purpose column

loandata['purpose'].unique()
loandata.describe()

#describe data by specific column
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

#using EXP() to get the annual income
income = np.exp(loandata['log.annual.inc'])
loandata['annual_income'] = income

#working with If statements

a = 40
b = 500

if b > a:
    print('b is greater than a')

#adding more conditions

a = 40
b = 500
c = 1000

if b > a and b < c:
    print('b is greater than a but less than c')

#what if a condition is not met

a = 40
b = 500
c = 20

if b > a and b < c:
    print('b is greater than a but less than c')
else:
    print('no conditions met')

#another condition with different metrics

a = 40
b = 0
c = 30

if b > a and b < c:
    print('b is greater than a but less than c')
elif b > a and b > c:
    print('b is greater than a and c')
else:
    print('no conditions met')


#working with or
a = 40
b = 500
c = 30

if b > a or b < c:
    print('b is greater than a but less than c')
else:
    print('no conditions met')

#fico score

fico = 250

#fico >= 300 and < 400:'Very Poor'
#fico >= 400 and ficoscore < 600:'Poor'
#fico >= 601 and ficoscore < 660:'Fair'
#fico >= 660 and ficoscore < 700:'Good'
#fico >=700:'Excellent'

if fico >= 300 and fico < 400:
    ficocat = 'Very Poor'
elif fico >= 400 and fico < 600:
    ficocat = 'Poor'
elif fico >= 601 and fico < 660:
    ficocat = 'Fair'
elif fico >= 660 and fico < 700:
    ficocat = 'Good'
elif fico >= 700:
    ficocat = 'Excellent'
else:
    ficocat = 'Unknown'
print(ficocat)

#for loops

fruits = ['apples', 'pears', 'bananas']

for x in fruits:
    print(x)
    y = x+' fruit'
    print(y)

for x in range(0,3):
    y = fruits[x]
    print(y)

#applying for loops to loan data
#using first 10


length = len(loandata)
ficocat = []
for x in range(0, length):
    category = loandata['fico'][x]
    
    try:        
        if category >= 300 and category < 400:
            cat = 'Very Poor'
        elif category >= 400 and category < 600:
            cat = 'Poor'
        elif category >= 601 and category < 660:
            cat = 'Fair'    
        elif category >= 660 and category < 700:
            cat = 'Good'
        elif category >= 700:
            cat = 'Excellent'
        else:
            cat = 'Unknown'
    except:
            cat = 'Unknown'
    ficocat.append(cat)
    
ficocat = pd.Series(ficocat)

loandata['fico.category'] = ficocat

    
#df.loc as conditional statement
#df.loc[df[column_name] condition, newcolumn_name] = 'value if condition is met'

#for interest rates a new column is wanted. rate > 0.12 then high, else low

loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'

#number of loans or rows by fico category

catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color = 'blue', width = 0.5)
plt.show()

purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.bar(color = 'green', width = 0.5)
plt.show()

#scatterplots 

ypoint = loandata['annual_income']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint, color = 'green')
plt.show()

#writing to csv
loandata.to_csv('Loan_Cleaned.csv', index = True)
















































