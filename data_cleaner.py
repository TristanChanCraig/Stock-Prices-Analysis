import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../data.csv')
missing = df.isnull().sum()
missing[0:10]