const API_BASE = "http://127.0.0.1:8000/api";

const surahListEl = document.getElementById("surahList");
const ayahContainer = document.getElementById("ayahContainer");
const surahTitle = document.getElementById("surahTitle");


// Load Surahs on page load
async function loadSurahs() {
    const res = await fetch(`${API_BASE}/surahs`);
    const surahs = await res.json();

    surahListEl.innerHTML = "";

    surahs.forEach(surah => {
        const li = document.createElement("li");
        li.innerText = `${surah.surah_number}. ${surah.name_en || ""}`;
        
        li.onclick = () => loadAyahs(surah.surah_number, surah.name_en);

        surahListEl.appendChild(li);
    });
}


// Load Ayahs of a surah
async function loadAyahs(surahNumber, surahName) {

    surahTitle.innerText = `Surah ${surahNumber} - ${surahName}`;

    const res = await fetch(`${API_BASE}/surahs/${surahNumber}/ayahs`);
    const data = await res.json();

    ayahContainer.innerHTML = "";

    data.ayahs.forEach(ayah => {
        const div = document.createElement("div");
        div.className = "ayah";

        div.innerHTML = `
            <span class="ayah-number">(${ayah.ayah_number})</span>
            ${ayah.text_ar}
        `;

        ayahContainer.appendChild(div);
    });
}


// Start app
loadSurahs();