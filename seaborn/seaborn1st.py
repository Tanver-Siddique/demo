# Importing requries Libraties
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
tips = sns.load_dataset('tips')
#print(tips.head())
hue_color = {'Yes': 'green', 'No': 'red'}
# plot the data
sns.relplot(x= "total_bill", y="tip", data= tips, kind= "scatter", row="time", col='day', col_order= ['Thur', 'Fri', 'Sat', 'Sun'])
plt.show()