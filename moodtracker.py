import os
import time
from datetime import date
from datetime import datetime

#creates the full file name so the program can find the mood text file from anywhere its run
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "mood_history.txt")


def view():
    #view mood logs so far
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if not lines:
                print('You have no saved moods.')
            else:
                for line in lines:
                    print(line.strip())
    except FileNotFoundError:
        print("No mood history file found yet.")    

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_help():
    print('''mood - enter your mood for today
view - shows you your logged moods so far
quit - quits the program
''')

def log_mood():
    date_today = date.today()
    formatted_date = date_today.strftime("%d-%m-%Y")
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    user_mood = input('How are you feeling today? ')
    while True:
        sure = input('Are you sure this is your current mood today? (Y/N)').lower().strip()
        if sure == 'y':
            print(f'You are feeling {user_mood} today, your mood has been saved to your history')
            with open(file_path, 'a', encoding='utf-8') as file:
                file.write(f'{formatted_date}, {hour}:{minute}: {user_mood}\n')
                break
        elif sure == 'n':
            print('You cancelled the operation.')
            break
        else:
            print('Please enter a valid input.')


print('This is your mood tracker. ')
print('Type "help" for a list of commands. "quit" to quit the program')


while True:
    user_command = input('> ').lower().strip() 
    if user_command == 'mood':
        log_mood()
    elif user_command == 'view':
        clear_screen()
        view()
    elif user_command == 'help':
        print_help()
    elif user_command == 'clear':
        clear_screen()   
    elif user_command == 'quit':
        print('Signing off, see you tomorrow!')
        time.sleep(3)
        break
    else:
        print('I do not understand that command, type "help" for help.')
