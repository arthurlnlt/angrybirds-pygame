from functions import *

import button

pygame.init()

# créer la fenêtre de jeu
fenetre_x = 700
fenetre_y = 500
background = pygame.image.load("images/fonds/Sans titre (1).png")
background = pygame.transform.scale(background, (700, 500))

screen = pygame.display.set_mode((fenetre_x, fenetre_y))
pygame.display.set_caption("Menu Principal")

# game variables
game_paused = False
menu_state = "main"

# define fonts
font = pygame.font.SysFont("Jackpot", 40)

# define colours
TEXT_COL = (255, 255, 255)

# association des images aux boutons
resume_img = pygame.image.load("images/fonds/button_resume.png").convert_alpha()
options_img = pygame.image.load("images/fonds/button_options.png").convert_alpha()
quit_img = pygame.image.load("images/fonds/button_quit.png").convert_alpha()
back_img = pygame.image.load('images/fonds/button_back.png').convert_alpha()
start_btn = pygame.image.load('images/fonds/start_button.png').convert_alpha()

start_button = button.bouton(215, 200, start_btn, 1)
resume_button = button.bouton(304, 125, resume_img, 1)
options_button = button.bouton(297, 500, options_img, 1)
quit_button = button.bouton(336, 375, quit_img, 1)
back_button = button.bouton(332, 450, back_img, 1)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


boucle_jeu = False
# game loop
run = True
while run:
    screen.blit(background, (0, 0))
    pygame.image.load("images/fonds/a.png")
    if not game_paused:
        if menu_state == "main":
            if start_button.draw(screen):
                boucle_jeu = True
                run = False
            if options_button.draw(screen):
                menu_state = "options"
    # acquisition des évènements
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
