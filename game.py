import pygame
from menu import *
from montanha_russa.montanhaRussa import Simulador

class Game():
  def __init__(self):
    pygame.init()
    self.quantidade_vagas = 0
    self.credit_cood = 0
    
    self.running, self.playing = True, False
    self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.MOUSEBUTTONUP, self.MOUSEBUTTONDOWN, self.K_LEFT, self.K_RIGHT =  False, False, False, False, False, False, False, False
    self.DISPLAY_W, self.DISPLAY_H = 480*2, 270*2
    self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
    self.janela = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
    self.font_name = '8-BIT WONDER.TTF'
    self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
    self.main_menu = MainMenu(self)
    self.credits = CreditsMenu(self)
    self.simulador = Simulador(self)
    self.curr_menu = self.main_menu
  def game_loop(self):
    while self.playing:
      self.check_events()
      if self.START_KEY:
        self.playing= False
      self.display.fill(self.BLACK)
      
      self.simulador.play_simulador()
      
      pygame.display.update()
      self.reset_keys()
  def check_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.running, self.playing = False, False
        self.curr_menu.run_display = False
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
          self.START_KEY = True
        if event.key == pygame.K_BACKSPACE:
          self.BACK_KEY = True
        if event.key == pygame.K_DOWN:
          self.DOWN_KEY = True
        if event.key == pygame.K_UP:
          self.UP_KEY = True
        if event.key == pygame.K_LEFT:
          self.K_LEFT = True
        if event.key == pygame.K_RIGHT:
          self.K_RIGHT = True
      if event.type == pygame.MOUSEBUTTONUP:
        self.MOUSEBUTTONUP = True
        self.MOUSEBUTTONDOWN = False
      if event.type == pygame.MOUSEBUTTONDOWN:
        self.MOUSEBUTTONDOWN = True
  def reset_keys(self):
    self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.MOUSEBUTTONUP, self.MOUSEBUTTONDOWN, self.K_LEFT, self.K_RIGHT =  False, False, False, False, False, False, False, False
  def draw_text(self, text, size, x, y ):
    font = pygame.font.Font(self.font_name,size)
    text_surface = font.render(text, True, self.WHITE)
    text_rect = text_surface.get_rect()
    text_rect.center = (x,y)
    self.display.blit(text_surface,text_rect)
    
    if(text == "Creditos"):
      self.credit_cood = text_surface.get_rect()
