def start_screen():
    global game
    fon = pygame.transform.scale(load_image('C:/Users/USER/Desktop/piton/RABOTI/Игра/image.bmp'), (width, height))
    screen.blit(fon, (0, 0))

    button_1 = Button()
    button_1.create_button(screen, 'red', 40, 40, 100, 200, 100, 'Начать новую игру', 'black')

    button_2 = Button()
    button_2.create_button(screen, 'red', 140, 140, 100, 200, 100, 'Продолжить', 'black')

    button_3 = Button()
    button_3.create_button(screen, 'red', 240, 240, 100, 200, 100, 'Настройки', 'black')

    button_4 = Button()
    button_4.create_button(screen, 'red', 340, 340, 100, 200, 100, 'Выход', 'black')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
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
                    pygame.quit()
                return

        pygame.display.flip()
        clock.tick(50)