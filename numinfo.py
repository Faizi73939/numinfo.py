"""
NumDex — numinfo.py
Repository: Faizi73939/Numinfo

Author / Coder Details (START — DO NOT REMOVE)
------------------------------------------------
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

# ---------------- LOGO ----------------

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
        (Fore.BLUE, f"🔧 CPU       : {platform.processor() or 'Unknown'}"),
        (Fore.RED, f"🌐 Local IP  : {local_ip}"),
        (Fore.GREEN, f"🌍 Public IP : {public_ip}"),
        (Fore.BLUE, f"📅 Date      : {time.strftime('%d-%m-%Y')}"),
        (Fore.RED, f"⏰ Time      : {time.strftime('%H:%M:%S')}"),
        (Fore.BLUE, "━" * 45)
    ]
    for c, t in info:
        type_print(t, 0.01, c)

# ---------------- CORE LOOKUP (NEW SITE) ----------------

def numinfo(mobile_number):
    try:
        session = requests.Session()

        headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Mobile Safari/537.36",
            "referer": "https://pamsim.info",
            "origin": "https://paksim.info/search.php/",
            "content-type": "application/x-www-form-urlencoded"
        }

        # form field commonly used on this site
        data = {
            "search": mobile_number.strip()
        }

        response = session.post(
            "https://paksim.info/sim-database-online-2022-result.php",
            headers=headers,
            data=data,
            allow_redirects=True,
            timeout=15
        )

        soup = BeautifulSoup(response.text, "html.parser")

        # Try to read table-based results
        rows = soup.find_all("tr")

        if rows and len(rows) > 1:
            for tr in rows[1:]:
                tds = tr.find_all("td")
                if len(tds) >= 4:
                    number = tds[0].get_text(strip=True)
                    name = tds[1].get_text(strip=True)
                    cnic = tds[2].get_text(strip=True)
                    address = tds[3].get_text(strip=True)

                    type_print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", color=Fore.MAGENTA)
                    type_print(f"[+] 📞 Number  : {number}", color=Fore.GREEN)
                    type_print(f"[+] 🧑 Name    : {name}", color=Fore.BLUE)
                    type_print(f"[+] 🆔 CNIC    : {cnic}", color=Fore.RED)
                    type_print(f"[+] 🏠 Address : {address}", color=Fore.GREEN)
                    type_print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", color=Fore.MAGENTA)
            return

        # Fallback: check page text for no-data message
        page_text = soup.get_text(" ", strip=True).lower()
        if "no data" in page_text or "not found" in page_text:
            type_print(f"[❌] No Data Found for: {mobile_number}", color=Fore.LIGHTRED_EX)
        else:
            type_print("[⚠] Data format changed or blocked by site.", color=Fore.YELLOW)

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
