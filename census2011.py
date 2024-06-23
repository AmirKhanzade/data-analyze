#This data is about total Population , Demography , Literacy , Districts , States, Workers , Religion , Education , Age .
#The data used here is of 2011 India Census of each district.
import pandas as pd
data=pd.read_csv(r'C:\Users\amirk\OneDrive\Desktop\FULLSTACK\DATAANALYZ\DATA-ANALYZE-PROJECTS\5-census 2011\__ 006 Census-2011.csv')
print(data.head())
print('==========')
### 1. How will you hide the indexes of the dataframe.
# df.style.hide_index()      
data.style.hide_index()
### 2. How can we set the caption / heading on the dataframe.
# df.style.set_caption('Caption')
data.style.set_caption('this data gathered from india') #we need to use jinja
print(data.head(2))
print('==========')
### 3. Show the records related with the districts - New Delhi , Lucknow , Jaipur.
#df[df['Col_name'].isin(['Item_1' , 'Item_2' , 'Item_3'])]
print(data[data['District_name'].isin(['New Delhi','Lucknow','jaipur'])])
### 4. Calculate state-wise :
### A. Total number of population.
### B. Total no. of population with different religions.
# df.groupby('Col_name_1').Col_names.sum()

#data.groupby('State_name').Population.sum().sort_values(ascending = False)

#data.groupby('State_name')['Hindus', 'Muslims', 'Christians', 'Sikhs', 'Buddhists', 'Jains'].sum().sort_values(by = 'Col_name')
data.groupby('State_name').Population.sum().sort_values(ascending=False)
data.groupby('State_name')['Hindus','Muslims','Christians','Sikhs','Buddhists','Jains'].sum().sort_values(by='Muslims')
### 5. How many Male Workers were there in Maharashtra state ?
# df[df.Col_name_1 == 'Item']['Col_name_2'].sum()
# data[data.State_name == 'MAHARASHTRA']['Male_Workers'].sum()
data[data.State_name=='MAHARASHTRA']['Male-Workers'].sum()
### 6. How to set a column as index of the dataframe ?
# df = df.set_index('Col_name')
data=data.set_index('District_code')
### 7a. Add a Suffix to the column names.
### 7b. Add a Prefix to the column names.
#7a. df = df.add_suffix('_value')

#7b. df = df.add_prefix('value_')

data=data.add_prefix('leftone_')

