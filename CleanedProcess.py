import pandas as pd
import re

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


def is_valid_pan(pan):
    if(len(pan) != 10):
        return False
    
    ''' (^ — Start of string ) ([A-Z]{5} — First 5 characters) ([0-9]{4} — Next 4 characters)
    ([A-Z] — Last character) ($ — End of string) '''
    if not re.match(r'^[A-Z]{5}[0-9]{4}[A-Z]$', pan): # Not + regular exp. -> not None = true 
        return False                                  # if(not none = true) return false
    
    if has_adjacent_rep(pan):
        return False
    
    if has_sequence(pan):
        return False
    
    return True

dataframe["Status"] = dataframe["Pan_Numbers"].apply(lambda x: "Valid" if is_valid_pan(x) else "Invalid")
print(dataframe.head(10))   


# Summary of All in New Data Frame(Dictonary)
Total_Pan_no = len(pd.read_excel('PAN Number Validation Dataset.xlsx'))
Valid_pan = (dataframe["Status"] == "Valid").sum()
Invalid_pan = (dataframe["Status"] == "Invalid").sum()
Missing_pan = Total_Pan_no - (Valid_pan + Invalid_pan)


print("Total PAN_No in file = " ,Total_Pan_no)
print("Total Valid PAN in File = ",Valid_pan)
print("Total Invalid PAN in File = ",Invalid_pan)
print("Total Missing PAN in File = ",Missing_pan)
