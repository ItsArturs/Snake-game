import pygame
import random

pygame.init()

clock = pygame.time.Clock()
font = pygame.font.Font(None, 60)

WIDTH = 600
HEIGHT = 600
CELL_SIZE = 20

snake_x = 300
snake_y = 300
snake_body = [(snake_x, snake_y)]

direction_x = 0
direction_y = 0

last_direction_x = 0
last_direction_y = 0

score = 0

def create_food():
    while True:
        x = random.randrange(0, WIDTH, CELL_SIZE)
        y = random.randrange(0, HEIGHT, CELL_SIZE)

        if (x, y) not in snake_body:
            return x, y
food_x, food_y = create_food()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

running = True
game_over = False


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                if last_direction_y != 1:  # Nedos čūskai atpakaļ iet
                     direction_x = 0
                     direction_y = -1

            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if last_direction_y != -1:
                    direction_x = 0
                    direction_y = 1

            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if last_direction_x != 1:
                    direction_x = -1
                    direction_y = 0

            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if last_direction_x != -1:
                    direction_x = 1
                    direction_y = 0

            if event.key == pygame.K_r and game_over:
                snake_x = 300
                snake_y = 300
                snake_body = [(snake_x, snake_y)]
                direction_x = 0
                direction_y = 0
                last_direction_x = 0
                last_direction_y = 0
                score = 0
                food_x, food_y = create_food()
                game_over = False


    screen.fill((0, 0, 0))


    # Vertikālās līnijas
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, HEIGHT))
    # Horizontālās līnijas
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, (40, 40, 40), (0, y), (WIDTH, y))

    if not game_over:
        snake_x += direction_x * CELL_SIZE
        snake_y += direction_y * CELL_SIZE

        last_direction_x = direction_x
        last_direction_y = direction_y

    if snake_x < 0 or snake_x >= WIDTH or snake_y < 0 or snake_y >= HEIGHT:
        game_over = True

    if (snake_x, snake_y) in snake_body[1:]:
        game_over = True

    snake_body.append((snake_x, snake_y))

    if snake_x == food_x and snake_y == food_y:
        score += 1
        food_x, food_y = create_food()
    else:
        snake_body.pop(0)

    for part in snake_body:
        pygame.draw.rect(screen, (0, 255, 0), (part[0], part[1], CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, (255, 0, 0), (food_x, food_y, CELL_SIZE, CELL_SIZE))

    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))


    if game_over:
        game_over_text = font.render("Game over!", True, (255, 255, 255))
        screen.blit(game_over_text,(180, 270))
        restart_text = font.render("Press R to restart", True, (255, 255, 255))
        screen.blit(restart_text, restart_text.get_rect(center=(WIDTH // 2, 340)))

    pygame.display.update()

    clock.tick(10)

pygame.quit()