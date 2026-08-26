import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler

border = "-"*70

data = {
  
    'Name':['Amit','Sagar','Pooja'],
    'Math':[85,90,78],
    'Science':[92,88,80],
    'English':[75,85,82]
  
}
#########################################################
#print the dataframe
print(border)
df = pd.DataFrame(data)
print("Data Frame:")
print(df)
print(border)

scaler = MinMaxScaler()
df[["Math"]] =  scaler.fit_transform(df[['Math']])

print("Normalize the math scores using Min-max scaling")
print(df)

print(border)
#########################################################

print("Group students by gender and calculate average marks:")
df['Gender'] = ["Male","Male","Female"]
df['Total'] = [253,260,242]

Average = df.groupby("Gender")["Total"].mean()

print("Average Marks:")
print(Average)

print(border)

#########################################################

print("Create a gender column and perform one- hot encoding")

encodedf = pd.get_dummies(df,columns=['Gender'],dtype=int)

print(encodedf)

print(border)
#########################################################

print("Plot a pie chart of subject marks for Sagar")

Name = "Sagar"

subject = {
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}

marks = [
    subject['Math'][0],
    subject['Science'][0],
    subject['English'][0]
]

labels = ['Math', 'Science', 'English']

plt.pie(marks, labels=labels, autopct="%1.1f%%")

plt.title("Pie Chart - Subject Marks for Sagar")

plt.show()

print(border)
############################################################
print("Add a new column status whhere student total with >= 250 are 'pass'else fail")

totalpass = df['Total']

status = []

for i in totalpass:
  if i >= 250:
     status.append("Pass")
  else:
    status.append("Fail")

df['Status'] = status

print(df)
print(border)

############################################################
print("Count How Many Student Passed")

cnt = 0
for i in status:
  if i == "Pass":
    cnt = cnt + 1
print("Total student passed:")
print(cnt)
print(border)
###########################################################

print("Export the final dataframe to a csv file")

Filename = open("Dataframe.csv","w")

Filename.write(str(df))

print("Data exported in csv succesfully..")

Filename.close()

print(border)
#############################################################

print("Plot a histogram for math marks")


plt.hist(df['Math'])

plt.title("Math Marks")
plt.xlabel("Marks")
plt.ylabel("Number of students")


plt.show()
print(border)
###########################################################

df.rename(columns = {"Math":"Mathematics"},inplace=True)

print(df)
print(border)

######################################################

plt.boxplot(df["English"], showmeans=True)

plt.title("English Marks - Distribution and Outliers")
plt.ylabel("Marks")

plt.show()
