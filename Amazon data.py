# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 11:55:49 2023

@author: Shomari
"""
#Code analysing the amazon order history data of a user using the order history
#downloaed from their profile

#########################################################################
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/Shomari/OneDrive/Desktop/amazon-orders.csv') #imports csv
df.head() #look at the first few rows of data
df.shape # gets the size of the data set

df = df.fillna(0) #This is used to fill in all of the NaN fields with a zero. 'def =' is used to redefine the data frame
df.head()

###need to convert the string values in the data to floats and remove the $ sign in order to do calculations on the data
df ["Total Charged"]= df ["Total Charged"].str.replace('$','').astype(float) #df + column name allows us to adjust the values of only that column within the data frame
df.head()

##########################
#Running calculations on the data

#####Basic calculations on total

df["Total Charged"].sum() # sums all of the values in the column: 1777.7300000000002
df["Total Charged"].mean() # calculates the mean of the column: 30.131016949152546
df["Total Charged"].median() #calculates the median value of the column as mean can sometimes have outliers: 15.95
df["Total Charged"].max() #calculates the max spend: 210.99
df["Total Charged"].min() #calculates the min spend: 1.04

#####Calculations on taxes

df["Tax Charged"] = df["Tax Charged"].str.replace('$','').astype(float) #cleaning the data
df.head()

df["Tax Charged"].sum() #52.60999999999999
(df["Tax Charged"].sum() / df["Total Charged"].sum()) * 100 # Calculating the overall tax rate by dividing total taxed by total charged and multiplying by 100 to get the %: 2.95

##################################
#Spending over time

df['Order Date'] = pd.to_datetime(df['Order Date']) #converting dates to datetime data so python can recognise it
df.head()

df.plot.bar(x='Order Date', y='Total Charged', rot=90, figsize=(20,10)) #Plotting the total charged values per day
plt.show()

daily_orders = df.groupby('Order Date').sum()["Total Charged"] # grouping all of the values on one day together
daily_orders.head()

daily_orders.plot.bar(figsize=(20,10)) # plotting the new graph
plt.show()

daily_orders.plot.bar(figsize=(20, 10), color='blue') #changing the colour to green
plt.title("Total expnses", color = 'red') #adds a title
plt.legend(["Total Charged"], loc='upper right', title='Total') #adds a legend
plt.xticks(rotation=45, ha='right') #rotate axis on an angle
plt.ylabel('Total spent')
plt.show()





