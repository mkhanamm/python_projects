import pygame
import sys
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 700, 700
BLOCK_SIZE = 25
FPS = 7

WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

# Load images
background_img = pygame.transform.scale(
    pygame.image.load("background.jpg"), (WIDTH, HEIGHT)
)

snake_head_img = pygame.transform.scale(
    pygame.image.load("snake_head.png"), (BLOCK_SIZE, BLOCK_SIZE)
)

food_img = pygame.transform.scale(
    pygame.image.load("apple.jpg"), (BLOCK_SIZE, BLOCK_SIZE)
)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Font
font = pygame.font.SysFont("consolas", 35)


def draw_text(text, size, color, y_offset=0):
    font = pygame.font.SysFont("consolas", size)
    text_surface = font.render(text, True, color)
    rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + y_offset))
    screen.blit(text_surface, rect)


def draw_snake(snake_body):
    for i, part in enumerate(snake_body):
        if i == 0:
            screen.blit(snake_head_img, part)
        else:
            pygame.draw.rect(screen, RED, (*part, BLOCK_SIZE, BLOCK_SIZE))


def show_intro():
    while True:
        screen.fill(BLACK)
        draw_text("Welcome to Snake Game", 45, WHITE, -50)
        draw_text("Press SPACE to Begin", 30, RED, 30)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return


def show_game_over(score):
    while True:
        screen.fill(BLACK)
        draw_text("Game Over!", 60, RED, -50)
        draw_text(f"Score: {score}", 40, WHITE, 20)
        draw_text("Press R to Restart or Q to Quit", 30, WHITE, 80)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_r:
                    main()


def main():
    clock = pygame.time.Clock()

    snake = [[100, 50], [75, 50], [50, 50]]
    direction = "RIGHT"
    score = 0

    food = [
        random.randrange(0, WIDTH, BLOCK_SIZE),
        random.randrange(0, HEIGHT, BLOCK_SIZE),
    ]

    running = True

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"

        head_x, head_y = snake[0]

        if direction == "UP":
            head_y -= BLOCK_SIZE
        if direction == "DOWN":
            head_y += BLOCK_SIZE
        if direction == "LEFT":
            head_x -= BLOCK_SIZE
        if direction == "RIGHT":
            head_x += BLOCK_SIZE

        new_head = [head_x, head_y]
        snake.insert(0, new_head)

        if new_head == food:
            score += 1
            food = [
                random.randrange(0, WIDTH, BLOCK_SIZE),
                random.randrange(0, HEIGHT, BLOCK_SIZE),
            ]
        else:
            snake.pop()

        # Collision check
        if (
            head_x < 0
            or head_x >= WIDTH
            or head_y < 0
            or head_y >= HEIGHT
            or new_head in snake[1:]
        ):
            show_game_over(score)

        # Draw everything
        screen.blit(background_img, (0, 0))
        draw_snake(snake)
        screen.blit(food_img, food)

        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()


# Run game
show_intro()
main()
