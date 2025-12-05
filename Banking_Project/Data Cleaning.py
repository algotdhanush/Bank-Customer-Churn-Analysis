import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv("C:\\Users\\dhanu\\Downloads\\bank_customer_churn_20000.csv")

# Removes Duplicates
duplicate_remove = df.drop_duplicates(subset=['CustomerID'])
print(duplicate_remove)
print(df.shape)

#Convert Categorial variables to Category type
df['Gender'] =df['Gender'].astype('category')
df['Geography'] =df['Geography'].astype('category')
print(df.columns)

# Create New Column
df['Customervalue'] =(df['Balance']*0.4 +
                      df['EstimatedSalary']*0.3+
                      df['NumOfProducts']*0.2+
                      df['IsActiveMember']*0.1)
print(df['Customervalue'])

#Making A tenuregroup b/w the ages
df["TenureGroup"]= pd.cut(df["Tenure"],bins=[-1, 2, 5,10], labels=['0-2 yrs', '3-5 yrs', '6-10 yrs'])

#Making AgeGroups b/w ages
df['AgeGroup']= pd.cut(df['Age'], bins=[17, 30, 45, 60, 80], labels=['18-30', '31-45', '46-60', '61+'])

print(df.head())
print(df.info())
print(df.shape)

# Exploratory Data Analysis(EDA)
#Churyn by Gender
sns.countplot(data=df, x='Gender', hue='Exited')
plt.title('Count Of Exited Gender')
plt.show()

#Churn by Geography
sns.countplot(data=df, x= 'Geography', hue='Exited')
plt.title('Churn by Country')
plt.show()

#churn by AgeGroup
sns.countplot(data=df, x='AgeGroup', hue='Exited')
plt.title('Churn by Age Group')
plt.show()

#Churn by TenureGroup
sns.countplot(data=df, x='TenureGroup', hue='Exited')
plt.title('Churn by Tenure Group')
plt.show()

#Churn by Activity Level
sns.countplot(data=df, x='IsActiveMember', hue='Exited')
plt.title('Churn by IsActiveMember')
plt.show()

#Avg Balance for Churn Vs Non-Churn
df.groupby('Exited')['Balance'].mean()

#Correlation Heatmap
plt.figure(figsize=(10,5))
sns.heatmap(df.corr(numeric_only=True), annot=True,cmap='Blues')
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.show()

#df.to_excel("New_bank.xlsx")