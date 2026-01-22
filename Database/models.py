from Database.db import get_connection

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    
    # 1. SCHOOLS TABLE (Updated: Removed 'cluster' column)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS schools(
            udise TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            block TEXT
        );
    """)

    # 2. TEACHERS TABLE
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS teachers(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            employee_id TEXT UNIQUE,
            school_udise TEXT NOT NULL, -- Links to schools.udise
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            preferred_language TEXT,
            subjects TEXT,
            classes TEXT
        );
    """)

    # 3. CRP TABLE
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS crps(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            employee_id TEXT UNIQUE,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            assigned_cluster TEXT, -- Kept for legacy compatibility
            assigned_block TEXT,
            domain TEXT
        );
    """)

    # 4. BRP TABLE
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

    # 5. ARP TABLE
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

    # 6. GUIDANCE TABLE
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS guidance(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            crp_id TEXT,
            school_id TEXT,
            title TEXT,
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    # 7. VISITS TABLE
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS visits(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            crp_id TEXT,
            school_id TEXT,
            visit_date DATE,
            visit_time TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    # 8. INTERACTION LOGS
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS interaction_logs(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            request_id TEXT UNIQUE,
            teacher_id TEXT,
            school_id TEXT,
            topic TEXT,
            query_text TEXT,
            solution_shown TEXT,
            worked BOOLEAN, 
            feedback_text TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    # 9. ESCALATIONS
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS escalations(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            teacher_id TEXT,
            school_id TEXT,
            query_text TEXT,
            status TEXT DEFAULT 'Open',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    # 10. MICROLEARNING (New Table for File Uploads)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS microlearning(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            class_level TEXT,
            subject TEXT,
            content_type TEXT,
            duration TEXT,
            file_path TEXT,
            uploaded_by TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    conn.commit()
    conn.close()
    print("Database Tables Initialized Successfully.")

if __name__ == "__main__":
    create_tables()