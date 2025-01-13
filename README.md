# alpm
Arch Linux Package Manager 

This is just an attempt, made for fun, to implement a basic pacman alternative with easy-to-remember (at least, for me) options.
It will become also an AUR helper.

Easier to understand when some examples are given:

$ actual pacman command + option ----> alpm command + option

$ sudo pacman -Syu        -----> alpm update
$ ------------------------------------------------------------
$ sudo pacman -S package  -----> alpm install package
$ sudo pacman -R package  -----> alpm remove package
$ sudo pacman -Rs package -----> alpm removedeps package
$ ------------------------------------------------------------
$ pacman -Ss string       -----> alpm search string
$ pacman -Qs string       -----> alpm local-search string
$ ------------------------------------------------------------
$ pacman -Si package      -----> alpm info package
$ pacman -Qi package      -----> alpm local-info package
$ ------------------------------------------------------------
$ pacman -Ql package      -----> alpm list-files package
$ ------------------------------------------------------------
$ pacman -Sl group        -----> alpm list-group group

These are the feature to implement for 0.1.0 version:
- commands listed above
- automatic sudo execution, given command
- AUR helper capabilities

I plan to implement it in Python, for now. Maybe I can RIIR :D
