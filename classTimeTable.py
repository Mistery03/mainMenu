import pygame
from menu import *;

class game():
    def __init__(self):
        pygame.init();
        self.running, self.playing = True, False;
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False;
        self.DISPLAY_W, self.DISPLAY_H = 480, 270;
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H));
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)));
        self.fontName = '8-BIT WONDER.TTF';
        #self.font_name = pygame.font.get_default_font();
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255);
        self.main_menu = mainMenu(self);
        self.options = OptionsMenu(self);
        self.credits = CreditsMenu(self);
        self.currMenu = self.main_menu;

    def gameLoop(self):
        while self.playing:
            self.checkEvents();
            if self.START_KEY:
                self.playing= False;
            self.display.fill(self.BLACK);
            self.drawText('Thanks for Playing', 20, self.DISPLAY_W/2, self.DISPLAY_H/2);
            self.window.blit(self.display, (0,0));
            pygame.display.update();
            self.resetKeys();

    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False;
                self.currMenu.runDisplay = False;
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True;
                if event.key == pygame.K_BACKSPACE or event.key == pygame.K_ESCAPE:
                    self.BACK_KEY = True;
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.DOWN_KEY = True;
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.UP_KEY = True;

    def resetKeys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False;

    def drawText(self, text, size, x, y ):
        font = pygame.font.Font(self.fontName,size);
        textSurface = font.render(text, True, self.WHITE);
        textRect = textSurface.get_rect();
        textRect.center = (x,y);
        self.display.blit(textSurface,textRect);
