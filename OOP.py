import pygame
import time
import os
import random
class Game:
    def __init__(self) -> None:
        self.WIDTH,self.HEIGHT=700,700
        self.WIN=pygame.display.set_mode((self.WIDTH,self.HEIGHT))
        pygame.display.set_caption("SNAKE GAME")
        self.BG=pygame.image.load()