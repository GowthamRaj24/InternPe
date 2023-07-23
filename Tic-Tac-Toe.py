import random
import sys
import time
Bv = [" " for i in range(9)]
def print_Board():
    row1 = []
    row2 = []
    row3 = []
    print(f'|{Bv[0]} |{Bv[1]} |{Bv[2]} |')
    print('----------')
    print(f'|{Bv[3]} |{Bv[4]} |{Bv[5]} |')
    print('----------')
    print(f'|{Bv[6]} |{Bv[7]} |{Bv[8]} |')
def player_move():
    print("Player Move ('X'):\n")
    print("Enter your Choice(1-9): ")
    val = int(input())
    if val>=1 and val<=9:
        if Bv[val-1]!=" ":
            print("Value is already Occupied")
            player_move()
        else:
            Bv[val-1]='X'
    else:
        print("Entered input is invalid.")
        player_move()
def computer_move():
    time.sleep(1)
    print("")
    print("Its Computer Move ('O'): \n")
    a=[]
    for i in range(len(Bv)):
        if Bv[i]==" ":
            a.append(i)
    comp = random.choice(a)
    print(f'Computer Choose : {comp}')
    time.sleep(1)
    Bv[comp]='O'
def Victory():
    if (Bv[0]==Bv[1]==Bv[2]=='X' or Bv[3]==Bv[4]==Bv[5]=='X' or Bv[6]==Bv[7]==Bv[8]=='X'\
        or Bv[0]==Bv[3]==Bv[6]=='X' or Bv[1]==Bv[4]==Bv[7]=='X' or Bv[2]==Bv[5]==Bv[8]=='X'\
        or Bv[0]==Bv[4]==Bv[8]=='X' or Bv[6]==Bv[4]==Bv[2]=='X'):
        print("")
        print('Congratulations.....Player Wins!!!')
        sys.exit()
        
    elif (Bv[0]==Bv[1]==Bv[2]=='O' or Bv[3]==Bv[4]==Bv[5]=='O' or Bv[6]==Bv[7]==Bv[8]=='O'\
        or Bv[0]==Bv[3]==Bv[6]=='O' or Bv[1]==Bv[4]==Bv[7]=='O' or Bv[2]==Bv[5]==Bv[8]=='O'\
        or Bv[0]==Bv[4]==Bv[8]=='O' or Bv[6]==Bv[4]==Bv[2]=='O'):
        print('Computer Wins!!!.......You Lose')
        sys.exit()
    elif " " not in Bv:
        print("It's a Draw")
        sys.exit()
    else:
        pass
print_Board()

while True:
    player_move()
    print_Board()
    Victory()
    computer_move()
    print_Board()
    Victory()