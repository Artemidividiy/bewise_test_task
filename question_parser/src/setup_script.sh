cd backend;
python3 -m virtualenv venv;
source venv/bin/activate;
pip install -r requirements.txt;
cd backend && uvicorn  backend.main:app --reload --port=8000;