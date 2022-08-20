from colorama import Fore, init
from discord_webhook import DiscordEmbed, DiscordWebhook
import requests
import os
import colorama
import sys
import time
colorama.init()

# This is an Fake Image logger
# U can change code and make it ur own image logger to sell to people...

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter);sys.stdout.flush();time.sleep(0.05)

os.system('cls')
print(colorama.Fore.RED)
print_slow("Welcome to Image Logger Made By BlueWave!\n")
# Change Title if you want!

init()
os.system("title 𝙙 𝙄𝙢𝙖𝙜𝙚 𝙇𝙤𝙜𝙜𝙚𝙧")
os.system("cls")
print(f"""{Fore.BLUE}

  ▄▄▄▄     ██▓    █    ██  ▓█████ █     █░ ▄▄▄      ██▒   █▓ ▓█████
 ▓█████▄  ▓██▒    ██  ▓██▒ ▓█   ▀▓█░ █ ░█░▒████▄   ▓██░   █▒ ▓█   ▀
 ▒██▒ ▄██ ▒██░   ▓██  ▒██░ ▒███  ▒█░ █ ░█ ▒██  ▀█▄  ▓██  █▒░ ▒███  
 ▒██░█▀   ▒██░   ▓▓█  ░██░ ▒▓█  ▄░█░ █ ░█ ░██▄▄▄▄██  ▒██ █░░ ▒▓█  ▄
▒░▓█  ▀█▓▒░██████▒▒█████▓ ▒░▒████░░██▒██▓ ▒▓█   ▓██   ▒▀█░  ▒░▒████
░░▒▓███▀▒░░ ▒░▓  ░▒▓▒ ▒ ▒ ░░░ ▒░ ░ ▓░▒ ▒  ░▒▒   ▓▒█   ░ ▐░  ░░░ ▒░ 
░▒░▒   ░ ░░ ░ ▒  ░░▒░ ░ ░ ░ ░ ░    ▒ ░ ░  ░ ░   ▒▒    ░ ░░  ░ ░ ░  
  ░    ░    ░ ░   ░░░ ░ ░     ░    ░   ░    ░   ▒        ░      ░  
░ ░      ░    ░     ░     ░   ░      ░          ░        ░  ░   ░  

{Fore.BLUE}[Image Logger]{Fore.WHITE} made by Bluewave devs
""")
# Change Title if you want..

print(
    f"{Fore.BLUE}[1]{Fore.WHITE} Image Logger")
print(
    f"{Fore.BLUE}[2]{Fore.WHITE} Webhook Tester")


Termed = input(f"{Fore.WHITE}[>>] ")

if Termed == "1":
        menu = 1

if Termed == "2":
    menu = 2


if menu ==1:
  os.system("cls")
  print_slow(f"{Fore.WHITE}Welcome to Image Logger Tool! ")
  input("Click Enter to Continue! ")
  os.system("cls")
  image = input(f"{Fore.WHITE}Input Image: ")
  os.system("cls")
  TermedName = input(f"{Fore.WHITE}Input Logger File name: ")
  os.system("cls")
  Termedwebhook = input("input webhook: ")
  os.system("cls")
  print("loading...")
  time.sleep(2)
  os.system("cls")
  print("installing requirements...")
  time.sleep(2)
  os.system("cls")
  print(f"Turning {TermedName} into Image...")
  time.sleep(2)
  # This is just to make the image logger a bit more real!
  os.system('cls' if os.name == 'nt' else 'clear')
  print("loading...")
  time.sleep(2)
  os.system("cls")
  webhook = DiscordWebhook(url={Termedwebhook}, username="BlueWave",
  avatar_url="https://media.discordapp.net/attachments/1001266120323510374/1005533858390872064/dsl.gif?width=432&height=432",)
  embed = DiscordEmbed(title='BlueWave Logger', description='Your Image is here!', color='00d3ff')
  embed.set_footer(text='Image Logger made by ឵Blues#0001 | Join https://discord.gg/95nyjCdTG6',)
  embed.set_image(url=f'{image}', inline=False)
  webhook.add_embed(embed)
  response = webhook.execute()
  print(f"{Fore.GREEN}Your Image is done! ")
  time.sleep(1)
  print(F"{Fore.WHITE}Check ur Discord Channel! ")
  time.sleep(1)
  input(F"{Fore.WHITE}Click Enter to Exit: ")
  exit()

if menu ==2:
  os.system("cls")

webhook = input("input webhook: ")
print("loading...")
webhook = DiscordWebhook(url={webhook}, username="BlueWave Webhook",
avatar_url="https://media.discordapp.net/attachments/1001266120323510374/1005533858390872064/dsl.gif?width=432&height=432",)
embed = DiscordEmbed(title='BlueWave', description='Webhook Working!', color='00d3ff')
webhook.add_embed(embed)
response = webhook.execute()
input(f"{Fore.GREEN}Webhook is valid!")
os.system("cls")
input(f"{Fore.WHITE}Click enter to exit: ")
exit()