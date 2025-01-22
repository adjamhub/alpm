# Andrea Diamantini
# ALPM Project

import config

import sys
import subprocess

def printHelp():
    file = open("alpm_help.txt","r")
    content = file.read()
    file.close()
    print(content)
    return

def printHelpCommand(command:str):
    print("help about", command)
    if command not in config.commands:
        print("Unknown command")
        return
    
    print(f"alpm {command} --->", " ".join(config.commands[command]))
    return
# ---------------------------------------------------------------

commandList = sys.argv

if len(commandList) <= 1:
    printHelp()
    exit(1)

command = commandList[1]

if command == "help":
    if len(commandList) == 2:
        printHelp()
    else:
        printHelpCommand(commandList[2])
    exit(2)
    
if command not in config.commands:
    printHelp()
    exit(1)

pacmanCommand = config.commands[command]
packages = commandList[2:]

print("COMMAND:", command)
print("PACMAN:", pacmanCommand)
print("PACKAGE(s):", packages)
    
subprocess.run( pacmanCommand + packages )
exit(0)
