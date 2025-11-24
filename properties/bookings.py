from utils.connection import get_db_connection

#Create

def booking_aviable_room(room_id, employee_name, phone_number, email, start_time, end_time, title, description=None):
    """
    БД: 
    """
    #checkbooking_time(room_name,start_time, end_time)
    conn = get_db_connection()
    try:
        conn.execute("""INSERT INTO bookings 
                     (room_id, employee_name, phone_number, email, 
                     start_time, end_time, title, description)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    """,(room_id, employee_name, phone_number, email, 
                         start_time, end_time, title, description))
        conn.commit()
        info = True
    except Exception as e:
        print(f"Error: {e}")
        info = False
    finally:
        conn.close()
    return info


def check_booking_time(room_name,start_time, end_time): 
    """
    БД: check
    """
    conn = get_db_connection()
    # Проверка входных данных
    booked = None
    try:
        booked = conn.execute("""SELECT r.room_name, b.title,b.employee_name,
                              b.start_time, b.end_time 
                     FROM bookings b
                     JOIN rooms r ON b.room_id = r.id
                     WHERE r.room_name = ? AND DATE(b.start_time) = ?
                              OR DATE(b.end_time) = ?
                              
                              
                     ORDER BY b.start_time DESC
                     """, 
                    (room_name, start_time[:10], end_time[:10])).fetchall()
    except Exception as e:
        print(f"Произошла ошибка при  проверке: {e}")
    finally:
        conn.close()
    return booked

    
def send_nothification_by_email():
    """"""
    pass


#Read
def get_booking_info(room_name):
    """
    БД: 
    """
    pass

#Update
def update_booking_info():
    conn = get_db_connection()
    conn.execute("")
    conn.commit()
    conn.close()

#Delete
def cancel_booking():
    conn = get_db_connection()
    conn.execute("")
    conn.commit()
    conn.close()
