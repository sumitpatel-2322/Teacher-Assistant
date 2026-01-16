from Database.db import get_connection

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    
    # ==========================================
    # 1. TEACHERS TABLE
    # Stores: tname, tid, school_ucode, emailid, language, subjects, classes
    # ==========================================
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS teachers(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            employee_id TEXT UNIQUE,
            school_udise TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            preferred_language TEXT,
            subjects TEXT,  -- Stored as "Math, Science"
            classes TEXT    -- Stored as "1, 2, 3"
        );
    """)

    # ==========================================
    # 2. CRP TABLE (Cluster Resource Person)
    # Stores: full_name, cid, emailid_admin, assign_cluster, domain
    # ==========================================
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS crps(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            employee_id TEXT UNIQUE, -- Matches 'cid'
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            assigned_cluster TEXT,   -- The jurisdiction
            domain TEXT              -- e.g. Academic/Admin
        );
    """)

    # ==========================================
    # 3. BRP TABLE (Block Resource Person)
    # Standalone table as requested
    # ==========================================
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS brps(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            employee_id TEXT UNIQUE,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            assigned_block TEXT,     -- The jurisdiction
            domain TEXT
        );
    """)

    # ==========================================
    # 4. ARP TABLE (Academic Resource Person)
    # Standalone table as requested
    # ==========================================
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS arps(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            employee_id TEXT UNIQUE,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            assigned_block TEXT,
            specialization TEXT      -- Mapped from Domain or separate field if added later
        );
    """)
    
    conn.commit()
    conn.close()
    print("Database Tables Initialized Successfully.")

# Run this once to setup DB
if __name__ == "__main__":
    create_tables()