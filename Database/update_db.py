import sqlite3

DB_PATH = "teachers.db"

def add_language_column():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    try:
        # Add the new column with a default of 'en' (English)
        cursor.execute("ALTER TABLE teachers ADD COLUMN preferred_language TEXT DEFAULT 'en'")
        print("✅ Success: Added 'preferred_language' column to teachers table.")
    except sqlite3.OperationalError as e:
        print(f"ℹ️ Note: {e} (Column might already exist)")
        
    conn.commit()
    conn.close()

if __name__ == "__main__":
    add_language_column()