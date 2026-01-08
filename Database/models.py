from Database.db import get_connection

def create_teacher_table():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS teachers(
                       id INTEGER PRIMAR KEY,
                      username TEXT UNIQUE NOT NULL,
                      password TEXT NOT NULL);
                      """)
    conn.commit()
    conn.close()