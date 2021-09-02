import random
from datetime import datetime
today_date=datetime.now()

rules_willingness=input("If you want to know the rules enter Y and for not seeing press any key: ")
# This set of code is writeen for seeing the rules
if rules_willingness.lower()=='y':
    with open('rules.txt','r') as file1:
        for each_line in file1:
            print(each_line.strip('\n'))   #strip function removes trailing whitespaces from eachline

winners_list_willingness=input("If you want to see the list of the winners then enter Y else press any key: ")
# This set of code is writeen for seeing the list of winners
if winners_list_willingness.lower()=='y':
    with open('winners.txt','r') as file3:
        for each_line in file3:
            print(each_line.strip('\n'))

name=input('Enter player name : ')
number_of_times_game_to_be_played=int(input("How many times you would like to play? "))
_copy=number_of_times_game_to_be_played
a=0
b=0
c=0
#0 denotes stone                 these values are obtained by randint function below
#1 denotes paper
#2 denotes scissor
computer_value=random.randint(0,2)


while(_copy>0):
    #updating the value of n so that the loop terminates when n is less than zero
    _copy=_copy-1
    computer_value=random.randint(0,2)
    _value=input("Enter stone paper or scissor: ")
    human_value = _value.lower()

    if(computer_value==0):
        print("Computer choose stone")
        if(human_value=="paper"):
            print("You won this try")
            b=b+1
        elif (human_value == "stone"):
            print("Stone can't cut stone itself")
            c=c+1
        else:
            print("You lost this try")
            a=a+1


    if(computer_value==1):
        print("Computer choose paper")
        if (human_value == "scissor"):
            print("You won this try")
            b=b+1
        elif (human_value == "paper"):
            print("Paper cant cover paper")
            c=c+1
        else:
            print("You lost this try")
            a=a+1


    if(computer_value==2):
        print("Computer choose scissor")
        if(human_value=="stone"):
            print("You won this try")
            b=b+1
        elif (human_value == "scissor"):
            print("Scissor cant cut scissor")
            c = c + 1
        else:
            print("You lost this try")
            a=a+1


print("Tie between you and computer: ",c)
print(f'{name} won {b} times')
print(f'Computer won {a} times')

with open('winners.txt','a') as file2:
    if b>a:
        print(f"Final winner is {name}")
        file2.write('\n')
        file2.write(f'Winner was {name} at {today_date} with {name} winning {b} times out of {number_of_times_game_to_be_played} times')
    elif a==b:
        print(f'Tie btw {name} and computer')
        file2.write('\n')
        file2.write(f'Winner was {name} and computer i.e. tie at {today_date} with both winning {a} times out of {number_of_times_game_to_be_played} times')
    else:
        print('Final winner is Computer')
        file2.write('\n')
        file2.write(f'Winner was computer at {today_date} with computer winning {a} times out of {number_of_times_game_to_be_played} times')

