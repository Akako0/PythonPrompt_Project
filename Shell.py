import os
import Extension.SpecialCommands as SC
import Utilities as Uts
from importlib.machinery import SourceFileLoader

def get_command (command_plus_args):
    commands = []
    for i in command_plus_args.split():
        commands.append(i)
    return commands

def process(command):
    proc = command[0].lower()
    
    if proc == 'exit':
        SC.Command.Quit('see ya !')
        
    elif proc == 'run':
        if len(command) > 1:
            execute(command[1:])
        else:
            SC.Command.Warning(f'run take at least one arguments ( {len(command - 1)} given)')
        
    elif proc == 'clear':
        Uts.clear()

    elif proc == 'time':
        Uts.time()
        
    elif proc == 'date':
        Uts.date()
    
    elif proc == 'help':
        Uts.help()
#this is a comment, it is the only one you will see on this code... sad for u :)
    else:
        SC.Command.Warning(f'no command named {proc} found')
def execute (extension):
    
    for _, _, files in os.walk("./Pyextensions/"):
        files = [ fi for fi in files if fi.endswith(".py") ]
        
        for i in files:
            if extension[0] == i[:-3]:
                try:
                    foo = SourceFileLoader('foo','./Pyextensions/'+i).load_module()
                except Exception as E:
                    SC.Command.Warning(f'error while importing {extension[0]}: ERROR: {E}')
                    return
                SC.Command.Print(f'{extension[0]} running ...')
                try:
                    foo.main(extension[1:])
                except Exception as E:
                    SC.Command.Warning(f'error while ruuning main() function in {extension[0]}: ERROR: {E}')
                return
    SC.Command.Warning(f'no extension found with the name {extension[0]}')