import pygame
from time import sleep
from random import uniform as func  # Імпорт функції uniform

pygame.init()
WIDTH, HEIGHT = 600, 800
win = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("My Game")

clock = pygame.time.Clock()

# Колір
bound = 5
c2s = 30  # кадри на секунду
white = (255, 255, 255)
black = (0, 0, 0)

# Змінні для м'яча
x, y = WIDTH // 2, HEIGHT // 2
radius = 10
velocity = 8
vx = func(velocity - 3, velocity + 3)  # Випадкова швидкість для руху по осі X
vy = func(velocity - 3, velocity + 3)  # Випадкова швидкість для руху по осі Y

# Змінні для майданчика
height = 10
width = 100
xp = (WIDTH - width) // 2
yp = HEIGHT - height
vp = 10  # Швидкість переміщення майданчика

# Оголошення меж для відбиття м'яча
border_l = bound + radius
border_r = WIDTH - bound - radius
border_u = bound + radius

score = 0  # Лічильник очок

# Завантаження фону
background = pygame.image.load("image for game/back.jpg").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Функція для малювання вікна
def drawWindow():
    win.blit(background, (0, 0))  # Відображення фону
    pygame.draw.rect(win, white, (0, 0, WIDTH, bound))  # верх
    pygame.draw.rect(win, white, (0, 0, bound, HEIGHT))  # ліво
    pygame.draw.rect(win, white, (WIDTH - bound, 0, bound, HEIGHT))  # право
    pygame.draw.rect(win, white, (xp, yp, width, height))  # майданчик
    pygame.draw.circle(win, white, (int(x), int(y)), radius)  # м'яч
    pygame.display.update()

# Функція для виведення результату гри
def drawScore():
    win.fill(black)
    pygame.font.init()
    path = pygame.font.match_font("arial")
    Font = pygame.font.Font(path, 30)
    text = f'Your score: {score}'  # Виведення кількості очок
    a = Font.render(text, 1, (255, 255, 255))
    win.blit(a, (WIDTH // 2 - 70, HEIGHT // 3))
    pygame.display.update()

run = True
while run:
    clock.tick(c2s)

    # Обробка подій для закриття вікна та переміщення майданчика
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Перевірка на натискання клавіш для переміщення майданчика
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and xp > bound:
        xp -= vp
    if keys[pygame.K_RIGHT] and xp < WIDTH - bound - width:
        xp += vp

    # Оновлення положення м'яча
    x += vx
    y += vy

    # Перевірка відбиття м'яча від границь
    if x < border_l or x > border_r:
        vx = -vx
    if y < border_u:
        vy = -vy

    # Відбиття м'яча від майданчика
    if yp <= y + radius <= yp + height and xp <= x <= xp + width:
        vy = -abs(vy)  # Змінюємо напрямок руху вгору
        vx *= 1.5  # Прискорення швидкості по X
        vy *= 1.5  # Прискорення швидкості по Y
        score += 1  # Збільшуємо рахунок

    # Перевірка падіння м'яча за межі екрану
    if y > HEIGHT:  # Якщо м'яч виходить за межі екрану внизу
        drawScore()
        sleep(1)  # Затримка перед завершенням
        run = False

    # Малювання всіх елементів гри
    drawWindow()

pygame.quit()
