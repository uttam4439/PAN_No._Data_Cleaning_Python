import pandas as pd;

datafile = pd.read_excel('PAN Number Validation Dataset.xlsx')  # Reading excel file 

print(datafile.head(10)) # I want to print data records upto
print("Total No. of Data = ", len(datafile)) # total no. of data

# Change dataset datatype object to string and then operation for remove spaces and make uppercase
datafile["Pan_Numbers"] = datafile["Pan_Numbers"].astype('string').str.strip().str.upper()
print(datafile.head(10))

# Python or pandas behave differently with null value || Empty String 
'''
pandas uses openpyxl (or xlrd) under the hood.
By default, it interprets empty cells as NaN (Not a Number) — not as empty strings ''.
'''
print(datafile[datafile["Pan_Numbers"] == ''])

# To get actual no. of null values contain by dataset
print(datafile[datafile["Pan_Numbers"].isna()])

# Since i don't have any method to drop ' ' empty string i have to change it to NA value
datafile = datafile.replace({"Pan_Numbers" : ''}, pd.NA)
print(datafile[datafile["Pan_Numbers"] == '']) # Now it gives no value  
print(datafile[datafile["Pan_Numbers"].isna()]) # Empty value cell added to isna Category

# Drop the NAValue
datafile = datafile.dropna(subset="Pan_Numbers")
print(len(datafile))

''' This saves your cleaned data (no missing PANs, all uppercase, etc.) into a new Excel file.
When you save a DataFrame to Excel (or CSV), pandas includes that index by default so 
to not add index we give false;
'''
datafile.to_excel("Cleaned_PAN_Data.xlsx" , index= False)