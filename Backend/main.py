from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import create_tables
from routes.surahs import router as surah_router

app = FastAPI(title="QuranSpeak API")

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables on startup
create_tables()

# Include routes
app.include_router(surah_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "QuranSpeak API is running"}