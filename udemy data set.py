#This dataset contains all course data for all subjects. 
#We will analyze this data using the Pandas Library.
import pandas as pd
data=pd.read_csv(r'C:\Users\amirk\OneDrive\Desktop\FULLSTACK\DATAANALYZ\DATA-ANALYZE-PROJECTS\6-udeemy data set\__ 007 Project-7-Udemy-Dataset.csv')
print(data.head(2))
print('==========')
### 1. What are all different subjects for which Udemy is offering courses ?
#data.subject.unique()
print(data.subject.unique())
print('===========')
### 2. Which subject has the maximum number of courses.
#data.subject.value_counts()
print(data.subject.value_counts())
print('=============')
### 3. Show all the courses which are Free of Cost.
#data[data.is_paid == False]
print(data[data.is_paid==False])
print('==============')
### 4. Show all the courses which are Paid.
print(data[data.is_paid==True])
print('================')
### 5. Which are Top Selling Courses ?
#data.sort_values('num_subscribers', ascending = False)
print(data.sort_values('num_subscribers',ascending=False))
print('===========')
### 6. Which are Least Selling Courses ?
print(data.sort_values('num_subscribers'))
### 7. Show all courses of Graphic Design where the price is below 100 ?
#Correct Solution :
data1=data[data.price!='Free'] # - Removing all rows which contains Free and creating a new dataframe 'data1'.
data1.price=data1.price.astype(int)
#- Changing the price column datatype to 'int'.
print(data1[(data1.subject=='Graphic Design')&(data1.price<100)]) #- Applying the logic now
### 8. List out all the courses that are related with 'Python'.
#data[data.course_title.str.contains('Python')]
print(data[data.course_title.str.contains('Python')])
print('==============')
### 9. What are courses that published in year 2015 ?
#data.dtypes
#data['published_timestamp'] = pd.to_datetime(data.published_timestamp)
#data.dtypes
#data['Year'] = data['published_timestamp'].dt.year
#data[data.Year == 2015]
data['published_timestamp']=pd.to_datetime(data.published_timestamp)
data['Year']=data['published_timestamp'].dt.year
print(data[data.Year==2015])
print('=============')
### 10. What are the Max. Number of Subscribers for Each Level of courses ?
#data.groupby('level')['num_subscribers'].max()
#data.groupby('level').max()
print(data.groupby('level')['num_subscribers'].max())
