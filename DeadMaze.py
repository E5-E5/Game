import os
import pygame
from moviepy.editor import *
import random

pygame.display.set_mode((750, 750))
next = False
count = 1
s = 1
rectcount = 0
color = "dark green"
color2 = "red"
a = 0
colorflag = 0
start_x = {1: 216, 2: 250, 3: 530, 4: 250, 5: 187, 6: 250, 7: 555, 8: 250, 9: 265, 10: 250, 11: 350,
           12: 250, 13: 160, 14: 250, 15: 40, 16: 250, 17: 400, 18: 250, 19: 600, 20: 250, 21: 100,
           22: 250, 23: 400, 24: 250, 25: 250, 26: 250, 27: 30, 28: 250}
start_y = {1: 645, 2: 250, 3: 710, 4: 250, 5: 710, 6: 250, 7: 684, 8: 250, 9: 679, 10: 250, 11:
           680, 12: 250, 13: 700, 14: 250, 15: 700, 16: 250, 17: 700, 18: 250, 19: 600, 20: 250, 21: 700,
           22: 250, 23: 700, 24: 250, 25: 250, 26: 250, 27: 380, 28: 250}


def terminate():
    pygame.quit()
    sys.exit()


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


class Finish(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__(all_sprites)
        self.image = load_image(f"data/Finish{s}.png", -1)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = 750
        self.button = 0
        self.good = 0
        self.bad = 0

    def update(self):
        self.image = load_image(f"data/Finish{s}.png", -1)
        self.mask = pygame.mask.from_surface(self.image)
        if s % 2 == 0 and s < 26:
            if s < 11:
                COLOR = "dark grey"
            else:
                COLOR = "white"
            QUESTION_1 = Button()
            QUESTION_1.create_button(screen, COLOR, 40, 240, 50, 50, 100,
                                     '', 'black')
            if event.type == pygame.MOUSEBUTTONUP:
                if QUESTION_1.pressed(event.pos):
                    self.button = 1

            QUESTION_2 = Button()
            QUESTION_2.create_button(screen, COLOR, 40, 340, 50, 50, 100,
                                     '0', 'black')
            if event.type == pygame.MOUSEBUTTONUP:
                # return  # начинаем игру
                if QUESTION_2.pressed(event.pos):
                    self.button = 2

            QUESTION_3 = Button()
            QUESTION_3.create_button(screen, COLOR, 40, 440, 50, 50, 100,
                                     '0', 'black')
            if event.type == pygame.MOUSEBUTTONUP:
                # return  # начинаем игру
                if QUESTION_3.pressed(event.pos):
                    self.button = 3

            QUESTION_4 = Button()
            QUESTION_4.create_button(screen, COLOR, 40, 540, 50, 50, 100, '0',
                                     'black')
            if event.type == pygame.MOUSEBUTTONUP:
                # return  # начинаем игру
                if QUESTION_4.pressed(event.pos):
                    self.button = 4

            if self.button == 1:
                QUESTION_3.create_button(screen, "dark green", 40, 240, 50, 50, 100,
                                       '0', 'black')
            else:
                QUESTION_3.create_button(screen, COLOR, 40, 240, 50, 50, 100,
                                       '0', 'black')

            if self.button == 2:
                QUESTION_3.create_button(screen, "dark green", 40, 340, 50, 50, 100,
                                       '0', 'black')
            else:
                QUESTION_3.create_button(screen, COLOR, 40, 340, 50, 50, 100,
                                       '0', 'black')

            if self.button == 3:
                QUESTION_3.create_button(screen, "dark green", 40, 440, 50, 50, 100,
                                       '0', 'black')
            else:
                QUESTION_3.create_button(screen, COLOR, 40, 440, 50, 50, 100,
                                       '0', 'black')

            if self.button == 4:
                QUESTION_3.create_button(screen, "dark green", 40, 540, 50, 50, 100,
                                       '0', 'black')
            else:
                QUESTION_3.create_button(screen, COLOR, 40, 540, 50, 50, 100,
                                       '0', 'black')
            if self.button == 1 or self.button == 3:
                self.good += 1
            else:
                self.bad += 1


class Maze(pygame.sprite.Sprite):
    print(s)
    image = load_image(f"data/Level{s}.png", -1)

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Maze.image
        self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        # располагаем горы внизу
        self.rect.bottom = 750

    def update(self):
        self.image = load_image(f"data/Level{s}.png", -1)
        self.mask = pygame.mask.from_surface(self.image)


class Trigger(pygame.sprite.Sprite):
    if s == 13:
        image = load_image(f"data/trigger13.png", -1)
    elif s == 23:
        image = load_image(f"data/trigger23.png", -1)
    else:
        image = load_image(f"data/Finish28.png", -1)

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Trigger.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = 750

    def update(self):
        if s == 13:
            self.image = load_image(f"data/Trigger13.png", -1)
            self.mask = pygame.mask.from_surface(self.image)
        elif s == 23:
            self.image = load_image(f"data/Trigger23.png", -1)
            self.mask = pygame.mask.from_surface(self.image)
        else:
            self.image = load_image(f"data/Finish28.png", -1)
            self.mask = pygame.mask.from_surface(self.image)


screen_rect = (0, 0, 750, 750)


class Particle(pygame.sprite.Sprite):
    fire = [load_image("data/flowerpart.png")]
    for scale in (5, 10, 20):
        fire.append(pygame.transform.scale(fire[0], (scale, scale)))

    def __init__(self, pos, dx, dy):
        super().__init__(all_sprites)
        self.image = random.choice(self.fire)
        self.rect = self.image.get_rect()

        # у каждой частицы своя скорость — это вектор
        self.velocity = [dx, dy]
        # и свои координаты
        self.rect.x, self.rect.y = pos

        # гравитация будет одинаковой (значение константы)
        self.gravity = 1
        self.checkpart = 0

    def update(self):
        # применяем гравитационный эффект:
        # движение с ускорением под действием гравитации
        self.velocity[1] += self.gravity
        # перемещаем частицу
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        self.checkpart += self.gravity
        # убиваем, если частица ушла за экран
        if self.checkpart > 10:
            self.kill()


def create_particles(position):
    # количество создаваемых частиц
    particle_count = 10
    # возможные скорости
    numbers = range(-5, 3)
    for _ in range(particle_count):
        Particle(position, random.choice(numbers), random.choice(numbers))


class Button:
    def create_button(self, surface, color, x, y, length, height, width, text,
                      text_color):
        surface = self.draw_button(surface, color, length, height, x, y, width)
        surface = self.write_text(surface, text, text_color, length, height, x,
                                  y)
        self.rect = pygame.Rect(x, y, length, height)
        return surface

    def write_text(self, surface, text, text_color, length, height, x, y):

        myFont = pygame.font.SysFont("Calibri", 30)
        myText = myFont.render(text, 1, text_color)
        surface.blit(myText, ((x + length / 2) - myText.get_width() / 2,
                              (y + height / 2) - myText.get_height() / 2))
        return surface

    def draw_button(self, surface, color, length, height, x, y, width):
        for i in range(1, 10):
            s = pygame.Surface((length + (i * 2), height + (i * 2)))
            s.fill(color)
            alpha = (255 / (i + 2))
            if alpha <= 0:
                alpha = 1
            s.set_alpha(alpha)
            pygame.draw.rect(s, color, (x - i, y - i, length + i, height + i),
                             width)
            surface.blit(s, (x - i, y - i))
        pygame.draw.rect(surface, color, (x, y, length, height), 0)
        pygame.draw.rect(surface, (190, 190, 190), (x, y, length, height), 1)
        return surface

    def pressed(self, mouse):
        if mouse[0] > self.rect.topleft[0]:
            if mouse[1] > self.rect.topleft[1]:
                if mouse[0] < self.rect.bottomright[0]:
                    if mouse[1] < self.rect.bottomright[1]:
                        print("Some button was pressed!")
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False


class Boss(pygame.sprite.Sprite):
    image = load_image("data/boss.png", -1)

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Boss.image
        self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        # располагаем горы внизу
        self.rect.x = start_x[s]
        self.rect.y = start_y[s] + 70
        self.boss_killing = 0

    def update(self):
        if pygame.sprite.collide_mask(self, land):
            global rectcount
            pygame.mouse.set_pos(start_x[s], start_y[s])
            self.boss_killing += 1
            mountain.rect[1] = 0
            rectcount = 0
            self.rect.x = start_x[s]
            self.rect.y = start_y[s] + 70


class Cursor(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.image = load_image("data/arrow.png", -1)
        self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y


    def update(self):
        global s
        global rectcount
        if s > 9:
            self.image = load_image("data/cursor2.png", -1)
            self.mask = pygame.mask.from_surface(self.image)
        badcollide = pygame.mixer.Sound(
            r'data/badcollide.wav')
        goodcollide = pygame.mixer.Sound(
            r'data/goodcollide.wav')
        if (s % 2 != 0 or s == 28) and pygame.sprite.collide_mask(self, mountain):
            pygame.mouse.set_pos(start_x.get(s), start_y.get(s))
            create_particles(pygame.mouse.get_pos())
            if s < 10:
                goodcollide.play()
            else:
                badcollide.play()
            mountain.rect[1] = 0

            rectcount = 0
        if s % 2 != 0 and pygame.sprite.collide_mask(self, finish):
            global next
            next = True
        elif s % 2 == 0 and finish.button != 0 and pygame.sprite.collide_mask(self, finish)\
                and event.type == pygame.MOUSEBUTTONDOWN:
            next = True
        elif s > 25 and s % 2 == 0 and pygame.sprite.collide_mask(self, finish)\
                and event.type == pygame.MOUSEBUTTONDOWN:
            next = True
        if s == 13 and pygame.sprite.collide_mask(self, trigger):
            s = 1
            goodcollide.play()
        if s == 23 and pygame.sprite.collide_mask(self, trigger):
            s = 19
            goodcollide.play()



pygame.init()

all_sprites = pygame.sprite.Group()
my_group = pygame.sprite.Group()

mountain = Maze()
finish = Finish()
trigger = Trigger()
land = Cursor(750, 750)
boss = None
x1, y1 = 0, 0
clock = pygame.time.Clock()
size = width, height = 750, 750

screen = pygame.display.set_mode(size)
running = True
boss_flag = True
trigger_flag = True
music = True
sunnybackground = None
boss_killing = 0
pygame.mouse.set_pos(450, 500)
game = 3


def start_screen():
    global game
    fon = pygame.transform.scale(load_image('data/Level0.jpg'),
                                 (width, height))
    screen.blit(fon, (0, 0))

    button_1 = Button()
    button_1.create_button(screen, 'dark grey', 40, 40, 200, 50, 100,
                           'Новая игра', 'black')

    button_2 = Button()
    button_2.create_button(screen, 'dark grey', 40, 140, 200, 50, 100,
                           'Продолжить', 'black')

    button_3 = Button()
    button_3.create_button(screen, 'dark grey', 40, 240, 200, 50, 100,
                           'Правила', 'black')

    button_4 = Button()
    button_4.create_button(screen, 'dark grey', 40, 340, 200, 50, 100, 'Выход',
                           'black')


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                # return  # начинаем игру
                if button_1.pressed(event.pos):
                    game = 1
                elif button_2.pressed(event.pos):
                    game = 2
                elif button_3.pressed(event.pos):
                    game = 3
                    options()
                elif button_4.pressed(event.pos):
                    terminate()
                return

        pygame.display.flip()
        clock.tick(50)


def options():
    intro_text = ["ПРАВИЛА", "",
                  "правила очень простые",
                  "проходите лабиринты, но не касайтесь стенок",
                  "при столкновении курсор будет возвращаться ",
                  "в начало уровня",
                  "удачи вам, и приятной игры"]
    global game
    fon = pygame.transform.scale(load_image('data/Level0.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    button_1 = Button()
    button_1.create_button(screen, 'dark gray', 320, 400, 100, 50, 200, 'Назад',
                           'black')
    for line in intro_text:
        string_rendered = font.render(line, True, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                # return  # начинаем игру
                if button_1.pressed(event.pos):
                    return

        pygame.display.flip()
        clock.tick(50)


def result():
    ending = ''
    if boss_killing > 5:
        if finish.good > finish.bad:
            intro_text = ["     К сожалению, вы не смогли убежать от своего врага,",
                          "      но либо вы ему понравились, либо у него хорошее настроение,",
                          "      поэтому он решил оставить вас в живых,",
                          "      но вы до конца своих дней останетесь в этом лабиринте,",
                          "      помогая теперь уже своему новому другу"]
            ending = 'Босс оставил вас в живых'
        else:
            intro_text = ["     Вы не смогли убежать от своего врага...",
                          "     В этот раз вы проиграли ваму заклятому врагу",
                          "      умерев в несовсем честной битве"]
            ending = 'Босс догнал вас'
    else:
        if finish.good > finish.bad:
            intro_text = ["     Поздравляю!!!",
                          "     Вы смогли убежать от никчёмного шара.",
                          "     Добежав до выхода перед вами открылась дверь в новый мир,",
                          "      но это уже другая история..."]
            ending = 'Вы спаслись'
        else:
            intro_text = ["     Несмотря на то что вы смогли добраться до выхода,",
                          "      дверь оказалась какой-то странной.",
                          "     Прыгнув в нее, вы начали лететь в какую-то пустоту,",
                          "      окружённую стенками лабиринта.",
                          "     Вы всё летите и летите, а конца не видно...",
                          "     Возможно, вы могли что-то именить?..."]
            ending = 'Где я? Куда я попал?'

    global game
    fon = pygame.transform.scale(load_image('data/result.png'),
                                 (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    button_1 = Button()
    button_1.create_button(screen, 'dark green', 40, 340, 100, 50, 200, 'Далее',
                           'white')
    for line in intro_text:
        string_rendered = font.render(line, True, pygame.Color('dark green'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        flag = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_1.pressed(event.pos):
                    flag = True
        if flag:
            try:
                f = open('data/result.txt', 'r+',
                         encoding='utf-8')
                temp = f.readlines()[-1]
                if temp:
                    temp = f'\n{int(temp.split()[0]) + 1} {ending}'
            except Exception:
                print(3)
                f = open('data/result.txt', 'w',
                         encoding='utf-8')
                temp = f'{1} {ending}'
            f.write(temp)
            f.close()
            terminate()

        pygame.display.flip()
        clock.tick(50)

while game == 3:
    start_screen()

if game == 1:
    s = 1
    f = open('autosave.txt', 'w')
    f.write(str(s))
    f.close()
    pygame.mouse.set_pos(168, 695)
if game == 2:
    try:
        f = open('autosave.txt', 'r')
        for i in f:
            s = int(i)
        if s % 2 == 0:
            s -= 1
        f.close()
    except Exception:
        s = 1

if game == 1 or game == 2:
    pygame.mouse.set_visible(False)
    sunnybackground = pygame.mixer.Sound(
        r'data/sunnybackground.mp3')
    sunnybackground.play(-1)
    while running:
        if next:
            if s > 8 and music:
                music = False
                sunnybackground.stop()
                backgroundwind = pygame.mixer.Sound(
                    r'data/backgroundwind.wav')
                backgroundwind.play(-1)
            pygame.mouse.set_pos(start_x.get(s), start_y.get(s))
            s = s + 1
            if boss_flag == False:
                boss_killing = boss.boss_killing
                boss.kill()
                boss_flag = True
            f = open('data/autosave.txt', 'w')
            f.write(str(s))
            f.close()
            mountain.update()
            finish.update()
            finish.button = 0
            next = False
            pygame.mouse.set_pos(start_x.get(s), start_y.get(s))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                x1, y1 = event.pos
                land.rect.x = x1
                land.rect.y = y1
                print(x1, y1)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_4:
                    s += 1
                    if boss_flag == False:
                        boss.kill()
                        boss_flag = True
                if event.key == pygame.K_SPACE:
                    s = 1
        if s == 28:
            mountain.rect[1] -= 4
            rectcount += 4
            print(rectcount)
            if rectcount > 4000:
                result()
        if s == 19 or s == 21 or s == 28:
            if boss_flag:
                boss = Boss()
                boss_flag = False
            if x1 - 10 > boss.rect.x:
                boss.rect[0] += 2
            else:
                boss.rect[0] -= 2
            if y1 - 10 > boss.rect.y:
                boss.rect[1] += 2
            else:
                boss.rect[1] -= 2
        if s < 10:
            screen.fill(pygame.Color("yellow"))
        else:
            screen.fill(pygame.Color("black"))
        all_sprites.draw(screen)
        all_sprites.update()
        my_group.draw(screen)
        my_group.update()
        pygame.display.flip()
        clock.tick(100)

terminate()
