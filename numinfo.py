"""
NumDex — numinfo.py
Author  : Faizi Mods
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
    colors = [
        Fore.RED,
        Fore.YELLOW,
        Fore.GREEN,
        Fore.CYAN,
        Fore.BLUE,
        Fore.MAGENTA
    ]
    for i, char in enumerate(text):
        print(colors[i % len(colors)] + char, end='', flush=True)
        time.sleep(0.002)
    print(Style.RESET_ALL)

def gradient_line():
    rainbow_print("━" * 50)

# ---------------- LOGO ----------------

def logo():
    type_print(" _   _ _   _ __  __ _____ _   _ _____ ___ ", Fore.GREEN)
    type_print("| \\ | | | | |  \\/  |_   _| \\ | |  ___/ _ \\", Fore.BLUE)
    type_print("|  \\| | | | | |\\/| | | | |  \\| | |_ | | | |", Fore.RED)
    type_print("| . ` | | | | |  | | | | | . ` |  _|| | | |", Fore.GREEN)
    type_print("| |\\  | |_| | |  | |_| |_| |\\  | |  | |_| |", Fore.BLUE)
    type_print("|_| \\_|\\___/|_|  |_|_____|_| \\_|_|   \\___/ ", Fore.BLUE)
    type_print("🔥 INFO TOOL v1.0 (Faizi Mods) 🔥", Fore.RED)

# ---------------- USER INFO ----------------

def show_user_info():
    try:
        import socket, urllib.request
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        public_ip = urllib.request.urlopen("https://api.ipify.org").read().decode()
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
        (Fore.BLUE, "━" * 45)
    ]

    for c, t in info:
        type_print(t, 0.01, c)

# ---------------- LOOKUP FUNCTION ----------------

def numinfo(mobile_number):
    try:
        session = requests.Session()

        headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 13)",
            "content-type": "application/x-www-form-urlencoded",
            "referer": "https://paksim.info/search.php",
            "origin": "https://paksim.info",
            "cookie": "agent=923319728307"
        }

        data = {
            "cnnum": mobile_number.strip()
        }

        response = session.post(
            "https://paksim.info/sim-database-online-2022-result.php",
            headers=headers,
            data=data,
            timeout=20
        )

        soup = BeautifulSoup(response.text, "html.parser")
        rows = soup.find_all("tr")

        if rows and len(rows) > 1:
            for tr in rows[1:]:
                tds = tr.find_all("td")
                if len(tds) >= 4:
                    type_print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", Fore.MAGENTA)
                    type_print(f"📞 Number  : {tds[0].text.strip()}", Fore.GREEN)
                    type_print(f"🧑 Name    : {tds[1].text.strip()}", Fore.BLUE)
                    type_print(f"🆔 CNIC    : {tds[2].text.strip()}", Fore.RED)
                    type_print(f"🏠 Address : {tds[3].text.strip()}", Fore.GREEN)
                    type_print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", Fore.MAGENTA)
            return

        type_print("❌ No Data Found / Cookie Expired", Fore.LIGHTRED_EX)

    except Exception as e:
        type_print(f"Error: {e}", Fore.RED)

# ---------------- MAIN ----------------

def main():
    clear_screen()
    logo()
    show_user_info()
    gradient_line()

    while True:
        ans = input("\nSearch data? (yes/no): ").strip().lower()
        if ans == "no":
            break
        elif ans == "yes":
            mobile = input("Enter Mobile/CNIC: ").strip()
            if mobile:
                numinfo(mobile)
        else:
            print("Sirf yes ya no likhein")

# ---------------- RUN ----------------

if __name__ == "__main__":
    main()
