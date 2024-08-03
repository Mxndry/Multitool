import discord
from discord.ext import commands
import requests
import json
import urllib.request
import os
import sys
import random
import string
import base64
from colorama import Fore, init


init(autoreset=True)

R = Fore.RED
G = Fore.GREEN
Y = Fore.YELLOW
W = Fore.WHITE
PP = Fore.MAGENTA

def start():
    os.system('mode 120,28' if os.name == 'nt' else 'printf "\e[8;28;120t"')
    os.system("cls" if os.name == "nt" else "clear")
    print(f"""{PP}
                    _ _   _ _              _ 
                 | | | (_) |            | |
  _ __ ___  _   _| | |_ _| |_ ___   ___ | |
 | '_ ` _ \| | | | | __| | __/ _ \ / _ \| |
 | | | | | | |_| | | |_| | || (_) | (_) | |
 |_| |_| |_|\__,_|_|\__|_|\__\___/ \___/|_|
                                           
                                           
                   {R}[+] Created By Linho{PP}
  """)

def menu():
    while True:
        try:
            print(f"""
{PP}[1] {R}Check your IP info{W}
{PP}[2] {R}Check other IP info{W}
{PP}[3] {R}Trace IP with more details{W}
{PP}[4] {R}Webhook Info{W}
{PP}[5] {R}Server Lookup{W}
{PP}[7] {R}Message Deleter{W}
{PP}[8] {R}Token Info{W}
{PP}[9] {R}Emoji Scraper{W}
{PP}[10] {R}Mass Leave Servers{W}
{PP}[11] {R}Token Checker{W}
{PP}[12] {R}Password Gen{W}
{PP}[13] {R}Exit{W}
{PP}[14] {R}Token Fucker{W}
{PP}[15] {R}Token Bruteforce{W}
""")
            choice = int(input(f"{PP}[>] {W}"))
            if choice == 1:
                check_own_ip()
            elif choice == 2:
                check_ip()
            elif choice == 3:
                trace_ip()
            elif choice == 4:
                webhook_info()
            elif choice == 5:
                server_lookup()
            elif choice == 6:
                token_login()
            elif choice == 7:
                message_deleter()
            elif choice == 8:
                token_info()
            elif choice == 9:
                emoji_scraper()
            elif choice == 10:
                mass_leave_servers()
            elif choice == 11:
                token_checker()
            elif choice == 12:
                password_gen()
            elif choice == 13:
                print("Exit...")
                exit()
            elif choice == 14:
                token_fucker()
            elif choice == 15:
                token_bruteforce()
            else:
                print(f"{R}\nInvalid choice! Please try again{W}\n")
        except ValueError:
            print(f"{R}\nInvalid choice! Please try again{W}\n")

def check_own_ip():
    url = 'http://ip-api.com/json/'
    finder(url)

def check_ip():
    ip = input(f"\n{G}Enter IP Address/Website > {W}")
    if ip == "":
        print(f"{R}Enter a valid IP Address/website address!{W}")
        check_ip()
    else:
        url = f'http://ip-api.com/json/{ip}'
        finder(url)

def trace_ip():
    ip = input(f"\n{G}Enter IP Address/Website > {W}")
    if ip == "":
        print(f"{R}Enter a valid IP Address/website address!{W}")
        trace_ip()
    else:
        url = f'http://ip-api.com/json/{ip}'
        finder(url, detailed=True)

def finder(url, detailed=False):
    try:
        response = urllib.request.urlopen(url)
        data = json.load(response)
        if detailed:
            print(f"{G}[>] {R}IP Address{PP} [>] {W}{data['query']} {W}")
            print(f"{G}[>] {R}Org{PP}        [>] {W}{data['org']} {W}")
            print(f"{G}[>] {R}City{PP}       [>] {W}{data['city']} {W}")
            print(f"{G}[>] {R}Region{PP}     [>] {W}{data['regionName']} {W}")
            print(f"{G}[>] {R}Country{PP}    [>] {W}{data['country']} {W}")
            print(f"{G}[>] {R}Lattitude{PP}  [>] {W}{data['lat']} {W}")
            print(f"{G}[>] {R}Longitude{PP}  [>] {W}{data['lon']} {W}")
        else:
            print(f"{G}[>] {R}IP Address{PP} [>] {W}{data['query']} {W}")
            print(f"{G}[>] {R}Org{PP}        [>] {W}{data['org']} {W}")
            print(f"{G}[>] {R}City{PP}       [>] {W}{data['city']} {W}")
            print(f"{G}[>] {R}Region{PP}     [>] {W}{data['regionName']} {W}")
            print(f"{G}[>] {R}Country{PP}    [>] {W}{data['country']} {W}")
    except Exception as e:
        print(f"{R}[!] Error: {e}{W}")

def webhook_info():
    webhook_url = input(f"{G}Enter Webhook URL > {W}")
    try:
        response = requests.get(webhook_url)
        if response.status_code == 200:
            data = response.json()
            print(f"{G}[>] {R}Webhook ID{PP}    [>] {W}{data['id']} {W}")
            print(f"{G}[>] {R}Webhook Name{PP}  [>] {W}{data['name']} {W}")
            print(f"{G}[>] {R}Webhook Channel{PP} [>] {W}{data['channel_id']} {W}")
        else:
            print(f"{R}[!] Error: Could not retrieve webhook info.{W}")
    except Exception as e:
        print(f"{R}[!] Error: {e}{W}")

