import csv
import pandas as pd
import matplotlib.pyplot as plt

x = pd.read_csv('/home/avms/PycharmProjects/Population_analysis/new_data_base.csv')
df = pd.DataFrame(x)
age = df["Age"]
kilo = df['Kilograms']
bmi = df['BMI'] = df['Kilograms'] / ((df['Centimeters'] / 100) ** 2)
print(bmi)
input_list = sorted(df['BMI'], reverse=False)
print(input_list)
severeThinness = [0]
moderateThinness = input_list[:2]
print(moderateThinness)
mildThinness = input_list[3:37]
print(mildThinness)

