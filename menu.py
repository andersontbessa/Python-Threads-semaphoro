import pygame

class Menu():
  def __init__(self, game):
      self.game = game
      self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
      self.run_display = True
      self.cursor_rect = pygame.Rect(0, 0, 20, 20)
      self.offset = -130

  def draw_cursor(self):
    self.game.draw_text('-', 15, self.cursor_rect.x, self.cursor_rect.y)

  def blit_screen(self):
    self.game.janela.blit(self.game.display, (0, 0))
    pygame.display.update()
    self.game.reset_keys()

class MainMenu(Menu):
  def __init__(self, game):
    Menu.__init__(self, game)
    self.state = "Start"
    self.startx, self.starty = self.mid_w, self.mid_h + 30
    self.optionsx, self.optionsy = self.mid_w, self.mid_h + 50
    self.creditsx, self.creditsy = self.mid_w, self.mid_h + 70
    self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

  def display_menu(self):
    self.run_display = True
    while self.run_display:
      self.game.check_events()
      self.check_input()
      self.game.display.fill(self.game.BLACK)
      self.game.draw_text('Multithreading', 40, self.game.DISPLAY_W / 2, (self.game.DISPLAY_H - 33) / 2 - 40)
      self.game.draw_text('Problema do vagao', 25, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
      
      self.game.draw_text("Vagas", 20, self.startx, self.starty)
      self.game.draw_text(str(self.game.quantidade_vagas), 20, self.startx + 150, self.starty)

      # self.game.draw_text("Passageiros", 20, self.optionsx, self.optionsy)
      # self.game.draw_text(str(self.game.passengers), 20,  self.optionsx + 150, self.optionsy)

      self.game.draw_text("Aperte 'enter' para continuar", 7, self.optionsx, self.optionsy + 25)

      self.game.draw_text("Creditos", 10, self.creditsx, self.game.DISPLAY_H - 15)

      self.draw_cursor()
      self.blit_screen()

  def move_cursor(self):
    if self.game.MOUSEBUTTONUP: 
      mpos = pygame.mouse.get_pos()   
      self.game.credit_cood.x = self.creditsx - 75/2
      self.game.credit_cood.y = (self.game.DISPLAY_H - 15 ) - 10/2
      if (self.game.credit_cood.collidepoint(mpos)):
        self.game.curr_menu = self.game.credits
    if self.game.K_LEFT:
      if(self.state == 'Start'):
        if(self.game.quantidade_vagas == 0):
          self.game.quantidade_vagas = self.game.quantidade_vagas
        else:
          self.game.quantidade_vagas -=1
      elif(self.state == 'Options'):
        if(self.game.passengers == 0):
          self.game.passengers = self.game.passengers
        else:
          self.game.passengers -=1
    if self.game.K_RIGHT:
      if(self.state == 'Start'):
        if(self.game.quantidade_vagas == 10):
          self.game.quantidade_vagas = self.game.quantidade_vagas
        else:
          self.game.quantidade_vagas +=1
      elif(self.state == 'Options'):
        if(self.game.passengers == 10):
          self.game.passengers = self.game.passengers
        else:
          self.game.passengers +=1

  def check_input(self):
    self.move_cursor()
    if self.game.START_KEY:
        self.game.playing = True
    if self.game.MOUSEBUTTONUP:
      if self.state == 'Credits':
        self.game.curr_menu = self.game.credits
    self.run_display = False

class CreditsMenu(Menu):
  def __init__(self, game):
    Menu.__init__(self, game)

  def display_menu(self):
    self.run_display = True
    while self.run_display:
      self.game.check_events()
      if self.game.START_KEY or self.game.BACK_KEY or self.game.MOUSEBUTTONUP:
        self.game.curr_menu = self.game.main_menu
        self.run_display = False
      self.game.display.fill(self.game.BLACK)
      self.game.draw_text('Creditos', 40, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 25)
      self.game.draw_text('Anderson & Samuel & Jardel', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 10)
      self.blit_screen()
