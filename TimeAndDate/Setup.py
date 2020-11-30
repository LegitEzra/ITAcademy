import os
os.system("pip3 install ntplib")
os.system("pip3 install termcolor")
from termcolor import colored, cprint
cprint("\nSuccessfully Installed Required Libraries", "green")
question = input(colored("Would you like to update the date and time now? ", "red"))
if question.lower() == "yes" or question.lower() == "y":
    os.system("python3 ./TimeDate.py")
else:
    os.system("clear")
    cprint(":( \nOkay run TimeDate.py at any time to update the computers date and time with the server", "red")
