# Project Sparrow V1

A futuristic desktop AI assistant focused on natural English + Tamil + Tanglish interaction.

## V1
- Dark futuristic Sparrow interface
- Text chat
- Browser voice input using Web Speech API
- Lightweight Tanglish intent normalization
- FastAPI backend skeleton
- Mock AI mode so the UI runs without an API key

## Run

### Backend
```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

### Frontend
Open `frontend/index.html` with a local server. Recommended:
```bash
cd frontend
python -m http.server 5500
```
Then open http://localhost:5500

The frontend calls http://localhost:8000/chat.

## Next modules
1. Real LLM integration
2. PC action tools
3. Better Tanglish intent/entity extraction
4. Persistent memory
5. Vision
6. Android control
7. ESP32/IoT control
