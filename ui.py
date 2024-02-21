import pygame
import constants

class SideBar:
    BUTTON_WIDTH = 200
    BUTTON_HEIGHT = 60  # Reduced button height
    MARGIN = 20  # Increased margin between buttons
    BACKGROUND_COLOR = (205, 240, 255)

    def __init__(self, window, draw_info, algorithms, infobar):
        self.window = window
        self.draw_info = draw_info
        self.algorithms = algorithms
        self.selected_algorithm = "Bubble Sort"  # Set default selected algorithm to Bubble Sort
        self.infobar = infobar  # Store the infobar object
        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        total_button_height = len(self.algorithms) * (self.BUTTON_HEIGHT + self.MARGIN) - self.MARGIN  # Adjusted total button height calculation
        available_height = self.draw_info.height - self.MARGIN * 2
        start_y = (available_height - total_button_height) // 2 + self.MARGIN + 20  # Increased start_y by 20 pixels

        for algo_name in self.algorithms:
            button_rect = pygame.Rect(self.MARGIN, start_y, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)
            button = pygame.Rect(self.MARGIN, start_y, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)
            self.buttons.append((button, algo_name))
            start_y += self.BUTTON_HEIGHT + self.MARGIN

    def draw(self, sidebar_width, ascending):  # Add the ascending parameter

        # Draw background color for the sidebar
        sidebar_rect = pygame.Rect(0, 0, self.BUTTON_WIDTH + 2 * self.MARGIN, self.draw_info.height)
        pygame.draw.rect(self.window, self.BACKGROUND_COLOR, sidebar_rect)

        # Draw the title indicating ascending or descending order
        title_text = self.draw_info.FONT.render(("Ascending" if ascending else "Descending"), True, constants.BLACK)
        title_rect = title_text.get_rect(center=((self.BUTTON_WIDTH + 2 * self.MARGIN) // 2, 50))  # Adjusted y-coordinate
        self.window.blit(title_text, title_rect)

        # Adjust the starting y-position for the buttons to accommodate the title
        total_button_height = len(self.algorithms) * (self.BUTTON_HEIGHT + self.MARGIN) - self.MARGIN  # Adjusted total button height calculation
        available_height = self.draw_info.height - self.MARGIN * 2 - title_rect.height
        start_y = (available_height - total_button_height) // 2 + self.MARGIN + title_rect.height

        # Draw buttons
        for button, algo_name in self.buttons:
            button.y = start_y
            pygame.draw.rect(self.window, constants.BLACK, button, 2)  # Use constants.BLACK
            text = self.draw_info.FONT.render(algo_name, True, constants.BLACK)  # Use constants.BLACK
            # Adjust font size for button text
            text = pygame.transform.scale(text, (self.BUTTON_WIDTH - 20, self.BUTTON_HEIGHT - 20))
            text_rect = text.get_rect(center=button.center)
            self.window.blit(text, text_rect)
            start_y += self.BUTTON_HEIGHT + self.MARGIN

    def handle_click(self, pos):
        for button, algo_name in self.buttons:
            if button.collidepoint(pos):
                self.selected_algorithm = algo_name
                self.draw_info.infobar.set_algorithm(algo_name)  # Update selected algorithm in the info bar
                break

class InfoBar:
    INFO_HEIGHT = 100  # Increase the height of the info bar
    TEXT_COLOR = (0, 0, 0)  # Black text color

    def __init__(self, window, font, width, height, sidebar_width):  # Add sidebar_width parameter
        self.window = window
        self.font = font
        self.selected_algorithm = "Bubble Sort"  # Set default selected algorithm to Bubble Sort
        self.controls_text = "SPACE - Run Algorithm    R - Reset    A - Ascending   D - Descending"
        self.width = width
        self.height = height  # Store the height parameter
        self.sidebar_width = sidebar_width  # Store the width of the sidebar

    def set_algorithm(self, algorithm_name):
        self.selected_algorithm = algorithm_name

    def draw(self):
        pygame.draw.rect(self.window, SideBar.BACKGROUND_COLOR, (self.sidebar_width, 0, self.width - self.sidebar_width, self.INFO_HEIGHT))  # Use SideBar.BACKGROUND_COLOR for the background color
        algorithm_text = self.font.render(self.selected_algorithm, True, self.TEXT_COLOR)
        controls_text = pygame.font.Font(None, 30).render(self.controls_text, True, self.TEXT_COLOR)  # Smaller font size
        
        # Calculate the y-coordinate for the algorithm text at the top
        algorithm_text_y = 10  # Increase separation from the top of the info bar
        # Calculate the y-coordinate for the controls text at the bottom
        controls_text_y = self.INFO_HEIGHT - controls_text.get_height() - 20  # Increase separation from the bottom of the info bar
        
        # Center the algorithm name text horizontally
        algorithm_text_x = self.sidebar_width + (self.width - self.sidebar_width - algorithm_text.get_width()) / 2
        # Center the controls text horizontally
        controls_text_x = self.sidebar_width + (self.width - self.sidebar_width - controls_text.get_width()) / 2
        
        # Draw the algorithm name text near the top of the info bar
        self.window.blit(algorithm_text, (algorithm_text_x, algorithm_text_y))  
        # Draw the controls text near the bottom of the info bar
        self.window.blit(controls_text, (controls_text_x, controls_text_y))  
