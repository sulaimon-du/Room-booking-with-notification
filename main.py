from controllers import bookings
from models.db import create_db


def rooms_booking():
    while True:
        print("Добро пожаловать в программу по бронированию кабинетов.\n")
        print("""
        Доступно:\n
            Для бронирование кабинета наберите - 1.\n
            Для просмотра броней по кабинету и дате - 2.\n
              
        Скоро:\n
            Для просмотра броней по дате - 3.\n
            Для просмотра брони по её названию - 4.\n
            Для выхода - 5.\n
            выберите действие: ....""", end=' ')
        try:
            action = int(input())
        except:
            action = int(input("Недопустимое число или символ.\n Введите заново: ...."))

        match action:
            case 1:
                check = bookings.check_time()
                if check:
                    print(check["message"])
                    bookings.booking_after_check(check["room_name"], check["start_time"], check["end_time"])
            case 2: # Просмотр броней по кабинету и дате
                check = bookings.check_time()
            case 3:
                try:
                    num = int(input("Просмот броней по дате"))
                except:
                    print(": ....")
                    num = int(input(""))
            case 4:
                try:
                    num = int(input("Просмотр брони по её названию"))
                except:
                    print(": ....")
                    num = int(input(""))
            case 5:
                break


create_db()
rooms_booking()