#The data used here is till 29-April-2020 and has records as on 29-April-2020.
#We will analyze this data using the Pandas DataFrame.
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv(r'C:\Users\amirk\OneDrive\Desktop\FULLSTACK\DATAANALYZ\DATA-ANALYZE-PROJECTS\3-covid19-data\__ 004 Covid-19-data.csv')
print(data.head(5))
print('=========')
## 1. 
# df.count()
# df.isnull().sum()
# Null Values means Missing Values
print(data.count())
print('=========')
print(data.isnull().sum())
print('===========')
### Q.1 ) Show the number of Confirmed , Deaths and Recovered cases in each Region.
#df.groupby('Region')['Confirmed', 'Recovered'].sum()
print(data.groupby('Region')['Confirmed'].sum())
print(data.groupby('Region')['Recovered'].sum())
print('==========')
### Q2) Remove all the records where Confirmed Cases is Less Than 10.
#df = df[~(df.Confirmed < 10)]
data=data[~(data['Confirmed'] < 10)]
### Q.3) In which Region, maximum number of Confirmed cases were recorded ?
#df.groupby('Region').Confirmed.sum().sort_values(ascending = False).head(20)
print(data.groupby('Region')['Confirmed'].sum().sort_values(ascending=False).head(20))
### Q.4) In which Region, minimum number of Deaths cases were recorded ?
print(data.groupby('Region')['Deaths'].sum().sort_values(ascending=True).head(20))
print('===============')
### Q.5) How many Confirmed , Deaths & Recovered cases were reported from India till 29 April 2020 ?
#df[df['Region'] == 'Country_name']
print(data[data['Region']=='India'])
print('==========')
### Q. 6-A ) Sort the entire data wrt No. of Confirmed cases in ascending order.
#df.sort_values(by= ['Confirmed'] , ascending = True)
data.sort_values(by=['Confirmed'],ascending=True)
### Q. 6-B ) Sort the entire data wrt No. of Recovered cases in descending order.
data.sort_values(by=['Confirmed'],ascending=False)


