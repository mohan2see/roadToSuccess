import sys
import pygame


class AlienInvasion:
    """ a class for alien invasion game"""
    def __init__(self):
        """ Initializing the game and create game resources """
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        # set the background color
        self.bg_color = (130, 130, 130)

    def run_game(self):
        """ Starts the main loop for game """
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # fill the background color during each pass through the loop
            self.screen.fill(self.bg_color)
            # Make the most recently drawn screen visible.call to pygame.display.flip() tells Pygame to make the most
            # recently drawn screen visible. In this case, it simply draws an empty screen
            # on each pass through the while loop, erasing the old screen so only the new
            # screen is visible. When we move the game elements around, pygame.display
            # .flip() continually updates the display to show the new positions of game
            # elements and hides the old ones, creating the illusion of smooth movement.
            pygame.display.flip()


if __name__ == '__main__':
    # make the game instance, and runs the game
    ai = AlienInvasion()
    ai.run_game()




