import pygame
import sys
from config import SCREEN_SIZE
class Canvas: 
    def __init__(self): 
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("Fourier Series")
        self.running = True
        self.clock = pygame.time.Clock()
        self.fps = 60 
        self.N = 5 # Number of vectors 
        self.drawing = False
        self.curve_points = [] 




    def handle_events(self): 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                self.running = False 
            elif event.type == pygame.MOUSEBUTTONDOWN: 
                if event.button == 1: 
                    self.drawing = True
                    self.curve_points = []
            elif event.type == pygame.MOUSEBUTTONUP: 
                if event.button == 1: 
                    self.drawing = False


    def update(self): 
        pass 

    def render(self): 
        self.screen.fill((0,0,0))

        pygame.display.flip()
        self.clock.tick(self.fps)

    def run(self): 
        while(self.running): 
            self.handle_events()
            self.update()
            self.render()
        pygame.quit()
        sys.exit()
