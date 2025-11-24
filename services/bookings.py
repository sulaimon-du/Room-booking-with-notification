from datetime import datetime

from properties.bookings import  check_booking_time, booking_aviable_room, update_booking_info, cancel_booking
from services.rooms import room_info as get_room_info



def booking_room(room_name, employee_name, phone_number, email, start_time, end_time, title, description=None):
    """
    """
    room_info = get_room_info(room_name)
    room_id = room_info[0]

    booked = booking_aviable_room(room_id, employee_name, phone_number, email, start_time, end_time, title, description)
    if booked:
        return f"Ваше бронирование успешно добавленно."
    else:
        print(booked)
        return None
        

def check_is_aviable(room_name, start_time, end_time):
    """
    """
    check = check_booking_time(room_name, start_time, end_time)
    start_time = time_in_minute(start_time)
    end_time = time_in_minute(end_time)
    day_booking = []
    booked_times = []
    
    if check:
        for i in check:
            for k in i:
                day_booking.append(k)
            a_s_t = time_in_minute(day_booking[3])
            a_e_t = time_in_minute(day_booking[4])
            if (start_time < (a_s_t or a_e_t) < end_time) :
                booked_times.append(day_booking)
            day_booking = []
        return booked_times or None
    else:
        return None


def time_in_minute(time):
    """"""
    time = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
    minutes = time.hour * 60 + time.minute
    return minutes

