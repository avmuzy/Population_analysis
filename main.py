import csv
import pandas as pd
import matplotlib.pyplot as plt

x = pd.read_csv('/home/avms/data_base.csv')
df = pd.DataFrame(x)
print(x)
print(df[['Kilograms', 'Centimeters']])
print(type(x))
bmi = df['BMI'] = df['Kilograms'] / ((df['Centimeters']/100)**2)
print(bmi)

idade = df['Age']
'''fig, ax = plt.subplots()
ax.pie(idade, labels=bmix, autopct='%1.1f%%', shadow=True, startangle=90)
ax.axis('equal')
plt.show()

fig, ax = plt.subplots()
ax.plot(idade, bmix)
ax.set(xlabel='Age', ylabel='BMI',
       title='AGE X BMI')
ax.grid()

fig.savefig("test.png")
plt.show()
print(x.head())'''

# nem variables
severeThinness = (list(filter(lambda b: b < 16.9, bmi)))
moderateThinness = (list(filter(lambda b: 17 < b < 18.4, bmi)))
mildThinness = (list(filter(lambda b: 18.5 < b < 24.9, bmi)))
normal = (list(filter(lambda b: 25 < b < 29.9, bmi)))
overweight = (list(filter(lambda b: 30 < b < 34.9, bmi)))
obeseClassI = (list(filter(lambda b: 35 < b < 39.9, bmi)))
obeseClassII = (list(filter(lambda b: 40 < b < 49.9, bmi)))
obeseClassIII = (list(filter(lambda b: b > 50, bmi)))

# variables length
print('Severe Thinness:  ', len(severeThinness), severeThinness)
print('Moderate Thinness:', len(moderateThinness), moderateThinness)
print('Mild Thinness:   ', len(mildThinness), mildThinness)
print('Normal:          ', len(normal), normal)
print('Overweight:      ', len(overweight), overweight)
print('Obese Class I:   ', len(obeseClassI), obeseClassI)
print('Obese Class II:  ', len(obeseClassII), obeseClassII)
print('Obese Class III: ', len(obeseClassIII), obeseClassIII)
print(len(severeThinness), len(moderateThinness), len(mildThinness), len(normal), len(overweight),
      len(obeseClassI), len(obeseClassII), len(obeseClassIII))

# data for a pie plot
bmiNames = ['Severe Thinness', 'Moderate Thinness', 'Mild Thinness', 'Normal', 'Overweight', 'Obese Class I',
            'Obese Clas II', 'Obese Class III']
bmirange = len(severeThinness), len(moderateThinness), len(mildThinness), len(normal), len(overweight),
len(obeseClassI), len(obeseClassII), len(obeseClassIII)

# pie plot
fig = plt.figure(figsize=(10, 7))
plt.pie(bmirange, labels=bmiNames)
plt.show()