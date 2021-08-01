import pygame;
from classTimeTable import game;

g = game();

while g.running:
    g.currMenu.displayMenu();
    g.gameLoop();

pygame.quit();
quit();
