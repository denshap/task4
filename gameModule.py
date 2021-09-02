def guessNum():
    userNum=input("Enter the number:")
    import random
    if userNum.isdigit() and int(userNum)==random.randint(0,10): 
        print("Win")
    else:
        print("Try again")