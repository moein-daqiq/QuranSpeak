from fastapi import APIRouter
from database import get_connection

router = APIRouter()

# Get all surahs
@router.get("/surahs")
def get_surahs():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM surahs ORDER BY surah_number")
    rows = cursor.fetchall()

    surahs = [dict(row) for row in rows]

    conn.close()
    return surahs


# Get ayahs of a surah
@router.get("/surahs/{surah_number}/ayahs")
def get_ayahs(surah_number: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT ayah_number, text_ar
        FROM ayahs
        WHERE surah_number = ?
        ORDER BY ayah_number
    """, (surah_number,))

    rows = cursor.fetchall()

    ayahs = [dict(row) for row in rows]

    conn.close()
    return {
        "surah_number": surah_number,
        "ayahs": ayahs
    }
from fastapi import APIRouter
from database import get_connection

router = APIRouter()

@router.get("/surah/{surah_id}/ayahs")
def get_ayahs(surah_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT ayah, text_ar FROM ayahs WHERE surah = ? ORDER BY ayah ASC",
        (surah_id,)
    )

    rows = cursor.fetchall()

    conn.close()

    return [
        {
            "ayah": row[0],
            "text": row[1]
        }
        for row in rows
    ]