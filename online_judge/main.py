import os
import sys
from source import task
from source import contest

def main():
    #path of repository
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    print('\n\n>>> Welcome to CPLIB!')

    is_correct_input = False
    while (not(is_correct_input)):
        contest_type = input('>>> Please enter the contest type: ')
        contest_number = input('>>> Please enter the contest number: ')
        proceed = input('>>> Is this correct? (y/n): ')
        is_correct_input = proceed == 'y' or proceed == 'Y'

    contest_instance = contest.Contest(path, contest_type, contest_number)
    
    tasklist = contest_instance.taskdict[contest_type]
    current_task = tasklist[0]
    
    while True:
        command = input('>>> ').split()
        if command[0] == 't':
            contest_instance.marge(current_task)
            contest_instance.test(current_task)
        
        elif command[0] == 'c':
            if command[1] in tasklist:
                current_task = command[1]
            else:
                print('>>> No such task')
        
        elif command[0] == 's':
            contest_instance.submit(current_task)
            
        elif command[0] == 'exit_from_this_contest':
            print('>>> Bye!')
            break
            
        else:
            print('>>> No such command')
            
    exit()
    
main()