import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv("C:\\Users\\dhanu\\Downloads\\bank_customer_churn_20000.csv")
print(df.head())
print(df.tail())

#getting information about the data
print(df.info())

#Understanding data with Summary stats
print(df.describe())

#Checking null values
print(df.isnull().sum())

#Checking Class Distribution
print(df['Exited'].value_counts(normalize=True)*100)

#Visualization
sns.countplot(x= "Exited", data=df)
plt.title("Churn Distribution")
plt.show()



