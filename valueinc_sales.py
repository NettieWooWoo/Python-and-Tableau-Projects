# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 21:19:59 2022

@author: shaga
"""

import pandas as pd

# file_name = pd.read_csv('file.csv')  format for read.csv how to bring in file

data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv' , sep=';')

#summary of the data
data.info()

#working with calculations
#defining variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6

#mathematical operations of tableau

ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberOfItemsPurchased*ProfitPerItem
CostPerTransaction = NumberOfItemsPurchased*CostPerItem
SellingPriceTransaction = NumberOfItemsPurchased*SellingPricePerItem

#CostPerTransaction column calculation

#CostPerTransaction = CostPerItem * NumberOfItemsPurchased
#variable = df['column_name]

CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemsPurchased

#adding new column to dataframe

data['CostPerTransaction'] = CostPerTransaction

#Sales per transaction

data['SalesPerTransaction'] = data['SellingPricePerItem'] * NumberOfItemsPurchased

#Profit Calculation = Sales - Cost
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - CostPerTransaction

#Markup Calculation = Sales - Cost/Cost
data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction']/data['CostPerTransaction'])
data['Markup'] = (data['ProfitPerTransaction']) /data['CostPerTransaction']

#Round syntax = round(variable, digits)
#rounding Markup

roundmarkup = round(data['Markup'], 2)
data['Markup'] = round(data['Markup'], 2)

#combining data fields

my_name = 'Antoinette'+'Wood'
my_date = 'Day'+'/'+'Month'+'/'+'Year'

#change column type with astype
day = data['Day'].astype(str)
year = data['Year'].astype(str)
print(day.dtype)
print(year.dtype)

my_date = day+'/'+data['Month']+'/'+year
data['Date'] = my_date

#using iloc to view specific columns
#data.iloc[0] #views row with index 0
#data.iloc[0:3] #first 3 rows
#data.iloc[-5:] #last 5 rows

data.head(5) #first five rows

#data.iloc[:-2] #brings in all rows on second column
#data.iloc[4,2] #brings in fourth row, second column

#using split to split the clientkeywords column
#new_var = column.str.split('sep', expand = True)

split_col = data['ClientKeywords,,'].str.split(',', expand = True)

#creating new columns for split columns in ClienKeywords,,

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthOfContract'] = split_col[2]

#replace square brackets with nothing using replace function

data['ClientAge'] = data['ClientAge'].str.replace('[' , '')
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']' , '')

#using the lower function to change item to lowercase
data['ItemDescription'] = data['ItemDescription'].str.lower()

#how to merge files
#bringing in a new dataset

seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

#merging files: merge_df = pd.merge(df_old, df_new, on = 'key')

data = pd.merge(data, seasons, on = 'Month')

#dropping columns: df = df.drop('column_name', axis = 1)

data = data.drop('ClientKeywords,,', axis = 1)
data = data.drop('Day', axis = 1)
data = data.drop(['Year', 'Month'], axis = 1)

#export into csv 
data.to_csv('ValueInc_Cleaned.csv', index = False)






 




















































