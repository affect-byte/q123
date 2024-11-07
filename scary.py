import pygame as pg

pg.init()
pg.font.init()
pg.mixer.init()
screen = pg.display.set_mode((900, 900))
font = pg.font.SysFont("None", 30)

sound = pg.mixer.Sound("final_.mp3")
sound.set_volume(0.7)
pg.display.set_caption("Game")
screamer = pg.image.load("screamer.png")
screamer = pg.transform.scale(screamer, (900, 900))

clock = pg.time.Clock()
screamer_rect = pg.draw.rect(screen, (255, 255, 255), (180, 300, 550, 400))
screamer_rect = screamer.get_rect(center=(2000, 2000))

rect = pg.Rect((150, 750, 150, 800))
rect2 = pg.Rect((700, 700, 150, 800))
rect3 = pg.Rect((150, 670, 150, 550))
rect4 = pg.Rect((150, 470, 150, 750))
rect5 = pg.Rect((150, 470, 400, 300))
rect6 = pg.Rect((460, 470, 400, 320))
rect7 = pg.Rect((488, 283, 388, 183))
rect8 = pg.Rect((446, 283, 500, 283))
rect9 = pg.Rect((446, 240, 446, 340))
rect10 = pg.Rect((446, 240, 446, 240))
rect11 = pg.Rect((488, 190, 546, 140))
rect12 = pg.Rect((466, 135, 446, 240))

jumpscare_point_rect = pg.Rect((446, 260, 460, 260))

player_image = pg.image.load("igrok.png").convert_alpha()
player_image = pg.transform.scale(player_image, (20, 20))
player_rect = player_image.get_rect(topleft=(160, 770)) 

speed = 1

run = True
jumpscare = False

show_menu = True
while show_menu:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            show_menu = False
            run = False
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()
            if play_button_rect.collidepoint(mouse_pos):
                show_menu = False
            if quit_button_rect.collidepoint(mouse_pos):
                show_menu = False
                run = False

    screen.fill("black")

    play_text = font.render("Играть", True, "white")
    play_button_rect = play_text.get_rect(center=(450, 400))
    screen.blit(play_text, play_button_rect)

    quit_text = font.render("Выход", True, "white")
    quit_button_rect = quit_text.get_rect(center=(450, 500))
    screen.blit(quit_text, quit_button_rect)

    pg.display.flip()

while run:
    clock.tick(120)
    keys = pg.key.get_pressed()
    screen.fill("black")

    surf = pg.Surface((550, 50))
    surf.fill("purple")
    screen.blit(surf, rect)

    surf2 = pg.Surface((50, 100))
    surf2.fill("purple")
    screen.blit(surf2, rect2)

    surf3 = pg.Surface((600, 50))
    surf3.fill("purple")
    screen.blit(surf3, rect3)

    surf4 = pg.Surface((50, 250))
    surf4.fill("purple")
    screen.blit(surf4, rect4)

    surf5 = pg.Surface((315, 50))
    surf5.fill("purple")
    screen.blit(surf5, rect5)

    surf6 = pg.Surface((40, 13))
    surf6.fill("purple")
    screen.blit(surf6, rect6)

    surf7 = pg.Surface((13, 200))
    surf7.fill("purple")
    screen.blit(surf7, rect7)

    surf8 = pg.Surface((55, 13))
    surf8.fill("purple")
    screen.blit(surf8, rect8)

    surf9 = pg.Surface((13, 55))
    surf9.fill("purple")
    screen.blit(surf9, rect9)

    surf10 = pg.Surface((55, 13))
    surf10.fill("purple")
    screen.blit(surf10, rect10)

    surf11 = pg.Surface((13, 55))
    surf11.fill("purple")
    screen.blit(surf11, rect11)

    surf12 = pg.Surface((55, 80))
    surf12.fill("white")
    screen.blit(surf12, rect12)

    jumpscare_surf = pg.Surface((13, 13))
    jumpscare_surf.fill("purple")
    screen.blit(jumpscare_surf, jumpscare_point_rect)

    screen.blit(player_image, player_rect)

    me_rect = player_rect

    surf_rect = surf.get_rect(topleft=(150, 750))
    surf_rect2 = surf2.get_rect(topleft=(700, 700))
    surf_rect3 = surf3.get_rect(topleft=(150, 670))
    surf_rect4 = surf4.get_rect(topleft=(150, 470))
    surf_rect5 = surf5.get_rect(topleft=(150, 470))
    surf_rect6 = surf6.get_rect(topleft=(460, 470))
    surf_rect7 = surf7.get_rect(topleft=(488, 283))
    surf_rect8 = surf8.get_rect(topleft=(446, 283))
    surf_rect9 = surf9.get_rect(topleft=(446, 240))
    surf_rect10 = surf10.get_rect(topleft=(446, 140))
    surf_rect11 = surf11.get_rect(topleft=(446, 240))

    surf_rect_jumpscare = jumpscare_surf.get_rect(topleft=(446, 250))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    if keys[pg.K_w] or keys[pg.K_UP]:
        player_rect.y -= speed

    if keys[pg.K_d] or keys[pg.K_RIGHT]:
        player_rect.x += speed

    if keys[pg.K_a] or keys[pg.K_LEFT]:
        player_rect.x -= speed

    if keys[pg.K_s] or keys[pg.K_DOWN]:
        player_rect.y += speed

    if (not surf_rect.colliderect(me_rect)
            and not surf_rect2.colliderect(me_rect)
            and not surf_rect3.colliderect(me_rect)
            and not surf_rect4.colliderect(me_rect)
            and not surf_rect5.colliderect(me_rect)
            and not surf_rect6.colliderect(me_rect)
            and not surf_rect7.colliderect(me_rect)
            and not surf_rect8.colliderect(me_rect)
            and not surf_rect9.colliderect(me_rect)
            and not surf_rect10.colliderect(me_rect)):
        print('Столкновение')
        player_rect.topleft = (160, 770)
    if surf_rect_jumpscare.colliderect(me_rect) and not jumpscare:
        sound.play()
        jumpscare = True
        screamer_rect = screamer.get_rect(center=(450, 450))
        screamer = pg.transform.scale(pg.image.load("screamer.png").convert(), (900, 900))

    text = font.render(f"Тут Вискас)", False, 'red')
    screen.blit(text, (525, 198))

    screen.blit(screamer, screamer_rect)
    pg.display.update()
pg.quit()