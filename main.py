import pandas as pd
import matplotlib.pyplot as plt
x = pd.read_csv('/home/avms/data_base.csv')
df = pd.DataFrame(x)
print(x)
print(df[['Kilograms', 'Centimeters']])
print(type(x))
bmix = df['BMI'] = df['Kilograms'] / ((df['Centimeters']/100)**2)
print(bmix)
idade = df['Age']
fig, ax = plt.subplots()
ax.pie(idade, labels=bmix, autopct='%1.1f%%', shadow=True, startangle=90)
ax.axis('equal')
plt.show()
