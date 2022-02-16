import sys, pygame, pygame_menu

pygame.init()

size = width, height = 640, 480
dx = 1
dy = 1
x = 163
y = 120
black = (0,0,0)
white = (255,255,255)

screen = pygame.display.set_mode(size)

def start_game():
    print('hello')
    pass

menu = pygame_menu.Menu('Welcome', 400, 300, theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Name:', default='Silly Goose')
menu.add.button('Play', start_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(screen)

# while 1:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT: sys.exit()

#     x += dx
#     y += dy

#     if x < 0 or x > width:
#         dx = -dx
    
#     if y < 0 or y > height:
#         dy = -dy

#     screen.fill(black)

#     pygame.draw.circle(screen, white, (x,y), 8)

#     pygame.display.flip()