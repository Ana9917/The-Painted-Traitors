import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_title():
    title_card = """
╔══════════════════════════════════════════════════╗
║                                                  ║
║          ✦  𝕿𝖍𝖊 𝕻𝖆𝖎𝖓𝖙𝖊𝖉 𝕿𝖗𝖆𝖎𝖙𝖔𝖗𝖘  ✦              ║
║      ──────────────────────────────────────      ║
║              [ Press ENTER to Start ]            ║
║                                                  ║
╚══════════════════════════════════════════════════╝
"""
    clear_screen()
    print(title_card)

show_title()