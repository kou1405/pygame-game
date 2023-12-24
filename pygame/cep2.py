import pygame
import sys
import random
pygame.init()
screen = pygame.display.set_mode((640,480), pygame.RESIZABLE)
pygame.display.set_caption(" Snake (lytsoft)")
UPDATE_SNAKE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(UPDATE_SNAKE_EVENT, 500)
def game_over():
    font = pygame.font.Font(None, 36)
    text = font.render("Game Over. Press R to restart.", True, (255, 255, 255))
    text_width, text_height = text.get_size()
    text_x = (screen.get_width() - text_width) / 2
    text_y = (screen.get_height() - text_height) / 2
    screen.blit(text, (text_x, text_y))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    snake = [(300,300),(320,300)]
                    x = random.randint(radius, screen.get_width()-radius) // segment_size * segment_size
                    y = random.randint(radius, screen.get_height()-radius) // segment_size * segment_size
                    apple = (x,y)
                    direction = (segment_size,0)
                    return



segment_size = 20
snake = [(300,300),(320,300)]
radius = segment_size - 10
x = random.randint(radius, screen.get_width()-radius) // segment_size * segment_size
y = random.randint(radius, screen.get_height()-radius) // segment_size * segment_size
apple = (x,y)
direction = (segment_size,0)
score = 0





while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != (segment_size, 0):
                direction = (-segment_size, 0)
            elif event.key == pygame.K_RIGHT and direction != (-segment_size, 0):
                direction = (segment_size, 0)
            elif event.key == pygame.K_UP and direction != (0, segment_size):
                direction = (0, -segment_size)
            elif event.key == pygame.K_DOWN and direction != (0, -segment_size):
                direction = (0, segment_size)
        elif event.type == UPDATE_SNAKE_EVENT:
            # update snake position
            for i in range(len(snake)-1, 0, -1):
                snake[i] = (snake[i-1][0], snake[i-1][1])
            snake[0] = (snake[0][0] + direction[0], snake[0][1] + direction[1])
           
            threshold = segment_size * 1.5

            dx = (snake[0][0] + segment_size/2) - (apple[0] + segment_size/2)
           
            dy = (snake[0][1] + segment_size/2) - (apple[1] + segment_size/2)
            distance = (dx*dx + dy*dy)**0.5
            if snake[0] == apple or distance < threshold:
                score += 1
               
           
                snake.append((snake[-1][0], snake[-1][1]))
               
               
                x = random.randint(radius, screen.get_width()-radius) // segment_size * segment_size
                y = random.randint(radius, screen.get_height()-radius) // segment_size * segment_size
                apple = (x,y)
               
       
                speed = 500 - (score * 10)
                speed = max(speed, 100)
                pygame.time.set_timer(UPDATE_SNAKE_EVENT, speed+10)
   
    if snake[0][0] < 0 or snake[0][0] >= screen.get_width() or snake[0][1] < 0 or snake[0][1] >= screen.get_height():
        game_over()
  
    for segment in snake[1:]:
        if snake[0] == segment:
            game_over()
    screen.fill((0,0,0))
    font = pygame.font.Font(None,36)
    score_txt = f"score : {score}"
    txt = font.render(score_txt,True,(255,255,255))
    screen.blit(txt,(10,10))

    for x , y in snake :
        pygame.draw.rect(screen,(255,255,255),(x,y,segment_size,segment_size))

    pygame.draw.circle(screen, (255, 0, 0), apple, radius)
   
    pygame.display.update()   
    pygame.time.delay(100)#//score