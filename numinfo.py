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

# ⚠️ NONCE ROZ CHANGE HOTA HAI — MANUALLY UPDATE
NONCE = "PASTE_NEW_NONCE_HERE"

HEADERS = {  
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "origin": "https://rashidminhas.com.pk",
    "referer": "https://rashidminhas.com.pk/blog/sim-owner-details/",
    "sec-ch-ua": "\"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
}

QUOTES = [  
    "Information is power — use it wisely.",  
    "Knowledge without ethics is dangerous.",  
    "Think before you act, data never lies.",  
    "Discipline turns tools into power.",  
    "Responsibility defines the user."  
]  

# ================= UI =================  

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

def robot(text, speed=0.04, color=Fore.LIGHTGREEN_EX):  
    print(color, end="", flush=True)  
    for ch in text:  
        print(ch, end="", flush=True)  
        time.sleep(speed)  
    print(Style.RESET_ALL)  

# ================= LOGO =================  

def ascii_logo():  
    clear()  
    slow_print("NUMINFO — Faizi Mods", Fore.CYAN, center=True)  
    line("═", Fore.MAGENTA)  

# ================= SEARCH =================  

def numinfo(query):  
    robot("Searching, please wait...", 0.04, Fore.CYAN)  
    line("─", Fore.CYAN)  

    payload = {  
        "action": "fetch_simdata",  
        "nonce": NONCE,  
        "track": query.strip()  
    }  

    try:  
        r = requests.post(API_URL, headers=HEADERS, data=payload, timeout=20)  
        raw = r.text.strip()  
    except Exception as e:  
        robot(f"Network error: {e}", 0.04, Fore.RED)  
        return  

    if raw == "0":  
        robot("Nonce expired — update token", 0.04, Fore.RED)  
        return  

    try:  
        res = json.loads(raw)  
    except:  
        robot("Invalid server response", 0.04, Fore.RED)  
        return  

    if not res.get("success"):  
        robot("No record found", 0.04, Fore.RED)  
        return  

    records = res.get("data", {}).get("Mobile", [])  
    for i, rec in enumerate(records, 1):  
        robot(f"Record {i}", 0.03, Fore.YELLOW)  
        slow_print(f"👤 Name    : {rec.get('Name','N/A')}", Fore.GREEN)  
        slow_print(f"🆔 CNIC    : {rec.get('CNIC','N/A')}", Fore.GREEN)  
        slow_print(f"📞 Mobile  : {rec.get('Mobile','N/A')}", Fore.GREEN)  
        slow_print(f"🏠 Address : {rec.get('Address','N/A')}", Fore.GREEN)  
        line("═", Fore.MAGENTA)  

# ================= MAIN =================  

def main():  
    ascii_logo()  
    slow_print(f"💬 {random.choice(QUOTES)}", Fore.YELLOW, center=True)  
    line("═", Fore.GREEN)  

    while True:  
        ans = colored_input("🔍 Search SIM data? (yes/no): ", Fore.CYAN).lower()  
        if ans == "no":  
            robot("Tool closed — Allah Hafiz", 0.04, Fore.GREEN)  
            break  
        elif ans == "yes":  
            q = colored_input("📥 Enter Mobile / CNIC: ", Fore.YELLOW)  
            if q.strip():  
                numinfo(q)  
        else:  
            robot("Please type yes or no", 0.04, Fore.RED)  

if __name__ == "__main__":  
    main()
