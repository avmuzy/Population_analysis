import pandas as pd
import matplotlib.pyplot as plt
import statistics
from functools import reduce

# reading csv
x = pd.read_csv('/home/avms/data_base.csv')
df = pd.DataFrame(x)
# defining the column to be analyzed
age = df["Age"]
