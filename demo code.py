import pandas as pd
import matplotlib.pyplot as plt

# load the data
data = pd.read_csv('climate_change.csv', index_col='date', parse_dates=['date'])

# create a scatter plotpython
plt.style.use("ggplot")
fig, ax = plt.subplots()
ax.scatter(data['co2'], data['relative_temp'], c=data.index)
fig.set_size_inches
