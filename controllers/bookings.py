import sqlite3


from services.bookings import booking_room, check_is_aviable
from services.notifications import send_notification


def check_time():
    """
    Controllers:  Проверка доступности брони
    """
    try:
        print("\nПожалуйста введите заполните следующие строки:")
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
        return None
    else:
        message = f"Это время свободно, можно бронировать"
        return {"message": message, "room_name": room_name, "start_time": start_time,"end_time": end_time}
    

def booking_after_check(room_name, start_time, end_time):
    """
    Controllers: Бронь
    """
    first_name = input("Введите пожалуйста ваше Имя: ")
    last_name = input("Вашу Фамилию: ")
    phone_number= input("Ваш номер телефона: ")
    email= input("Ваша почта: ")
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