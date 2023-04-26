import random
import pygame
pygame.init()

screen = pygame.display.set_mode([1270, 780])
pygame.display.set_caption('triland')



peak_b = pygame.image.load("images/peak.png").convert_alpha()
peak_b = pygame.transform.scale(peak_b, (350//2, 720//2))
peak_b_mask = pygame.mask.from_surface(peak_b)

peak_t = pygame.image.load("images/peak.png").convert_alpha()
peak_t = pygame.transform.scale(peak_t, (350//2, 720//2))
peak_t = pygame.transform.rotate(peak_t, 180)
peak_t_mask = pygame.mask.from_surface(peak_t)

char = pygame.image.load("images/char.png").convert_alpha()
char = pygame.transform.scale(char, (120, 120))
char_mask = pygame.mask.from_surface(char)
mov = 0
gravity = 0.01
by = 6
velocity = 0
y = 0

xt = -175

GameOver = False
canIncrementScore = False
canPrev = canIncrementScore
# def jump():
#     velocity = 0
point = 0 
font = pygame.font.SysFont("Verdana", 50)

dis = [125, 190, 170, 160]
upd = random.choice(dis)

running = True
while running:
    screen.fill((14,47,68))
    xb = xt + (120 + upd)
    # print(upd)

    y = y + velocity

    offset1 = ((1270/2) - xt, y - 0)
    offset2 = ((1270/2) - xb, y - 780+(720//2))
    res1coll = peak_t_mask.overlap(char_mask, offset1)
    res2coll = peak_b_mask.overlap(char_mask, offset2)
    if res1coll or res2coll:
        GameOver = True
        print("coll")
   

    k_sp = False
    if GameOver:
        re = font.render("Game Over", True, (255, 20, 147))
        xt = -900
        velocity = -400
        screen.blit(re, ((1270/2)-50*2.5, 780/2))
    if y+120/2 >= 300 and abs(xt+(350//2)/2 - 635+(120/2) ) <= 30:
        # point += 1
        canIncrementScore = True
    else:
        canIncrementScore = False

    if canIncrementScore == True and canPrev == False:
        point += 1

    canPrev = canIncrementScore
        # print("ok")


    
    xt += 1
    # and abs(xt+(350//2)/2 - 635+(120/2) ) <= 50
    # print(abs(xt+(350//2)/2 - 635+(120/2) ))

    # print(xt+(350//2)/2, 780-(720//2), xb+(350//2)/2, "=++++", y)
    
    if xt > 1270 + (350//2):
        xt = -(175 + (120 + 260))
        upd = random.choice(dis)
        



    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_UP:
                k_sp = True

        elif event.type == pygame.QUIT:
            running = False

    if k_sp:
        velocity -= 2.5

    if y < 780 - ((120)-27) and k_sp != True:
        velocity += gravity
    # print(point)
    # screen, (255, 20, 147), (0,0), (1270,0)
    screen.blit(peak_b, (xb, 780-(720//2)))
    screen.blit(peak_t, (xt, 0))

    # charRect = /
    # print(780 - ((120-27)-27))
    screen.blit(char, (1270/2, y))
    rect_top = pygame.Rect(0, 0, 1270, 27)
    pygame.draw.rect(screen, (255, 20, 147), rect_top)
    rect_bottom = pygame.Rect(0, 780-27, 1270, 27)
    pygame.draw.rect(screen, (255, 20, 147), rect_bottom)
    # pygame.draw.line(screen, (0, 255, 0), (xt+(350//2)/2, 300), (xb+(350//2)/2, 300))
    # pygame.draw.circle(screen, (255, 255, 0), (635+(120/2), y+120/2), 10)
    # pygame.draw.circle(screen, (255, 0, 0), (xt+(350//2)/2, y+120/2), 10)
    # pygame.draw.circle(screen, (255, 0, 255), (xb+(350//2)/2, y+120/2), 10)
    # h
    sc = font.render(f"Score: {point}", True, (255, 20, 147))
    screen.blit(sc, (1270-350, 50))



    pygame.display.flip()
pygame.quit()