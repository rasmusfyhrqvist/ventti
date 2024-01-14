import os, math, random

red = '\033[31m'
white = '\033[0m'
blue = '\033[38;5;17m'
yellow = '\033[38;5;214m'

class card:
  def __init__(self, id):
    self.suit = suits[math.floor(id/13)]
    self.value = (id%13)+1
    self.strValue = str(self.value).replace('11','J').replace('12','Q').replace('13','K').replace('1','A').replace('A0','10')
    self.group = (suits.index(self.suit)>1)
  
  def __str__(self):
    # Tulostetaan kortti
    color = (red if self.group else blue)
    return color+(self.suit+' '+self.strValue).ljust(4,' ')+white


suits = ('♠','♣','♥','♦')
deck = list(map(lambda i: card(i), list(range(52))))
random.shuffle(deck)


playerPoints = 0
computerPoints = 0

def getCardSum (cards):
  sum = 0
  for i in cards:
    sum += i.value
  return sum

def printCards (cards):
  os.system('clear')
  print('\n\n        Ventti\n\n')
  print('        Tilanne\n\n   Minä  '+str(computerPoints)+' - '+str(playerPoints)+'  Sinä\n\n')
  print("Sinun kortit:")
  i = 1
  for kortti in cards:
    print('Kortti '+str(i)+'. '+ str(kortti))
    i+=1
  
  summa = getCardSum(player)
  print('\nKorttien summa: '+str(summa))

  return summa

def newCard():
  uusiKortti = deck.pop()
  if uusiKortti.value == 1:
    if str(input('Haluatko ässän arvoksi 1 vai 14? ')) == "1":
      print('Ässän arvoksi valittu 1')
    else:
      print('Ässän arvoksi valittu 14')
      uusiKortti.value = 14
      uusiKortti.strValue = "14"
  return uusiKortti


while str(input('Haluatko pelata pelin Venttiä? (k/e) '))!='e':
  
  os.system('clear')
  print('Uusi peli: luodaan kortteja...\n\n')
  
  deck = list(map(lambda i: card(i), list(range(52))))
  random.shuffle(deck)
  
  # Pelaajan kortit
  player = [newCard(), newCard()]  
  while printCards(player)<21 and str(input('\nHaluatko uuden kortin? (k/e) '))=="k":
    player += [newCard()]

  # Tietokoneen kortit
  computer = [deck.pop()]
  while getCardSum(computer)<17:
    computer += [deck.pop()]

  
  print("\n\nMinun kortit:")
  i = 1
  for kortti in computer:
    print('Kortti '+str(i)+'. '+ str(kortti))
    i+=1
  
  summa = getCardSum(computer)
  print('\nKorttien summa: '+str(summa))

  computerSum = 21 - getCardSum(computer)
  playerSum = 21 - getCardSum(player)

  print(yellow)
  
  if playerSum<0:
    print('Voitin pelin')
    computerPoints += 1
  elif computerSum<0:
    print('Voitit pelin!')
    playerPoints += 1
  elif computerSum == playerSum:
    print('Tasapeli')
  elif computerSum>playerSum:
    print('Voitit pelin!')
    playerPoints += 1
  elif playerSum>computerSum:
    print('Voitin pelin')
    computerPoints += 1

  print(white+'\n\n')  