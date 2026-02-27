import sqlite3

# connect to database
conn = sqlite3.connect("quran.db")
cursor = conn.cursor()

# create ayahs table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS ayahs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    surah INTEGER,
    ayah INTEGER,
    text_ar TEXT
)
""")

# open the downloaded file
with open("quran-simple.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# insert data
for line in lines:
    parts = line.strip().split("|")
    if len(parts) == 3:
        surah = int(parts[0])
        ayah = int(parts[1])
        text = parts[2]

        cursor.execute(
            "INSERT INTO ayahs (surah, ayah, text_ar) VALUES (?, ?, ?)",
            (surah, ayah, text)
        )

# save
conn.commit()
conn.close()

print("✅ Quran imported successfully!")