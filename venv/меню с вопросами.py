class Finish(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__(all_sprites)
        self.image = load_image(f"Finish{s}.png", -1)
        self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        # располагаем горы внизу
        self.rect.bottom = height
        self.button = 0

    def update(self):
        self.image = load_image(f"Finish{s}.png", -1)
        self.mask = pygame.mask.from_surface(self.image)
        if s % 2 == 0:
            COLOR = "dark green"
            QUESTION_1 = Button()
            QUESTION_1.create_button(screen, COLOR, 40, 240, 50, 50, 100,
                                     '0', 'black')
            
            if event.type == pygame.MOUSEBUTTONUP:
                # return  # начинаем игру
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
                QUESTION_3.draw_button(screen, "red", 40, 240, 50, 50, 100, '0', 'black')
            else:
                QUESTION_3.draw_button(screen, COLOR, 40, 240, 50, 50, 100, '0', 'black')

            if self.button == 2:
                QUESTION_3.draw_button(screen, "red", 40, 340, 50, 50, 100, '0', 'black')
            else:
                QUESTION_3.draw_button(screen, COLOR, 40, 340, 50, 50, 100, '0', 'black')

            if self.button == 3:
                QUESTION_3.draw_button(screen, "red", 40, 440, 50, 50, 100, '0', 'black')
            else:
                QUESTION_3.draw_button(screen, COLOR, 40, 440, 50, 50, 100, '0', 'black')

            if self.button == 4:
                QUESTION_3.draw_button(screen, "red", 40, 540, 50, 50, 100, '0', 'black')
            else:
                QUESTION_3.draw_button(screen, COLOR, 40, 540, 50, 50, 100, '0', 'black')
