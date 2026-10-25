"""
Suite de Pruebas Automatizadas para la API de Telemetría y Optimización
Equipo: Algoritmo Verde YT | Yachay Open Science Week 2026
Framework: pytest + fastapi.testclient.TestClient
"""

import os
import sys
import shutil
import pytest
from fastapi.testclient import TestClient

# Asegurar que el módulo api_telemetria sea importable
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

import api_telemetria
from api_telemetria import app

client = TestClient(app)

@pytest.fixture(autouse=True)
def isolate_telemetry_storage(tmp_path, monkeypatch):
    """
    Aísla el archivo de persistencia de telemetría en un directorio temporal
    para evitar mutaciones en el repositorio durante las pruebas POST.
    """
    original_file = api_telemetria.FILE_TELEMETRIA
    if os.path.exists(original_file):
        temp_file = str(tmp_path / "telemetria_temp.json")
        shutil.copy2(original_file, temp_file)
        monkeypatch.setattr(api_telemetria, "FILE_TELEMETRIA", temp_file)
    yield
    # Monkeypatch se revierte automáticamente al finalizar cada test


def test_root_endpoint():
    """Verifica el endpoint raíz y metadatos de autoría."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["proyecto"] == "Algoritmo Verde YT"
    assert "Reto N° 6" in data["reto"]
    assert "openapi_docs" in data
    assert "uptime_segundos" in data

def test_health_check_endpoint():
    """Verifica el diagnóstico de salud, almacenamiento y probes de readiness."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "timestamp" in data
    assert data["almacenamiento"]["telemetria_presente"] is True
    assert data["almacenamiento"]["optimizacion_presente"] is True
    assert data["almacenamiento"]["total_registros_telemetria"] > 0

def test_get_metrics():
    """Verifica la recuperación de métricas de optimización matemática SLSQP."""
    response = client.get("/api/v1/metrics")
    assert response.status_code == 200
    data = response.json()
    params = data["parametros_sistema"]
    assert params["longitud_total_m"] == 980
    assert params["costo_total_usd"] == 1470.0
    assert params["total_plantulas"] == 1960
    assert len(data["cercas_optimizadas"]) == 3

def test_get_stations():
    """Verifica el listado de las 6 estaciones de bio-monitoreo georreferenciadas."""
    response = client.get("/api/v1/stations")
    assert response.status_code == 200
    data = response.json()
    assert data["total"] == 6
    ids = [e["id"] for e in data["estaciones"]]
    assert ids == ["T-01", "T-02", "T-03", "T-04", "T-05", "T-06"]
    for e in data["estaciones"]:
        assert "lat" in e and "lon" in e
        assert e["base"] > 0
        assert e["estado_operativo"] == "Operativa"

def test_get_station_detail_valid():
    """Verifica el detalle individual de una estación y su historial temporal."""
    response = client.get("/api/v1/stations/T-02")
    assert response.status_code == 200
    data = response.json()
    assert data["estacion"]["id"] == "T-02"
    assert "Las Multis" in data["estacion"]["nombre"]
    assert data["total_lecturas"] >= 16

def test_get_station_detail_invalid():
    """Verifica rechazo 422 para códigos de estación fuera del regex ^T-0[1-6]$."""
    response = client.get("/api/v1/stations/T-99")
    assert response.status_code == 422

def test_get_telemetry_filters():
    """Verifica consultas de telemetría con filtrado por estación y rango de semanas."""
    response = client.get("/api/v1/telemetry?estacion_id=T-03&semana_min=5&semana_max=8")
    assert response.status_code == 200
    data = response.json()
    assert data["total_registros"] == 4
    for item in data["lecturas"]:
        assert item["estacion_id"] == "T-03"
        assert 5 <= item["semana"] <= 8

def test_post_telemetry_ingestion():
    """Verifica el registro atómico de una nueva lectura de campo y cálculo de reducción."""
    payload = {
        "estacion_id": "T-01",
        "semana": 17,
        "capturas": 12,
        "temperatura_c": 21.8,
        "humedad_pct": 68.0,
        "viento_ms": 2.4,
        "notas": "Muestreo entomológico de verificación post-consolidación"
    }
    response = client.post("/api/v1/telemetry", json=payload)
    assert response.status_code == 201
    res = response.json()
    assert res["status"] == "success"
    reg = res["registro"]
    assert reg["estacion_id"] == "T-01"
    assert reg["capturas_semanales"] == 12
    assert reg["fase"] == "Consolidación Ecosistémica"
    assert reg["reduccion_pct"] > 80.0

