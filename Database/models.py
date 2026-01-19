from Database.db import get_connection

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    
    # 1. TEACHERS TABLE
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS teachers(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            employee_id TEXT UNIQUE,
            school_udise TEXT NOT NULL, -- This acts as the School ID
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            preferred_language TEXT,
            subjects TEXT,
            classes TEXT
        );
    """)

    # 2. CRP TABLE
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS crps(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            employee_id TEXT UNIQUE,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            assigned_cluster TEXT,
            domain TEXT
        );
    """)

    # 3. BRP TABLE
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS brps(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            employee_id TEXT UNIQUE,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            assigned_block TEXT,
            domain TEXT
        );
    """)

    # 4. ARP TABLE
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS arps(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            employee_id TEXT UNIQUE,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            assigned_block TEXT,
            specialization TEXT
        );
    """)

    # 5. GUIDANCE TABLE (Linked to School)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS guidance(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            crp_id TEXT,
            school_id TEXT, -- Target School (e.g., 'Gurukul')
            title TEXT,
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    # 6. VISITS TABLE (Linked to School)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS visits(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            crp_id TEXT,
            school_id TEXT, -- Target School
            visit_date DATE,
            visit_time TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    
    conn.commit()
    conn.close()
    print("Database Tables Initialized Successfully.")

if __name__ == "__main__":
    create_tables()