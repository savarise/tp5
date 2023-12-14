"""
Modèle de départ pour la programmation Arcade.
Il suffit de modifier les méthodes nécessaires à votre jeu.
"""
from enum import Enum

import random

import arcade
#import arcade.gui

#from attack_animation import AttackType, AttackAnimation
#from game_state import GameState

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Roche, papier, ciseaux"
DEFAULT_LINE_HEIGHT = 45  # The default line height for text.

class AttackType(Enum):
   """
   Simple énumération pour représenter les différents types d'attaques.
   """
   ROCK = 0,
   PAPER = 1,
   SCISSORS = 2

class MyGame(arcade.Window):
   """
   La classe principale de l'application

   NOTE: Vous pouvez effacer les méthodes que vous n'avez pas besoin.
   Si vous en avez besoin, remplacer le mot clé "pass" par votre propre code.
   """

   PLAYER_IMAGE_X = (SCREEN_WIDTH / 2) - (SCREEN_WIDTH / 4)
   PLAYER_IMAGE_Y = SCREEN_HEIGHT / 2.5
   COMPUTER_IMAGE_X = (SCREEN_WIDTH / 2) * 1.5
   COMPUTER_IMAGE_Y = SCREEN_HEIGHT / 2.5
   ATTACK_FRAME_WIDTH = 154 / 2
   ATTACK_FRAME_HEIGHT = 154 / 2

   def __init__(self, width, height, title):
       super().__init__(width, height, title)


       self.player = arcade.Sprite("img/img_6.png", 0.3)
       self.computer = arcade.Sprite("img/img_7.png", 1.3)
       self.players = None
       self.rock = arcade.Sprite("img/img.png", 0.6)
       self.paper = arcade.Sprite("img/img_2.png", 0.6)
       self.scissors = arcade.Sprite("img/img_4.png", 0.6)
       self.player_score = 0
       self.computer_score = 0
       self.player_attack_type = {}
       self.computer_attack_type = None
       self.player_attack_chosen = False
       self.player_won_round = None
       self.draw_round = None
       self.game_state = "NOT_STARTED"

   def on_draw(self):
       # Cette commande permet d'effacer l'écran avant de dessiner. Elle va dessiner l'arrière
       # plan selon la couleur spécifié avec la méthode "set_background_color".
       arcade.start_render()

       # Display title
       arcade.draw_text(SCREEN_TITLE,
                        0,
                        SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 2,
                        arcade.color.BLACK_BEAN,
                        60,
                        width=SCREEN_WIDTH,
                        align="center")
       self.player.center_x = self.PLAYER_IMAGE_X
       self.player.center_y = self.PLAYER_IMAGE_Y
       self.player.draw()

       self.rock.center_x = self.PLAYER_IMAGE_X - 100
       self.rock.center_y = self.scissors.center_y
       self.rock.draw()

       self.paper.center_x = self.PLAYER_IMAGE_X + 100
       self.paper.center_y = self.scissors.center_y
       self.paper.draw()

       self.scissors.center_x = self.PLAYER_IMAGE_X
       self.scissors.center_y = self.PLAYER_IMAGE_Y - 100
       self.scissors.draw()

       self.computer.center_x = self.COMPUTER_IMAGE_X
       self.computer.center_y = self.COMPUTER_IMAGE_Y
       self.computer.draw()

       if self.game_state == "ROUND_ACTIVE" and self.computer_attack_type==AttackType.ROCK:
           self.rock.center_x = self.COMPUTER_IMAGE_X
           self.rock.center_y = self.rock.center_y
           self.rock.draw()


       arcade.draw_rectangle_outline(self.scissors.center_x, self.scissors.center_y, self.ATTACK_FRAME_WIDTH,
                                     self.ATTACK_FRAME_HEIGHT, arcade.color.PURPLE, 1, 0)
       arcade.draw_rectangle_outline(self.paper.center_x, self.paper.center_y, self.ATTACK_FRAME_WIDTH,
                                     self.ATTACK_FRAME_HEIGHT, arcade.color.PURPLE, 1, 0)
       arcade.draw_rectangle_outline(self.rock.center_x, self.rock.center_y, self.ATTACK_FRAME_WIDTH,
                                     self.ATTACK_FRAME_HEIGHT, arcade.color.PURPLE, 1, 0)
       arcade.draw_rectangle_outline(self.COMPUTER_IMAGE_X, self.rock.center_y, self.ATTACK_FRAME_WIDTH,
                                     self.ATTACK_FRAME_HEIGHT, arcade.color.PURPLE, 1, 0)
       if self.game_state == "ROUND_DONE" or self.game_state == "GAME_OVER": arcade.draw_text("Appuie sur espace pour recommencer", 0, SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 4, arcade.color.LIGHT_BLUE, 40, width=SCREEN_WIDTH, align="center")
       if self.game_state == "NOT_STARTED": arcade.draw_text("Clique sur une image pour faire une attaque", 0, SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 4, arcade.color.LIGHT_BLUE, 40, width=SCREEN_WIDTH, align="center")
       if self.game_state == "ROUND_DONE": arcade.draw_text("L'ordinateur a gagné", 0, SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 6, arcade.color.LIGHT_BLUE, 40, width=SCREEN_WIDTH, align="center")
       if self.game_state == "ROUND_DONE": arcade.draw_text("Tu as gagné", 0, SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 6, arcade.color.LIGHT_BLUE, 40, width=SCREEN_WIDTH, align="center")
       #afficher l'attaque de l'ordinateur selon l'état de jeu
       #afficher le résultat de la partie si l'ordinateur a joué (ROUND_DONE)

   def on_mouse_press(self, x, y, button, key_modifiers):
       if self.game_state == "NOT_STARTED":
           self.game_state = "ROUND_ACTIVE"
           if self.rock.collides_with_point((x, y)):
               print("L'usager a cliqué sur le r.")
               self.player_attack_type = AttackType.ROCK

           if self.paper.collides_with_point((x, y)):
               print("L'usager a cliqué sur le p.")
               self.player_attack_type = AttackType.PAPER

           if self.scissors.collides_with_point((x, y)):
               print("L'usager a cliqué sur le s.")
               self.player_attack_type = AttackType.SCISSORS

   def on_key_press(self, key, key_modifiers):
    if key == arcade.key.SPACE:
        if self.game_state == "ROUND_ACTIVE":
            self.game_state = "ROUND_DONE"

   def on_update(self, delta_time):
       if self.game_state == "ROUND_ACTIVE":
           pc_attack = random.randint(0, 2)
           if pc_attack == 0:
               self.computer_attack_type = AttackType.ROCK
           elif pc_attack == 1:
               self.computer_attack_type = AttackType.PAPER
           else:
               self.computer_attack_type = AttackType.SCISSORS

def main():
   """ Main method """
   game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
   arcade.run()

if __name__ == "__main__":
   main()
