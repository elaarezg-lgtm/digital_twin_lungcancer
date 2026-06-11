
# ============================================================
# backend/api.py
# EGFR Lung Cancer Digital Twin API
# Serves global trusted dashboard data
# ============================================================

from pathlib import Path
import json
from typing import Any, Dict, List, Optional

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles


BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
DASHBOARD_DIR = BASE_DIR / "dashboard"

SIM_DATA_PATH = DATA_DIR / "dashboard_simulation_patients_verified.json"
GLOBAL_SIM_DATA_PATH = DATA_DIR / "dashboard_simulation_patients_global.json"
CONFIG_PATH = DATA_DIR / "dashboard_config.json"

DASHBOARD_FILE_CANDIDATES = [
    DASHBOARD_DIR / "EGFR Lung Cancer Digital Twin.htm",
    DASHBOARD_DIR / "EGFR Lung Cancer Digital Twin.html",
    DASHBOARD_DIR / "index.html",
]


app = FastAPI(
    title="EGFR Lung Cancer Digital Twin API",
    description="Research prototype moving toward reliable oncology decision support after validation.",
    version="13.0-global-evidence-dashboard",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def read_json_file(path: Path, default: Any = None) -> Any:
    if default is None:
        default = {}

    if not path.exists():
        return default

    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default


def load_patients() -> List[Dict[str, Any]]:
    path = SIM_DATA_PATH

    if not path.exists() and GLOBAL_SIM_DATA_PATH.exists():
        path = GLOBAL_SIM_DATA_PATH

    if not path.exists():
        return []

    data = read_json_file(path, default=[])

    if isinstance(data, dict):
        if "patients" in data:
            data = data["patients"]
        elif "data" in data:
            data = data["data"]
        else:
            data = []

    if not isinstance(data, list):
        return []

    return data


def load_config() -> Dict[str, Any]:
    return read_json_file(CONFIG_PATH, default={
        "clinical_use_statement": (
            "Research prototype under development. The long-term objective is to become a reliable, "
            "evidence-grounded oncology decision-support system after rigorous validation."
        ),
        "decision_support_goal": (
            "Designed toward reliable EGFR-mutated NSCLC/LUAD precision-oncology decision support."
        ),
    })


def find_patient(patient_id: str) -> Optional[Dict[str, Any]]:
    patients = load_patients()

    for patient in patients:
        if str(patient.get("patient_id")) == str(patient_id):
            return patient

        if str(patient.get("global_patient_id")) == str(patient_id):
            return patient

    return None


def safe_get(d: Dict[str, Any], *keys: str, default: Any = None) -> Any:
    cur = d

    for key in keys:
        if not isinstance(cur, dict):
            return default

        cur = cur.get(key)

        if cur is None:
            return default

    return cur


@app.get("/")
def root() -> Dict[str, Any]:
    patients = load_patients()
    config = load_config()

    return {
        "status": "ok",
        "message": "EGFR Lung Cancer Digital Twin API",
        "dashboard": "/dashboard",
        "patients": len(patients),
        "model": config.get("model_version"),
        "clinical_use_statement": config.get("clinical_use_statement"),
        "decision_support_goal": config.get("decision_support_goal"),
    }


@app.get("/health")
def health() -> Dict[str, Any]:
    patients = load_patients()

    return {
        "status": "ok",
        "patients_loaded": len(patients),
        "data_path": str(SIM_DATA_PATH),
        "global_data_path": str(GLOBAL_SIM_DATA_PATH),
        "dashboard_dir": str(DASHBOARD_DIR),
        "data_exists": SIM_DATA_PATH.exists(),
        "global_data_exists": GLOBAL_SIM_DATA_PATH.exists(),
    }


@app.get("/api/config")
def get_config() -> Dict[str, Any]:
    return load_config()


@app.get("/api/simulation/summary")
def simulation_summary() -> Dict[str, Any]:
    patients = load_patients()
    config = load_config()

    if not patients:
        return {
            "status": "empty",
            "patients": 0,
            "message": "No simulation patient data found.",
            "expected_file": str(SIM_DATA_PATH),
        }

    best_drugs = []
    model_versions = []
    sources = []

    for patient in patients:
        best_drugs.append(safe_get(patient, "best_treatment", "drug", default="Unknown"))
        model_versions.append(patient.get("model_version", "Unknown"))
        sources.append(safe_get(patient, "clinical", "source_name", default="Unknown"))

    return {
        "status": "ok",
        "patients": len(patients),
        "model_versions": sorted(list(set(model_versions))),
        "best_treatment_distribution": dict(sorted(
            {drug: best_drugs.count(drug) for drug in set(best_drugs)}.items()
        )),
        "source_distribution": dict(sorted(
            {src: sources.count(src) for src in set(sources)}.items()
        )),
        "clinical_use_statement": config.get("clinical_use_statement"),
        "decision_support_goal": config.get("decision_support_goal"),
        "dataset": config.get("active_dataset"),
    }


@app.get("/api/simulation/patients")
def list_patients() -> List[Dict[str, Any]]:
    patients = load_patients()

    result = []

    for patient in patients:
        clinical = patient.get("clinical", {})
        molecular = patient.get("molecular", {})
        best = patient.get("best_treatment", {})
        kg = patient.get("knowledge_grounding", {})

        result.append({
            "patient_id": patient.get("patient_id"),
            "global_patient_id": patient.get("global_patient_id"),
            "source_name": clinical.get("source_name"),
            "source_group": clinical.get("source_group"),
            "age": clinical.get("age"),
            "age_display": clinical.get("age_display"),
            "sex": clinical.get("sex"),
            "stage": clinical.get("stage"),
            "egfr": molecular.get("alteration_group") or molecular.get("egfr_class") or molecular.get("egfr_raw"),
            "egfr_raw": molecular.get("egfr_raw"),
            "exact_protein_change": molecular.get("exact_protein_change"),
            "best_drug": best.get("drug"),
            "best_score": best.get("final_score"),
            "evidence_count": kg.get("matched_evidence_count", 0),
            "model_version": patient.get("model_version"),
        })

    return result


@app.get("/api/simulation/patient/{patient_id}")
def get_patient(patient_id: str) -> Dict[str, Any]:
    patient = find_patient(patient_id)

    if patient is None:
        raise HTTPException(status_code=404, detail=f"Patient not found: {patient_id}")

    return patient


@app.get("/api/simulation/patient/{patient_id}/ranking")
def get_patient_ranking(patient_id: str) -> Dict[str, Any]:
    patient = find_patient(patient_id)

    if patient is None:
        raise HTTPException(status_code=404, detail=f"Patient not found: {patient_id}")

    return {
        "patient_id": patient.get("patient_id"),
        "ranking": patient.get("ranking", []),
        "best_treatment": patient.get("best_treatment", {}),
    }


@app.get("/api/simulation/patient/{patient_id}/timeline")
def get_patient_timeline(patient_id: str) -> Dict[str, Any]:
    patient = find_patient(patient_id)

    if patient is None:
        raise HTTPException(status_code=404, detail=f"Patient not found: {patient_id}")

    return {
        "patient_id": patient.get("patient_id"),
        "timeline": patient.get("timeline", []),
    }


@app.get("/api/simulation/patient/{patient_id}/pathway")
def get_patient_pathway(patient_id: str) -> Dict[str, Any]:
    patient = find_patient(patient_id)

    if patient is None:
        raise HTTPException(status_code=404, detail=f"Patient not found: {patient_id}")

    return {
        "patient_id": patient.get("patient_id"),
        "pathway_state": patient.get("pathway_state", {}),
        "microenvironment": patient.get("microenvironment", {}),
        "protein_viewer": patient.get("protein_viewer", {}),
    }


@app.get("/dashboard", response_class=HTMLResponse)
def dashboard() -> HTMLResponse:
    for dashboard_file in DASHBOARD_FILE_CANDIDATES:
        if dashboard_file.exists():
            html = dashboard_file.read_text(encoding="utf-8", errors="ignore")
            return HTMLResponse(content=html)

    return HTMLResponse(
        content="""
        <html>
        <body style="font-family:Arial;background:#020617;color:white;padding:30px;">
            <h1>Dashboard file not found</h1>
            <p>Expected one of:</p>
            <ul>
                <li>dashboard/EGFR Lung Cancer Digital Twin.htm</li>
                <li>dashboard/EGFR Lung Cancer Digital Twin.html</li>
                <li>dashboard/index.html</li>
            </ul>
        </body>
        </html>
        """,
        status_code=404,
    )


if DASHBOARD_DIR.exists():
    app.mount("/static-dashboard", StaticFiles(directory=str(DASHBOARD_DIR)), name="static-dashboard")
