# Andrea Diamantini
# ALPM Project

import sys
import subprocess

commandList = sys.argv

if len(commandList) <= 1:
    print("alpm")
    exit(1)
    
if len(commandList) > 3:
    print("alpm cannot yet manage more than one package/instruction at time")
    print("Sorry for the inconvenience")
    exit(3)
    
command = commandList[1]

if len(commandList) == 2:
    if command != "update":
        print("alpm")
        exit(1)
    
    # execute 'sudo pacman -Syu'
    subprocess.run( ["sudo", "pacman", "-Syu"] )
    exit(0)

if command not in ("install","remove","removedeps","search","local-search","info","local-info","list-files","list-group"):
    print("aaaalllppppmmm")
    exit(1)

package = commandList[2]
print("COMMAND:", command)
print("PACKAGE:", package)

if command == "install":
    # execute 'sudo pacman -S package'
    subprocess.run( ["sudo", "pacman", "-S", package] )
    exit(0)
    
if command == "remove":
    # execute 'sudo pacman -R package'
    subprocess.run( ["sudo", "pacman", "-R", package] )
    exit(0)

if command == "removedeps":
    # execute 'sudo pacman -Rs package'
    subprocess.run( ["sudo", "pacman", "-Rs", package] )
    exit(0)

if command == "search":
    # execute 'pacman -Ss package'
    subprocess.run( ["pacman", "-Ss", package] )
    exit(0)

if command == "local-search":
    # execute 'pacman -Qs package'
    subprocess.run( ["pacman", "-Qs", package] )
    exit(0)

if command == "info":
    # execute 'pacman -Si package'
    subprocess.run( ["pacman", "-Si", package] )
    exit(0)

if command == "local-info":
    # execute 'pacman -Qi package'
    subprocess.run( ["pacman", "-Qi", package] )
    exit(0)

if command == "list-files":
    # execute 'pacman -Ql package'
    subprocess.run( ["pacman", "-Ql", package] )
    exit(0)

if command == "list-group":
    # execute 'pacman -Sl package'
    subprocess.run( ["pacman", "-Sl", package] )
    exit(0)

