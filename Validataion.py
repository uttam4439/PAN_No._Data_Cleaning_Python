import pandas as pd;

datafile = pd.read_excel('PAN Number Validation Dataset.xlsx')  # Reading excel file 

print(datafile.head(10)) # I want to print data records upto
print("Total No. of Data = ", len(datafile)) # total no. of data

# Change dataset datatype object to string and then operation for remove spaces and make uppercase
datafile["Pan_Numbers"] = datafile["Pan_Numbers"].astype('string').str.strip().str.upper()
print(datafile.head(10))

# Python or pandas behave differently with null value 
print(datafile[datafile["Pan_Numbers"] == ''])

# To get actual no. of null values contain by dataset
print(datafile[datafile["Pan_Numbers"].isna()])