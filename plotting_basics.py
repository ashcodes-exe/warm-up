import matplotlib.pyplot as plt

data = [[6, 3, 9, 5, 11], [15, 12, 18, 11, 16]] # defining 2 separate data sets
labels = ['A', 'B']
x_list = [1, 4, 6, 2, 5]
y_list = [1,4,9,16,25]

plt.boxplot(data, tick_labels=labels) # tick_labels = label labels each box plot according to the defined labels
plt.show()

plt.violinplot(data) # violin plot
plt.show()

plt.hist(x_list, y_list) # histogram
plt.show()
