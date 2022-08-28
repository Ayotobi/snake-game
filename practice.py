from re import T
import pygame
import random
import time
import datetime


pygame.font.init()
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SNAKE GAME")


class Snake:
    def __init__(self, parent_screen) -> None:
        SNAKE_SIZE = 30, 50
        self.snake_vel = 2
        self.SNAKE = pygame.transform.rotate(pygame.transform.scale(
            pygame.image.load("assets/snake.png"), SNAKE_SIZE), 0)
        self.SNAKE_RIGHT = pygame.transform.rotate(pygame.transform.scale(
            pygame.image.load("assets/snake.png"), SNAKE_SIZE), 90)
        self.SNAKE_UP = pygame.transform.rotate(pygame.transform.scale(
            pygame.image.load("assets/snake.png"), SNAKE_SIZE), 180)
        self.SNAKE_LEFT = pygame.transform.rotate(pygame.transform.scale(
            pygame.image.load("assets/snake.png"), SNAKE_SIZE), 270)
        self.body_width = 13
        self.body_radius = 14
        self.body_image = pygame.transform.scale(
            pygame.image.load("assets/circle.png"), SNAKE_SIZE)
        self.direction = ""
        self.parent_screen = parent_screen
        self.length = 1
        self.x = [250]
        self.y = [400]

    def collision(self):
        for i in range(5, self.length):
            if abs(self.x[0] - self.x[i]) < self.snake_vel and abs(self.y[0]-self.y[i]) < self.snake_vel:
                raise 'Game Over'

    def increase_length_giant_apple(self):
        self.increase_length()
        self.increase_length()
        self.increase_length()
        self.increase_length()
        self.increase_length()
        self.increase_length()
        self.increase_length()
        self.increase_length()
        self.increase_length()
        self.increase_length()

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def walk(self):
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

    def direction_change(self, drctn):
        if drctn == "down":
            if self.direction != "up":
                self.direction = "down"

        if drctn == "up":
            if self.direction != "down":
                self.direction = "up"

        if drctn == "left":
            if self.direction != "right":
                self.direction = "left"

        if drctn == "right":
            if self.direction != "left":
                self.direction = "right"

    def move(self):
        if self.direction == "up":
            self.move_up()
        elif self.direction == "down":
            self.move_down()
        elif self.direction == "left":
            self.move_left()
        elif self.direction == "right":
            self.move_right()

        self.walk()
        pygame.display.update()

    def move_up(self):
        for i in range(1, self.length):
            pygame.draw.circle(self.parent_screen, (160, 196, 50, 255),(self.x[i]+15, self.y[i]+50), self.body_radius, self.body_width)
        self.y[0] -= self.snake_vel

        self.parent_screen.blit(self.SNAKE_UP, (self.x[0], self.y[0]))

    def move_down(self):
        for i in range(1, self.length):
            pygame.draw.circle(self.parent_screen, ((160, 196, 50, 255)),(self.x[i]+15, self.y[i]+0), self.body_radius, self.body_width)
        self.y[0] += self.snake_vel

        self.parent_screen.blit(self.SNAKE, (self.x[0], self.y[0]))

    def move_left(self):
        for i in range(1, self.length):
            pygame.draw.circle(self.parent_screen, (160, 196, 50, 255),(self.x[i]+50, self.y[i]+15), self.body_radius, self.body_width)
        self.x[0] -= self.snake_vel

        self.parent_screen.blit(self.SNAKE_LEFT, (self.x[0], self.y[0]))

    def move_right(self):
        for i in range(1, self.length):
            pygame.draw.circle(self.parent_screen, (160, 196, 50, 255),(self.x[i]-0, self.y[i]+15), self.body_radius, self.body_width)

        self.x[0] += self.snake_vel

        self.parent_screen.blit(self.SNAKE_RIGHT, (self.x[0], self.y[0]))

    def warp_snake(self):
        if self.x[0] > WIDTH:
            self.x[0] = 0
        elif self.x[0] < -30:
            self.x[0] = WIDTH

        if self.y[0] > HEIGHT:
            self.y[0] = 0
        elif self.y[0] < -30:
            self.y[0] = HEIGHT

    def speed_checker(self, score):
        if score >= 10 and score < 20:
            self.snake_vel +=1

        if score > 20:
            self.snake_vel +=2

        if score > 50:
            self.snake_vel +=3


