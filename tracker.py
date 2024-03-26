from datetime import datetime
from os import system, makedirs, path, name as os_name

from utils import green, white


# Функция для сохранения данных о матчах в файл
def save_data_match(data):
    with open("matches.txt", "a") as file:
        file.write(data + "\n")


# Функция для сохранение данных о тренировке в файл
def save_data_training(data):
    with open("training.txt", "a") as file:
        file.write(data + "\n")


while True:
    system("cls" if os_name == "nt" else "clear")
    header = (
        f"Выбертие действие: "
    )

    print(header)

    for i, name in enumerate([
        "Добавить матч",
        "Добавить тренировку",
        "Изменить время последнего занятия",
        "Добавить подпись к последнему занятию"
    ]):
        print(f"{green}{'edci'[i]}{white}: {name}")

    print()

    # Gain input
    session_id = input("\nВвод: ")
    if session_id.isdigit():
        session_id = int(session_id)
    elif session_id in ('e', 'd', 'c', 'i'):
        session_id = "edci".index(session_id) + 1
    else:
        session_id = 0

    if session_id == 1:
        # Получаем данные о матче
        score = input("Введите счет матча: ")
        kills = input("Введите количество убийств: ")
        deaths = input("Введите количество смертей: ")
        assists = input("Введите количество помощи: ")
        headshot_percentage = input("Введите процент хедшотов: ")
        adr = input("Введите ADR (средний урон за раунд): ")

        # Форматируем данные о матче
        match_data = f"{datetime.now()}: Счет - {score}, Убийства - {kills}, Смерти - {deaths}, Помощь - {assists}, Хедшоты - {headshot_percentage}%, ADR - {adr}"

        # Сохраняем данные в файл
        save_data_match(match_data)
        print("Данные о матче успешно сохранены.")
        input("\nНажмите Enter для продолжения...")

    if session_id == 2:
        time = input("Введите время тренировки: ")

        training_data = f"{datetime.now()}: Время тренировки - {time}"

        save_data_match(training_data)
        print("Данные о тренировке успешно сохранены.")
        input("\nНажмите Enter для продолжения...")
