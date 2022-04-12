import os
try:
    os.system('cls')
except:
    os.system('clear')

import LocalMod.SpecialCommands as SC
import LocalMod.Shell as Shell
running = True

while running:
    commandInput = SC.Command.Input("Akatools:\\>")
    command = Shell.get_command(commandInput)
    
    #if command is empty 
    if not command:
        continue
    
    Shell.process(command)