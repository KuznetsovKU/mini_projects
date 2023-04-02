import random

meeting_message = "Привет! Добро пожаловать в игру \"Угадай число\"!"
second_message = "Давай установим границы ))) " \
                 "Укажи максимальное целое число, в границах от 0 до которого я загадаю свое число: "
range_message = "А может быть все-таки введем целое число?"
start_message1 = "Итак, я загадал число в диапазоне от 1 до "
start_message2 = ". Попробуй его угадать!"
too_less_message = "Твое число меньше загаданного, попробуй еще разок"
too_much_message = "Твое число больше загаданного, попробуй еще разок"
win_message = "Ты угадал, поздравляю!"
efforts_message = "Количество попыток: "
play_again_message = "Сыграем еще? (1 = \"Да, давай играть!\"; 0 = \"Может в другой раз\""
goodbye_message = "Спасибо, что играли в игру \"Угадай число\". Еще увидимся..."
try_message = "Введи свой вариант: "
invalid_try_message = "А может быть все-таки введем целое число из заданного диапазона?"


def game():
    game_starter = True
    while game_starter:
        print()
        print(meeting_message)
        print(second_message)
        player_range = input()

        while not player_range.isdigit():
            print(range_message)
            player_range = input()

        player_range = int(player_range)
        secret_number = random.randint(1, player_range)
        print(start_message1, player_range, start_message2)
        answer = -1
        efforts_counter = 1
        while answer != secret_number:
            answer = get_answer(player_range)
            if answer < secret_number:
                print(too_less_message)
            elif answer > secret_number:
                print(too_much_message)
            else:
                print(win_message)
                print(efforts_message, efforts_counter)
            efforts_counter += 1
        print(play_again_message)
        game_starter = is_valid(1, input())
        if not game_starter:
            print(goodbye_message)


def get_answer(some_range):
    print(try_message, end='')
    player_num = input()
    while not is_valid(some_range, player_num):
        print(invalid_try_message)
        player_num = input()
    return int(player_num)


def is_valid(some_range, num):
    if str(num).isdigit():
        return 0 < int(num) <= some_range
    return False
