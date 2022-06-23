import pandas as pd
import csv
import matplotlib.pyplot as plt
x = pd.read_csv('new_data_base.csv')
df = pd.DataFrame(x)
age = df["Age"]
kilo = df['Kilograms']
bmix = df['BMI'] = df['Kilograms'] / ((df['Centimeters']/100)**2)
print(x.head())
maxBmi = df['BMI'].max()
minBmi = df['BMI'].min()
print(maxBmi, minBmi)