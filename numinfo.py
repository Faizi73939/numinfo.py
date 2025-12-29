"""
Numinfo — numinfo.py
Repository: Faizi73939/Numinfo
Commit: f1a4480f8de36f80a01b6022f0d10dd21344a36e

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

# ---------------- UTILS ----------------

def clear_screen():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def type_print(text, delay=0.004, color=Fore.WHITE):
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

# ---------------- LOGO ----------------
# (IMPORTANT: logo() MUST be defined BEFORE main)

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
        local_ip = "Unknown"
        public_ip = "Unknown"

    info_lines = [
        (Fore.GREEN, "📱 Device Information"),
        (Fore.BLUE, "━" * 45),
        (Fore.RED, f"💻 OS        : {platform.system()}"),
        (Fore.GREEN, f"🖥 Machine   : {platform.machine()}"),
        (Fore.BLUE, f"🔧 CPU       : {proc}"),
        (Fore.RED, f"🌐 Local IP  : {local_ip}"),
        (Fore.GREEN, f"🌍 Public IP : {public_ip}"),
        (Fore.BLUE, f"⏰ Time      : {time.strftime('%H:%M:%S')}"),
        (Fore.RED, f"📅 Date      : {time.strftime('%d-%m-%Y')}"),
        (Fore.BLUE, "━" * 45)
    ]
    for color, line in info_lines:
        type_print(line, delay=0.01, color=color)

# ---------------- CORE FUNCTION ----------------

def numinfo(mobile_number):
    try:
        session = requests.Session()
        headers = {
            'user-agent': 'Mozilla/5.0 (Android)',
            'content-type': 'application/x-www-form-urlencoded'
        }
        data = {'number': mobile_number, 'search': ''}

        response = session.post(
            "https://freshsimownerdetails.com/SecureInfo.php",
            headers=headers,
            data=data,
            timeout=15
        )

        soup = BeautifulSoup(response.text, 'html.parser')
        rows = soup.find_all("tr")

        if len(rows) <= 1:
            type_print(f"[❌] No Data Found for: {mobile_number}", color=Fore.RED)
            return

        for tr in rows[1:]:
            tds = tr.find_all("td")
            if len(tds) >= 4:
                number, name, cnic, address = [td.text.strip() for td in tds[:4]]
                type_print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", color=Fore.MAGENTA)
                type_print(f"[+] 📞 Number  : {number}", color=Fore.GREEN)
                type_print(f"[+] 🧑 Name    : {name}", color=Fore.BLUE)
                type_print(f"[+] 🆔 CNIC    : {cnic}", color=Fore.RED)
                type_print(f"[+] 🏠 Address : {address}", color=Fore.GREEN)
                type_print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", color=Fore.MAGENTA)

    except Exception as e:
        type_print(f"[!] Error: {e}", color=Fore.RED)

# ---------------- MAIN ----------------

def main():
    clear_screen()
    logo()
    show_user_info()
    gradient_line()

    while True:
        ans = input(f"\n{Fore.CYAN}[?] Search data? (yes/no): {Style.RESET_ALL}").strip().lower()
        if ans == "no":
            type_print("👋 Tool closed. Shukriya!", color=Fore.MAGENTA)
            break
        elif ans == "yes":
            mobile = input(f"{Fore.YELLOW}[+] Enter Mobile/CNIC: {Style.RESET_ALL}").strip()
            if mobile:
                type_print("🔍 Searching...\n", color=Fore.YELLOW)
                numinfo(mobile)
            else:
                type_print("[!] Empty input!", color=Fore.RED)
        else:
            type_print("[!] Sirf yes ya no likhein.", color=Fore.RED)

# ---------------- RUN ----------------

if __name__ == "__main__":
    main()
