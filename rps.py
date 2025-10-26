# 가위바위보 미니게임
import random

def get_user_choice():
    choice = input("가위, 바위, 보 중 하나를 선택하세요: ")
    return choice

def get_computer_choice():
    choices = ["가위", "바위", "보"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "비겼습니다!"
    elif (
        (user_choice == "가위" and computer_choice == "보") or
        (user_choice == "바위" and computer_choice == "가위") or
        (user_choice == "보" and computer_choice == "바위")
    ):
        return "이겼습니다!"
    else:
        return "졌습니다.."