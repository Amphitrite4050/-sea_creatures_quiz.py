import random

def sea_creatures_quiz():
    # список вопросов и ответов
    questions = ["Как называется морское животное, которое может менять цвет?", 
                "Как называется морское животное, которое имеет восемь щупалец?",
                "Как называется морское животное, которое имеет раковину?",
                "Как называется морское животное, которое может изменять свою форму?",
                "Как называется морское животное, которое может светиться в темноте?"]
    answers = ["осьминог", "осьминог", "моллюск", "губка", "медуза"]
    # перемешиваем список вопросов
    random.shuffle(questions)
    # задаем пользователю вопросы
    score = 0
    for i in range(len(questions)):
        print(questions[i])
        user_answer = input("Введите ответ: ")
        if user_answer.lower() == answers[i]:
            print("Правильно!")
            score += 1
        else:
            print("Неправильно.")
    # выводим результат
    print("Вы ответили правильно на", score, "из", len(questions), "вопросов.")
    
sea_creatures_quiz()
