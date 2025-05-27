"""
File: babygraphics.py
Name: Chia-Chun Hung
--------------------------------
Description:
Completed as part of SC101 Assignment 4. I implemented the GUI visualization for historical
baby name rankings, including dynamic canvas drawing, label positioning, and line plotting
across multiple years. This enhanced my skills in coordinate geometry, data mapping, and
user-interactive visualization.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt',
    'data/full/baby-2020.txt'
]
CANVAS_WIDTH = 1080
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010, 2020]  # Be cautious: these are integers, not string
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']         # Colors used for lines
TEXT_DX = 2                                         # Horizontal offset for text labels
LINE_WIDTH = 2
MAX_RANK = 1000


# Computes the x-coordinate for a vertical line based on the year index
def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    x_coordinate = GRAPH_MARGIN_SIZE + year_index*((width-GRAPH_MARGIN_SIZE*2)//len(YEARS))
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    # clear any existing drawings
    canvas.delete('all')

    # Draw top and bottom horizontal lines
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)

    # Draw vertical lines and year labels evenly spaced across the canvas
    for i in range(len(YEARS)):
        x_coordinate = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x_coordinate, GRAPH_MARGIN_SIZE-18, x_coordinate, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE+18)
        canvas.create_text(x_coordinate+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=str(YEARS[i]), anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # Redraw background lines each time

    # Calculate the pixel height for each rank step
    rank_h = (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE*2)/MAX_RANK

    # Map each year to its corresponding x-coordinate
    x_dict = {}
    for i in range(len(YEARS)):
        x_dict[str(YEARS[i])] = get_x_coordinate(CANVAS_WIDTH, i)

    # coord_list stores two consecutive coordinates for each name to draw connecting lines
    time_to_create_line = 0
    coord_lst = []
    color_count = 0

    # Loop through all names requested for plotting
    for lookup_name in lookup_names:
        for year in x_dict:
            if year not in name_data[lookup_name]:
                # if rank data is missing, show * at the bottom.
                canvas.create_text(int(x_dict[year])+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=f'{lookup_name} *'
                                   , fill=COLORS[color_count], anchor=tkinter.SW)
                time_to_create_line += 1
                coord_lst.append(int(x_dict[year])+TEXT_DX)
                coord_lst.append(CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)

            else:
                # if rank data is available, plot name and rank at appropriate y-coordinate
                canvas.create_text(int(x_dict[year])+TEXT_DX, rank_h*int(name_data[lookup_name][year])+GRAPH_MARGIN_SIZE
                                   , text=f'{lookup_name} {name_data[lookup_name][year]}'
                                   , fill=COLORS[color_count], anchor=tkinter.SW)

                time_to_create_line += 1
                coord_lst.append(int(x_dict[year]) + TEXT_DX)
                coord_lst.append(rank_h*int(name_data[lookup_name][year])+GRAPH_MARGIN_SIZE)
            # after plotting two or more years, draw a line between the last two points
            if time_to_create_line > 1:
                canvas.create_line(coord_lst[0], coord_lst[1], coord_lst[2], coord_lst[3], width=LINE_WIDTH, fill=COLORS[color_count])
                coord_lst = [coord_lst[2], coord_lst[3]]

        # After finishing each name, reset drawing state for the next time
        coord_lst = []
        time_to_create_line = 0

        # Cycle through COLORS list to assign line colors
        color_count += 1
        if color_count == 4:
            color_count = 0


def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
