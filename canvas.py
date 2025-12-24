import pygame
import sys
from config import SCREEN_SIZE
import math 
from funcs import to_screen_coords, to_math_coords, resample_points, compute_fourier_coefficients
class Canvas: 
    def __init__(self): 
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("Fourier Series")
        self.running = True
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.dt = (1 / self.fps) * 0.1
        self.time = 0  
        self.N = 16 # Number of vectors to describe the curve 
        self.drawing = False
        self.curve_points = [] # stores points as complex numbers x + iy
        self.fourier_coeffs = [] 
        self.resolution = 500
        self.resultant_vectors = []
 




    def handle_events(self): 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                self.running = False 
            elif event.type == pygame.MOUSEBUTTONDOWN: 
                if event.button == 1: 
                    self.drawing = True
                    self.curve_points = []
                    self.fourier_coeffs = []
                    self.resultant_vectors = []
            elif event.type == pygame.MOUSEBUTTONUP: 
                if event.button == 1: 
                    self.drawing = False
                    self.curve_points = resample_points(self.curve_points, self.resolution) # Resample to 500 points
                    self.fourier_coeffs = compute_fourier_coefficients(self.curve_points, self.N)
            elif event.type == pygame.MOUSEMOTION: 
                if self.drawing: 
                    x, y = event.pos
                    self.curve_points.append(complex(x,y))


    def update(self): 
        if not self.drawing and self.fourier_coeffs: 
            self.time += self.dt
            # Loop time
            if self.time > 1: 
                self.time = 0
            resultant = 0 + 0j
            for i in range(len(self.fourier_coeffs)): 
                freq, coeff = self.fourier_coeffs[i]
                angle = 2 * math.pi * freq * self.time
                resultant += coeff * complex(math.cos(angle), math.sin(angle))
            self.resultant_vectors.append(resultant)
 


    def render(self): 
        self.screen.fill((0,0,0))
        if len(self.curve_points) > 1: 
            pygame.draw.lines(self.screen, (0,255,0), False, [(p.real, p.imag) for p in self.curve_points], 2)
        if len(self.resultant_vectors) > 2: 
            pygame.draw.lines(self.screen, (255,0,0), False, [(v.real, v.imag) for v in self.resultant_vectors], 2)
        pygame.display.flip()
        self.clock.tick(self.fps)

    def run(self): 
        while(self.running): 
            self.handle_events()
            self.update()
            self.render()
        pygame.quit()
        sys.exit()
