import pandas as pd

data = {'Name':['Raghib','Rizwan','Rabani'],'Age':[19,50,100]}
df = pd.DataFrame(data) # Creating dataframe
# df = pd.DataFrames(index = , data = data)
print(df)

data1 = {'Name':['Raghib','Rizwan','Rabani'],'Age':[19,50,100]}
data1 = pd.Series(data1) # Creating series
print(data1)

# xls = pd.ExcelFile(r'excelfile.xlsx') -> for reading excel file
# d1 = pd.read_excel(xls,'Sheet1') -> Reading excel file Sheet1
# data.head()
# data.tail()
# pd.read_csv('heart.csv')
# data[sex][data[sex] == 0] = 'Female' -> changing name of the column
# data = data.rename(columns = {'age':'Age','sex':'gender'}) -> Changing heading of column
# data.describe() -> gives all numerical columns
# data.insert(0,'name',names) -> names = list of names and 0 is the index of column
# data = data[['age','sex','cp']] -> printing specific columns
# data.drop(labels=['cp'],axis = 1, inplace = True) -> dropping whole column and inplace = true means the changes will be done in original data frame.
# data = data.append(newRow,ignore_index = True) -> newRow is the dictionary having column heading and its data
# data.loc[7] = ["Ali",1,4,5,7,8] -> adding row at specific index
# newdf = df.drop(labels[0,2], axis = 'rows) -> deletes rows at index 0 and 2
# newdf = df.drop('name',axis = 'columns')
# data.reset_index(drop = False, inplace = True)
# result = pd.concat([data,data1],ignore_index = True)
# result = pd.concat([data,data1],axis = 1,ignore_index = False)
# data[['age']] -> selecting specific column
# data.iloc[1][3] -> iloc access columns and rows by index
# data.iloc[1: , 1:3] -> iloc access columns and rows by index (row,column)
# data.set_index('name')
# data.at['Elon','chol'] = 120 -> change value at specific index where Elon is row and chol is column
# data['new_col'] = data['sex'] + data['age'] -> Creates new derived column
# data = data.dropna(axis = 1, how = 'all') -> deletes all data of null value (all,any)
# data['sex'].replace({'female':0 , 'male':1}, inplace = True)
# data.to_csv('FinalData.csv', index = True, header = 'True) -> index write row names and header write column names
# data.columns -> is used to get column names
# data['newCol'] = df['CC Number'].apply(last_four) -> last_four is the function of getting last 4 digits of a string
# data[data['total_bill'].between(10,20,inclusive = True)]
