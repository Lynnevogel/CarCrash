import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np


data = [1, 2, 3, 3, 3, 4, 4, 5]

# mean
mean = np.mean(data)
# median
median = np.median(data)
# standard deviation
std_dev = np.std(data)
# interquartile range
iqr = np.percentile(data, 75) - np.percentile(data, 25)
# shapiro-wilk test
statistic, p_value = stats.shapiro(data)

plt.hist(data)
# plt.show()

file_names = ["6x6_1_random", "6x6_2_random", "6x6_3_random", "9x9_4_random", "9x9_5_random", "9x9_6_random", "12x12_7_random"]

def load_random_data(file_names):
    for file_name in file_names:
        with open(f"data/{file_name}.csv") as file:
            next(file)
            for line in file: 
                data = line.strip().split(",")

def load_random_data_test():
    time = []
    number_of_moves = []
    number_of_states = []
    with open(f"data/6x6_2_random.csv") as file:
        next(file)
        for line in file: 
            data = line.strip().split(",")
            time_data = float(data[4])
            number_of_moves_data = int(data[5])
            number_of_states_data = int(data[6])

            time.append(time_data)
            number_of_moves.append(number_of_moves_data)
            number_of_states.append(number_of_states_data)
    
    return time, number_of_moves, number_of_states

def plot_histogram(data):
    plt.hist(data)
    plt.show()

def plot_boxplot(data):
    plt.boxplot(data)
    plt.show()


if __name__=="__main__":
    time, number_of_moves, number_of_states = load_random_data_test()

    plot_histogram(time)
    plot_histogram(number_of_moves)
    plot_histogram(number_of_states)

    plot_boxplot(time)
    plot_boxplot(number_of_moves)
    plot_boxplot(number_of_states)
