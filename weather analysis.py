#Here, 
#The Weather Dataset is a time-series data set with per-hour information about the weather conditions at a particular location.
#It records Temperature, Dew Point Temperature, Relative Humidity, Wind Speed, Visibility, Pressure, and Conditions.
#This data is available as a CSV file. We are going to analyze this data set using the Pandas DataFrame.
import pandas as pd

data=pd.read_csv(r'C:\Users\amirk\OneDrive\Desktop\FULLSTACK\DATAANALYZ\DATA-ANALYZE-PROJECTS\1-weather data analyze\__ 001 Project-1-Weather-Dataset.csv') #import data files
print(data.head()) #it shows the n rows first data(default n=5)
#It shows the total no. of rows and no. of columns of the dataframe
print(data.shape)
## .index
#his attribute provides the index of the dataframe
print(data.index)
#.columns
#It shows the name of each column
print(data.columns)
#it shows the type of data for each column
print(data.dtypes)
#.unique()
#In a column, it shows all the unique values. 
#It can be applied on a single column only, not on the whole dataframe.
print(data['Weather'].unique())
#.nunique()
#It shows the total no. of unique values in each column. 
#It can be applied on a single column as well as on whole dataframe.
print(data.nunique())
#.count 
#It shows the total no. of non-null values in each column. 
#It can be applied on a single column as well as on whole dataframe.
print(data.count())
# .value_counts
#In a column, it shows all the unique values with their count. It can be applied on single column only.
print(data['Wind Speed_km/h'].value_counts())
#.info()
#Provides basic information about the dataframe.
print(data.info())
print('==============')
## Q) 1.  Find all the unique 'Temp_C' values in the data.
print(data['Temp_C'].nunique())
print('========')
## Q) 2. Find the number of times when the 'Weather is exactly Clear'.
## Filtering
print(data[data.Weather=='Clear'])
## groupby()
print(data.groupby('Weather').get_group('Clear'))
print('==========')
## Q) 3. Find the number of times when the 'Wind Speed was exactly 4 km/h'.
print(data.groupby('Wind Speed_km/h').get_group(4))
print(data[data['Wind Speed_km/h']==4]) #way2
print('===============')
## Q. 4) Find out all the Null Values in the data.
print(data.isnull().sum())
print('==============')
## Q. 5) Rename the column name 'Weather' of the dataframe to 'Weather Condition'
data.rename(columns={'Weather':'Weather condition'},inplace=True)
print(data.head())
print('=============')
## Q.6) What is the mean 'Visibility' ?
print(data.Visibility_km.mean())
print('==============')
## Q. 7) What is the Standard Deviation of 'Pressure'  in this data?
print(data.Press_kPa.std())
print('==============')
# Q. 8) Whats is the Variance of 'Relative Humidity' in this data ?
print(data['Rel Hum_%'].var())
print('==========')
# Q. 9) Find all instances when 'Snow' was recorded.
print(data[data['Weather condition']== 'Snow'])
## str.contains
data[data['Weather condition'].str.contains('Snow')].tail(50)
# Q. 10) Find all instances when 'Wind Speed is above 24' and 'Visibility is 25'.
print(data[(data['Wind Speed_km/h']>24) & (data['Visibility_km']==25)])
# Q. 11) What is the Mean value of each column against each 'Weather Conditon' ?
print(data.groupby('Weather condition').mean())
print('===========')
# Q. 12) What is the Minimum & Maximum value of each column against each 'Weather Conditon' ?
print(data.groupby('Weather condition').min())
print(data.groupby('Weather condition').max())
print('==========')
# Q. 13) Show all the Records where Weather Condition is Fog.
print(data[data['Weather condition']== 'Fog'])
print(data.groupby('Weather condition').get_group('Fog'))
# Q. 14) Find all instances when 'Weather is Clear' or 'Visibility is above 40'.
print(data[(data['Weather condition'] == 'Clear') & (data['Rel Hum_%'] > 50)|(data['Visibility_km'] > 40)])
# Q. 15) Find all instances when :
### A. 'Weather is Clear' and 'Relative Humidity is greater than 50'
### or
### B. 'Visibility is above 40'

print(data[(data['Weather condition'] == 'Clear') & (data['Rel Hum_%'] > 50)|(data['Visibility_km'] > 40)])