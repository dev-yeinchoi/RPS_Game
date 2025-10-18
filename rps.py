# 가위바위보 미니게임
import random

def get_user_choice():
    choice = input("가위, 바위, 보 중 하나를 선택하세요: ")
    return choice

def get_computer_choice():
    choices = ["가위", "바위", "보"]
    return random.choice(choices)