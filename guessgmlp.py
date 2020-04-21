import random   #for taking random ip
winning_num=random.randint(1,100)
guess=1  #  for count
num=input("enter a number")
num=int(num)
game_over=False
while not game_over:
    if(num==winning_num):
        print(f"you win and guessed in {guess} times")
        game_over=True
    else:
        if(num<winning_num):
            print("too low")
           
        else:
            print("too high")
        guess+=1
        num=input("guess again")
        num=int(num)


            