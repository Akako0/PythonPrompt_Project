#colors to make the terminal nicer
class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#make new function for nicer terminal

class Machinery ():
    def Upper (content):
        return content[0].upper()+ content[1:]

    def Print(color, content, end='\n'):
        print(color+ Machinery.Upper(content) +Bcolors.ENDC ,end)

class Command ():
    def Input (content, end=''):
        return input(Bcolors.HEADER+ Machinery.Upper(content) +Bcolors.ENDC+ end)

    def Print (content, end='\n'):
        Machinery.Print(Bcolors.OKCYAN, content, end=end)

    def Warning (content, end='\n'):
        Machinery.Print(Bcolors.WARNING, content , end=end)

    def Quit (content):
        Machinery.Print(Bcolors.FAIL, content)
        quit()
        
class Debug ():
    def Print(color, content, end='\n'):
        Machinery.Print(color, content, end)