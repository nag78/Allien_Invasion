import sys

import pygame

def run_game():
    #Инициализируем игру и создаем объект экрана.
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    #Назначение цвета фона
    bg_color = (230,230,230)

    #Запуск основного цикла игры
    while True:
        #Отслеживание событий клавиатуры и мыши.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #При каждом проходе цикла перерисовывается экрае
        screen.fill(bg_color)
        #Отображение последнего прорисованного экрана.
        pygame.display.flip()
run_game()
