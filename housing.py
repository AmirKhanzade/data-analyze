#This dataset is primarily centered around the housing market of London. It contains a lot of additional relevant data:

#* Monthly average house prices
#* Yearly number of houses sold
#* Monthly number of crimes committed
import pandas as pd
data=pd.read_csv(r'C:\Users\amirk\OneDrive\Desktop\FULLSTACK\DATAANALYZ\DATA-ANALYZE-PROJECTS\4-housing data\__ 005 Housing-Data.csv')
print(data.head(10))
print('=========')
### (A) Convert the Datatype of 'Date' column to Date-Time format.
#data.dtypes
#data.date = pd.to_datetime(data.date)
data['date']=pd.to_datetime(data.date)
print(data.head())
print('==========')
### (B.1) Add a new column ''year'' in the dataframe, which contains years only.
# data['New_Column'] = df.Date_Column.dt.year
data['year']=data.date.dt.year #add year from date coloumn to the year coloumn
print(data.head())
print('========')
### (B.2) Add a new column ''month'' as 2nd column in the dataframe, which contains month only.
# df.insert( index , ‘new_column_name’, new_column_values)
# data.insert (1 , 'month' , data.date.dt.month)
data.insert(1,'month',data.date.dt.month)
#add month from date column to new month column #above
print(data.head())
print('==========')
### (C) Remove the columns 'year' and 'month' from the dataframe.
#data.drop(['month', 'year'] , axis=1 , inplace = True)
data.drop(['month','year'],axis=1,inplace=True)
print(data.head(2))
print('=========')
data['year']=data.date.dt.year
### (D) Show all the records where 'No. of Crimes' is 0. And, how many such records are there ?
# data[data.no_of_crimes == 0]
# len(data[data.no_of_crimes == 0])
print(data[data.no_of_crimes==0])
print(len(data[data.no_of_crimes==0]))
### (E) What is the maximum & minimum 'average_price' per year in england ?
df1=data[data.area=='england']
df1.groupby('year').average_price.mean()
df1.groupby('year').average_price.max()
df1.groupby('year').average_price.min()
### (F) What is the Maximum & Minimum No. of Crimes recorded per area ?
print(data.groupby('area').no_of_crimes.max())
print('=============')
print(data.groupby('area').no_of_crimes.min())
print('============')
### (G) Show the total count of records of each area, where average price is less than 100000.
print(data[data.average_price<100000].area.value_counts())


