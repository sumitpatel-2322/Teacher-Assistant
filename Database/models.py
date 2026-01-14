from Database.db import get_connection

def create_teacher_table():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Create table if not exists (Standard Structure)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS teachers(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            role TEXT NOT NULL,
            school_name TEXT NOT NULL,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        );
    """)
    
    # ---------------------------------------------------------
    # MIGRATION: Add columns for Profile Preferences if missing
    # ---------------------------------------------------------
    try:
        # Check if column exists
        cursor.execute("SELECT preferred_class FROM teachers LIMIT 1")
    except Exception:
        # If not, add them
        print("Migrating DB: Adding preferred_class and preferred_subject...")
        cursor.execute("ALTER TABLE teachers ADD COLUMN preferred_class TEXT")
        cursor.execute("ALTER TABLE teachers ADD COLUMN preferred_subject TEXT")
        
    conn.commit()
    conn.close()