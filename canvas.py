import pygame
from config import SCREEN_SIZE
class Canvas: 
    def __init__(self): 
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("Fourier Series")
        self.running = True
        self.clock = pygame.time.Clock()
        