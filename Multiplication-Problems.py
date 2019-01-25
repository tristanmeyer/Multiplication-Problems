#Tristan Meyer
#Multiplication Problems
from random import randint

ix = randint(1,10)
iy = randint(1,10)
x = str(ix)
y = str(iy)

answer = int(input("what is "+x+"*"+y+"? "))
ranswer = ix*iy


if ranswer == answer:
    print("Correct!")
    
if ranswer != answer:
    print("Incorrect, the answer was",ranswer)
