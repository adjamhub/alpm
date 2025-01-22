# Andrea Diamantini
# ALPM Project

commands = {
    "update"       : ["sudo", "pacman","-Syu"],
    "install"      : ["sudo", "pacman","-S"],
    "remove"       : ["sudo", "pacman","-R"],
    "removedeps"   : ["sudo", "pacman","-Rs"],
    "search"       : ["pacman", "-Ss"],
    "local-search" : ["pacman","-Qs"],
    "info"         : ["pacman","-Si"],
    "local-info"   : ["pacman","-Qi"],
    "list-files"   : ["pacman","-Ql"],
    "list-group"   : ["pacman","-Sl"]
    }