class Game:
    def __init__(self):
        self.BG = pygame.transform.scale(pygame.image.load("assets/background-black.png"), (WIDTH, HEIGHT))
        self.APPLE = pygame.transform.scale(pygame.image.load("assets/apple.png"), (30, 30))
        self.clock = pygame.time.Clock()
        self.FPS = 120
        self.score = 0
        self.main_font = pygame.font.SysFont("comicsans", 20)
        self.score_label = self.main_font.render(f"Score:{self.score}", 1, (255, 255, 255))
        self.gldn_apple = pygame.image.load("assets/bob.png")
        self.gldn_apple_x = WIDTH +100
        self.gldn_apple_y = HEIGHT+100
        self.gldn_pnt = 0
        self.snake = Snake(WIN)
        self.apple_x = random.randint(0, 550)
        self.apple_y = random.randint(20, 550)
        self.start_time = time.time()
        self.future_time = None
        self.visible = False

    def draw_apple(self):
        WIN.blit(self.APPLE, (self.apple_x, self.apple_y))
        pygame.display.update()

    def increase_score(self):
        self.gldn_pnt += 1
        self.score += 1

    def random_apple_pos(self):
        self.apple_x = random.randint(0, WIDTH-50)
        self.apple_y = random.randint(20, HEIGHT-50)

    def random_golden_apple_pos(self):
        self.gldn_apple_x = random.randint(0, WIDTH-60)
        self.gldn_apple_y = random.randint(20, HEIGHT-60)
        self.gldn_pnt = 0
        self.visible = True

    def time_checker(self):
        now_time = datetime.datetime.now()
        self.future_time = now_time+datetime.timedelta(seconds=5)

    def golden_apple_collision(self):
        if abs(self.snake.x[0] - self.gldn_apple_x) <= 56 and abs(self.snake.y[0] - self.gldn_apple_y) <= 60:
            self.snake.increase_length_giant_apple()
            self.score += 10
            self.gldn_apple_x = WIDTH+100
            self.gldn_apple_y = HEIGHT+100

    def game_over(self,timed):
        WIN.blit(self.BG, (0, 0))
        game_over_msg = self.main_font.render(f"Game over Your Score Was:{self.score}", 1, (255, 255, 255))
        WIN.blit(game_over_msg, (300,300))
        line= self.main_font.render(f"To play agian press enter ", 1, (255, 255, 255))
        WIN.blit(line, (300,360))
        end_time = time.time()
        Timer = end_time-timed
        if Timer > 60:
            survived= self.main_font.render(f'YOU LASTED FOR {int(Timer//60)} Minute(s) {int(Timer % 60)} SECONDS', 1, (255, 255, 255))
        else:
            survived = self.main_font.render(f'YOU LASTED FOR {int(Timer)} SECONDS', 1, (255, 255, 255))
        WIN.blit(survived,(300,330))
        pygame.display.update()

    def reset(self):
        self.score=0
        self.snake.length=(self.snake.length + 1)-self.snake.length
        self.snake.x = [250]
        self.snake.y = [400]
        self.snake.direction = ""
        self.gldn_apple_x = WIDTH+100
        self.gldn_apple_y = HEIGHT+100
        self.gldn_pnt = 0
        self.snake.snake_vel = 4

    def redraw(self):

        WIN.blit(self.BG, (0, 0))

        WIN.blit(self.gldn_apple, (self.gldn_apple_x, self.gldn_apple_y))

        WIN.blit(self.APPLE, (self.apple_x, self.apple_y))

        WIN.blit(self.score_label, (10, 10))

        self.score_label = self.main_font.render(
            f"Score:{self.score}", 1, (255, 255, 255))
        self.snake.move()
        pygame.display.update()

    def run(self):
        self.running = True
        stop=False
        while self.running:
            try:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key== pygame.K_RETURN:
                            stop= False

                if stop == False:
                                       
                    self.redraw()
                    self.clock.tick(self.FPS)
                    self.snake.collision()
                    self.snake.warp_snake()
            
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_DOWN:
                            self.snake.direction_change('down')
                        elif event.key == pygame.K_UP:
                            self.snake.direction_change('up')
                        elif event.key == pygame.K_LEFT:
                            self.snake.direction_change('left')
                        elif event.key == pygame.K_RIGHT:
                            self.snake.direction_change('right')
                    self.snake.speed_checker(self.score)

                    if abs(self.snake.x[0] - self.apple_x) <= 25 and abs(self.snake.y[0] - self.apple_y) <= 25:
                        self.increase_score()
                        self.snake.increase_length()
                        self.random_apple_pos()

                        if self.gldn_pnt == 20:
                            self.random_golden_apple_pos()
                            self.time_checker()

                    if self.visible == True:
                        if datetime.datetime.now() > self.future_time:
                            self.gldn_apple_x = WIDTH +100
                            self.gldn_apple_y = HEIGHT+100
                            self.visible = False

                    self.golden_apple_collision()
            except Exception as e:
                self.game_over(self.start_time)
                stop=True
                self.reset()
                self.start_time=time.time()


game = Game()
game.run()
