import matplotlib.pyplot as plt
import numpy as np
from code.classes.cars import Car


def visualize_board(board: list[list[str]], cars: dict[str, Car], save_path: str) -> None:
    """
    Visualizes the game board and car positions.
    Preconditions:
    - board is a nested list with strings representing the game board.
    - cars is a dictionary containing car objects, where the keys are car IDs and the values are Car objects.
    - save_path is de directory where the file is saved
    """
    dim = len(board)
    car_list = []

    for car in cars:
        car_list.append(car)

    # Create a grid
    grid = np.zeros((dim, dim), dtype=int)

    # Define color for each car using hex values
    car_colors = {'A': '#1f9dfa',
                  'B': '#f7175d',
                  'C': '#b314e2',
                  'D': '#6a2af2',
                  'E': '#324def',
                  'F': '#24cdf5',
                  'G': '#16aa93',
                  'H': '#43c92d',
                  'I': '#ff4d00',
                  'J': '#d5e70f',
                  'K': '#d4de6a',
                  'L': '#facc00',
                  'M': '#f09c39',
                  'N': '#eb6437',
                  'O': '#ff6561',
                  'P': '#ff4f93',
                  'Q': '#cb53f2',
                  'R': '#9a69f9',
                  'S': '#7181f6',
                  'T': '#52bcff',
                  'U': '#42dffe',
                  'V': '#38cbb9',
                  'W': '#6ae05e',
                  'Y': '#a9e654',
                  'AA': '#e3f23f',
                  'AB': '#ff8e8e',
                  'AC': '#ffb2d0',
                  'AD': '#eab3f9',
                  'AE': '#d1befc',
                  'AF': '#c1c9f9',
                  'AG': '#aee3ff',
                  'AH': '#a2f4ff',
                  'AI': '#98ecea',
                  'AJ': '#bbf1bb',
                  'AK': '#d8f7af',
                  'AL': '#f4fa9c',
                  'AM': '#fdf287',
                  'AN': '#f8d669',
                  'AO': '#f5b961',
                  'AP': '#e2150a',
                  'AQ': '#ae0456',
                  'AR': '#2c0fd3',
                  'AS': '#0f6972',
                  'X': '#e00d0d'}

    # Loop through the board and assign values to the grid based on the car positions
    for row in range(dim):
        for col in range(dim):
            if board[row][col] in car_list:
                car = board[row][col]
                grid[row][col] = car_list.index(car) + 1

    figure_size = dim * (2/3)
    fig, ax = plt.subplots(figsize=(figure_size, figure_size))

    # Set the background color
    fig.set_facecolor('#000010')  # Light gray

    # Loop through the grid and plot each car as a block of color with the letter on top
    for row in range(dim):
        for col in range(dim):
            car = board[row][col]
            if car != '-':
                color = car_colors[car]
                ax.add_patch(plt.Rectangle((col, row), 1, 1, facecolor=color, edgecolor='#000010'))
                ax.text(col + 0.5, row + 0.5, car, ha='center', va='center', fontsize=28, color='#000010', fontname='Monospace')

    for row in range(dim):
        if 'X' in board[row]:
            exit_row = row
            break

    # plot "exit" on exit block
    exit_col = dim - 1
    exit_color = '#000010'
    ax.add_patch(plt.Rectangle((exit_col, exit_row), 1, 1, facecolor=exit_color, edgecolor='#000010'))
    ax.text(exit_col + 0.5, exit_row + 0.5, 'EXIT', ha='center', va='center', fontsize=13, color='#00ff7b', fontname='Monospace', fontweight='bold')

    ax.set_xlim(0, dim + 0.5)
    ax.set_ylim(0, dim + 0.5)
    ax.grid(color='#fff', linewidth=0.3)
    ax.axis('off')
    ax.invert_yaxis()

    # Save the plot as an image
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
