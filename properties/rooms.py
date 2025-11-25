from utils.connection import get_db_connection


#Create
def create_room(room_name, description = None):
    """
    БД: Создание комнаты
    """
    conn = get_db_connection()
    # Проверка входных данных
    try:
        conn.execute("INSERT INTO rooms (room_name, description) VALUES (?, ?)", 
                    (room_name, description))
        conn.commit()
    except Exception as e:
        error = f"Произошла ошибка при добавлении комнаты: {e}"
    finally:
        conn.close()


#Read
def get_room_info(room_name):
    """
    БД: Получение данных комнаты по room_name
    """
    conn = get_db_connection()
    info = None
    # Проверка входных данных
    try:
        info = conn.execute(
            "SELECT id, room_name, description FROM rooms WHERE room_name = ?", 
            (room_name,)).fetchone()
    except Exception as e:
        print(e)
        print('Ошибка')
    finally:
        conn.close()
    
    return info


#Update
def update_room_info():
    conn = get_db_connection()
    conn.execute("")
    conn.commit()
    conn.close()


#Delete
def deactivate_room():
    conn = get_db_connection()
    conn.execute("")
    conn.commit()
    conn.close()