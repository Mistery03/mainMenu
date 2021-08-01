import pygame;

class Menu():
    def __init__(self,game):
        self.game = game;
        self.mid_w, self.mid_h = self.game.DISPLAY_W/2, self.game.DISPLAY_H/2;
        self.runDisplay = True;
        self.cursorRect = pygame.Rect(0,0,20,20);
        self.offset = -100;

    def drawCursor(self):
        self.game.drawText("*",20,self.cursorRect.x,self.cursorRect.y);

    def blitScreen(self):
        self.game.window.blit(self.game.display, (0,0));
        pygame.display.update()
        self.game.resetKeys();

class mainMenu(Menu):
    def __init__(self,game):
        Menu.__init__(self,game);
        self.state = "Start";
        self.startx, self.starty = self.mid_w, self.mid_h + 30;
        self.optionx, self.optiony = self.mid_w, self.mid_h + 50;
        self.creditx, self.credity = self.mid_w, self.mid_h + 70;
        self.cursorRect.midtop = (self.startx + self.offset, self.starty);

    def displayMenu(self):
        self.runDisplay = True;
        while self.runDisplay:
            self.game.checkEvents()
            self.checkInput();
            self.game.display.fill(self.game.BLACK);
            self.game.drawText('Main Menu', 20, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2-20);
            self.game.drawText('Start', 20,self.startx,self.starty );
            self.game.drawText('Options', 20, self.optionx,self.optiony);
            self.game.drawText('Credits', 20, self.creditx,self.credity);
            self.drawCursor();
            self.blitScreen();
            
    def moveCursor(self):
        if self.game.DOWN_KEY:
            if self.state == "Start":
                self.cursorRect.midtop = (self.optionx + self.offset, self.optiony);
                self.state = "Options";
            elif self.state == "Options":
                self.cursorRect.midtop = (self.creditx + self.offset, self.credity);
                self.state = "Credits";
            elif self.state == "Credits":
                self.cursorRect.midtop = (self.startx + self.offset, self.starty);
                self.state = "Start";
        elif self.game.UP_KEY:
            if self.state == "Start":
                self.cursorRect.midtop = (self.creditx + self.offset, self.credity);
                self.state = "Credits";
            elif self.state == "Options":
                self.cursorRect.midtop = (self.startx + self.offset, self.starty);
                self.state = "Start";
            elif self.state == "Credits":
                self.cursorRect.midtop = (self.optionx + self.offset, self.optiony);
                self.state = "Options";

    def checkInput(self):
        self.moveCursor();
        if self.game.START_KEY:
            if self.state == "Start":
                self.game.playing = True;
            elif self.state == "Options":
                self.game.currMenu = self.game.options;
            elif self.state == "Credits":
               self.game.currMenu = self.game.credits;
            
            self.runDisplay = False;

class OptionsMenu(Menu):
    def __init__(self,game):
            Menu.__init__(self,game);
            self.state = "Volume";
            self.volx,self.voly = self.mid_w, self.mid_h + 20;
            self.controlx,self.controly = self.mid_w, self.mid_h + 40;
            self.cursorRect.midtop = (self.volx + self.offset, self.voly);

    def displayMenu(self):
        self.runDisplay = True;
        while self.runDisplay:
            self.game.checkEvents();
            self.checkInput();
            self.game.display.fill(self.game.BLACK);
            self.game.drawText('Options', 20, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2-30);
            self.game.drawText('Volume', 15,self.volx,self.voly );
            self.game.drawText('Controls', 15, self.controlx,self.controly);
            self.drawCursor();
            self.blitScreen();

    def checkInput(self):
        if self.game.BACK_KEY:
            self.game.currMenu = self.game.main_menu;
            self.runDisplay = False;
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == "Volume":
                self.cursorRect.midtop = (self.controlx + self.offset, self.controly);
                self.state = "Controls";
            elif self.state == "Controls":
                self.cursorRect.midtop = (self.volx + self.offset, self.voly);
                self.state = "Volume";
        elif self.game.START_KEY:
            #create volume and control
            pass;

class CreditsMenu(Menu):
    def __init__(self,game):
        Menu.__init__(self,game);

    def displayMenu(self):
        self.runDisplay = True;
        while self.runDisplay:
            self.game.checkEvents();
            self.checkInput();
            self.game.display.fill(self.game.BLACK);
            self.game.drawText('Credits', 20, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2-20);
            self.game.drawText('Made by Mistery', 15, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2);
            self.blitScreen();

    def checkInput(self):
         if self.game.START_KEY or self.game.BACK_KEY:
            self.game.currMenu = self.game.main_menu;
            self.runDisplay = False;
            
        
            
                
        
        

