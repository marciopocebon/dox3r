#! usr/bin/python
# -*- coding: utf-8 -*-
import requests
import time
import os
import pylint 
from time import sleep
import warnings
from urllib3.exceptions import  InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)

os.system('clear')

class bcolors:
    Redd         = "\033[31m"
    Greenn        = "\033[32m"
    White        = "\033[97m"

''' RECHERCHE PAR PSEUDONYME '''
username = input('\033[92m[✓] Entrer le pseudonyme : ')


# INSTAGRAM
instagram = f'https://www.instagram.com/{username}'

# FACEBOOK
facebook = f'https://www.facebook.com/{username}'

#TWITTER
twitter = f'https://www.twitter.com/{username}'

# YOUTUBE
youtube = f'https://www.youtube.com/{username}'

# GOOGLE+
google_plus = f'https://plus.google.com/s/{username}/top'

# REDDIT
reddit = f'https://www.reddit.com/user/{username}'

# WORDPRESS
wordpress = f'https://{username}.wordpress.com'

# PINTEREST
pinterest = f'https://www.pinterest.com/{username}'

# GITHUB
github = f'https://www.github.com/{username}'

# STEAM
steam = f'https://steamcommunity.com/id/{username}'

# IMGUR
imgur = f'https://imgur.com/user/{username}'

# SPOTIFY
spotify = f'https://open.spotify.com/user/{username}'

# BADOO
badoo = f'https://www.badoo.com/en/{username}'

# DAILYMOTION
dailymotion = f'https://www.dailymotion.com/{username}'

# KEYBASE
keybase = f'https://keybase.io/{username}'

# PASTEBIN
pastebin = f'https://pastebin.com/u/{username}'

# ROBLOX
roblox = f'https://www.roblox.com/user.aspx?username={username}'

# TRIPADVISOR
tripadvisor = f'https://tripadvisor.com/members/{username}'

# WIKIPEDIA
wikipedia = f'https://www.wikipedia.org/wiki/User:{username}'

# HACKERNEWS
hackernews = f'https://news.ycombinator.com/user?id={username}'

# EBAY
ebay = f'https://www.ebay.com/usr/{username}'


''' WEBSITE LIST - USE FOR SEARCHING OF USERNAME '''
WEBSITES = [
instagram, facebook, twitter, youtube, google_plus, reddit,
wordpress, pinterest, github, steam, imgur, spotify,
badoo, dailymotion, keybase, pastebin, roblox, 
tripadvisor, wikipedia, hackernews, ebay,
]


''' FONCTION COULEUR '''
def outer_func(colour):
    def inner_function(msg):
        print(f'{colour}{msg}')
    return inner_function


''' COULEUR PRINT '''
GREEN = outer_func('\033[92m')
YELLOW = outer_func('\033[93m')
RED = outer_func('\033[31m')
PURPLE =    outer_func('\033[95m')
DarkGray = outer_func('\033[90m')

''' BANNER '''
def banner():
    print(bcolors.Redd + 
"""

▓█████▄  ▒█████  ▒██   ██▒▓█████  ██▀███  
▒██▀ ██▌▒██▒  ██▒▒▒ █ █ ▒░▓█   ▀ ▓██ ▒ ██▒
░██   █▌▒██░  ██▒░░  █   ░▒███   ▓██ ░▄█ ▒
░▓█▄   ▌▒██   ██░ ░ █ █ ▒ ▒▓█  ▄ ▒██▀▀█▄  
░▒████▓ ░ ████▓▒░▒██▒ ▒██▒░▒████▒░██▓ ▒██▒
 ▒▒▓  ▒ ░ ▒░▒░▒░ ▒▒ ░ ░▓ ░░░ ▒░ ░░ ▒▓ ░▒▓░
 ░ ▒  ▒   ░ ▒ ▒░ ░░   ░▒ ░ ░ ░  ░  ░▒ ░ ▒░
 ░ ░  ░ ░ ░ ░ ▒   ░    ░     ░     ░░   ░ 
   ░        ░ ░   ░    ░     ░  ░   ░     
 ░                                        
                                                                        
        \033[33m DOX3R outil de recherche avancée \033[33m  
        \033[33m Developpeur : \032 https://github.com/haisenberg 
        """)

def search():
    RED(f'[✓] Votre analyse à bien était envoyée sur :{username}')
    time.sleep(0.5)
    print('[✓] Analyse en cours veuillez patienter...')
    time.sleep(0.5)

    time.sleep(3)

    count = 0
    match = True 
    for url in WEBSITES:
        r = requests.get(url)

        if r.status_code == 200:
            if match == True:
                GREEN('[✓] Information trouvée !')
                match = False
            PURPLE(f'\n{url} - {r.status_code} - [✓]')
            if username in r.text:
                GREEN(f'[DOX3R] TROUVER: Username:{username} - utilisateur trouver dans ce site web ')
            else:
                GREEN(f'[DOX3R] INTROUVABLE: Username:{username} - \033[91m Utilisateur introuvable')

    print(bcolors.Redd + 'Fin de la recherche de DOX3R...')



if __name__=='__main__':
    banner()
    search()
