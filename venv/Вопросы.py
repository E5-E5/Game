def Question(text, ques):
    intro_text = ["Когда ты какал"]
    fon = pygame.transform.scale(load_image('C:/Users/USER/Desktop/piton/RABOTI/Игра/image.bmp'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    button_question = Button()
    button_question.create_button(screen, 'red', 40, 40, 100, 200, 100, 'Назад', 'black')
    string_rendered = font.render('zzzzzzzzzzzzzzzzz', True, pygame.Color('black'))

    intro_rect = string_rendered.get_rect()
    intro_rect.top = text_coord
    screen.blit(string_rendered, intro_rect)

    button_1 = Button()
    button_2 = Button()
    button_3 = Button()
    button_4 = Button()
    button_5 = Button()
    res = 0
    if len(ques) >= 1:
        button_1.create_button(screen, 'white', 100, 100, 100, 200, 100, '124421', 'black')
    if len(ques) >= 2:
        button_2.create_button(screen, 'white', 200, 200, 100, 200, 100, '21421', 'black')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # return  # начинаем игру
                if button_1.pressed(event.pos):
                    print('Первый отв')
                    res = 1
                elif button_2.pressed(event.pos):
                    print('Второй отв')
                    res = 2
                elif button_question.pressed(event.pos):
                    global next_question
                    next_question = False
                print(res)
                return
