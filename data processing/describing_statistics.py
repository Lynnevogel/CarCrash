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

file_names = ["6x6_1_random", "6x6_2_random", "6x6_3_random", "9x9_4_random", "9x9_5_random", "9x9_6_random", "12x12_7_random"]

def load_random_data_multiple(file_names):
    for file_name in file_names:
        load_random_data(file_name)

def load_random_data(file_name):
    time = []
    number_of_moves = []
    number_of_states = []
    with open(f"data/{file_name}.csv") as file:
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
    time, number_of_moves, number_of_states = load_random_data("6x6_1_random")

    statistic, p_value = stats.shapiro(number_of_moves)

    # plot_histogram(time)
    # plot_histogram(number_of_moves)
    # plot_histogram(number_of_states)

    # plot_boxplot(time)
    # plot_boxplot(number_of_moves)
    # plot_boxplot(number_of_states)

    # load_data()
    data1 = [1, 2, 3, 3, 3, 4, 4, 5]
    data2 = [2, 3, 4, 4, 4, 5, 5, 6]
    data3 = [3, 4, 5, 5, 5, 6, 6, 7]

    boxprops = {'color': 'blue', 'linewidth': 2}
    whiskerprops = {'color': 'red', 'linewidth': 2}
    medianprops = {'color': 'black', 'linewidth': 2}
    flierprops = {'marker': 'o', 'markeredgecolor': 'gray', 'markerfacecolor': 'gray'}

    positions = [1, 2, 3]

    # Create the boxplots and get the box artists
    boxplot = plt.boxplot([data1, data2, data3], positions=positions, patch_artist=True,
                          boxprops=boxprops, whiskerprops=whiskerprops,
                          capprops=whiskerprops, medianprops=medianprops,
                          flierprops=flierprops)

    # Customize box colors
    colors = ['lightblue', 'lightgreen', 'lightyellow']
    for box, color in zip(boxplot['boxes'], colors):
        box.set(facecolor=color)

    plt.xlabel("Category")
    plt.ylabel("Values")
    plt.title("Multiple Box Plots")

    # Customize x-axis ticks
    x_ticks = positions
    x_tick_labels = ["Data 1", "Data 2", "Data 3"]
    plt.xticks(x_ticks, x_tick_labels)

    # Customize y-axis ticks
    y_ticks = [0, 2, 4, 6, 8]
    y_tick_labels = ["0", "2", "4", "6", "8"]
    plt.yticks(y_ticks, y_tick_labels)

    plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
    plt.show()