def server_lookup():
    server_id = input(f"{G}Enter Server ID > {W}")
    token = input(f"{G}Enter Token > {W}")
    headers = {
        'Authorization': f'Bot {token}'
    }
    url = f'https://discord.com/api/v10/guilds/{server_id}'
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            print(f"{G}[>] {R}Server Name{PP}    [>] {W}{data['name']} {W}")
            print(f"{G}[>] {R}Server ID{PP}      [>] {W}{data['id']} {W}")
            print(f"{G}[>] {R}Server Region{PP}  [>] {W}{data['region']} {W}")
            print(f"{G}[>] {R}Member Count{PP}   [>] {W}{data['member_count']} {W}")
        else:
            print(f"{R}[!] Error: Could not retrieve server info.{W}")
    except Exception as e:
        print(f"{R}[!] Error: {e}{W}")


def message_deleter():
    token = input(f"{G}Enter Token > {W}")
    channel_id = input(f"{G}Enter Channel ID > {W}")
    message_id = input(f"{G}Enter Message ID > {W}")
    headers = {
        'Authorization': f'Bot {token}'
    }
    url = f'https://discord.com/api/v10/channels/{channel_id}/messages/{message_id}'
    try:
        response = requests.delete(url, headers=headers)
        if response.status_code == 204:
            print(f"{G}[>] {R}Message Deleted{W}")
        else:
            print(f"{R}[!] Error: Could not delete message.{W}")
    except Exception as e:
        print(f"{R}[!] Error: {e}{W}")

def token_info():
    token = input(f"{G}Enter Token > {W}")
    headers = {
        'Authorization': f'Bot {token}'
    }
    url = 'https://discord.com/api/v10/users/@me'
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            print(f"{G}[>] {R}User ID{PP}        [>] {W}{data['id']} {W}")
            print(f"{G}[>] {R}Username{PP}      [>] {W}{data['username']}#{data['discriminator']} {W}")
            print(f"{G}[>] {R}Email{PP}         [>] {W}{data.get('email', 'No email found')} {W}")
            print(f"{G}[>] {R}Phone Number{PP}  [>] {W}{data.get('phone', 'No phone number found')} {W}")
        else:
            print(f"{R}[!] Error: Token is invalid or cannot access user info.{W}")
    except Exception as e:
        print(f"{R}[!] Error: {e}{W}")

def emoji_scraper():
    token = input(f"{G}Enter Token > {W}")
    server_id = input(f"{G}Enter Server ID > {W}")
    headers = {
        'Authorization': f'Bot {token}'
    }
    url = f'https://discord.com/api/v10/guilds/{server_id}/emojis'
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            emojis = response.json()
            for emoji in emojis:
                print(f"{G}[>] {R}Emoji Name{PP}    [>] {W}{emoji['name']} {W}")
                print(f"{G}[>] {R}Emoji ID{PP}      [>] {W}{emoji['id']} {W}")
        else:
            print(f"{R}[!] Error: Could not retrieve emojis.{W}")
    except Exception as e:
        print(f"{R}[!] Error: {e}{W}")

def mass_leave_servers():
    token = input(f"{G}Enter Token > {W}")
    headers = {
        'Authorization': f'Bot {token}'
    }
    url = 'https://discord.com/api/v10/users/@me/guilds'
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            servers = response.json()
            for server in servers:
                server_id = server['id']
                leave_url = f'https://discord.com/api/v10/users/@me/guilds/{server_id}'
                leave_response = requests.delete(leave_url, headers=headers)
                if leave_response.status_code == 204:
                    print(f"{G}[>] {R}Left Server ID {PP}[>] {W}{server_id}{W}")
                else:
                    print(f"{R}[!] Error: Could not leave server {W}{server_id}{W}")
        else:
            print(f"{R}[!] Error: Could not retrieve server list.{W}")
    except Exception as e:
        print(f"{R}[!] Error: {e}{W}")

def token_checker():
    token = input(f"{G}Enter Token > {W}")
    headers = {
        'Authorization': f'Bot {token}'
    }
    url = 'https://discord.com/api/v10/users/@me'
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print(f"{G}[>] {R}Token is valid!{W}")
        else:
            print(f"{R}[!] Token is invalid or expired.{W}")
    except Exception as e:
        print(f"{R}[!] Error: {e}{W}")

def password_gen():
    length = int(input(f"{G}Enter the length of the password > {W}"))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    print(f"{G}[>] {R}Generated Password{PP} [>] {W}{password}{W}")

def token_fucker():
    token = input(f"{G}Enter Token > {W}")
    headers = {
        'Authorization': f'Bot {token}'
    }
    url = 'https://discord.com/api/v10/users/@me'
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print(f"{G}[>] {R}Token Fucker no terminado{W}")
            # el token fucker no lo termino todavia jeje
        else:
            print(f"{R}[!] Token is invalid or cannot access user info.{W}")
    except Exception as e:
        print(f"{R}[!] Error: {e}{W}")

def token_bruteforce():
    user_id = input(f"{G}Enter user ID: {W}")
    if not user_id:
        print(f"{R}User ID cannot be empty!{W}")
        token_bruteforce()
        return

    base64_id = base64.b64encode(user_id.encode()).decode()
    print(f"{G}Base64 Encoded ID: {W}{base64_id}{W}")

if __name__ == "__main__":
    start()
    menu()
