#!/usr/bin/env python

import os
from subprocess import call
from shutil import copyfile, move
from platform import system

# {{{Initialization
RED = "\033[0;31m"
BRED = "\033[1;31m"
GREEN = "\033[0;32m"
BGREEN = "\033[1;32m"
YELLOW = "\033[0;33m"
BYELLOW = "\033[1;33m"
BLUE = "\033[0;34m"
BBLUE = "\033[1;34m"
NC = "\033[0m"
os.chdir(os.popen("git rev-parse --show-toplevel").read().rstrip("\n"))


# }}}
def general(style, font_path):
    """
    general setup for all styles
    """
    os.chdir(".cache")
    if style == "Op":
        # patch ligatures
        copyfile(font_path, "./Operator Mono Book Italic.otf")
        print("\n" + BYELLOW + "==>" + NC + " " + BGREEN +
              "Patching ligatures..." + NC + "\n")
        os.chdir("operator-mono-lig")
        move("../Operator Mono Book Italic.otf",
             "./original/OperatorMono-BookItalic.otf")
        call(["npm", "install"])
        if system() == "Windows":
            os.system(os.path.abspath("build.bat"))
        else:
            call(["sh", "build.sh"])
        copyfile("./build/OperatorMonoLig-BookItalic.otf",
                 "../Operator Mono Book Italic.otf")
        os.chdir("..")
        # patch nerd font symbols
        print("\n" + BYELLOW + "==>" + NC + " " + BGREEN +
              "Patching nerd font symbols..." + NC + "\n")


general("Op", "/home/sainnhe/.local/share/fonts/Operator Mono Book Italic.otf")
