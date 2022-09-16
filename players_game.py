import random

# player class 
class Player:
  def __init__(self, player_name):
    self.name = player_name
    self.card = 0
    self.total_score = 0
  
# function 1
def get_num():
  return random.randint(0, 10)

# function 2
def compare(x, y):
  if x > y:
    return 1
  elif y > x:
    return 2
  else:
    return 0

# function 3 
def check_winner(p1: Player, p2: Player):
  if p1.total_score >= 15 or p2.total_score >= 15:
    if p1.total_score > p2.total_score:
      print()
      print(f"***** P1 {p1.name.upper()} WINS *****")
    else:
      print()
      print(f"***** P2 {p2.name.upper()} WINS *****")
    print(f"Score: P1:{p1.total_score}   P2:{p2.total_score}")

    return True
  else:
    return False

# helper functin to format and print scorecard
def print_score():
  print("--------------------")
  print(f"Round {round_num}")
  print("--------------------")

  print(f"Player 1 Draw: {p1.card}")
  print(f"Player 2 Draw: {p2.card}")
  print(f"Current Score: P1:{p1.total_score}   P2: {p2.total_score}")
  print()

# player object declaration
p1 = Player("Osama")
p2 = Player("Basit")

round_num = 0 # keeps track of current round

print("**** Battle of the Cards ****")
print(f"{p1.name}(P1) VS {p2.name}(P2)")

# main execution
while not check_winner(p1, p2):
  p1.card = get_num()
  p2.card = get_num() 
  
  difference = abs(p1.card - p2.card)
  
  if compare(p1.card, p2.card) == 1:
    p1.total_score += difference
  else:
    p2.total_score += difference
    
  print_score()
  round_num +=1
  
  
