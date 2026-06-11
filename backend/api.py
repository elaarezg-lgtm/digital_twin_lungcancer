from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import json, math

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / 'data'
DASHBOARD_FILE = ROOT / 'dashboard' / 'index.html'
DATA_CANDIDATES = [
    DATA_DIR / 'dashboard_simulation_patients_verified_15B_repaired.json',
    DATA_DIR / 'dashboard_simulation_patients_verified.json',
    DATA_DIR / 'dashboard_simulation_patients_global.json',
]

app = FastAPI(title='EGFR Video Dashboard Exact Restore')
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_methods=['*'], allow_headers=['*'])

def clean(x):
    if isinstance(x, float) and (math.isnan(x) or math.isinf(x)):
        return None
    if isinstance(x, list):
        return [clean(i) for i in x]
    if isinstance(x, dict):
        return {k: clean(v) for k, v in x.items()}
    return x

def load_patients():
    for p in DATA_CANDIDATES:
        if p.exists():
            with open(p, 'r', encoding='utf-8') as f:
                data = clean(json.load(f))
            if isinstance(data, list):
                return data, str(p)
            if isinstance(data, dict):
                if isinstance(data.get('patients'), list): return data['patients'], str(p)
                if isinstance(data.get('data'), list): return data['data'], str(p)
    return [], 'NO_DATA'

@app.get('/')
def root():
    pts, src = load_patients()
    return {'status':'running', 'dashboard':'/dashboard', 'patients_count':len(pts), 'source':src, 'dashboard_file_exists':DASHBOARD_FILE.exists()}

@app.get('/health')
def health():
    pts, src = load_patients()
    return {'status':'ok', 'patients_count':len(pts), 'source':src, 'dashboard_file_exists':DASHBOARD_FILE.exists()}

@app.get('/patients')
@app.get('/api/patients')
def patients():
    pts, _ = load_patients()
    return pts

@app.get('/dashboard')
def dashboard():
    if not DASHBOARD_FILE.exists():
        return JSONResponse({'error':'dashboard/index.html missing', 'expected':str(DASHBOARD_FILE)}, status_code=404)
    return FileResponse(str(DASHBOARD_FILE), media_type='text/html')
