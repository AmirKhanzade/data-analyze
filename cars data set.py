## Cars Dataset
#***
#Here, 
#The data of different cars is given with their specifications.
#This data is available as a CSV file. We are going to analyze this data set using the Pandas DataFrame.
import pandas as pd

data=pd.read_csv(r'C:\Users\amirk\OneDrive\Desktop\FULLSTACK\DATAANALYZ\DATA-ANALYZE-PROJECTS\2-cars data set\__ 002 Project-2-Cars-Dataset.csv')
print(data.head())
print(data.shape)
print('=========')
#1) Instruction ( For Data Cleaning ) 
#- Find all Null Values in the dataset. If there is any null value in any column, then fill it with the mean of that column. 
print(data.isnull().sum())
data['Cylinders'].fillna(data['Cylinders'].mean(),inplace=True)
#2) Question ( Based on Value Counts )
#- Check what are the different types of Make are there in our dataset. And, what is the count (occurrence) of each Make in the data
#?
print(data['Make'].value_counts())
#3) Instruction ( Filtering )
#- Show all the records where Origin is Asia or Europe.
print(data[data['Origin'].isin(['Asia','Europe'])])
print('============')
#4) Instruction ( Removing unwanted records )
#- Remove all the records (rows) where Weight is above 4000.
data[~( data['Weight'] > 4000)]
#5) Instruction ( Applying function on a column )
#- Increase all the values of 'MPG_City' column by 3.
data['MPG_City']=data['MPG_City'].apply(lambda x:x+3)
print(data.head(400))
