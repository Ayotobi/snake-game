# Add background image and music

import pygame
from pygame.locals import *
import time
import random

SIZE = 10
BACKGROUND_COLOR = (110, 110, 5)

class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.transform.scale(pygame.image.load("assets/apple.png"),(30,30))
        self.x = 120
        self.y = 120

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.update()

    def move(self):
        self.x = random.randint(50,600)
        self.y = random.randint(50,600)

class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.HEAD_DOWN = pygame.transform.scale(pygame.image.load("assets/snake.png"),(30,50))
        self.HEAD_UP=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("assets/snake.png"), (30,50)), 180)
        self.HEAD_RIGHT =  pygame.transform.rotate(pygame.transform.scale(pygame.image.load("assets/snake.png"), (30,50)), 90)
        self.HEAD_LEFT=  pygame.transform.rotate(pygame.transform.scale(pygame.image.load("assets/snake.png"), (30,50)), 270)

        self.head_image = self.HEAD_DOWN
        
        self.body_image= pygame.transform.scale(pygame.image.load("assets/circle.png"),(30,30))
        self.direction = 'down'

        self.length = 1
        self.x = [40]
        self.y = [40]

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):
        # update body
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
            
        # update head
        if self.direction == 'left':
            self.x[0] -= SIZE
            self.head_image = self.HEAD_LEFT
        if self.direction == 'right':
            self.x[0] += SIZE
            self.head_image = self.HEAD_RIGHT
        if self.direction == 'up':
            self.y[0] -= SIZE
            self.head_image = self.HEAD_UP
        if self.direction == 'dofdwn':
            self.y[0] += SIZE
            self.head_image = self.HEAD_DOWN

        self.draw()

    def draw(self):
        self.parent_screen.blit(self.head_image, (self.x[0], self.y[0]))
        for i in range(1, self.length):
            self.parent_screen.blit(self.body_image, (self.x[i], self.y[i]))

        pygame.display.update()

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

class Game:
    def __init__(self):
        pygame.display.set_caption("Snake Game")
        self.clock= pygame.time.Clock()
        self.FPS=60
        pygame.font.init()
        # pygame.mixer.init()
        # self.play_background_music()
        self.WIDTH,self.HEIGHT= 650,650
        self.surface = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
        self.snake = Snake(self.surface)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    # def play_background_music(self):
    #     pygame.mixer.music.load('assets/bg_music_1.mp3')
    #     pygame.mixer.music.play(-1, 0)

    # def play_sound(self, sound_name):
    #     if sound_name == "crash":
    #         sound = pygame.mixer.Sound("assets/crash.mp3")
    #     elif sound_name == 'ding':
    #         sound = pygame.mixer.Sound("assets/ding.mp3")

        # pygame.mixer.Sound.play(sound)

    def reset(self):
        self.snake = Snake(self.surface)
        self.apple = Apple(self.surface)

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def render_background(self):
        bg = pygame.transform.scale(pygame.image.load("assets/background-black.png"),(self.WIDTH,self.HEIGHT))
        self.surface.blit(bg, (0,0))

    def play(self):
        self.render_background()
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.update()

        # snake eating apple scenario
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            # self.play_sound("ding")
            self.snake.increase_length()
            self.apple.move()

        # snake colliding with itself
        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                # self.play_sound('crash')
                raise "Collision Occurred"

    def display_score(self):
        font = pygame.font.SysFont('comicsans ',15)
        score = font.render(f"Score: {self.snake.length}",True,(200,200,200))
        self.surface.blit(score,(425,5))

    def show_game_over(self):
        self.render_background()
        font = pygame.font.SysFont('comicsans', 15)
        line1 = font.render(f"Game is over! Your score is {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(line1, (100, 150))
        line2 = font.render("To play again press Enter. To exit press Escape!", True, (255, 255, 255))
        self.surface.blit(line2, (100, 125))
        # pygame.mixer.music.pause()
        pygame.display.update()

    def run(self):
        running = True
        pause = False

        while running:
            self.clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        # pygame.mixer.music.unpause()
                        pause = False

                    if not pause:
                        if event.key == K_LEFT:
                            if self.snake.direction != "right":                                
                                self.snake.move_left()

                        if event.key == K_RIGHT:
                           if self.snake.direction != "left": 
                            self.snake.move_right()

                        if event.key == K_UP:
                            if self.snake.direction != "down":
                                self.snake.move_up()

                        if event.key == K_DOWN:
                            if self.snake.direction != "up":
                                self.snake.move_down()

                elif event.type == QUIT:
                    running = False
            try:

                if not pause:
                    self.play()

            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()

            time.sleep(.25)

if __name__ == '__main__':
    game = Game()
    game.run()