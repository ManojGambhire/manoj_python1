import random
import f1 as s

# compurter choice
print("comp turn:-  snake(s) water(w) or gun(g) ")
random=random.randint(1,3)
if random==1:
    comp='s'
elif random==2:
    comp='w'
elif random==3:
    comp='g'
# your choice
you=input("your turn:-  snake(s) water(w) or gun(g) :=   ")
a = s.game_win_lose(comp,you)

print(f"computer chose {comp}")
print(f"you chose {you}")

if (a==None):
    print("the game is tie\n")
elif(a==True):
    print("you win\n")
else:
    print("you lose\n") 

