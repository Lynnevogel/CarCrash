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

def load_data_multiple(file_names: list[str]) -> tuple[list[list[int]]|list[list[int]]|list[list[int]]]:
    time_random = []
    number_of_moves_random = []
    number_of_states_random = []
    for file_name in file_names:
        time, number_of_moves, number_of_states = load_data(file_name)
        time_random.append(time)
        number_of_moves_random.append(number_of_moves)
        number_of_states_random.append(number_of_states)
    
    return time_random, number_of_moves_random, number_of_states_random


def load_data(file_name: str):
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


def plot_boxplot(data):
    data1 = data[0]
    data2 = data[1]
    data3 = data[2]
    data4 = data[3]
    data5 = data[4]
    data6 = data[5]
    data7 = data[6]

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

    plt.xlabel("Gameboard")
    plt.ylabel("Moves")
    plt.title("Random Algoritme")

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

def plot_boxplot_hillclimber(data):
    data1 = data[0]
    data2 = data[1]
    data3 = data[2]

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
    # colors = ['lightblue', 'lightgreen', 'lightyellow']
    # for box, color in zip(boxplot['boxes'], colors):
    #     box.set(facecolor=color)

    plt.xlabel("Gameboard")
    plt.ylabel("Moves")
    plt.title("Hillclimber Algoritme")

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

def plot_boxplot_hill_rand(data_random, data_hillclimber, title):
    boxprops = {'color': 'blue', 'linewidth': 2}
    whiskerprops = {'color': 'red', 'linewidth': 2}
    medianprops = {'color': 'black', 'linewidth': 2}
    flierprops = {'marker': 'o', 'markeredgecolor': 'gray', 'markerfacecolor': 'gray'}

    positions = [1, 2]

    # Create the boxplots and get the box artists
    boxplot = plt.boxplot([data_random, data_hillclimber], positions=positions, patch_artist=True,
                          boxprops=boxprops, whiskerprops=whiskerprops,
                          capprops=whiskerprops, medianprops=medianprops,
                          flierprops=flierprops)

    plt.xlabel("Algorithm")
    plt.ylabel("Number of moves")
    plt.title(title)

    # Customize x-axis ticks
    x_ticks = positions
    x_tick_labels = ["Random", "Hillclimber"]
    plt.xticks(x_ticks, x_tick_labels)

    plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
    plt.savefig(f"data_images/boxplot_{title}", dpi=300, bbox_inches='tight')
    # plt.show()


