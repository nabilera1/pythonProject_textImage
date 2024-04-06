import os
import time
import platform

# 플랫폼에 따른 키 입력 감지 함수
def key_pressed():
    try:
        # Windows용
        import msvcrt
        return msvcrt.kbhit()
    except ImportError:
        # UNIX/Linux/macOS용
        import sys
        import select
        return select.select([sys.stdin], [], [], 0)[0] != []

def clear_screen():
    """
    운영 체제에 따라 화면을 지우는 함수.
    """
    os_type = platform.system()
    if os_type == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def print_house(door_offset):
    """
    미닫이문이 밀린 상태와 함께 집을 표현하는 함수.
    door_offset은 문의 오프셋(0에서 4 사이)을 나타냄.
    """
    print("     ^     ")
    print("    / \\    ")
    print("   /   \\   ")
    print("  /     \\  ")
    print(" /_______\\ ")
    print("|         |")
    print("|" + " " * door_offset + "    _" + " " * (4 - door_offset) + "|")  # 문 위치 조정
    # 문 아래 부분과 함께 움직이도록 조정
    print("|" + " " * door_offset + "| | | |" + " " * (4 - door_offset) + "|")
    print("|" + "_" * door_offset + "|_| |_|" + "_" * (4 - door_offset) + "|")

try:
    door_offset = 0  # 문의 시작 위치
    opening = True  # 문이 열리고 있는지 여부

    while True:
        if key_pressed():  # 아무 키나 눌렀을 때 종료
            break

        print_house(door_offset)
        time.sleep(0.5)  # 0.5초 기다림
        clear_screen()  # 화면 지우기

        if door_offset == 4:
            opening = False
        elif door_offset == 0:
            opening = True

        door_offset += 1 if opening else -1

finally:
    clear_screen()  # 프로그램 종료 시 화면을 한 번 더 지움
    print("Program terminated.")
