import pandas as pd
import matplotlib.pyplot as plt
import statistics
from functools import reduce

# reading csv
x = pd.read_csv('/home/avms/data_base.csv')
df = pd.DataFrame(x)
# defining the column to be analyzed
age = df["Age"]

# Age group
children = (list(filter(lambda a: a <= 14, age)))
print(len(children), children)
youth = list(filter(lambda a: 15 <= a <= 24, age))
print(len(youth), youth)
adults = list(filter(lambda a: 25 <= a <= 64, age))
print(len(adults), adults)
senior = list(filter(lambda a: a >= 65, age))
print(len(senior), senior)
ageGroup = [0, 481, 2960, 1559]
ageDefinition = ['Children', 'Youth', 'Adult', 'Senior']

# pie plot
fig = plt.figure(figsize=(10, 7))
plt.pie(ageGroup, labels=ageDefinition)
plt.show()
