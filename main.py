import random


def chooseCpu():
    # random number gen, pick 0-2, translate choice and return the number.
    options = [1, 2, 3]
    return random.choice(options)


if __name__ == '__main__':
    print("Welcome to RPS. First to 5 points wins!")
    uScore = 0
    cScore = 0

    while uScore <= 4 and cScore <= 4:
        u = int(input("Choose: \n1. Rock \n2. Paper \n3. Scissors\n"))
        comp = chooseCpu()
        if u == 1:
            print("User chose Rock")
            if comp == 1:
                print("Both players chose rock. It's a draw!")
            elif comp == 2:
                print("The Computer chose paper. Computer wins this hand!")
                cScore += 1
            else:
                print("The Computer chose Scissors. User wins this hand!")
                uScore += 1
        elif u == 2:
            print("User chose Paper")
            if comp == 1:
                print("The Computer chose rock. Computer wins this hand!")
                cScore += 1
            elif comp == 2:
                print("Both players chose paper. It's a draw!")
            else:
                print("The Computer chose rock. User wins this hand!")
                uScore += 1
        elif u == 3:
            print("User chose Scissors")
            if comp == 1:
                print("The Computer chose Rock. Computer wins this hand!")
                cScore += 1
            elif comp == 2:
                print("The Computer chose paper. User wins this hand!")
                uScore += 1
            else:
                print("Both players chose Scissors. It's a draw!")
        print(uScore)
        print(cScore)

    if uScore > cScore:
        print("Congratulations, you win!")
    else:
        print("The computer has won!")
