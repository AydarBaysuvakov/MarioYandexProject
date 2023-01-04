import pygame
from GameComponents.Window import SIZE, TITLE
from GameComponents.StartScreen import Start_Screen
from GameComponents.GameWindow import Game_Window
from GameComponents.LevelChooseWindow import Level_Choise
from GameComponents.LoadComponents import load_level

if __name__ == '__main__':
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption(TITLE)
    Start_Window = Start_Screen(screen)
    Game_window = Game_Window(screen, load_level('test_level.txt'))
    Levels = Level_Choise(screen, 'Level_list.txt')
    running = True
    while running:
        last_pressed_button = Start_Window.show()
        if last_pressed_button == "Начать игру":
            Game_window.show()
        elif last_pressed_button == "Выбрать уровень":
            last_pressed_button = Levels.show()
            Game_window = Game_Window(screen, load_level(Levels.levels[last_pressed_button]))
            Game_window.show()
        elif last_pressed_button == "Правила":
            pass