import pandas as pd

dataframe = pd.read_excel("Cleaned_PAN_Data.xlsx")
print(len(dataframe))

#Unique Value in table
print('Unique Values = ',dataframe["Pan_Numbers"].nunique())

#Drop Duplicates
dataframe = dataframe.drop_duplicates(subset="Pan_Numbers",keep='first')
print(len(dataframe))

#Validation Process
''' Creating a function for checking Adjacent Character is same '''

def has_adjacent_rep(pan):
    for i in range(len(pan)-1):
        if(pan[i] == pan[i+1]):
            return True
        return False