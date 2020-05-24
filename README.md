# Codeforces & AtCoder Parser

## Installation guide
1. Install **WSL** and **Ubuntu** as shown [here](https://docs.microsoft.com/en-us/windows/wsl/install-win10)
2. Install **Python 64-bit** from [here](https://www.python.org/downloads/windows/)
3. Install Python libraries *colorama*, *requests* and *pyperclip*
4. Install **Windows Terminal** from [here](https://aka.ms/terminal)
5. Open *main.py* and set `user`, `path_cf` and `path_atc` to your username, Codeforces path and AtCoder path, respectively.
6. Create a cf.cmd file and edit it to `python path`, where `path` is path to *main.py*
7. Add the folder with cf.cmd file to Windows PATH

## Run guide
1. Open Windows Terminal, type `cf` and hit enter
2. Enjoy, for help type `help`

## Issues
1. WSL currently enforces a stack limit of 8MB
