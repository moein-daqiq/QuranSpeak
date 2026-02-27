from database import get_connection

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Surahs table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS surahs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        surah_number INTEGER UNIQUE,
        name_ar TEXT,
        name_en TEXT,
        total_ayahs INTEGER
    )
    """)

    # Ayahs table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ayahs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        surah_number INTEGER NOT NULL,
        ayah_number INTEGER NOT NULL,
        text_ar TEXT NOT NULL,
        created_at TEXT DEFAULT (datetime('now')),
        UNIQUE (surah_number, ayah_number)
    )
    """)

    conn.commit()
    conn.close()