if __name__=="__main__":
    # time, number_of_moves, number_of_states = load_random_data("6x6_1_random")
    
    time_random, number_of_moves_random, number_of_states_random = load_data_multiple(file_names_random)
    time_hillclimber, number_of_moves_hillclimber, number_of_states_hillclimber = load_data_multiple(file_names_hillclimber)

    # print(f"time random: {time_random}")
    # print(f"number_of_moves: {number_of_moves_random}")
    # print(f"number_of_states: {number_of_states_random}")

    # # Random 6x6_1 moves 
    # statistic, p_value = stats.shapiro(number_of_moves_random[0])
    # median_6x6_1_moves_random = np.median(number_of_moves_random[0])
    # iqr_6x6_1_moves_random_25 = np.percentile(number_of_moves_random[0], 25)
    # iqr_6x6_1_moves_random_75 = np.percentile(number_of_moves_random[0], 75)
    # print(f"Random 6x6_1: statistic: {statistic}, p_value: {p_value}, median: {median_6x6_1_moves_random}, iqr_25: {iqr_6x6_1_moves_random_25}, iqr_75: {iqr_6x6_1_moves_random_75}")

    # # Random 6x6_2 moves 
    # statistic, p_value = stats.shapiro(number_of_moves_random[1])
    # median_6x6_2_moves_random = np.median(number_of_moves_random[1])
    # iqr_6x6_2_moves_random_25 = np.percentile(number_of_moves_random[1], 25)
    # iqr_6x6_2_moves_random_75 = np.percentile(number_of_moves_random[1], 75)
    # print(f"Random 6x6_2: statistic: {statistic}, p_value: {p_value}, median: {median_6x6_2_moves_random}, iqr_25: {iqr_6x6_2_moves_random_25}, iqr_75: {iqr_6x6_2_moves_random_75}")

    # statistic, p_value = stats.shapiro(number_of_moves_random[2])
    # median_6x6_3_moves_random = np.median(number_of_moves_random[2])
    # iqr_6x6_3_moves_random_25 = np.percentile(number_of_moves_random[2], 25)
    # iqr_6x6_3_moves_random_75 = np.percentile(number_of_moves_random[2], 75)
    # print(f"Random 6x6_3: statistic: {statistic}, p_value: {p_value}, median: {median_6x6_3_moves_random}, iqr_25: {iqr_6x6_3_moves_random_25}, iqr_75: {iqr_6x6_3_moves_random_75}")

    # # Random 9x9_4 moves 
    # statistic, p_value = stats.shapiro(number_of_moves_random[3])
    # median_9x9_4_moves_random = np.median(number_of_moves_random[3])
    # iqr_9x9_4_moves_random_25 = np.percentile(number_of_moves_random[3], 25)
    # iqr_9x9_4_moves_random_75 = np.percentile(number_of_moves_random[3], 75)
    # print(f"Random 9x9_4: statistic: {statistic}, p_value: {p_value}, median: {median_9x9_4_moves_random}, iqr_25: {iqr_9x9_4_moves_random_25}, iqr_75: {iqr_9x9_4_moves_random_75}")

    # # Random 9x9_5 moves 
    # statistic, p_value = stats.shapiro(number_of_moves_random[4])
    # median_9x9_5_moves_random = np.median(number_of_moves_random[4])
    # iqr_9x9_5_moves_random_25 = np.percentile(number_of_moves_random[4], 25)
    # iqr_9x9_5_moves_random_75 = np.percentile(number_of_moves_random[4], 75)
    # print(f"Random 9x9_5: statistic: {statistic}, p_value: {p_value}, median: {median_9x9_5_moves_random}, iqr_25: {iqr_9x9_5_moves_random_25}, iqr_75: {iqr_9x9_5_moves_random_75}")

    # # Random 9x9_6 moves 
    # statistic, p_value = stats.shapiro(number_of_moves_random[5])
    # median_9x9_6_moves_random = np.median(number_of_moves_random[5])
    # iqr_9x9_6_moves_random_25 = np.percentile(number_of_moves_random[5], 25)
    # iqr_9x9_6_moves_random_75 = np.percentile(number_of_moves_random[5], 75)
    # print(f"Random 9x9_6: statistic: {statistic}, p_value: {p_value}, median: {median_9x9_6_moves_random}, iqr_25: {iqr_9x9_6_moves_random_25}, iqr_75: {iqr_9x9_6_moves_random_75}")

    # # Random 12x12_7 moves 
    # statistic, p_value = stats.shapiro(number_of_moves_random[5])
    # median_12x12_7_moves_random = np.median(number_of_moves_random[5])
    # iqr_12x12_7_moves_random_25 = np.percentile(number_of_moves_random[5], 25)
    # iqr_12x12_7_moves_random_75 = np.percentile(number_of_moves_random[5], 75)
    # print(f"Random 12x12_7: statistic: {statistic}, p_value: {p_value}, median: {median_12x12_7_moves_random}, iqr_25: {iqr_12x12_7_moves_random_25}, iqr_75: {iqr_12x12_7_moves_random_75}")

    # # Hillclimber 6x6_1 moves 
    # statistic, p_value = stats.shapiro(number_of_moves_hillclimber[0])
    # median_6x6_1_moves_hillclimber = np.median(number_of_moves_hillclimber[0])
    # iqr_6x6_1_moves_hillclimber_25 = np.percentile(number_of_moves_hillclimber[0], 25)
    # iqr_6x6_1_moves_hillclimber_75 = np.percentile(number_of_moves_hillclimber[0], 75)
    # print(f"Hillclimber 6x6_1: statistic: {statistic}, p_value: {p_value}, median: {median_6x6_1_moves_hillclimber}, iqr_25: {iqr_6x6_1_moves_hillclimber_25}, iqr_75: {iqr_6x6_1_moves_hillclimber_75}")

    # # Hillclimber 6x6_2 moves 
    # statistic, p_value = stats.shapiro(number_of_moves_hillclimber[1])
    # median_6x6_2_moves_hillclimber = np.median(number_of_moves_hillclimber[1])
    # iqr_6x6_2_moves_hillclimber_25 = np.percentile(number_of_moves_hillclimber[1], 25)
    # iqr_6x6_2_moves_hillclimber_75 = np.percentile(number_of_moves_hillclimber[1], 75)
    # print(f"Hillclimber 6x6_2: statistic: {statistic}, p_value: {p_value}, median: {median_6x6_2_moves_hillclimber}, iqr_25: {iqr_6x6_2_moves_hillclimber_25}, iqr_75: {iqr_6x6_2_moves_hillclimber_75}")

    # # Hillclimber 9x9_4 moves 
    # statistic, p_value = stats.shapiro(number_of_moves_hillclimber[2])
    # median_9x9_4_moves_hillclimber = np.median(number_of_moves_hillclimber[2])
    # iqr_9x9_4_moves_hillclimber_25 = np.percentile(number_of_moves_hillclimber[2], 25)
    # iqr_9x9_4_moves_hillclimber_75 = np.percentile(number_of_moves_hillclimber[2], 75)
    # print(f"Hillclimber 9x9_4: statistic: {statistic}, p_value: {p_value}, median: {median_9x9_4_moves_hillclimber}, iqr_25: {iqr_9x9_4_moves_hillclimber_25}, iqr_75: {iqr_9x9_4_moves_hillclimber_75}")

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

    # Random en Hillclimber boxplot
    # 6x6_1
    # plot_boxplot_hill_rand(number_of_moves_random[0], number_of_moves_hillclimber[0], "Gameboard 6x6_1")
    # 6x6_2
    # plot_boxplot_hill_rand(number_of_moves_random[1], number_of_moves_hillclimber[1], "Gameboard 6x6_2")
    # 9x9_4
    # plot_boxplot_hill_rand(number_of_moves_random[3], number_of_moves_hillclimber[2], "Gameboard 9x9_4")
