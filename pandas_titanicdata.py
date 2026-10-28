import pandas as pd # july 22

titanicdata = pd.read_csv("titanic.csv") # importing data

titanicdata.to_excel("titanic.xlsx", sheet_name = "passengers", index=False) # index is used to control whether we need index labelling with True/False

titanicdata.head(12) # start = head, end = tail; fetch all rows in this range (12 to 21)
titanicdata.tail(18)

print(titanicdata.columns) # fetch all column labels

print(titanicdata[["Name", "Age"]]) # NEEDS 2 []

print(titanicdata[0:5]) # row index - fetch a range of rows

titanicdata.set_index("Name", inplace = True) # convert a column to be the index of the rows

titanicdata.loc["Montvila, Rev. Juozas"] # fetch data from the new index (which is name)

titanicdata["Condition"] = ["Normal", "Disease", "Disease"] * int(891/3) # adds a column called "condition" with the following inputs

print(titanicdata.columns)

titanicdata.drop("Condition", axis = 1) # axis = 0 deletes the whole row (horizontal axis), axis = 1 deletes the whole column (vertical axis)

print(titanicdata[titanicdata["Age"]<18]) # filter everyone in this category based on given parameter

print(titanicdata[titanicdata["Age"]<18][titanicdata["Sex"] == "female"])

print(titanicdata.groupby("Condition").describe()) # shows the descriptive stats of the given column/data set 

age_male = titanicdata[titanicdata["Sex"] == "male"]["Age"] # categorize groups into a variable
age_female = titanicdata[titanicdata["Sex"] == "female"]["Age"]

titanicdata.isnull()
titanicdata.dropna(inplace = True)
titanicdata.fillna("NA")
