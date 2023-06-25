import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np


data = [1, 2, 3, 3, 3, 4, 4, 5]

# mean
mean = np.mean(data)
print(f"mean: {mean}")
# median
median = np.median(data)
print(f"median: {median}")
# standard deviation
std_dev = np.std(data)
print(f"standard deviation: {std_dev}")
# interquartile range
iqr = np.percentile(data, 75) - np.percentile(data, 25)
print(f"iqr: {iqr}")

statistic, p_value = stats.shapiro(data)
print("Shapiro-Wilk Test Statistic:", statistic)
print("P-value:", p_value)

plt.hist(data)
plt.show()