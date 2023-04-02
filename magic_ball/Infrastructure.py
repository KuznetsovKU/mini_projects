import random

answers = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да", "Можешь быть уверен в этом",
           "Мне кажется - да", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - да", "Да",
           "Пока неясно, попробуй снова", "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя предсказать",
           "Сконцентрируйся и спроси опять",
           "Даже не думай", "Мой ответ - нет", "По моим данным - нет", "Перспективы не очень хорошие",
           "Весьма сомнительно"]

questions = []

meeting_message = "Привет, я магический шар, и я знаю ответ на любой твой вопрос."
ask_name_message = "Как тебя зовут?"
hello_message = "Привет,"
start_message = "Задавай свой вопрос."
wrong_question = "Не понимаю вопроса. Перефразируй, пожалуйста."
skip_message = "Я уже отвечал на этот вопрос. Спроси что-нибудь еще."
play_again_message = "Хочешь спросить что-то еще? (1 = \"Да, хочу!\"; 0 = \"Может в другой раз\")"
goodbye_message = "Возвращайся если возникнут вопросы!"


def game():
    print()
    print(meeting_message)
    print(ask_name_message)
    name = input()
    print(hello_message, name, "!")
    game_starter = True
    while game_starter:
        print(start_message)
        ready_to_listen = True
        while ready_to_listen:
            question = input()
            if not is_valid_question(question):
                print(wrong_question)
            elif question in questions:
                print(skip_message)
            else:
                questions.append(question)
                ready_to_listen = False
        print(random.choice(answers))
        print(play_again_message)
        player_choice = input()
        if player_choice != "1":
            game_starter = False
            print(goodbye_message)


def is_valid_question(question):
    if len(question) < 2:
        return False
    if str(question).isdigit():
        return False
    return True
