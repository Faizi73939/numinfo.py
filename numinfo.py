"""
NUMINFO — SIM & CNIC Lookup Tool
Author : Faizi Mods
"""

import requests
import time
import os
import platform
import random
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

# ================= CONFIG =================

WIDTH = 70
TYPE_SPEED = 0.01

API_URL = "https://livetracker.net.pk/wp-admin/admin-ajax.php"
NONCE = "fb638b05b4"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Linux; Android)",
    "Accept": "*/*",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Referer": "https://livetracker.net.pk/",
    "Origin": "https://livetracker.net.pk"
}

QUOTES = [
    "Information is power — use it wisely.",
    "Knowledge without ethics is dangerous.",
    "Powerful tools demand disciplined users.",
    "Think before you act, data never lies.",
    "Your intention defines the outcome."
]

# ================= BASIC UI =================

def clear():
    os.system("cls" if platform.system() == "Windows" else "clear")

def line(char="─", color=Fore.CYAN):
    print(color + char * WIDTH + Style.RESET_ALL)

def slow_print(text, color=Fore.WHITE, delay=TYPE_SPEED, center=False):
    if center:
        text = text.center(WIDTH)
    for ch in str(text):
        print(color + ch, end="", flush=True)
        time.sleep(delay)
    print(Style.RESET_ALL)

def colored_input(text, color):
    return input(color + text + Style.RESET_ALL)

# ================= ROBOT BEEP =================

def robot_beep(text, speed=0.05, color=Fore.LIGHTGREEN_EX):
    print(color, end="", flush=True)
    for ch in text:
        print(ch, end="", flush=True)
        if ch.isalnum():
            print("\a", end="", flush=True)
        time.sleep(speed)
    print(Style.RESET_ALL)

# ================= NUMINFO ASCII LOGO =================

def ascii_logo():
    clear()
    logo = [
        "███╗   ██╗██╗   ██╗███╗   ███╗██╗███╗   ██╗███████╗ ██████╗ ",
        "████╗  ██║██║   ██║████╗ ████║██║████╗  ██║██╔════╝██╔═══██╗",
        "██╔██╗ ██║██║   ██║██╔████╔██║██║██╔██╗ ██║█████╗  ██║   ██║",
        "██║╚██╗██║██║   ██║██║╚██╔╝██║██║██║╚██╗██║██╔══╝  ██║   ██║",
        "██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║██║ ╚████║██║     ╚██████╔╝",
        "╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ "
    ]
    for l in logo:
        slow_print(l, Fore.CYAN)

    slow_print("NUMINFO TOOL", Fore.MAGENTA, center=True)
    line("═", Fore.MAGENTA)
    robot_beep("Welcome to Faizi Mods Tool", 0.04)
    line("═", Fore.MAGENTA)

# ================= QUOTE + DATE TIME =================

def show_quote_datetime():
    now = datetime.now()
    slow_print(f"💬 Quote : {random.choice(QUOTES)}", Fore.YELLOW, center=True)
    slow_print(f"📅 Day   : {now.strftime('%A')}", Fore.CYAN, center=True)
    slow_print(f"📆 Date  : {now.strftime('%d %B %Y')}", Fore.CYAN, center=True)
    slow_print(f"⏰ Time  : {now.strftime('%I:%M:%S %p')}", Fore.CYAN, center=True)
    line("═", Fore.GREEN)

# ================= DEVELOPER DETAILS =================

def developer_details():
    slow_print("👨‍💻 DEVELOPER DETAILS", Fore.GREEN, center=True)
    line("─", Fore.GREEN)

    slow_print("🧑 Developer Name   : Faizan Rajpoot", Fore.CYAN)
    slow_print("⚙️ Developer Status : Broken", Fore.RED)
    slow_print("📞 Developer WP     : 03706058550", Fore.GREEN)
    slow_print("📢 Channel Name     : Faizi Mods", Fore.BLUE)
    slow_print("❤️ Favorite Anime   : Itachi Uchiha", Fore.MAGENTA)

    line("═", Fore.GREEN)

# ================= DEVICE DETAILS =================

def device_details():
    slow_print("📱 DEVICE DETAILS", Fore.YELLOW, center=True)
    line("─", Fore.YELLOW)

    slow_print(f"💻 OS        : {platform.system()} {platform.release()}", Fore.CYAN)
    slow_print(f"🧠 Machine   : {platform.machine()}", Fore.CYAN)
    slow_print(f"🧩 Processor : {platform.processor() or 'Unknown'}", Fore.CYAN)

    line("═", Fore.YELLOW)

# ================= WARNING =================

def warning():
    print(Fore.RED + "!" * WIDTH)
    slow_print("⚠️ Do not use this tool for illegal or wrong purposes.", Fore.YELLOW, center=True)
    slow_print("You are responsible for your own actions.", Fore.YELLOW, center=True)
    print(Fore.RED + "!" * WIDTH)
    time.sleep(1)

# ================= NUMINFO SEARCH =================

def numinfo(query):
    robot_beep("Searching details please wait", 0.04, Fore.CYAN)
    line("─", Fore.CYAN)

    payload = {
        "action": "fetch_simdata",
        "nonce": NONCE,
        "track": query.strip()
    }

    try:
        r = requests.post(API_URL, headers=HEADERS, data=payload, timeout=20)
        res = r.json()
    except:
        robot_beep("Network error occurred", 0.05, Fore.RED)
        return

    if not res.get("success"):
        robot_beep("No record found", 0.05, Fore.RED)
        return

    records = res.get("data", {}).get("Mobile", [])
    if not records:
        robot_beep("No SIM data available", 0.05, Fore.RED)
        return

    warning()
    line("═", Fore.MAGENTA)

    for i, rec in enumerate(records, 1):
        robot_beep(f"Record {i} Found", 0.04, Fore.LIGHTYELLOW_EX)
        line("─", Fore.MAGENTA)

        slow_print(f"👤 Name     : {rec.get('Name','N/A')}", Fore.GREEN)
        slow_print(f"🆔 CNIC     : {rec.get('CNIC','N/A')}", Fore.GREEN)
        slow_print(f"📞 Mobile   : {rec.get('Mobile','N/A')}", Fore.GREEN)
        slow_print(f"🏠 Address  : {rec.get('Address','N/A')}", Fore.GREEN)

        line("═", Fore.MAGENTA)

# ================= EXIT (COLOR ONLY) =================

def exit_msg():
    line("═", Fore.MAGENTA)
    robot_beep("Thanks for using NUMINFO Tool", 0.04, Fore.GREEN)
    slow_print("📢 Join Telegram Channel : Faizi Mods", Fore.BLUE, center=True)
    slow_print("🤝 Developed by Faizan Rajpoot", Fore.CYAN, center=True)
    slow_print("👋 Allah Hafiz — Tool Closed", Fore.YELLOW, center=True)
    line("═", Fore.MAGENTA)

# ================= MAIN =================

def main():
    ascii_logo()
    show_quote_datetime()
    developer_details()
    device_details()

    while True:
        ans = colored_input("🔍 Search SIM data? (yes/no): ", Fore.CYAN).lower().strip()
        if ans == "no":
            exit_msg()
            break
        elif ans == "yes":
            q = colored_input("📥 Enter Mobile / CNIC: ", Fore.YELLOW).strip()
            if q:
                numinfo(q)
        else:
            robot_beep("Please type yes or no", 0.05, Fore.RED)

# ================= RUN =================

if __name__ == "__main__":
    main()