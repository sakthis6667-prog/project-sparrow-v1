from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Project Sparrow API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str
    language: str = "auto"

class ChatResponse(BaseModel):
    reply: str
    intent: str
    language: str

def detect_language(text: str) -> str:
    t = text.lower()
    tamil_markers = ["pannu", "panra", "venum", "enna", "irukku", "open pannu",
                     "thiran", "seyyu", "podu", "kudu", "inga", "anga"]
    if any(x in t for x in tamil_markers):
        return "Tanglish"
    return "English"

def understand(text: str):
    t = text.lower().strip()

    if ("open" in t or "open pannu" in t) and "chrome" in t:
        return "open_app", "Sure bro, Chrome open panna ready."
    if "spotify" in t and ("open" in t or "pannu" in t):
        return "open_app", "Sure bro, Spotify open panna ready."
    if "screenshot" in t or "screen shot" in t:
        return "screenshot", "Screenshot action ready."
    if "weather" in t or "weather eppadi" in t:
        return "weather", "Weather module next phase-la connect pannalaam."
    if "reminder" in t or "reminder podu" in t:
        return "create_reminder", "Reminder module next phase-la connect pannalaam."
    return "chat", "Got it bro. Naan understand panniten. Real AI brain next module-la connect pannalaam."

@app.get("/health")
def health():
    return {"status": "online", "assistant": "Sparrow"}

@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    language = req.language if req.language != "auto" else detect_language(req.message)
    intent, reply = understand(req.message)
    return ChatResponse(reply=reply, intent=intent, language=language)
