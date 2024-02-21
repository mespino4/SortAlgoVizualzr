# main.py
import pygame
import math
import random
from visualization import DrawInformation
from sorting_algorithms import bubble_sort, insertion_sort, quick_sort, shell_sort, heap_sort, selection_sort
from ui import SideBar, InfoBar  # Import InfoBar
import constants

pygame.init()

def generate_starting_list(n, min_val, max_val):
    lst = []
    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)
    return lst

def draw(draw_info, sidebar, infobar, ascending, background_color):
    draw_info.window.fill(background_color)
    
    # Draw sorting info
    draw_info.draw_list()
    
    # Draw the info bar
    infobar.draw()  # Draw the contents of the info bar

    # Draw the sidebar on top of the info bar and visualization
    sidebar.draw(sidebar.BUTTON_WIDTH + 2 * sidebar.MARGIN, ascending)

    pygame.display.update()

def main():
    run = True
    clock = pygame.time.Clock()
    n = 100
    min_val = 0
    max_val = 200

    lst = generate_starting_list(n, min_val, max_val)
    draw_info = DrawInformation(1000, 600, lst, infobar=None)  # Pass infobar=None initially
    infobar = InfoBar(draw_info.window, draw_info.FONT, draw_info.width, draw_info.height, SideBar.BUTTON_WIDTH)  # Pass draw_info.window instead of None

    background_color = constants.BACKGROUND_COLOR  # or any other color you want

    algorithms = ["Insertion Sort", "Bubble Sort", "Quick Sort", "Shell Sort", "Heap Sort", "Selection Sort"]
    sidebar = SideBar(draw_info.window, draw_info, algorithms, infobar)  # Pass infobar instead of None

    # Assign the infobar to the draw_info after it's created
    draw_info.infobar = infobar

    sorting = False
    ascending = True

    sorting_algorithm = bubble_sort
    sorting_algo_name = "Bubble Sort"
    sorting_algorithm_generator = None

    while run:
        clock.tick(60)

        if sorting:
            try:
                next(sorting_algorithm_generator)
                draw(draw_info, sidebar, infobar, ascending, background_color)  # Pass background_color
            except StopIteration:
                sorting = False
        else:
            draw(draw_info, sidebar, infobar, ascending, background_color)  # Pass background_color

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                sidebar.handle_click(pos)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    lst = generate_starting_list(n, min_val, max_val)
                    draw_info.set_list(lst)
                    sorting = False
                elif event.key == pygame.K_SPACE and not sorting:
                    if sidebar.selected_algorithm == "Insertion Sort":
                        sorting_algorithm = insertion_sort
                    elif sidebar.selected_algorithm == "Bubble Sort":
                        sorting_algorithm = bubble_sort
                    elif sidebar.selected_algorithm == "Quick Sort":
                        sorting_algorithm = quick_sort
                    elif sidebar.selected_algorithm == "Shell Sort":
                        sorting_algorithm = shell_sort
                    elif sidebar.selected_algorithm == "Heap Sort":
                        sorting_algorithm = heap_sort
                    elif sidebar.selected_algorithm == "Selection Sort":
                        sorting_algorithm = selection_sort
                    sorting_algo_name = sidebar.selected_algorithm
                    sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
                    sorting = True
                elif event.key == pygame.K_a:
                    ascending = True
                elif event.key == pygame.K_d:
                    ascending = False
                infobar.set_algorithm(sidebar.selected_algorithm)  # Update the selected algorithm in the info bar

    pygame.quit()


if __name__ == "__main__":
    main()
