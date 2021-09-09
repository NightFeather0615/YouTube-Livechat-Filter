from asyncio.tasks import wait
import pytchat
from pytchat import *
import datetime
import time

print("----------------------------------------")
print("")

live_id = input("直播ID (網址結尾處編號): ")
retry = 0
user = None
chat = pytchat.create(video_id=f"{live_id}")

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(f" 聊天室已關閉 / 離線，將在{timer}後重試", end="\r")
        time.sleep(1)
        t -= 1

def start_print(live_id):
    print("")
    print("----------------------------------------")
    print("")
    print(f"{datetime.datetime.now().replace(microsecond=0) } [System] - 過濾已於 {datetime.datetime.now().replace(microsecond=0)} 開始，直播ID為: {live_id}")
    print("")
    print("----------------------------------------")
    print("")

def end_print():
    print("")
    print("----------------------------------------")
    print("")
    print(f"{datetime.datetime.now().replace(microsecond=0) } [System] - 聊天室已於 {datetime.datetime.now().replace(microsecond=0)} 關閉 / 離線，感謝收看！")
    print("")
    print("----------------------------------------")

def print_chat(c):
    print(f"{c.datetime} [{c.author.name}] - {c.message}")

def txt_logging(c):
    f = open('log.txt', 'a', encoding='utf-8')
    f.write(f"{c.datetime} [{c.author.name}] - {c.message} {c.amountString}\n")

def main_run(mod_msg, txt_log, user_msg, user = None):
    global retry
    retry = 0
    if txt_log == True:
        open('log.txt', 'w', encoding='utf-8')
    if user_msg == True:
        start_print(live_id)
        while chat.is_alive():
            for c in chat.get().sync_items():
                if c.author.name == f"{user}":
                    if txt_log == True:
                        txt_logging(c)
                    print_chat(c)
    else:
        if mod_msg ==  True:
            start_print(live_id)
            while chat.is_alive():
                for c in chat.get().sync_items():
                    if c.author.isChatModerator == True:
                        if txt_log == True:
                            txt_logging(c)
                        print_chat(c)
        else:
            start_print(live_id)
            while chat.is_alive():
                for c in chat.get().sync_items():
                        if txt_log == True:
                            txt_logging(c)
                        print_chat(c)


while True:
    user_msg = input("是否僅記錄特定成員訊息 (Y/N): ")
    if user_msg.lower() == "n":
        user_msg = False
        mod_msg = input("是否僅記錄管理員訊息 (Y/N): ")
        if mod_msg.lower() == "n":
            mod_msg = False
            txt_log = input("是否輸出聊天紀錄 (Y/N): ")
            if txt_log.lower() == "n":
                txt_log = False
                break
            elif txt_log.lower() == "y":
                txt_log = True
                break
            else:
                continue
        elif mod_msg.lower() == "y":
            mod_msg = True
        else:
            continue
    elif user_msg.lower() == "y":
        user_msg = True
        mod_msg = False
        user = input("成員名稱: ") or None
        txt_log = input("是否輸出聊天紀錄 (Y/N): ")
        if txt_log.lower() == "n":
            txt_log = False
            break
        elif txt_log.lower() == "y":
            txt_log = True
            break
    else:
        continue

while True:
    main_run(mod_msg, txt_log, user_msg, user)
    if chat.is_alive() == False:
        print("")
        print("----------------------------------------")
        print("")
        countdown(150)
        chat = pytchat.create(video_id=f"{live_id}")
        retry += 1
        if retry >= 5:
            break