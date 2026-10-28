import matplotlib.pyplot as plt 
x =  [1, 2, 3, 4, 5]
y = [2,3,5,7,11]
error = [0.5,1,1.5,1,2]

fig, ax = plt.subplots(2,2) # consolidates the data plots into small, concise visualizations

ax[0,0].hist(x+y, bins=3) # IMP: here. x+y does not add consecutive elements but adds the two data sets into 1; bins = number of intervals
ax[0,0].set_title("histogram")

ax[0,1].scatter(x,y)
ax[0,1].set_title("scatter plot")

ax[1,0].errorbar(x,y, yerr=error, fmt='o', ecolor = 'green', capsize = 3)
ax[1,0].set_title("plot with error bar")

ax[1,1].boxplot([x,y])
ax[1,1].set_title("box-plot")

plt.tight_layout()
plt.show()
