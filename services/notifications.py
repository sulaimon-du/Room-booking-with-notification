import smtplib
from email.mime.text import MIMEText


from utils import configs


def send_notification(email, room_name, employee_name, phone_number, start_time, end_time, title, description):
    subject = f"Алиф бронирование кабинета"
    body = f"""Вы успешно забронировали кабинет {room_name}.\n

Информация бронирования:
    
Кабинет: {room_name}
Название брони: {title}
Время начала: {start_time}
Время конца: {end_time}
Описание брони: {description or ' '}
Ваш номер телефона: {phone_number}

Спасибо что воспользовались - Алиф бронирование кабинета.

C уважением S.G.
    """
    send = send_email(email, subject, body)
    return None or send


def send_email(to_email: str, subject: str, body: str):
    msg = MIMEText(body, "plain")
    msg["Subject"] = subject
    msg["From"] = configs.my_email
    msg["To"] = to_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(configs.my_email, configs.my_password)
        server.send_message(msg)
    return None