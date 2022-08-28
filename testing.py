import pygame
import time
import os
import random
pygame.font.init()
WIDTH, HEIGHT = 600,600
WIN =pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("SNAKE GAME")

SNAKE =  pygame.transform.rotate(pygame.transform.scale(pygame.image.load("assets/snake.png"), (30,50)), 0)
SNAKE_RIGHT =  pygame.transform.rotate(pygame.transform.scale(pygame.image.load("assets/snake.png"), (30,50)), 90)
SNAKE_UP =  pygame.transform.rotate(pygame.transform.scale(pygame.image.load("assets/snake.png"), (30,50)), 180)
SNAKE_LEFT=  pygame.transform.rotate(pygame.transform.scale(pygame.image.load("assets/snake.png"), (30,50)), 270)
APPLE = pygame.transform.scale(pygame.image.load("assets/apple.png"), (30,30))
BODY = pygame.transform.scale(pygame.image.load("assets/blue square.png"), (20,20)) 
BG = pygame.transform.scale(pygame.image.load("assets/background-black.png"),(WIDTH,HEIGHT))


def main():
    score=0
    run=True
    FPS=60
    clock= pygame.time.Clock()
    snake_x = 250
    snake_y = 400
    apple_x = random.randint(0,550)
    apple_y = random.randint(0,550)
    direction = ""
    main_font = pygame.font.SysFont("comicsans",20)
    def redraw():
       WIN.blit(BG,(0,0))
       WIN.blit(APPLE, (apple_x,apple_y))
       
       Score_label=main_font.render(f"Score:{score}",1,(255,255,255))
      
       
       WIN.blit(Score_label,(10,10))
       
       if direction == 'up':
        WIN.blit(SNAKE_UP, (snake_x,snake_y))
        previous_pos=snake_x+4,snake_y+40
        
       elif direction == "left":
        WIN.blit(SNAKE_LEFT, (snake_x,snake_y)) 
        previous_pos=snake_x+40,snake_y+4
        
       elif direction == "right":
         WIN.blit(SNAKE_RIGHT, (snake_x,snake_y))
         previous_pos=snake_x-10,snake_y+4
         
       elif direction == "down":
         WIN.blit(SNAKE, (snake_x,snake_y))
         previous_pos=snake_x+4,snake_y-10
           

      
       

       pygame.display.update()
        
    while run:
        clock.tick(FPS)
        redraw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    direction = "down"
                elif event.key == pygame.K_UP:
                    direction = "up"
                elif event.key == pygame.K_LEFT:
                    direction = "left" 
                elif event.key == pygame.K_RIGHT:
                    direction = "right" 

        
        
        if direction == "up":
            snake_y-=1.5
        elif direction == "down":
           snake_y+=1.5
        elif direction == "left":
           snake_x-=1.5
        elif direction =="right":
            snake_x+=1.5
                
        if snake_x > WIDTH:
            snake_x=-20
        elif snake_x < -30:
            snake_x= WIDTH
        if snake_y > HEIGHT:
            snake_y=-20
        elif snake_y < -30:
            snake_y= HEIGHT

        

        if score >= 10 and score<20:
            
            if direction == "up":
                snake_y-=0.5
            elif direction == "down":
                snake_y+=0.5
            elif direction == "left":
                snake_x-=0.5
            elif direction =="right":
                snake_x+=0.5
        if score >= 20:
            
            if direction == "up":
                snake_y-=1
            elif direction == "down":
                snake_y+=1
            elif direction == "left":
                snake_x-=1
            elif direction =="right":
                snake_x+=1
        
        if abs(snake_x-apple_x)<=25 and abs(snake_y-apple_y)<=25:
           
           score+=1
           apple_x = random.randint(0,550)
           apple_y = random.randint(0,550)
           
        
 
main()
