import pygame
import sys
from config import SCREEN_SIZE
from funcs import to_screen_coords, to_math_coords, resample_points
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
        self.curve_points = [] # stores points as complex numbers x + iy 
        self.resolution = 500




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
                    # self.curve_points = resample_points(self.curve_points, self.resolution) # Resample to 500 points
            elif event.type == pygame.MOUSEMOTION: 
                if self.drawing: 
                    x, y = event.pos
                    self.curve_points.append(complex(x,y))


    def update(self): 
        pass 

    def render(self): 
        self.screen.fill((0,0,0))
        if len(self.curve_points) > 1: 
            pygame.draw.lines(self.screen, (0,255,0), False, [(p.real, p.imag) for p in self.curve_points], 2)

        pygame.display.flip()
        self.clock.tick(self.fps)

    def run(self): 
        while(self.running): 
            self.handle_events()
            self.update()
            self.render()
        pygame.quit()
        sys.exit()
