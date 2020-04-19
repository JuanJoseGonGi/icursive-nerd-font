#!/usr/bin/env python
"""
iCursive Nerd Font Patcher
"""

import os
from subprocess import call
from shutil import copyfile, move
from glob import glob
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
    if style == "Op":  # {{{
        copyfile(font_path, "./Operator Mono Book Italic.otf")
        # patch ligatures
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
        copyfile("Operator Mono Book Italic.otf",
                 "nerd-fonts/Operator Mono Book Italic.otf")
        os.chdir("nerd-fonts")
        call([
            "python", "font-patcher", "--mono", "-w", "-c", "-ext", "ttf",
            r"Operator Mono Book Italic.otf"
        ])
        for file in glob("Operator*Windows Compatible.ttf"):
            move(file, "../Operator Mono Book Italic.ttf")
        os.remove("Operator Mono Book Italic.otf")
        os.remove("../Operator Mono Book Italic.otf")
        os.chdir(os.popen("git rev-parse --show-toplevel").read().rstrip("\n"))
        # }}}
    elif style == "Dk":  # {{{
        copyfile(font_path, "Dank Mono Italic.ttf")
        # patch nerd font symbols
        print("\n" + BYELLOW + "==>" + NC + " " + BGREEN +
              "Patching nerd font symbols..." + NC + "\n")
        move("Dank Mono Italic.ttf", "nerd-fonts/Dank Mono Italic.ttf")
        os.chdir("nerd-fonts")
        call([
            "python", "font-patcher", "--mono", "-w", "-c", "-ext", "ttf",
            r"Dank Mono Italic.ttf"
        ])
        for file in glob("Dank*Windows Compatible.ttf"):
            move(file, "../Dank Mono Italic.ttf")
        os.remove("Dank Mono Italic.ttf")
        os.chdir(os.popen("git rev-parse --show-toplevel").read().rstrip("\n"))
        # }}}
    elif style == "Cg":  # {{{
        copyfile(font_path, "Cartograph Italic.ttf")
        # patch nerd font symbols
        print("\n" + BYELLOW + "==>" + NC + " " + BGREEN +
              "Patching nerd font symbols..." + NC + "\n")
        move("Cartograph Italic.ttf", "nerd-fonts/Cartograph Italic.ttf")
        os.chdir("nerd-fonts")
        call([
            "python", "font-patcher", "--mono", "-w", "-c", "-ext", "ttf",
            r"Cartograph Italic.ttf"
        ])
        for file in glob("*artograp*Windows Compatible.ttf"):
            move(file, "../Cartograph Italic.ttf")
        os.remove("Cartograph Italic.ttf")
        os.chdir(os.popen("git rev-parse --show-toplevel").read().rstrip("\n"))
        # }}}


general("Cg",
        "/home/sainnhe/.local/share/fonts/Cartograph Mono Regular Italic.ttf")
