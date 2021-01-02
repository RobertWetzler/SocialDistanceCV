import pygame
import math
white = (255, 255, 255)
black = (0, 0, 0)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

class LocationsGUI:


    def start(self):
        pygame.init()
        self.side = 800
        self.room_side = 14
        self.gameDisplay = pygame.display.set_mode((self.side, self.side))
        pygame.event.get()
        self.gameDisplay.fill(white)
        pygame.display.update()

    def draw_people(self, people):
        pygame.event.get()
        self.gameDisplay.fill(white)
        for person in people:
            angle = math.radians(person['angle'])
            d = person['dist']
            x = d*math.sin(angle) + self.room_side/2
            y = d*math.cos(math.pi/2-angle)
            #print(f'{x} {y} {angle}')
            x_norm = x/14
            y_norm = y/14

            x_screen = x_norm * self.side
            y_screen = y_norm * self.side

            pygame.draw.circle(self.gameDisplay, black, (x_screen, y_screen), 10)
        pygame.display.update()

    def draw_good(self):
        pygame.event.get()
        self.gameDisplay.fill(white)
        pygame.draw.circle(self.gameDisplay, red, (self.side//2, self.side//2), 40)
        pygame.display.update()

    def draw_bad(self):
        pygame.event.get()
        self.gameDisplay.fill(white)
        pygame.draw.circle(self.gameDisplay, green, (self.side//2, self.side//2), 40)
        pygame.display.update()



