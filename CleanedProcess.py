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

print("ABCDX ",has_adjacent_rep('ABCDX')) 
print("AABDC ",has_adjacent_rep('AABDC'))

''' Creating a function for checking it form a Character sequence or not'''
def has_sequence(pan):
    for i in range(len(pan)-1):
        if ord(pan[i+1]) - ord(pan[i]) != 1:
            return False
    return True

print("ABCDE ",has_sequence('ABCDE'))
print("ABCDE ",has_sequence('ABCDF'))
