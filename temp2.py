import os
import time
import platform

def clear_screen():
    """
    운영 체제에 따라 화면을 지우는 함수.
    """
    os_type = platform.system()
    if os_type == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def print_house(door_open):
    """
    집을 출력하는 함수. 문의 상태에 따라 문이 열리거나 닫힘.
    """
    print("     ^     ")
    print("    / \\    ")
    print("   /   \\   ")
    print("  /     \\  ")
    print(" /_______\\ ")
    print("|         |")
    if door_open:
        # 문이 열린 경우
        print("|  |   |  |")
    else:
        # 문이 닫힌 경우
        print("|    _    |")
    print("| | | | | |")
    print("|_| |_| |_|")

while True:
    print_house(False) # 문 닫힘
    time.sleep(2) # 2초 기다림
    clear_screen() # 화면 지우기
    print_house(True) # 문 열림
    time.sleep(2) # 다시 2초 기다림
    clear_screen() # 화면 지우기
