"""
API REST de Telemetría y Optimización - Reto N° 6: Control de Arenillas
Equipo: Algoritmo Verde YT | Yachay Open Science Week 2026
Compatible con despliegues en Azure / Heroku / Appwrite (GitHub Student Pack)
"""

import json
import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(
    title="Algoritmo Verde YT - Telemetría API",
    description="API de monitoreo biológico y optimización espacial para el control ecológico de arenillas en Yachay Tech.",
    version="1.0.0"
)

# Permitir CORS para consultas desde el visor web interactivo o aplicaciones móviles
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_OPTIMIZACION = os.path.join(BASE_DIR, "datos_optimizacion_cercas.json")
FILE_TELEMETRIA = os.path.join(BASE_DIR, "telemetria_trampas_simulada.json")

class NuevaLectura(BaseModel):
    estacion_id: str
    semana: int
    capturas: int
    temperatura_c: Optional[float] = 22.5
    humedad_pct: Optional[float] = 65.0
    notas: Optional[str] = None

@app.get("/", tags=["General"])
def root():
    return {
        "proyecto": "Algoritmo Verde YT",
        "evento": "Yachay Open Science Week 2026",
        "reto": "Reto N° 6 - Manejo Integrado de Arenillas",
        "docs": "/docs",
        "status": "healthy"
    }

@app.get("/api/v1/metrics", tags=["Métricas"])
def get_metrics():
    """Retorna las métricas consolidadas del sistema de cercas vivas y protección."""
    if not os.path.exists(FILE_OPTIMIZACION):
        raise HTTPException(status_code=404, detail="Datos de optimización no encontrados.")
    with open(FILE_OPTIMIZACION, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

@app.get("/api/v1/stations", tags=["Estaciones de Bio-Monitoreo"])
def get_stations():
    """Lista las 6 estaciones de monitoreo biológico georreferenciadas."""
    if not os.path.exists(FILE_TELEMETRIA):
        raise HTTPException(status_code=404, detail="Datos de telemetría no encontrados.")
    with open(FILE_TELEMETRIA, "r", encoding="utf-8") as f:
        data = json.load(f)
    return {"total": len(data.get("estaciones", [])), "estaciones": data.get("estaciones", [])}

@app.get("/api/v1/telemetry", tags=["Telemetría"])
def get_telemetry(estacion_id: Optional[str] = None, semana: Optional[int] = None):
    """Retorna la serie temporal de capturas. Permite filtrar por ID de estación o semana."""
    if not os.path.exists(FILE_TELEMETRIA):
        raise HTTPException(status_code=404, detail="Datos de telemetría no encontrados.")
    with open(FILE_TELEMETRIA, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    series = data.get("series_temporales", [])
    if estacion_id:
        series = [s for s in series if s["estacion_id"].upper() == estacion_id.upper()]
    if semana:
        series = [s for s in series if s["semana"] == semana]
        
    return {"total_registros": len(series), "lecturas": series}

@app.post("/api/v1/telemetry", tags=["Telemetría"], status_code=201)
def registrar_lectura(lectura: NuevaLectura):
    """Endpoint de ingesta para registrar nuevas observaciones de campo."""
    return {
        "status": "success",
        "mensaje": f"Lectura registrada para {lectura.estacion_id} en semana {lectura.semana}",
        "data": lectura.dict()
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api_telemetria:app", host="0.0.0.0", port=8000, reload=True)
