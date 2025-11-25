import sqlite3




def create_db():
    """
    DB creating, if not exists
    """
    conn = sqlite3.connect('rb.db')
    cursor = conn.cursor()

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS rooms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            room_name TEXT UNIQUE NOT NULL,
            description TEXT,
            deleted_at DATETIME,
            is_deleted BOOLEAN DEFAULT NULL
            )
            ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            room_id INTEGER NOT NULL,       
            employee_name TEXT NOT NULL,
            phone_number TEXT NOT NULL,
            email TEXT NOT NULL,           
            start_time DATETIME NOT NULL,
            end_time DATETIME NOT NULL,
            title TEXT NOT NULL,
            description TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME,
            deleted_at DATETIME,
            FOREIGN KEY (room_id) REFERENCES rooms(id)
        )
        ''')

    conn.commit()
    conn.close()