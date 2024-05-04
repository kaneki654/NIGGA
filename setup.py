from os import system
import os
import sys
import random

def banner():
    class colors:
        cyan = "\033[1;36m"
        
    print(colors.cyan + u'\033[40m' + """
              ▄▄▄▄
            ▄██████     ▄▄▄█▄
          ▄██▀░░▀██▄    ████████▄
         ███░░░░░░██     █▀▀▀▀▀██▄▄
       ▄██▌░░░░░░░██    ▐▌       ▀█▄
       ███░░▐█░█▌░██    █▌         ▀▌
      ████░▐█▌░▐█▌██   ██
     ▐████░▐░░░░░▌██   █▌
      ████░░░██░░██▌  █▌
      ████░░░██░░██▌  █▌
      ████▌░▐█░░███   █
      ▐████░░▌░███   ██
      ████░░░███    █▌
    ██████▌░████   ██
  ▐████████████   ███
  █████████████▄████
  ██████████████████
  ██████████████████
  █████████████████▀
  █████████████████
  ████████████████
  ████████████████""")

menu = input("GUSTO MO BA TLGA GAMITIN TO?(y)es or (n)o: ")

if menu.lower() == 'y':
    banner()
    os.system("sudo apt install ngrok")
    os.system("pip install httpx")
    os.system("pip install http")
    os.system("pip install threading")
    os.system("pip install requests")
    os.system("pip install socketserver")
    os.system("pip install asyncio")
    os.system("pip install user_agent_parser")
    os.system("pip install logging")
    
    pass    

elif menu.lower() == 'n':
    os.system('clear')
    exit()
    
else:
    print("LAH MALI PAG TYPE")