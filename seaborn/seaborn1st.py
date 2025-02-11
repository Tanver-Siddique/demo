# Importing requries Libraties
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
tips = sns.load_dataset('tips')
#print(tips.head())
hue_color = {'Yes': 'green', 'No': 'red'}
# plot the data
sns.scatterplot(x= 'total_bill', y= 'tip', data= tips, hue= 'smoker', hue_order= ['No', 'Yes'], palette= hue_color)
plt.show()