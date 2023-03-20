import random
# import calendar


HELP = """
help - Напечатать справку по программе.
add - Добавить задачу в список (название задачи запрашиваем у пользователя).
show - Напечатать все добавленные задачи
random - Добавить случайную задачу из списка на Сегодня"""

tasks = {}
random_task = ["Записаться в Нетологию", "Помыть машину", "Заняться бегом на дорожке", "Покормить котов"]



def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = [task]
    print("Задача ", task, "добавлена на дату ", date)


# def create_calendar(year, themonth):
#     calendar.calendar(year, themonth)
#     calendar.prmonth(year, themonth)

run = True

while run:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        date = input("Введите дату для отображения задач: ")
        if date in tasks:
            for task in tasks[date]:
                print("- ", task)
        else:
            print("Ничего не запланировано.")
    elif command == "add":
        date = input("Введите дату для задачи: ")
        task = input("Введите название задачи: ")
        add_todo(date, task)
    elif command == "random":
        task = random.choice(random_task)
        add_todo("Сегодня", task)
    else:
        print("Неизвестная комманда!")
        break
print("До свидания!")


# if __name__ == "__main__":
#     create_calendar(2023, 3)
