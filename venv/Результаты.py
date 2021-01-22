def result():
    if boss_killing > 5:
        if finish.good > finish.bad:
            intro_text = ["К сожалению, вы не смогли убежать от своего врага,",
                          " но либо вы ему понравились, либо у него хорошее настроение,",
                          " поэтому он решил оставить вас в живых,",
                          " но вы до конца своих дней останетесь в этом лабиринте,",
                          "помогая теперь уже своему новому другу"]
        else:
            intro_text = ["Вы не смогли убежать от своего врага...",
                          " В этот раз вы проиграли ваму заклятому врагу",
                          " умерев в несовсем честной битве"]
    else:
        if finish.good > finish.bad:
            intro_text = ["Поздравляю!!!",
                          " Вы смогли убежать от никчёмного шара.",
                          " Добежав до выхода перед вами открылась дверь в новый мир,",
                          "но это уже другая история..."]
        else:
            intro_text = ["Несмотря на то что вы смогли добраться до выхода,",
                          " дверь оказалась какой-то странной.",
                          " Прыгнув в нее, вы начали лететь в какую-то пустоту,",
                          " окружённую стенками лабиринта.",
                          " Вы всё летите и летите, а конца не видно...",
                          " Возможно, вы могли что-то именить?...",]

    global game
    fon = pygame.transform.scale(load_image('Level0.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    button_1 = Button()
    button_1.create_button(screen, 'dark gray', 40, 340, 100, 50, 200, 'Далее',
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
        flag = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_1.pressed(event.pos):
                    flag = True
        if flag:
            if boss_killing > 5:
                if finish.good > finish.bad:
                    clip = get_clip('C:/Users/USER/Desktop/piton/RABOTI/Игра/boss_good.mp4')
                    clip.preview()
                else:
                    clip = get_clip('C:/Users/USER/Desktop/piton/RABOTI/Игра/boss_bad.mp4')
                    clip.preview()
            else:
                if finish.good > finish.bad:
                    clip = get_clip('C:/Users/USER/Desktop/piton/RABOTI/Игра/good.mp4')
                    clip.preview()
                else:
                    clip = get_clip('C:/Users/USER/Desktop/piton/RABOTI/Игра/bad.mp4')
                    clip.preview()
            start_screen()

        pygame.display.flip()
        clock.tick(50)
