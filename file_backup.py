import shutil
import os

def backup():
    src = input("Source file: ")
    dst = "backup_" + src
    if os.path.exists(src):
        shutil.copy(src, dst)
        print("Backup created")
    else:
        print("File not found")

backup()