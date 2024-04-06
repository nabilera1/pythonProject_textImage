import time

def print_house(door_open):
    print("     ^     ")
    print("    / \\    ")
    print("   /   \\   ")
    print("  /     \\  ")
    print(" /_______\\ ")
    print("|         |")
    if door_open:
        # 문이 열린 경우
        print("|  _ _  _ |")
    else:
        # 문이 닫힌 경우
        print("|  _   _  |")
    print("| | | | | |")
    print("|_| |_| |_|")

while True:
    print_house(False) # 문 닫힘
    time.sleep(2) # 2초 기다림
    print("\n" * 30) # 화면을 클리어하기 위해 여러 줄 공백 출력
    print_house(True) # 문 열림
    time.sleep(2) # 다시 2초 기다림
    print("\n" * 30) # 화면 클리어
