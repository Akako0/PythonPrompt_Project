import os
import Extension.SpecialCommands as SC
from datetime import datetime
now = datetime.now()

def time ():
    SC.Command.Print(now.strftime('it is %H:%M:%S'))
    
def date ():
    SC.Command.Print(now.strftime('today is %d/%m/%Y'))

def clear ():
    try:
        os.system('cls')
    except:
        os.system('clear')

def help ():
    SC.Command.Print('commands:\n'+
                    'run extension_name :-run an .py extension\n'+
                    'time :- gives you the time\n'+
                    'date :- gives you the date\n'+
                    'clear :- clear the terminal\n'+
                    'help :- gives you a list of all docummented commands\n')