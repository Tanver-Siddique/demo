# Importing requries Libraties
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
mpg = sns.load_dataset('mpg')
#print(tips.head())
# Create the acatter plot
sns.relplot(x='model_year', y='mpg', data=mpg, kind='line', ci=None, style='origin', hue='origin', markers='o', dashes=False)

plt.show()