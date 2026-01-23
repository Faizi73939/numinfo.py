"""
NUMINFO — SIM & CNIC Lookup Tool
Author : Faizi Mods
"""

import requests
import time
import os
import platform
import random
import json
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

# ================= CONFIG =================

WIDTH = 72
TYPE_SPEED = 0.01

API_URL = "https://rashidminhas.com.pk/blog/sim-owner-details/"
# NONCE = "7afcb32be2"   # ⚠️ Expire ho jaye to update karna

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Linux; Android)",
    "Accept": "*/*",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Referer": "https://rashidminhas.com.pk/blog/sim-owner-details/",
    "Origin": "https://rashidminhas.com.pk/blog/sim-owner-details/"
}

QUOTES = [
    "Information is power — use it wisely.",
    "Knowledge without ethics is dangerous.",
    "Think before you act, data never lies.",
    "Discipline turns tools into power.",
    "Responsibility defines the user."
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

def robot_beep(text, speed=0.05, color=Fore.LIGHTGREEN_EX):
    print(color, end="", flush=True)
    for ch in text:
        print(ch, end="", flush=True)
        if ch.isalnum():
            print("\a", end="", flush=True)
        time.sleep(speed)
    print(Style.RESET_ALL)

# ================= ASCII LOGO =================

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

    line("═", Fore.MAGENTA)
    robot_beep("Welcome to Faizi Mods Tool", 0.04)
    line("═", Fore.MAGENTA)

# ================= WARNING (FIXED) =================

def warning():
    print(Fore.RED + "!" * WIDTH)
    slow_print(
        "⚠️ WARNING: Do not use this tool for any illegal or wrong purpose.",
        Fore.YELLOW,
        center=True
    )
    slow_print(
        "You are fully responsible for your own actions.",
        Fore.YELLOW,
        center=True
    )
    print(Fore.RED + "!" * WIDTH)
    time.sleep(1)

# ================= INFO SECTIONS =================

def show_quote_datetime():
    now = datetime.now()
    slow_print(f"💬 Quote : {random.choice(QUOTES)}", Fore.YELLOW, center=True)
    slow_print(f"📅 Day   : {now.strftime('%A')}", Fore.CYAN, center=True)
    slow_print(f"📆 Date  : {now.strftime('%d %B %Y')}", Fore.CYAN, center=True)
    slow_print(f"⏰ Time  : {now.strftime('%I:%M:%S %p')}", Fore.CYAN, center=True)
    line("═", Fore.GREEN)

def developer_details():
    slow_print("👨‍💻 DEVELOPER DETAILS", Fore.GREEN, center=True)
    line("─", Fore.GREEN)
    slow_print("🧑 Developer Name   : Faizan Rajpoot", Fore.CYAN)
    slow_print("⚙️ Developer Status : Broken", Fore.RED)
    slow_print("📞 Developer WP     : 03706058550", Fore.GREEN)
    slow_print("📢 Channel Name     : Faizi Mods", Fore.BLUE)
    slow_print("❤️ Favorite Anime   : Itachi Uchiha", Fore.MAGENTA)
    line("═", Fore.GREEN)

def device_details():
    slow_print("📱 DEVICE DETAILS", Fore.YELLOW, center=True)
    line("─", Fore.YELLOW)
    slow_print(f"💻 OS        : {platform.system()} {platform.release()}", Fore.CYAN)
    slow_print(f"🧠 Machine   : {platform.machine()}", Fore.CYAN)
    slow_print(f"🧩 Processor : {platform.processor() or 'Unknown'}", Fore.CYAN)
    line("═", Fore.YELLOW)

# ================= SEARCH =================

def numinfo(query):
    # ✅ WARNING AB SEARCH SE PEHLE AAYEGI
    warning()

    robot_beep("Searching details please wait", 0.04, Fore.CYAN)
    line("─", Fore.CYAN)

    payload = {
        "action": "fetch_simdata",
        "nonce": NONCE,
        "track": query.strip()
    }

    try:
        r = requests.post(API_URL, headers=HEADERS, data=payload, timeout=20)
        raw = r.text.strip()
    except:
        robot_beep("Network error occurred", 0.05, Fore.RED)
        return

    if raw == "0":
        robot_beep("Token expired — update NONCE", 0.05, Fore.RED)
        return

    try:
        res = json.loads(raw)
    except:
        robot_beep("Invalid server response", 0.05, Fore.RED)
        return

    if not res.get("success"):
        robot_beep("No record found", 0.05, Fore.RED)
        return

    records = res.get("data", {}).get("Mobile", [])
    for i, rec in enumerate(records, 1):
        robot_beep(f"Record {i}", 0.04, Fore.LIGHTYELLOW_EX)
        slow_print(f"👤 Name    : {rec.get('Name','N/A')}", Fore.GREEN)
        slow_print(f"🆔 CNIC    : {rec.get('CNIC','N/A')}", Fore.GREEN)
        slow_print(f"📞 Mobile  : {rec.get('Mobile','N/A')}", Fore.GREEN)
        slow_print(f"🏠 Address : {rec.get('Address','N/A')}", Fore.GREEN)
        line("═", Fore.MAGENTA)

# ================= EXIT =================

def exit_msg():
    line("═", Fore.MAGENTA)
    robot_beep("Thanks for using NUMINFO Tool", 0.04, Fore.GREEN)
    slow_print("📢 Join Telegram Channel : Faizi Mods", Fore.BLUE, center=True)
    slow_print("👋 Allah Hafiz — Tool Closed", Fore.YELLOW, center=True)
    line("═", Fore.MAGENTA)

# ================= MAIN =================

def main():
    ascii_logo()
    show_quote_datetime()
    developer_details()
    device_details()

    while True:
        ans = colored_input("🔍 Search SIM data? (yes/no): ", Fore.CYAN).lower()
        if ans == "no":
            exit_msg()
            break
        elif ans == "yes":
            q = colored_input("📥 Enter Mobile / CNIC: ", Fore.YELLOW)
            if q.strip():
                numinfo(q)
        else:
            robot_beep("Please type yes or no", 0.05, Fore.RED)

if __name__ == "__main__":
    main()
