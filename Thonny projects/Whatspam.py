import pyautogui as pt
import time

limit = input("Enter limit:")
message = input("Enter message:")
i = 0
time.sleep(5)

while i < int(limit):
    pt.typewrite(f"{i + 1}: {message}")

    pt.press("enter")

    i += 1