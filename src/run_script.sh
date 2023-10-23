cd backend;
python3 -m virtualenv venv;
source venv/bin/activate;
uvicorn run main:app --port 8000;