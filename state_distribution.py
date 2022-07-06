import pandas as pd
import matplotlib.pyplot as plt
import statistics
from functools import reduce
# reading csv file
x = pd.read_csv('/home/avms/data_base.csv')
df = pd.DataFrame(x)
# setting target column
stateFull = df['StateFull']

