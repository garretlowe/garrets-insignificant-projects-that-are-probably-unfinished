import random

#######################
#      BLACKJACK      #
#######################
# Author: Garret Lowe #
# Updated: 2020-07-29 #
#######################

values = {
  1: "Ace",
  2: "Two", 
  3: "Three",
  4: "Four",
  5: "Five",
  6: "Six",
  7: "Seven",
  8: "Eight",
  9: "Nine",
  10: "Ten",
  11: "Jack", 
  12: "Queen", 
  13: "King"
}

def get_highest_valid(cards):
  total = 0
  ace_count = 0
  for card in cards:
    if not card.face_up:
      continue
    if card.value == 1:
      ace_count += 1
    else:
      if card.value > 10:
        total += 10
      else:
        total += card.value
  while(ace_count > 0):
    ace_count -= 1
    if total + ace_count <= 10:
      total += 11
    else:
      total += 1
  return total
    

class Card:
  SUITS = ["Hearts", "Clubs", "Diamonds", "Spades"]

  def __init__(self, value, suit, face_up=True):
    if suit not in Card.SUITS:
      print("boy, you got a big storm a commin.")
      return
    self.value = value
    self.suit = suit
    self.face_up = face_up

  def __eq__(self, value: int):
    return self.value == value

  def __add__(self, value: int):
    return self.value + value

  def to_string(self):
    if not self.face_up:
      return "[Face Down]"
    else:
      return "{} of {}".format(values[self.value], self.suit)

  def flip(self):
    self.face_up = not self.face_up


class Board:
  def __init__(self, player, num_of_decks = 1):
    self.deck = []
    for _ in range(num_of_decks):
      for value in range(1, 14):
        for suit in Card.SUITS:
          self.deck += [Card(value, suit)]
    random.shuffle(self.deck)
    self.pot = 0
    self.bets_placed = False
    self.field = []
    self.player = player
    self.hit_count = 0
  
  def deal(self, num_cards_to_deal = 1):
    card = self.deck.pop()
    print("You are dealt a {}.".format(card.to_string()))
    self.player.add_card(card)
    
    card = self.deck.pop()
    print("The dealer flips a {}.".format(card.to_string()))
    self.field.append(card)

    card = self.deck.pop()
    print("You are dealt a {}.".format(card.to_string()))
    self.player.add_card(card)
    
    card = self.deck.pop()
    card.flip()
    print("The dealer places a card face down.")
    self.field.append(card)
    print()
    if self.player.get_hand_value() == 21:
      self.field[-1].flip()
      print("The dealer flips a {}.".format(self.field[-1].to_string()))
      self.print_board()
      print()
      if self.get_field_value() == self.player.get_hand_value():
        print("Bets push.\n")
        self.player.pay(self.pot)
      else:
        print("Natural Blackjack! You win ${:.2f}\n".format(self.pot*2.5))
        self.player.pay(self.pot*2.5)
      self.reset()
      return False
    return True

  def hit(self) -> bool:
    print("You hit.")
    card = self.deck.pop()
    self.player.add_card(card)
    print("You are dealt a {} ({}).".format(card.to_string(), self.player.get_hand_value()))
    print()
    if self.player.get_hand_value() > 21:
      print("You bust.\n")
      self.reset()
      return False
    elif self.player.get_hand_value() == 21:
      if self.hit_count < 1:
        self.field[-1].flip()
        print("The dealer flips a {}.".format(self.field[-1].to_string()))
        self.print_board()
      if self.get_field_value() == self.player.get_hand_value():
        print("Bets push.\n")
        self.player.pay(self.pot)
      else:
        print("Blackjack! You win ${:.2f}\n".format(self.pot*2.5))
        self.player.pay(self.pot*2.5)
      self.reset()
      return False
    self.hit_count += 1
    if self.hit_count == 1:
      self.field[-1].flip()
      print("The dealer flips a {}.".format(self.field[-1].to_string()))
      self.print_board()
      while self.get_field_value() < 17:
        card = self.deck.pop()
        print("The dealer flips a {}.".format(card.to_string()))
        self.field.append(card)
        self.print_board()
      if self.get_field_value() > 21:
        print("The dealer busts. You win ${:.2f}\n".format(self.pot*2.0))
        self.player.pay(self.pot*2)
        self.reset()
        return False
    return True
  
  def stand(self):
    print("You stand.")
    if self.hit_count < 1:
      self.field[-1].flip()
      print("The dealer flips a {}.".format(self.field[-1].to_string()))
      self.print_board()
      while self.get_field_value() < 17:
        card = self.deck.pop()
        print("The dealer flips a {}.".format(card.to_string()))
        self.field.append(card)
        self.print_board()
      if self.get_field_value() > 21:
        print("The dealer busts. You win ${:.2f}\n".format(self.pot*2.0))
        self.player.pay(self.pot*2)
        self.reset()
        return
    if self.player.get_hand_value() > self.get_field_value():
      print("The hand is yours. You win ${:.2f}\n".format(self.pot*2.0))
      self.player.pay(self.pot*2)
      self.reset()
    elif self.player.get_hand_value() < self.get_field_value():
      print("Dealer wins.\n")
      self.reset()
    else:
      print("Bets push.\n")
      self.player.pay(self.pot)
      self.reset()
    return

  def get_field(self):
    out_string = ""
    for i in range(len(self.field)-1):
      out_string += "{}, ".format(self.field[i].to_string())
    out_string += "{}".format(self.field[-1].to_string())
    return out_string

  def get_field_value(self):
    return get_highest_valid(self.field)

  def print_board(self):
    print("Hand: {} ({})\nBoard: {} ({})".format(self.player.get_hand(), self.player.get_hand_value(), self.get_field(), self.get_field_value()))
    print()

  def reset(self):
    self.pot = 0
    self.field = []
    self.player.hand = []
    self.hit_count = 0


class Player:
  def __init__(self):
    self.hand = []
    self.wallet = 500

  def bet(self, amount: int, dealer: Board) -> bool:
    if amount > self.wallet:
      print("You don't have that kind of money!")
      print()
      return False
    else:
      self.wallet -= amount
      dealer.pot += amount
      dealer.bets_placed = True
      print()
      return True
  
  def add_card(self, card):
    self.hand.append(card)

  def get_hand(self):
    out_string = ""
    for i in range(len(self.hand)-1):
      out_string += "{}, ".format(self.hand[i].to_string())
    out_string += "{}".format(self.hand[-1].to_string())
    return out_string

  def get_hand_value(self):
    return get_highest_valid(self.hand)
  
  def pay(self, amount):
    self.wallet += amount


def main():
  player = Player()
  dealer = Board(player, 4)

  while(player.wallet > 0):
    print("You have ${:.2f} to play with.".format(player.wallet))
    while not dealer.bets_placed:
      player.bet(int(input("Place your bet: $")), dealer)

    cont = dealer.deal()
    while cont and player.get_hand_value() <= 21:
      dealer.print_board()
      in_string = input("Hit? [y/n]: ")
      if in_string != "y":
        dealer.stand()
        cont = False
      else:
        cont = dealer.hit()
    if player.get_hand_value() > 21:
      print("You bust.\n")
  
    dealer.bets_placed = False
  print("Y'outta money, my dude.")
  

main()