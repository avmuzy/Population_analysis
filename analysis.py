import csv
import pandas as pd
import matplotlib.pyplot as plt

x = pd.read_csv('/home/avms/PycharmProjects/Population_analysis/new_data_base.csv')
df = pd.DataFrame(x)
age = df["Age"]
kilo = df['Kilograms']
bmi = df['BMI'] = df['Kilograms'] / ((df['Centimeters'] / 100) ** 2)
print(bmi)

# manual slicing
'''
input_list = sorted(df['BMI'], reverse=False)
print(input_list)
severeThinness = []
print(len(severeThinness), severeThinness)
moderateThinness = input_list[:2]
print(len(moderateThinness), moderateThinness)
mildThinness = input_list[3:37]
print(len(mildThinness), mildThinness)
normal = input_list[38:66]
print(len(normal), normal)
overweight = input_list[67:84]
print(len(overweight), overweight)
obeseClass_I = input_list[85:96]
print(len(obeseClass_I), obeseClass_I)
obeseClass_II = input_list[97:99]
print(len(obeseClass_II), obeseClass_II)'''

# using filter and lambda functions
print(list(filter(lambda b: b < 16.9, bmi)))
print(list(filter(lambda b: 17 < b < 18.4, bmi)))
print(list(filter(lambda b: 18.5 < b < 24.9, bmi)))
print(list(filter(lambda b: 25 < b < 29.9, bmi)))
print(list(filter(lambda b: 30 < b < 34.9, bmi)))
print((list(filter(lambda b: 35 < b < 39.9, bmi))))
print((list(filter(lambda b: 40 < b < 49.9, bmi))))
print((list(filter(lambda b: b > 50, bmi))))
