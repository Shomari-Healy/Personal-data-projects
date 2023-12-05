# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 14:15:22 2023

@author: Shomari
"""
#Code analysing my Facebook post data

#########################################################################
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# read the json file into a dataframe
df = pd.read_json('C:/Users/Shomari/OneDrive/Desktop/Python projects/facebook-shomarihealy/posts/your_posts_1.json') 
df.head(3)

# rename the timestamp column
df.rename(columns={'timestamp': 'date'}, inplace=True)

#drop some unnecessary columns
df = df.drop(['attachments', 'title'], axis=1)

# making sure it's datetime format
pd.to_datetime(df['date'])

df.head(3)

print(df.shape) # (60, 2)
df.tail(3)

#Set date column as the index
df.set_index('date', inplace=True)

#Resample the data by month, counting how many posts occur in each month 
post_counts = df.resample('MS').size() #MS - month start

############################################
#Making graphs

# set figure size and font size
sns.set(rc={'figure.figsize':(40,20)})
sns.set(font_scale=2)

# set x labels
x_labels = post_counts.index

#create bar plot
sns.barplot(x=x_labels, y=post_counts, color="blue")

# only show x-axis labels for Jan 1 of every other year
tick_positions = np.arange(10, len(x_labels), step=24)

#reformat date to display year onlyplt.ylabel("post counts")
plt.xticks(tick_positions, x_labels[tick_positions].strftime("%Y"), rotation=45)

# Add labels
plt.ylabel("Post Count")
plt.gca().set_xlabel("Date")

# Add a title
plt.title("Monthly Post Counts")

# display the plot
plt.show()




