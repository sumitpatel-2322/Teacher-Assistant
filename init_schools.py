from Database.db import get_connection
# 1. Import the function to create tables
from Database.models import create_tables 

def initialize_schools():
    print("🔄 Creating Database Tables...")
    # 2. Create the tables (schools, teachers, crps, etc.) first!
    create_tables()
    
    conn = get_connection()
    cursor = conn.cursor()

    # Data: (udise, name, block)
    # 15 Schools across 3 Blocks (A, B, C)
    schools_data = [
        # --- BLOCK A ---
        ("121", "St. Mary's High School", "Block A"),
        ("122", "Government Public School", "Block A"),
        ("123", "Delhi Public School (DPS)", "Block A"),
        ("124", "S.M. Joshi Vidyalaya", "Block A"),
        ("125", "Vidya Mandir", "Block A"),

        # --- BLOCK B ---
        ("126", "Kendriya Vidyalaya", "Block B"),
        ("127", "Little Flower School", "Block B"),
        ("128", "Modern High School", "Block B"),
        ("129", "Saraswati Vidya Niketan", "Block B"),
        ("130", "Army Public School", "Block B"),

        # --- BLOCK C ---
        ("131", "Sunrise Global School", "Block C"),
        ("132", "Vivekananda Academy", "Block C"),
        ("133", "National High School", "Block C"),
        ("134", "Sacred Heart Convent", "Block C"),
        ("135", "Green Valley International", "Block C")
    ]

    try:
        # Clear old schools just in case, then insert new ones
        cursor.execute("DELETE FROM schools") 
        
        cursor.executemany("""
            INSERT OR IGNORE INTO schools (udise, name, block)
            VALUES (?, ?, ?)
        """, schools_data)
        
        conn.commit()
        print(f"✅ Success! Database initialized with {len(schools_data)} schools.")
        
    except Exception as e:
        print(f"❌ Error initializing data: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    initialize_schools()