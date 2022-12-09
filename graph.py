# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
 

# Set data
df = pd.DataFrame({
'group': ['A','B','C','D'],
'Business': [6.5, 15, 32, 14],
'Modelling': [7.5, 10, 9, 34],
'Analytics': [4.5, 15, 32, 14],
'Economics': [8, 15, 32, 14],
'Programming': [3, 15, 32, 14],
'Finance': [7.5, 31, 33, 14],
'Empiric': [3.5, 39, 23, 24]
})
# number of variable
categories=list(df)[1:]
N = len(categories)
 
# We are going to plot the first line of the data frame.
# But we need to repeat the first value to close the circular graph:
values=df.loc[0].drop('group').values.flatten().tolist()
values += values[:1]
values
 
# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
 
# Initialise the spider plot
ax = plt.subplot(111, polar=True)
 
# Draw one axe per variable + add labels
plt.xticks(angles[:-1], categories, color='black', size=10)
 
# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks([2,4,6], ["","",""], color="black", size=8)
plt.ylim(0,8)
 
# Plot data
ax.plot(angles, values, linewidth=1, linestyle='solid')
 
# Fill area
ax.fill(angles, values, 'red', alpha=0.1)

# Show the graph
plt.show()