# Lesson 3.1:
# Mini-Project: fill in the blank game

# Game has 3 or more levels and each level contains 4 or more blanks to fill in
# Immediately after running the program, user is prompted to select a difficulty level from easy / medium / hard

# Once a level is selected, game displays a fill-in-the-blank and a prompt to fill in the first blank.
#When player guesses correctly, new prompt shows with correct answer in the previous blank and a new prompt for the next blank
#
#When player guesses incorrectly, they are prompted to try again
#

# Your code here.


s1=["The bus stand is directly _________ the police station.",'behind']
s2=["As the doctor __________ into the room, the nurse handed him the temperature chart of the patient.The court _______ cognisance of the criminal's words.",'came','took']
s3=["The improvement made by changes in the system was ________ and did not warrant the large expenses.She takes delight _________ teasing boys.",'marginal','in']

def choose(n):
    if n==1:
        return s1
    elif n==2:
        return s2
    elif n==3:
        return s3

print("Enter the difficulty level from follows:\n 1.novice \n 2.Intermediate \n 3.Expert")
n=int(input())
if n>3 or n<1:
    print("choose correct level")
    exit()
s=choose(n)
if n>1:
    print(s[0])
    print("fill first blank")
    n1=input()
    n1.lower()
    while s[1]!=n1:
        print("Try Again")
        n1=input()
        n1.lower()
    print("Correct answer")
    print("fill Second blank")
    n1=input()
    n1.lower()
    while s[2]!=n1:
        print("Try Again")
        n1=input()
        n1.lower()
    print("Correct answer")
else:
    print(s[0])
    print("fill blank")
    n1=input()
    n1.lower()
    while s[1]!=n1:
        print("Try Again")
        n1=input()
        n1.lower()
    print("Correct answer")
    
    
