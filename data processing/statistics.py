import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np

# # Test
# data = [1, 2, 3, 3, 3, 4, 4, 5]

# # mean
# mean = np.mean(data)
# # median
# median = np.median(data)
# # standard deviation
# std_dev = np.std(data)
# # interquartile range
# iqr = np.percentile(data, 75) - np.percentile(data, 25)
# # shapiro-wilk test
# statistic, p_value = stats.shapiro(data)

file_names_random = ["6x6_1_random", "6x6_2_random", "6x6_3_random", "9x9_4_random", "9x9_5_random", "9x9_6_random", "12x12_7_random"]
file_names_hillclimber = ["6x6_1_hillclimber", "6x6_2_hillclimber", "9x9_4_hillclimber"]

def load_random_data_multiple(file_names: list[str]) -> tuple[list[list[int]]|list[list[int]]|list[list[int]]]:
    time_random = []
    number_of_moves_random = []
    number_of_states_random = []
    for file_name in file_names:
        time, number_of_moves, number_of_states = load_random_data(file_name)
        time_random.append(time)
        number_of_moves_random.append(number_of_moves)
        number_of_states_random.append(number_of_states)
    
    return time_random, number_of_moves_random, number_of_states_random


def load_random_data(file_name: str):
    """
    Load data from CSV file. 
    Preconditions: 
    - file_name is a string containing the file name. 
    """
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

def plot_histogram(data, hist_name: str, x_label: str, y_label: str, title: str) -> None:
    """
    Make histogram with the given data.
    """
    plt.hist(data, color='green')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.savefig(f"data_images/hist_{hist_name}", dpi=300, bbox_inches='tight')


def plot_boxplot(number_of_moves_random):
    data1 = number_of_moves_random[0]
    data2 = number_of_moves_random[1]
    data3 = number_of_moves_random[2]
    data4 = number_of_moves_random[3]
    data5 = number_of_moves_random[4]
    data6 = number_of_moves_random[5]
    data7 = number_of_moves_random[6]

    boxprops = {'color': 'blue', 'linewidth': 2}
    whiskerprops = {'color': 'red', 'linewidth': 2}
    medianprops = {'color': 'black', 'linewidth': 2}
    flierprops = {'marker': 'o', 'markeredgecolor': 'gray', 'markerfacecolor': 'gray'}

    positions = [1, 2, 3, 4, 5, 6, 7]

    # Create the boxplots and get the box artists
    boxplot = plt.boxplot([data1, data2, data3, data4, data5, data6, data7], positions=positions, patch_artist=True,
                          boxprops=boxprops, whiskerprops=whiskerprops,
                          capprops=whiskerprops, medianprops=medianprops,
                          flierprops=flierprops)

    # Customize box colors
    colors = ['lightblue', 'lightgreen', 'lightyellow']
    for box, color in zip(boxplot['boxes'], colors):
        box.set(facecolor=color)

    plt.xlabel("Moves")
    plt.ylabel("Frequency")
    plt.title("Random Algritme")

    # Customize x-axis ticks
    x_ticks = positions
    x_tick_labels = ["6x6_1", "6x6_2", "6x6_3", "9x9_4", "9x9_5", "9x9_6", "12x12_7"]
    plt.xticks(x_ticks, x_tick_labels)

    # Customize y-axis ticks
    # y_ticks = [0, 2, 4, 6, 8]
    # y_tick_labels = ["0", "2", "4", "6", "8"]
    # plt.yticks(y_ticks, y_tick_labels)

    plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
    plt.savefig(f"data_images/boxplot_random", dpi=300, bbox_inches='tight')
    # plt.show()


def print_summary_statistics(data, labels):
    for i in range(len(data)):
        statistic, p_value = stats.shapiro(data[i])
        median = np.median(data[i])
        iqr = np.percentile(data[i], 75) - np.percentile(data[i], 25)
        print(f"{labels[i]}: statistic: {statistic}, p_value: {p_value}, median: {median}, iqr: {iqr}")

