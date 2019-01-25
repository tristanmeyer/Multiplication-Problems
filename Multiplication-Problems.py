#Tristan Meyer
#Multiplication Problems
from random import randint

a = 0
for a in range(1000):
    if a < 5:
        
        ix = randint(1,10)
        iy = randint(1,10)
        x = str(ix)
        y = str(iy)
        answer = int(input("what is "+x+"*"+y+"? "))
        ranswer = ix*iy
        
        if ranswer != answer:
            print("Incorrect, the answer was",ranswer)
            print(a)

        if ranswer == answer:
            print("Correct!")
            a = a + 1 
            print(a)
            

