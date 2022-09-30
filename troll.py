import pygame
import random 

pygame.init()
screen=pygame.display.set_mode((500,500))
font1=pygame.font.Font("freesansbold.ttf",32)
font=pygame.font.Font("freesansbold.ttf",16)

x1,y1=100,400
x2,y2=400,400

t=True
while t:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            t=False
    mouse=pygame.mouse.get_pos()
    finger=pygame.FINGERMOTION
    
    #the button
    circle_yes=pygame.draw.circle(screen,(0,255,0),(x1,y1),30,30)
    circle_no=pygame.draw.circle(screen,(255,0,0),(x2,y2),30,30)

    #text of button
    no_text=font.render("no",True,(0,0,0))
    yes_text=font.render("yes",True,(0,0,0))
    screen.blit(no_text,(x2-10,y2-10))
    screen.blit(yes_text,(x1-10,y1-10))

    #comand no button
    if circle_no.collidepoint(mouse) and event.type == pygame.MOUSEBUTTONDOWN:
        pygame.draw.rect(screen,(0,0,0),(x2-40,y2-40,110,110))
        x2=random.randint(50,450)
        y2=random.randint(100,450)

    #command yes button
    if circle_yes.collidepoint(mouse) and event.type == pygame.MOUSEBUTTONDOWN:
        testo=font.render("I knew it ;)",True,(255,255,255))
        screen.blit(testo,(200,100))

    #istigating text
    testol=font1.render("are you gey ?",True,(255,255,255))
    screen.blit(testol,(150,0))

    pygame.display.update()