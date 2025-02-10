# Andrea Diamantini
# ALPM Project

import subprocess
import sys
from importlib import resources

from alpm import config

#config = importlib.import_module('config')
# ---------------------------------------------------------------

def printHelp() -> None:
    file = resources.open_text("alpm", "alpm_help.txt")
    content = file.read()
    file.close()
    print(content)
    return

# ---------------------------------------------------------------

def printHelpCommand(command:str):
    print("help about", command)
    if command not in config.commands:
        print("Unknown command")
        return

    print(f"alpm {command} --->", " ".join(config.commands[command]))
    return

# ---------------------------------------------------------------

def run() -> int:
    commandList = sys.argv

    if len(commandList) <= 1:
        printHelp()
        return 1

    command = commandList[1]

    if command == "help":
        if len(commandList) == 2:
            printHelp()
            return 1

        printHelpCommand(commandList[2])
        return 2

    if command not in config.commands:
        printHelp()
        return 1

    pacmanCommand = config.commands[command]
    packages = commandList[2:]

    print("COMMAND:", command)
    print("PACMAN:", pacmanCommand)
    print("PACKAGE(s):", packages)

    subprocess.run( pacmanCommand + packages )
    return 0

if __name__ == '__main__':
    print("running main test...")
    run()
