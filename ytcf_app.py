from asyncio.tasks import wait
import pytchat
from pytchat import *
import datetime
import time

print("----------------------------------------")
print("")

live_id = input("直播ID (網址結尾處編號): ")
t = 0
chat = pytchat.create(video_id=f"{live_id}", seektime = 0)

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

while True:
    user_msg = input("是否僅記錄特定成員訊息 (Y/N): ")
    if user_msg == "n" or user_msg == "N":
        while True:
            mod_msg = input("是否僅記錄管理員訊息 (Y/N): ")
            if mod_msg == "n" or mod_msg == "N":
                while True:
                    txt_log = input("是否輸出聊天紀錄 (Y/N): ")
                    if txt_log == "n" or txt_log == "N":
                        start_print(live_id)
                        while chat.is_alive():
                            for c in chat.get().sync_items():
                                print(f"{c.datetime} [{c.author.name}] - {c.message}")
                        end_print()
                    if txt_log == "y" or txt_log == "Y":
                        start_print(live_id)
                        f = open('log.txt', 'w', encoding='utf-8')
                        while chat.is_alive():
                            for c in chat.get().sync_items():
                                f = open('log.txt', 'a', encoding='utf-8')
                                f.write(f"{c.datetime} [{c.author.name}] - {c.message} {c.amountString}\n")
                                print(f"{c.datetime} [{c.author.name}] - {c.message}")
                        end_print()
            if mod_msg == "y" or mod_msg == "Y":
                while True:
                    txt_log = input("是否輸出聊天紀錄 (Y/N): ") 
                    if txt_log == "n" or txt_log == "N":
                        start_print(live_id)
                        while chat.is_alive():
                            for c in chat.get().sync_items():
                                if c.author.isChatModerator == True:
                                    print(f"{c.datetime} [{c.author.name}] - {c.message} {c.amountString}")
                        end_print()
                    if txt_log == "y" or txt_log == "Y":
                        start_print(live_id)
                        f = open('log.txt', 'w', encoding='utf-8')
                        while chat.is_alive():
                            for c in chat.get().sync_items():
                                if c.author.isChatModerator == True:
                                    f = open('log.txt', 'a', encoding='utf-8')
                                    f.write(f"{c.datetime} [{c.author.name}] - {c.message} {c.amountString}\n")
                                    print(f"{c.datetime} [{c.author.name}] - {c.message} {c.amountString}")
                        end_print()
            else:
                continue
            
    if user_msg == "y" or user_msg == "Y":
        user_msg = True
        while True:
            user = input("成員名稱: ") or None
            if user != None:
                while True:
                    txt_log = input("是否輸出聊天紀錄 (Y/N): ")
                    if txt_log == "n" or txt_log == "N":
                        start_print(live_id)
                        while chat.is_alive():
                            for c in chat.get().sync_items():
                                if c.author.name == f"{user}":
                                    print(f"{c.datetime} [{c.author.name}] - {c.message} {c.amountString}")
                        end_print()
                    if txt_log == "y" or txt_log == "Y":
                        start_print(live_id)
                        f = open('log.txt', 'w', encoding='utf-8')
                        while chat.is_alive():
                            for c in chat.get().sync_items():
                                if c.author.name == f"{user}":
                                    f = open('log.txt', 'a', encoding='utf-8')
                                    f.write(f"{c.datetime} [{c.author.name}] - {c.message} {c.amountString}\n")
                                    print(f"{c.datetime} [{c.author.name}] - {c.message} {c.amountString}")
                        end_print()
                    else:
                        continue
            else:
                continue
    else:
        continue