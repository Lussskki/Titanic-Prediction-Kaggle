import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

titanic_data = pd.read_csv('titanic/train.csv')

import seaborn as sns

sns.heatmap(titanic_data.corr(), cmap = 'YlgnBu')
print(plt.show)