def test_post_telemetry_validation_negative_captures():
    """Verifica rechazo 422 si se envían capturas negativas."""
    payload = {
        "estacion_id": "T-01",
        "semana": 18,
        "capturas": -5
    }
    response = client.post("/api/v1/telemetry", json=payload)
    assert response.status_code == 422

def test_analytics_summary_ttest():
    """Verifica el motor inferencial SciPy: t-test pareado, p-valor e intervalo al 95%."""
    response = client.get("/api/v1/analytics/summary")
    assert response.status_code == 200
    data = response.json()
    ttest = data["prueba_t_student_pareada"]
    assert ttest["estadistico_t"] > 20.0
    assert ttest["p_valor"] < 0.001
    assert ttest["es_estadisticamente_significativo"] is True
    metrics = data["metricas_captura"]
    assert metrics["reduccion_lograda_pct"] > 80.0
    assert "conclusion_apa" in data

def test_analytics_plume_dispersion():
    """Verifica el modelo de dispersión de pluma terpénica gaussiana."""
    # Distancia dentro de la zona de confort (20 m)
    r1 = client.get("/api/v1/analytics/plume?distancia_m=20.0&viento_ms=2.8")
    assert r1.status_code == 200
    d1 = r1.json()
    assert d1["concentracion_volatiles_ug_m3"] > 25.0
    assert d1["eficacia_repelente_activa"] is True
    assert d1["zona_confort_humano"] is True

    # Distancia lejana (80 m)
    r2 = client.get("/api/v1/analytics/plume?distancia_m=80.0&viento_ms=2.8")
    assert r2.status_code == 200
    d2 = r2.json()
    assert d2["concentracion_volatiles_ug_m3"] < 25.0
    assert d2["eficacia_repelente_activa"] is False

def test_optimization_slsqp_simulation():
    """Verifica la ejecución dinámica del solver SLSQP con presupuesto ampliado."""
    payload = {
        "presupuesto_max_usd": 2000.0,
        "costo_metro_usd": 1.50,
        "longitud_max_m": 1200.0,
        "k_atenuacion": 0.0075
    }
    response = client.post("/api/v1/optimization/simulate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["convergencia"] is True
    sol = data["solucion_optima"]
    assert sol["longitud_total_m"] > 980
    assert sol["costo_total_usd"] <= 2000.0
    assert len(sol["desglose_por_sector"]) == 3

def test_timeline_endpoint():
    """Verifica la estructura y metadatos de las 5 fases de la línea de tiempo."""
    response = client.get("/api/v1/timeline")
    assert response.status_code == 200
    data = response.json()
    assert data["duracion_total_semanas"] == 16
    assert len(data["fases"]) == 5
    fase_ids = [f["id"] for f in data["fases"]]
    assert fase_ids == ["T0", "T1", "T2", "T3", "T4"]
    t4 = data["fases"][4]
    assert t4["mitigacion_pct"] == 82.8
    assert t4["presupuesto_acumulado_usd"] == 1470.0

def test_geojson_export():
    """Verifica la exportación en estándar RFC 7946 GeoJSON para QGIS y ArcGIS."""
    for ltype in ["stations", "fences", "epicenters"]:
        response = client.get(f"/api/v1/geojson/{ltype}")
        assert response.status_code == 200
        geo = response.json()
        assert geo["type"] == "FeatureCollection"
        assert len(geo["features"]) > 0
        feat = geo["features"][0]
        assert "geometry" in feat and "properties" in feat

def test_geojson_invalid_layer():
    """Verifica error 400 para capa no reconocida."""
    response = client.get("/api/v1/geojson/inexistente")
    assert response.status_code == 400

def test_process_time_header():
    """Verifica la presencia del encabezado X-Process-Time-Ms de telemetría interna."""
    response = client.get("/health")
    assert "x-process-time-ms" in response.headers
    dur = float(response.headers["x-process-time-ms"])
    assert dur >= 0.0
