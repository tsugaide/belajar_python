import socket
from time import sleep

pc_name = socket.gethostname()

def welcome_message():
    
    style = "*" * (len(pc_name)+6)
    print(f"\n\n{style}")
    print(f"** {pc_name} **")
    print(f"{style}")

def stop():
    print("program akan di hentikan")
    sleep(0.5)
    print("3")
    sleep(0.5)
    print("2")
    sleep(0.5)
    print("1")
    sleep(0.5)
    print("Berhasil keluar")
    exit()

