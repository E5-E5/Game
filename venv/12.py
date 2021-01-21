import pygame
import os


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = pygame.Color('black')
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


class Boss(pygame.sprite.Sprite):
    image = load_image(f"C:/Users/USER/Desktop/piton/RABOTI/Игра/boss.png", -1)

    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.image = Boss.image
        self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        # располагаем горы внизу
        self.rect.x = x
        self.rect.y = y

    def update(self):
        if pygame.sprite.collide_mask(self, landing):
            pygame.mouse.set_pos(450, 500)


class Landing(pygame.sprite.Sprite):
    image = load_image("C:/Users/USER/Desktop/piton/RABOTI/pt.png", -1)

    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.image = Landing.image
        self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y



size = width, height = 501, 501
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption('Шарики')
all_sprites = pygame.sprite.Group()
running = True

# параметры круга
radius = 20
color = pygame.Color('red')
# Список для координат кругов
# Список для смещений координат кругов
# Создаем второй холст
screen2 = pygame.Surface(screen.get_size())
landing = Landing(0, 0)
boss = Boss(500, 500)
x1, y1 = 0, 0
# Запускаем окно
while running:
    for event in pygame.event.get():
        screen2 = pygame.Surface(screen.get_size())
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            x1, y1 = event.pos
            landing.rect.x = x1 + 5
            landing.rect.y = y1 + 5

    if x1 > boss.rect.x:
        boss.rect[0] += 2
    else:
        boss.rect[0] -= 2
    if y1 > boss.rect.y:
        boss.rect[1] += 2
    else:
        boss.rect[1] -= 2

    clock.tick(50)
    screen.fill(pygame.Color("black"))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
pygame.quit()