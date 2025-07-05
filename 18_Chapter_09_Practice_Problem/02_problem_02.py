import random

def gameFunc():
    print('You are Playing the Game !!')
    score  = random.randint(1,62)
    # Fetching the high Score from the file
    with open('02_highScore.txt') as f:
        highScore = f.read()
        if(highScore!=''):
            highScore=int(highScore)
        else:
            highScore=0
    print(f"Your score : {score}")
    if(score>highScore ):
        # write this new Score > highScore to the file 
        with open('02_highScore.txt','w') as f:
            f.write(str(score))
    return score


gameFunc()