class Mountain(pygame.sprite.Sprite):
    image = load_image(f"C:/Users/USER/Desktop/piton/RABOTI/Игра/start{s}.png", -1)

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Mountain.image
        self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        # располагаем горы внизу
        self.rect.bottom = height

    def update(self):
        self.image = load_image(f"C:/Users/USER/Desktop/piton/RABOTI/Игра/start{s}.png", -1)
        self.mask = pygame.mask.from_surface(self.image)


class Finish(pygame.sprite.Sprite):
    image = load_image(f"C:/Users/USER/Desktop/piton/RABOTI/Игра/finish{s}.png", -1)

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Finish.image
        self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        # располагаем горы внизу
        self.rect.bottom = height

    def update(self):
        self.image = load_image(f"C:/Users/USER/Desktop/piton/RABOTI/Игра/finish{s}.png", -1)
        self.mask = pygame.mask.from_surface(self.image)



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

    def update(self):
        global next_question, next
        if pygame.sprite.collide_mask(self, mountain):
            pygame.mouse.set_pos(450, 500)
        if pygame.sprite.collide_mask(self, finish) and not next:
            next_question = True
            next = True
