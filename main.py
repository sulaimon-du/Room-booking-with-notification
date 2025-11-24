import sqlite3


from services.bookings import booking_room, check_is_aviable
from services.notifications import send_notification


def rooms_booking():
    while True:
        print("Добро пожаловать в программу по бронированию кабинетов.\n")
        print("""
            Доступно\n:
            Для бронирование кабинета наберите - 1.\n
            Скоро\n:
            Для просмотра брони по её названию - 2.\n
            Для просмотра броней по дате - 3.\n
            Для просмотра броней по кабинету и дате - 4.\n
            Для выхода - 5.\n\n
выберите действие: ....""", end=' ')
        try:
            action = int(input())
        except:
            action = int(input("Недопустимое число или символ.\n Введите заново: ...."))
        match action:
            case 1:
                try:
                    print("Пожалуйста введите заполните следующие строки:")
                    date = str(input("\nГод, месяц и день брони, через тире(-) как тут :(0000-00-00): ...."))
                    start_time = str(input("Время начала брони, через (:) как тут :(00:00):...."))
                    end_time = str(input("Время конца брони, через (:) как тут :(00:00):...."))
                except:
                    print("Пожалуйста повторите как в примере.\n Введите заново: ....")
                    start_time = str(input("Время начала брони, через (:) как тут :(00:00): ...."))
                    end_time = str(input("Время конца брони, через (:) как тут :(00:00): ...."))
                finally:
                    start_time = f"{date} {start_time}:00"
                    end_time = f"{date} {end_time}:00"


                try:
                    room_name = str(input("Введите номер комнаты :...."))
                except:
                    print("Недопустимое число или символ.\n")
                    room_name = int(input("Введите номер комнаты :...."))

                check = check_is_aviable(room_name, start_time, end_time)
                if check:
                    print("К сожалению в данное время есть бронь/и :")
                    for i in check:
                        for k in i:
                            print(k)
                        print("*******")
                    return
                
                else:
                    print("Это время свободно, можно бронировать")

                    first_name = input("Введите пожалуйста ваше Имя: ")
                    last_name = input("Фамилия: ")
                    phone_number= input("Ваш номер телефона: ")
                    email= input("Вашу почта: ")
                    title = input("Название встречи: ")
                    description = input("Описание встречи (можно оставить пустым): ")

                    employee_name = f"{last_name} {first_name}"
                    booking = booking_room(room_name, employee_name, phone_number, email, start_time, end_time, title, description)
                    if booking:
                        print(booking)
                        notification = int(input("Получить подтверждение по электронной почте\nДа - 1 | Нет 0\n:"))
                        if notification == 1:
                            send = send_notification(email, room_name, employee_name, phone_number, start_time, end_time, title, description )
                            if not send:
                                print("Уведомление успешно отправленно.\n\n")
                        else:
                            return
                    else:
                        print(f"К сожалению что-то пошло не так, повторите пожалуйста")
                        return
                

            case 2:
                try:
                    num = int(input("Просмотр брони по её названию"))
                except:
                    print(": ....")
                    num = int(input(""))
            case 3:
                try:
                    num = int(input("Просмот броней по дате"))
                except:
                    print(": ....")
                    num = int(input(""))
            case 4:
                try:
                    num = int(input("Просмотр броней по кабинету и дате"))
                except:
                    print(": ....")
                    num = int(input(""))
            case 5:
                break


rooms_booking()