def plot_boxplot_hillclimber(number_of_moves_random):
    data1 = number_of_moves_random[0]
    data2 = number_of_moves_random[1]
    data3 = number_of_moves_random[2]

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

    plt.xlabel("Moves")
    plt.ylabel("Frequency")
    plt.title("Hillclimber Algritme")

    # Customize x-axis ticks
    x_ticks = positions
    x_tick_labels = ["6x6_1", "6x6_2","9x9_4"]
    plt.xticks(x_ticks, x_tick_labels)

    # Customize y-axis ticks
    # y_ticks = [0, 2, 4, 6, 8]
    # y_tick_labels = ["0", "2", "4", "6", "8"]
    # plt.yticks(y_ticks, y_tick_labels)

    plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
    plt.savefig(f"data_images/boxplot_hillclimber", dpi=300, bbox_inches='tight')
    # plt.show()

if __name__=="__main__":
    # time, number_of_moves, number_of_states = load_random_data("6x6_1_random")
    
    time_random, number_of_moves_random, number_of_states_random = load_random_data_multiple(file_names_random)
    time_hillclimber, number_of_moves_hillclimber, number_of_states_hillclimber = load_random_data_multiple(file_names_hillclimber)

    # print(f"time random: {time_random}")
    # print(f"number_of_moves: {number_of_moves_random}")
    # print(f"number_of_states: {number_of_states_random}")

    # # Random 6x6_1 time
    # statistic, p_value = stats.shapiro(time_random[0])
    # median_6x6_1_time_random = np.median(time_random[0])
    # iqr_6x6_1_time_random = np.percentile(time_random[0], 75) - np.percentile(time_random[0], 25)
    # print(f"Random 6x6_1: statistic: {statistic}, p_value: {p_value}, median: {median_6x6_1_time_random}, iqr: {iqr_6x6_1_time_random}")

    # # Random 6x6_2 time
    # statistic, p_value = stats.shapiro(time_random[1])
    # median_6x6_2_time_random = np.median(time_random[1])
    # iqr_6x6_2_time_random = np.percentile(time_random[1], 75) - np.percentile(time_random[1], 25)
    # print(f"Random 6x6_2: statistic: {statistic}, p_value: {p_value}, median: {median_6x6_2_time_random}, iqr: {iqr_6x6_2_time_random}")

    # # Random 9x9_4 time
    # statistic, p_value = stats.shapiro(time_random[2])
    # median_9x9_4_time_random = np.median(time_random[2])
    # iqr_9x9_4_time_random = np.percentile(time_random[2], 75) - np.percentile(time_random[2], 25)
    # print(f"Random 9x9_4: statistic: {statistic}, p_value: {p_value}, median: {median_9x9_4_time_random}, iqr: {iqr_9x9_4_time_random}")

    # Random 6x6_1 moves 
    # statistic, p_value = stats.shapiro(number_of_moves_random[0])
    # median_6x6_1_moves_random = np.median(number_of_moves_random[0])
    # iqr_6x6_1_moves_random = np.percentile(number_of_moves_random[0], 75) - np.percentile(number_of_moves_random[0], 25)
    # print(f"Random 6x6_1: statistic: {statistic}, p_value: {p_value}, median: {median_6x6_1_moves_random}, iqr: {iqr_6x6_1_moves_random}")

    # # Random 6x6_2 moves 
    # statistic, p_value = stats.shapiro(number_of_moves_random[1])
    # median_6x6_2_moves_random = np.median(number_of_moves_random[1])
    # iqr_6x6_2_moves_random = np.percentile(number_of_moves_random[1], 75) - np.percentile(number_of_moves_random[1], 25)
    # print(f"Random 6x6_2: statistic: {statistic}, p_value: {p_value}, median: {median_6x6_2_moves_random}, iqr: {iqr_6x6_2_moves_random}")

    # # Random 9x9_4 moves 
    # statistic, p_value = stats.shapiro(number_of_moves_random[2])
    # median_9x9_4_moves_random = np.median(time_random[2])
    # iqr_9x9_4_moves_random = np.percentile(number_of_moves_random[2], 75) - np.percentile(number_of_moves_random[2], 25)
    # print(f"Random 9x9_4: statistic: {statistic}, p_value: {p_value}, median: {median_9x9_4_moves_random}, iqr: {iqr_9x9_4_moves_random}")

    # # Random 6x6_1 states 
    # statistic, p_value = stats.shapiro(number_of_states_random[0])
    # median_6x6_1_states_random = np.median(number_of_states_random[0])
    # iqr_6x6_1_states_random = np.percentile(number_of_states_random[0], 75) - np.percentile(number_of_states_random[0], 25)
    # print(f"Random 6x6_1: statistic: {statistic}, p_value: {p_value}, median: {median_6x6_1_states_random}, iqr: {iqr_6x6_1_states_random}")

    # # Random 6x6_2 states
    # statistic, p_value = stats.shapiro(number_of_states_random[1])
    # median_6x6_2_states_random = np.median(number_of_states_random[1])
    # iqr_6x6_2_states_random = np.percentile(number_of_states_random[1], 75) - np.percentile(number_of_states_random[1], 25)
    # print(f"Random 6x6_2: statistic: {statistic}, p_value: {p_value}, median: {median_6x6_2_states_random}, iqr: {iqr_6x6_2_states_random}")

    # # Random 9x9-4 states
    # statistic, p_value = stats.shapiro(number_of_states_random[2])
    # median_9x9_4_states_random = np.median(number_of_states_random[2])
    # iqr_9x9_4_states_random = np.percentile(number_of_states_random[2], 75) - np.percentile(number_of_states_random[2], 25)
    # print(f"Random 9x9_4: statistic: {statistic}, p_value: {p_value}, median: {median_9x9_4_states_random}, iqr: {iqr_9x9_4_states_random}")

    # labels = [
    # "Random 6x6_1 time",
    # "Random 6x6_2 time",
    # "Random 9x9_4 time",
    # "Random 6x6_1 moves",
    # "Random 6x6_2 moves",
    # "Random 9x9_4 moves",
    # "Random 6x6_1 states",
    # "Random 6x6_2 states",
    # "Random 9x9-4 states"
    #     ]
    # print_summary_statistics(time_random, labels)
    # print_summary_statistics(number_of_moves_random, labels)
    # print_summary_statistics(number_of_states_random, labels)


    # Random histogrammen 
    # plot_histogram(number_of_moves_random[0], "6x6_1_moves_random", "Number of moves", "Frequency", "Random Algoritme 6x6_1")
    # plot_histogram(number_of_moves_random[1], "6x6_2_moves_random", "Number of moves", "Frequency", "Random Algoritme 6x6_2")
    # plot_histogram(number_of_moves_random[2], "6x6_3_moves_random", "Number of moves", "Frequency", "Random Algoritme 6x6_3")
    # plot_histogram(number_of_moves_random[3], "9x9_4_moves_random", "Number of moves", "Frequency", "Random Algoritme 9x9_4")
    # plot_histogram(number_of_moves_random[4], "9x9_5_moves_random", "Number of moves", "Frequency", "Random Algoritme 9x9_5")
    # plot_histogram(number_of_moves_random[5], "9x9_6_moves_random", "Number of moves", "Frequency", "Random Algoritme 9x9_6")
    # plot_histogram(number_of_moves_random[6], "12x12_7_moves_random", "Number of moves", "Frequency", "Random Algoritme 12x12_7")


    # Random boxplot
    # plot_boxplot(number_of_moves_random)

    # Hillclimber boxplot
    # plot_boxplot_hillclimber(number_of_moves_hillclimber)
