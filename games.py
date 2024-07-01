import pygame
import random

# Инициализация Pygame
pygame.init()

# Константы
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 20

# Настройка экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Змейка")

clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]
        self.direction = (20, 0)

    def move(self):
        head = self.body[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        self.body = [new_head] + self.body[:-1]

    def grow(self):
        self.body.append(self.body[-1])

    def change_direction(self, direction):
        self.direction = direction

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

    def check_collision(self):
        head = self.body[0]
        return (head in self.body[1:] or
                head[0] < 0 or head[0] >= SCREEN_WIDTH or
                head[1] < 0 or head[1] >= SCREEN_HEIGHT)

class Food:
    def __init__(self):
        self.respawn()

    def draw(self):
        pygame.draw.rect(screen, RED, (self.position[0], self.position[1], CELL_SIZE, CELL_SIZE))

    def respawn(self):
        self.position = (random.randint(0, (SCREEN_WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
                         random.randint(0, (SCREEN_HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)

# Основная функция игры
def game():
    snake = Snake()
    food = Food()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Получаем положение мыши
        mouse_x, mouse_y = pygame.mouse.get_pos()
        head = snake.body[0]

        # Определяем направление движения в зависимости от положения мыши
        if abs(mouse_x - head[0]) > abs(mouse_y - head[1]):
            if mouse_x > head[0] and snake.direction != (-CELL_SIZE, 0):
                snake.change_direction((CELL_SIZE, 0))
            elif mouse_x < head[0] and snake.direction != (CELL_SIZE, 0):
                snake.change_direction((-CELL_SIZE, 0))
        else:
            if mouse_y > head[1] and snake.direction != (0, -CELL_SIZE):
                snake.change_direction((0, CELL_SIZE))
            elif mouse_y < head[1] and snake.direction != (0, CELL_SIZE):
                snake.change_direction((0, -CELL_SIZE))

        snake.move()

        if snake.body[0] == food.position:
            snake.grow()
            food.respawn()

        screen.fill(BLACK)
        snake.draw()
        food.draw()
        pygame.display.flip()

        if snake.check_collision():
            running = False

        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    game()