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

def load_data_multiple(file_names: list[str]) -> tuple[list[list[float]],list[list[int]],list[list[int]]]:
    """
    Load data from multiple CSV files.
    Preconditions:
    - file_names is a list of strings containing the file names.
    Postconditions:
    - Three nested lists are returned with the time, moves and states for each gameboard.
    """
    time_random = []
    number_of_moves_random = []
    number_of_states_random = []
    for file_name in file_names:
        time, number_of_moves, number_of_states = load_data(file_name)
        time_random.append(time)
        number_of_moves_random.append(number_of_moves)
        number_of_states_random.append(number_of_states)
    
    return time_random, number_of_moves_random, number_of_states_random


def load_data(file_name: str) -> tuple[list[float],list[int],list[int]]:
    """
    Load data from CSV file. 
    Preconditions: 
    - file_name is a string containing the file name. 
    Postconditions:
    - Three lists are returned with the time, moves and states for each gameboard.
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

def plot_histogram(data: list[list[int]], hist_name: str, x_label: str, y_label: str, title: str) -> None:
    """
    Make a histogram with the given data.
    Preconditions:
    - data is a nested list with integers.
    - hist_name is a string representing the name of the histogram.
    - x_label is a string representing the label for the x-axis.
    - y_label is a string representing the label for the y-axis.
    - title is a string representing the title of the histogram.
    """
    plt.hist(data, color='#097a75')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.savefig(f"data_images/hist_{hist_name}", dpi=300, bbox_inches='tight')


def plot_boxplot_random(data: list[list[int]]) -> None:
    """
    Makes a boxplot with the given data.
    Preconditions:
    - data is a nested list with integers.
    """

    boxprops = {'color': 'black', 'linewidth': 1.5}
    whiskerprops = {'color': 'black', 'linewidth': 1.5}
    medianprops = {'color': 'black', 'linewidth': 1.5}
    flierprops = {'marker': 'o', 'markeredgecolor': 'black', 'markerfacecolor': 'black'}

    positions = [1, 2, 3, 4, 5, 6, 7]

    # Create the boxplots and get the box artists
    boxplot = plt.boxplot(data, positions=positions, patch_artist=True,
                          boxprops=boxprops, whiskerprops=whiskerprops,
                          capprops=whiskerprops, medianprops=medianprops,
                          flierprops=flierprops)

    # Customize box colors using a colormap
    cmap = plt.get_cmap('Spectral')
    for box, color in zip(boxplot['boxes'], cmap(np.linspace(0, 1, len(positions)))):
        box.set(facecolor=color)

    plt.xlabel("Gameboard")
    plt.ylabel("Moves")
    plt.title("Random Algorithm")

    # Customize x-axis ticks
    x_ticks = positions
    x_tick_labels = ["1 (6)", "2 (6)", "3 (6)", "4 (9)", "5 (9)", "6 (9)", "7 (12)"]
    plt.xticks(x_ticks, x_tick_labels)

    plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
    plt.savefig(f"data_images/boxplot_random", dpi=300, bbox_inches='tight')


def print_summary_statistics(data: list[int], title: str) -> None:
    """
    Print summary statistics for the given data.
    Preconditions:
    - data is a list of integers.
    - title is a string representing the title of the statistics.
    """
    statistic, p_value = stats.shapiro(data)
    median = np.median(data)
    iqr_25 = np.percentile(data, 25)
    iqr_75 = np.percentile(data, 75)
    print(f"{title}: statistic: {statistic}, p_value: {p_value}, median: {median}, iqr_25: {iqr_25}, iqr_75: {iqr_75}")

def plot_boxplot_hillclimber(data: list[list[int]]) -> None:
    """
    Makes a boxplot with the given data.
    Preconditions:
    - data is a nested list with integers.
    """

    boxprops = {'color': 'black', 'linewidth': 1}
    whiskerprops = {'color': 'black', 'linewidth': 1}
    medianprops = {'color': 'black', 'linewidth': 1}
    flierprops = {'marker': 'o', 'markeredgecolor': 'black', 'markerfacecolor': 'black'}

    positions = [1, 2, 3]

    # Create the boxplots and get the box artists
    boxplot = plt.boxplot(data, positions=positions, patch_artist=True,
                          boxprops=boxprops, whiskerprops=whiskerprops,
                          capprops=whiskerprops, medianprops=medianprops,
                          flierprops=flierprops)

    # Customize box colors using a colormap
    cmap = plt.get_cmap('Spectral')
    for box, color in zip(boxplot['boxes'], cmap(np.linspace(0, 1, len(positions)))):
        box.set(facecolor=color)

    plt.xlabel("Gameboard")
    plt.ylabel("Moves")
    plt.title("Hillclimber Algoritme")

    # Customize x-axis ticks
    x_ticks = positions
    x_tick_labels = ["6x6_1", "6x6_2","9x9_4"]
    plt.xticks(x_ticks, x_tick_labels)

    plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
    plt.savefig(f"data_images/boxplot_hillclimber", dpi=300, bbox_inches='tight')

def plot_boxplot_hill_rand(data_random: list[int], data_hillclimber: list[int], title: str) -> None:
    """
    Make a boxplot comparing the random and hillclimber algorithms.
    Preconditions:
    - data_random is a list of integers representing the data for the random algorithm.
    - data_hillclimber is a list of integers representing the data for the hillclimber algorithm.
    - title is a string representing the title of the plot. 
    """
    boxprops = {'color': 'black', 'linewidth': 1.5}
    whiskerprops = {'color': 'black', 'linewidth': 1.5}
    medianprops = {'color': 'black', 'linewidth': 1.5}
    flierprops = {'marker': 'o', 'markeredgecolor': 'black', 'markerfacecolor': 'black'}

    positions = [1, 2]

    # Create the boxplots and get the box artists
    boxplot = plt.boxplot([data_random, data_hillclimber], positions=positions, patch_artist=True,
                          boxprops=boxprops, whiskerprops=whiskerprops,
                          capprops=whiskerprops, medianprops=medianprops,
                          flierprops=flierprops)

    # Customize box colors using a colormap
    cmap = plt.get_cmap('Spectral')
    for box, color in zip(boxplot['boxes'], cmap(np.linspace(0, 1, len(positions)))):
        box.set(facecolor=color)

    plt.xlabel("Algorithm")
    plt.ylabel("Number of moves")
    plt.title(title)

    # Customize x-axis ticks
    x_ticks = positions
    x_tick_labels = ["Random", "Hillclimber"]
    plt.xticks(x_ticks, x_tick_labels)

    plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
    plt.savefig(f"data_images/boxplot_{title}", dpi=300, bbox_inches='tight')


if __name__=="__main__":
    # time, number_of_moves, number_of_states = load_random_data("6x6_1_random")
    
    time_random, number_of_moves_random, number_of_states_random = load_data_multiple(file_names_random)
    time_hillclimber, number_of_moves_hillclimber, number_of_states_hillclimber = load_data_multiple(file_names_hillclimber)

    # print(f"time random: {time_random}")
    # print(f"number_of_moves: {number_of_moves_random}")
    # print(f"number_of_states: {number_of_states_random}")

    # Random 6x6_1 moves 
    # print_summary_statistics(number_of_moves_random[0], "6x6_1_random")
    # Random 6x6_2 moves 
    # print_summary_statistics(number_of_moves_random[1], "6x6_2_random")
    # Random 6x6_3 moves 
    # print_summary_statistics(number_of_moves_random[2], "6x6_3_random")
    # Random 9x9_4 moves 
    # print_summary_statistics(number_of_moves_random[3], "9x9_4_random")
    # Random 9x9_5 moves 
    # print_summary_statistics(number_of_moves_random[4], "9x9_5_random")
    # Random 9x9_6 moves 
    # print_summary_statistics(number_of_moves_random[5], "9x9_6_random")
    # Random 12x12_7 moves 
    # print_summary_statistics(number_of_moves_random[6], "12x12_7_random")

    # Hillclimber 6x6_1 moves 
    # print_summary_statistics(number_of_moves_hillclimber[0], "6x6_1_hillclimber")
    # Hillclimber 6x6_2 moves 
    # print_summary_statistics(number_of_moves_hillclimber[1], "6x6_2_hillclimber")
    # Hillclimber 9x9_4 moves 
    # print_summary_statistics(number_of_moves_hillclimber[2], "9x9_4_hillclimber")


    # Random histogrammen 
    # plot_histogram(number_of_moves_random[0], "6x6_1_moves_random", "Number of moves", "Frequency", "Random Algoritme 6x6_1")
    # plot_histogram(number_of_moves_random[1], "6x6_2_moves_random", "Number of moves", "Frequency", "Random Algoritme 6x6_2")
    # plot_histogram(number_of_moves_random[2], "6x6_3_moves_random", "Number of moves", "Frequency", "Random Algoritme 6x6_3")
    # plot_histogram(number_of_moves_random[3], "9x9_4_moves_random", "Number of moves", "Frequency", "Random Algoritme 9x9_4")
    # plot_histogram(number_of_moves_random[4], "9x9_5_moves_random", "Number of moves", "Frequency", "Random Algoritme 9x9_5")
    # plot_histogram(number_of_moves_random[5], "9x9_6_moves_random", "Number of moves", "Frequency", "Random Algoritme 9x9_6")
    # plot_histogram(number_of_moves_random[6], "12x12_7_moves_random", "Number of moves", "Frequency", "Random Algoritme 12x12_7")


    # Random boxplot
    # plot_boxplot_random(number_of_moves_random)

    # Hillclimber boxplot
    # plot_boxplot_hillclimber(number_of_moves_hillclimber)

    # Random en Hillclimber boxplot
    # 6x6_1
    # plot_boxplot_hill_rand(number_of_moves_random[0], number_of_moves_hillclimber[0], "Gameboard 6x6_1")
    # 6x6_2
    # plot_boxplot_hill_rand(number_of_moves_random[1], number_of_moves_hillclimber[1], "Gameboard 6x6_2")
    # 9x9_4
    # plot_boxplot_hill_rand(number_of_moves_random[3], number_of_moves_hillclimber[2], "Gameboard 9x9_4")
