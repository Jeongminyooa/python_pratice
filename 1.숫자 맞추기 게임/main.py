from random import randint

random_number = randint(1, 100)

input_number = -1
game_count = 0

while input_number != random_number:
    try:
        input_number = int(input("1~100 사이 숫자를 맞춰보세요! : "))
        
        game_count += 1

        print("----------------------------------------")
        if input_number == random_number:
            print("정답입니다. 정답은", random_number, "입니다.")
            print(f"도전한 횟수는 {game_count}회 입니다!")
        else:
            print("오답입니다.")
            if input_number > random_number:
                print("입력하신 숫자보다 낮습니다.")
            else:
                print("입력하신 숫자보다 높습니다.")
        print("----------------------------------------")
    except:
        print("숫자를 입력하세요. ")