import random
num=random.randint(0,50)
chances=5
while chances>0:
    a=int(input("Guess a number:  "))
    if a>num:
        chances=chances-1
        print("YOUR GUESSING NUMBER IS MORE THAN THE ACTUAL NUMBER","remaining chances==",chances)
    elif a<num:
        chances=chances-1
        print("YOUR GUESSING NUMBER IS LESS THAN THE ACTUAL NUMBER","remaining chances==",chances)
    else:
        print("*****************     CONGRATS     **********\nYOUR GUESSING NUMBER IS EQUAL TO THE ACTUAL NUMBER")
        break
else:
    print("BETTER LUCK NEXT TIME\nTHE ACTUAL NUMBER IS",num)
