"""
NumDex — numinfo.py
Repository: Faizi73939/Numinfo

Author / Coder Details (START — DO NOT REMOVE)
------------------------------------------------
Important note for users:
If you use, modify, fork, or redistribute this file or code derived from it,
you MUST give clear credit to:

Author  : Faizi Mods
Handle  : Faizi Mods (Telegram)
Country : Pakistan 🇵🇰
Contact : +923706058550 (Whatsapp)
About   : Developer of NumDex — Mobile & CNIC Lookup tool
Date    : 2025-12-29
------------------------------------------------
"""

import requests
from bs4 import BeautifulSoup
import time
import os
import platform
import json
from colorama import Fore, Style, init

init(autoreset=True)

# ---------------- BASIC FUNCTIONS ----------------

def clear_screen():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def type_print(text, delay=0.003, color=Fore.WHITE):
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(delay)
    print(Style.RESET_ALL)

def rainbow_print(text):
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    for i, char in enumerate(text):
        print(colors[i % len(colors)] + char, end='', flush=True)
        time.sleep(0.002)
    print(Style.RESET_ALL)

def gradient_line():
    rainbow_print("━" * 50)

# ---------------- LOGO (MUST BE BEFORE main) ----------------

def logo():
    type_print(" _   _ _   _ __  __ _____ _   _ _____ ___ ", color=Fore.GREEN)
    type_print("| \\ | | | | |  \\/  |_   _| \\ | |  ___/ _ \\", color=Fore.BLUE)
    type_print("|  \\| | | | | |\\/| | | | |  \\| | |_ | | | |", color=Fore.RED)
    type_print("| . ` | | | | |  | | | | | . ` |  _|| | | |", color=Fore.GREEN)
    type_print("| |\\  | |_| | |  | |_| |_| |\\  | |  | |_| |", color=Fore.BLUE)
    type_print("|_| \\_|\\___/|_|  |_|_____|_| \\_|_|   \\___/ ", color=Fore.BLUE)
    type_print("🔥 INFO TOOL v1.0 (Developed by Faizi Mods) 🔥", color=Fore.RED)

# ---------------- USER INFO ----------------

def show_user_info():
    proc = platform.processor() or "Unknown"
    try:
        import socket, urllib.request
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        public_ip = urllib.request.urlopen("https://api.ipify.org").read().decode().strip()
    except:
        local_ip = public_ip = "Unknown"

    info = [
        (Fore.GREEN, "📱 Device Information"),
        (Fore.BLUE, "━" * 45),
        (Fore.RED, f"💻 OS        : {platform.system()}"),
        (Fore.GREEN, f"🖥 Machine   : {platform.machine()}"),
        (Fore.BLUE, f"🔧 CPU       : {proc}"),
        (Fore.RED, f"🌐 Local IP  : {local_ip}"),
        (Fore.GREEN, f"🌍 Public IP : {public_ip}"),
        (Fore.BLUE, f"📅 Date      : {time.strftime('%d-%m-%Y')}"),
        (Fore.RED, f"⏰ Time      : {time.strftime('%H:%M:%S')}"),
        (Fore.BLUE, "━" * 45)
    ]
    for c, t in info:
        type_print(t, 0.01, c)

# ---------------- CORE LOOKUP (ORIGINAL LOGIC RESTORED) ----------------

def numinfo(mobile_number):
    try:
        session = requests.Session()

        headers = {
            'authority': 'simownership.net',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://simownership.net',
            'referer': 'https://simownership.net',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Mobile Safari/537.36'
        }

        data = {
            'number': mobile_number.strip(),
            'search': ''
        }

        response = session.post(https://simownership.net",
            headers=headers,
            data=data,
            timeout=20
        )

        soup = BeautifulSoup(response.text, 'html.parser')
        rows = soup.find_all("tr")

        if len(rows) <= 1:
            type_print(f"[❌] No Data Found for: {mobile_number}", color=Fore.LIGHTRED_EX)
            return

        for tr in rows[1:]:
            tds = tr.find_all("td")
            if len(tds) >= 4:
                number, name, cnic, address = [td.text.strip() for td in tds[:4]]

                type_print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", color=Fore.MAGENTA)
                type_print(f"[+] 📞 Number  : {number}", color=Fore.GREEN)
                type_print(f"[+] 🧑 Name    : {name}", color=Fore.BLUE)
                type_print(f"[+] 🆔 CNIC    : {cnic}", color=Fore.RED)
                type_print(f"[+] 🏠 Address : {address}", color=Fore.GREEN)
                type_print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", color=Fore.MAGENTA)

    except Exception as e:
        type_print(f"[!] Error: {e}", color=Fore.RED)

# ---------------- MAIN ----------------

def main():
    clear_screen()
    logo()
    show_user_info()
    gradient_line()

    while True:
        ans = input(f"\n{Fore.CYAN}[❓] Search data? (yes/no): {Style.RESET_ALL}").strip().lower()
        if ans == "no":
            type_print("👋 Tool closed. Shukriya!", color=Fore.MAGENTA)
            break
        elif ans == "yes":
            mobile = input(f"{Fore.YELLOW}[📲] Enter Mobile/CNIC: {Style.RESET_ALL}").strip()
            if mobile:
                type_print("🔍 Searching...\n", color=Fore.YELLOW)
                numinfo(mobile)
            else:
                type_print("[⚠] Empty input!", color=Fore.LIGHTRED_EX)
        else:
            type_print("[⚠] Sirf yes ya no likhein.", color=Fore.LIGHTRED_EX)

# ---------------- RUN ----------------

if __name__ == "__main__":
    main()
