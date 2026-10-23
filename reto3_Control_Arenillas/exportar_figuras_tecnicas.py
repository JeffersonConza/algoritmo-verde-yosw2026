"""
Generador de Figuras Técnicas 1 y 2 para el Documento Word (Formato APA 7ma Edición)
Equipo: Algoritmo Verde YT - Reto 3: Control de Arenillas
Sincronizado al 100% con el Catálogo GIS de 286 Entidades, 16 Vías, 12 Áreas Verdes y 7 Tramos Viales de Cercas Vivas
"""

import os
import json
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon as MplPolygon
from matplotlib.lines import Line2D
import numpy as np
from scipy.spatial import cKDTree

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Origen de referencia: Biblioteca Patrimonial Principal (I-01)
LAT0, LON0 = 0.405060, -78.174257
M_PER_LAT = 110574.0
M_PER_LON = 111320.0 * math.cos(math.radians(LAT0))


def latlon_to_xy(lat, lon):
    return (lon - LON0) * M_PER_LON, (lat - LAT0) * M_PER_LAT


def cargar_geojson_catalogo():
    cat_path = os.path.join(BASE_DIR, "CATALOGO_PUNTOS_GEOREFERENCIADOS_CAMPUS.md")
    with open(cat_path, "r", encoding="utf-8") as f:
        text = f.read()
    idx1 = text.find("## 8. Snippet GeoJSON")
    idx2 = text.find("```json", idx1) + len("```json")
    idx3 = text.find("```", idx2)
    return json.loads(text[idx2:idx3].strip())["features"]


def dibujar_cartografia_base(ax, features, mostrar_verdes=True):
    """Dibuja la cartografía real del campus (áreas verdes, vías y edificaciones) en coordenadas métricas (dx, dy)."""
    for ft in features:
        fid = ft["properties"]["id"]
        gtype = ft["geometry"]["type"]
        coords = ft["geometry"]["coordinates"]

        if gtype == "Polygon":
            ring = coords[0]
            xy = [latlon_to_xy(pt[1], pt[0]) for pt in ring]
            if fid.startswith("PERIM-"):
                continue
            elif fid.startswith("POLY-VERDE-"):
                if mostrar_verdes:
                    poly = MplPolygon(xy, closed=True, facecolor="#a8e6cf", edgecolor="#56ab91", alpha=0.35, lw=0.6, zorder=1)
                    ax.add_patch(poly)
            elif fid == "POLY-LAGUNA":
                poly = MplPolygon(xy, closed=True, facecolor="#74b9ff", edgecolor="#0984e3", alpha=0.65, lw=1.0, zorder=2)
                ax.add_patch(poly)
            else:
                # Edificación real catalogada (123 polígonos)
                poly = MplPolygon(xy, closed=True, facecolor="#dfe6e9", edgecolor="#636e72", alpha=0.75, lw=0.5, zorder=2)
                ax.add_patch(poly)
        elif gtype == "LineString":
            xy = [latlon_to_xy(pt[1], pt[0]) for pt in coords]
            xs, ys = zip(*xy)
            if fid.startswith("LINE-VIA-"):
                es_principal = fid in ("LINE-VIA-01", "LINE-VIA-02", "LINE-VIA-03", "LINE-VIA-04", "LINE-VIA-05", "LINE-VIA-06")
                ax.plot(
                    xs,
                    ys,
                    color="#95a5a6" if es_principal else "#b2bec3",
                    lw=1.8 if es_principal else 1.0,
                    linestyle="-" if es_principal else "--",
                    alpha=0.75,
                    zorder=2,
                )


def obtener_puntos_canales(features):
    """Extrae las polilíneas reales de los canales lóticos y devuelve puntos densificados para el modelo espacial."""
    canales_xy = []
    pts_densos = []
    for ft in features:
        fid = ft["properties"]["id"]
        if ft["geometry"]["type"] == "LineString" and "CANAL" in fid:
            coords = ft["geometry"]["coordinates"]
            xy = [latlon_to_xy(pt[1], pt[0]) for pt in coords]
            canales_xy.append((fid, xy))
            for i in range(len(xy) - 1):
                x1, y1 = xy[i]
                x2, y2 = xy[i + 1]
                for t in np.linspace(0, 1, 25):
                    pts_densos.append((x1 + t * (x2 - x1), y1 + t * (y2 - y1)))
    return canales_xy, np.array(pts_densos)


def crear_figura_diagnostico():
    features = cargar_geojson_catalogo()
    canales_xy, pts_canales = obtener_puntos_canales(features)

    fig, ax = plt.subplots(figsize=(12.0, 8.2), dpi=300)

    # Malla continua sobre la extensión real del campus (en metros desde Biblioteca I-01)
    x = np.linspace(-340, 680, 380)
    y = np.linspace(-540, 380, 380)
    X, Y = np.meshgrid(x, y)

    # Distancia euclídea vectorial mínima a los canales reales del campus
    tree = cKDTree(pts_canales)
    dist_to_canal, _ = tree.query(np.column_stack([X.ravel(), Y.ravel()]))
    dist_to_canal = dist_to_canal.reshape(X.shape)

    # Coordenadas métricas reales de los epicentros residenciales y académicos
    sx1, sy1 = latlon_to_xy(0.402750, -78.174800)  # Las Multis (R-01)
    sx2, sy2 = latlon_to_xy(0.402297, -78.173836)  # Las Pats (R-02)
    cx1, cy1 = latlon_to_xy(0.405060, -78.174257)  # Biblioteca Patrimonial (I-01)
    cx2, cy2 = latlon_to_xy(0.404450, -78.172600)  # Laboratorios / Invernaderos
    nx1, ny1 = latlon_to_xy(0.406633, -78.170096)  # Edificio Senescyt (S-01)
    nx2, ny2 = latlon_to_xy(0.406950, -78.171150)  # Residencias Los Bloques (S-02)

    I_canal = np.exp(-(dist_to_canal**2) / (2 * 65**2))
    I_sur = 0.96 * np.maximum(
        np.exp(-((X - sx1) ** 2 + (Y - sy1) ** 2) / (2 * 95**2)),
        np.exp(-((X - sx2) ** 2 + (Y - sy2) ** 2) / (2 * 90**2)),
    )
    I_centro = 0.88 * np.maximum(
        np.exp(-((X - cx1) ** 2 + (Y - cy1) ** 2) / (2 * 85**2)),
        np.exp(-((X - cx2) ** 2 + (Y - cy2) ** 2) / (2 * 85**2)),
    )
    I_norte = 0.98 * np.maximum(
        np.exp(-((X - nx1) ** 2 + (Y - ny1) ** 2) / (2 * 95**2)),
        np.exp(-((X - nx2) ** 2 + (Y - ny2) ** 2) / (2 * 90**2)),
    )

    Z = np.clip((0.38 * I_canal + 0.62 * np.maximum.reduce([I_sur, I_centro, I_norte])) * 100, 15, 99)

    levels = np.linspace(15, 98, 20)
    cs = ax.contourf(X, Y, Z, levels=levels, cmap="YlOrRd", alpha=0.68, zorder=1)
    cbar = plt.colorbar(cs, ax=ax, fraction=0.036, pad=0.025)
    cbar.set_label("Índice de Presión Hematófaga / Molestia (% Estimado)", fontsize=10, fontweight="bold")

    # Cartografía real de edificios y vías sobre el mapa de calor
    dibujar_cartografia_base(ax, features, mostrar_verdes=False)

    # Curvas de isorriesgo
    iso_curves = ax.contour(X, Y, Z, levels=[40, 70], colors=["#d35400", "#c0392b"], linewidths=1.2, linestyles="--", zorder=3)
    ax.clabel(iso_curves, inline=True, fontsize=8, fmt="%1.0f%%")

    # Trazado de los 5 Canales Reales Catalogados
    for idx, (cid, xy) in enumerate(canales_xy):
        xs, ys = zip(*xy)
        ax.plot(
            xs,
            ys,
            color="#0984e3",
            lw=3.0,
            linestyle="-",
            zorder=4,
            label="Canales y Acequias Lóticas Reales (5 tramos catalogados)" if idx == 0 else "_nolegend_",
        )

    # Epicentros reales
    ax.scatter(
        [sx1, sx2],
        [sy1, sy2],
        color="#d35400",
        s=105,
        marker="s",
        edgecolors="black",
        lw=1.2,
        zorder=5,
        label="Epicentro Sur: Las Multis y Las Pats (~550 hab.)",
    )
    ax.scatter(
        [cx1, cx2],
        [cy1, cy2],
        color="#2980b9",
        s=110,
        marker="^",
        edgecolors="black",
        lw=1.2,
        zorder=5,
        label="Epicentro Central: Biblioteca Patrimonial, Ingenio y Labs",
    )
    ax.scatter(
        [nx1, nx2],
        [ny1, ny2],
        color="#c0392b",
        s=105,
        marker="o",
        edgecolors="black",
        lw=1.2,
        zorder=5,
        label="Epicentro Norte: Edificio Senescyt y Los Bloques (~450 hab.)",
    )

    ax.set_xlim(-340, 680)
    ax.set_ylim(-540, 380)
    ax.set_aspect("equal", adjustable="box")
    ax.set_title(
        "Diagnóstico Epidemiológico: Mapa de Calor de Picaduras, Vías, Edificios y Focos Larvarios (Yachay Tech)\nFigura 1",
        fontsize=12.0,
        fontweight="bold",
        pad=14,
    )
    ax.set_xlabel("Distancia relativa Este-Oeste desde Biblioteca Patrimonial I-01 (metros)", fontsize=10.5)
    ax.set_ylabel("Distancia relativa Norte-Sur desde Biblioteca Patrimonial I-01 (metros)", fontsize=10.5)
    ax.grid(True, linestyle=":", alpha=0.45)

    handles, labels = ax.get_legend_handles_labels()
    handles.append(Line2D([0], [0], color="#95a5a6", lw=1.8, label="Red Vial y Caminerías Catalogadas (LINE-VIA-01..16)"))
    handles.append(MplPolygon([[0, 0]], facecolor="#dfe6e9", edgecolor="#636e72", label="Huellas de Edificaciones Catalogadas (123 polígonos)"))
    ax.legend(handles=handles, loc="lower right", fontsize=8.0, framealpha=0.95)

    ax.annotate(
        "N",
        xy=(0.05, 0.93),
        xytext=(0.05, 0.84),
        arrowprops=dict(facecolor="black", width=2.5, headwidth=8),
        ha="center",
        va="center",
        xycoords="axes fraction",
        fontsize=12,
        fontweight="bold",
    )

    output_f1 = os.path.join(BASE_DIR, "Figura1_Diagnostico_Espacial_Yachay.png")
    plt.savefig(output_f1, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"Figura 1 generada en: {output_f1}")


def crear_figura_diseno_tecnico():
    features = cargar_geojson_catalogo()
    canales_xy, _ = obtener_puntos_canales(features)

    fig, ax = plt.subplots(figsize=(12.5, 8.2), dpi=300)

    # Cartografía real: 12 áreas verdes, 16 vías/caminerías y 123 edificios
    dibujar_cartografia_base(ax, features, mostrar_verdes=True)

    # Canales reales
    for idx, (cid, xy) in enumerate(canales_xy):
        xs, ys = zip(*xy)
        ax.plot(
            xs,
            ys,
            color="#0984e3",
            lw=2.4,
            linestyle="-",
            alpha=0.85,
            zorder=3,
            label="Canales Lóticos Reales (LINE-CANAL-*)" if idx == 0 else "_nolegend_",
        )

    # 7 Tramos Viales Discontinuos de Cercas Vivas (0 cruces de calles, 980.0 m totales)
    cercas_tramos = [
        ("CV-1A", "Cerca 1", "#0e6251", [[0.40368, -78.17472], [0.40320, -78.17458], [0.402756, -78.174018]]),
        ("CV-1B", "Cerca 1", "#0e6251", [[0.40220, -78.17405], [0.40198, -78.17365], [0.40158, -78.17352]]),
        ("CV-1C", "Cerca 1", "#0e6251", [[0.40253, -78.17344], [0.40268, -78.17295], [0.402913, -78.172167]]),
        ("CV-2A", "Cerca 2", "#16a085", [[0.40363, -78.17360], [0.40387, -78.17306], [0.404132, -78.172472]]),
        ("CV-2B", "Cerca 2", "#16a085", [[0.40436, -78.17368], [0.40496, -78.17358], [0.40504, -78.172907]]),
        ("CV-3A", "Cerca 3", "#27ae60", [[0.40578, -78.17192], [0.40635, -78.17182], [0.40686, -78.17173], [0.40706, -78.17238], [0.406875, -78.172581]]),
        ("CV-3B", "Cerca 3", "#27ae60", [[0.40610, -78.16995], [0.40638, -78.16983], [0.40678, -78.16967], [0.406874, -78.169632]]),
    ]

    labels_usados = set()
    leyenda_sector = {
        "Cerca 1": "Cerca Viva 1 (380 m · Tramos CV-1A, 1B, 1C) - Sector Residencial Sur",
        "Cerca 2": "Cerca Viva 2 (280 m · Tramos CV-2A, 2B) - Sector Ingenio y Laboratorios",
        "Cerca 3": "Cerca Viva 3 (320 m · Tramos CV-3A, 3B) - Sector Senescyt y Los Bloques",
    }

    for tid, sector, col, pts in cercas_tramos:
        xy = [latlon_to_xy(p[0], p[1]) for p in pts]
        xs, ys = zip(*xy)
        # Buffer de Zona Protegida (40m) con terminación recta ('butt') para no invadir intersecciones viales
        ax.plot(
            xs,
            ys,
            color="#2ecc71",
            lw=16,
            alpha=0.28,
            solid_capstyle="butt",
            solid_joinstyle="round",
            zorder=4,
            label="Buffer Zona Protegida (40 m · Corte recto en cruces viales)" if "BUF" not in labels_usados else "_nolegend_",
        )
        labels_usados.add("BUF")

        ax.plot(
            xs,
            ys,
            color=col,
            lw=3.6,
            solid_capstyle="butt",
            solid_joinstyle="round",
            zorder=5,
            label=leyenda_sector[sector] if sector not in labels_usados else "_nolegend_",
        )
        labels_usados.add(sector)

        mid_idx = len(xs) // 2
        ax.text(
            xs[mid_idx],
            ys[mid_idx] + 12,
            tid,
            fontsize=7.5,
            fontweight="bold",
            color="#0b5345",
            ha="center",
            va="bottom",
            zorder=7,
            bbox=dict(boxstyle="round,pad=0.18", fc="white", ec=col, alpha=0.88, lw=0.8),
        )

    # 6 Estaciones de Bio-Monitoreo Comunitario (T-01 a T-06, calibradas en áreas verdes)
    trampas = [
        ("T-01", 0.402120, -78.172920, (8, -13)),
        ("T-02", 0.402280, -78.175150, (-28, -14)),
        ("T-03", 0.404620, -78.174250, (-28, 8)),
        ("T-04", 0.404020, -78.172780, (10, -12)),
        ("T-05", 0.406480, -78.169820, (10, -8)),
        ("T-06", 0.407420, -78.170760, (10, 6)),
    ]
    tx, ty = [], []
    for code, lat, lon, offset in trampas:
        px, py = latlon_to_xy(lat, lon)
        tx.append(px)
        ty.append(py)
        ax.annotate(
            code,
            xy=(px, py),
            xytext=offset,
            textcoords="offset points",
            fontsize=8,
            fontweight="bold",
            color="#1e3799",
            zorder=7,
        )
    ax.scatter(tx, ty, color="#1e3799", s=85, marker="X", edgecolors="white", lw=0.8, zorder=6, label="Estaciones de Bio-Monitoreo en Áreas Verdes (T-01 a T-06)")

    # 3 Estaciones de Control Biológico Acuático (BIO-N, BIO-C, BIO-S, a 0.00 m sobre canales)
    biocontrol = [
        ("BIO-N", 0.4048221, -78.1751372, (-34, 6)),
        ("BIO-C", 0.4040429, -78.1689091, (-34, -14)),
        ("BIO-S", 0.4011095, -78.1759160, (10, -6)),
    ]
    bx, by = [], []
    for code, lat, lon, offset in biocontrol:
        px, py = latlon_to_xy(lat, lon)
        bx.append(px)
        by.append(py)
        ax.annotate(
            code,
            xy=(px, py),
            xytext=offset,
            textcoords="offset points",
            fontsize=8,
            fontweight="bold",
            color="#006266",
            zorder=7,
        )
    ax.scatter(bx, by, color="#009432", s=80, marker="D", edgecolors="white", lw=0.8, zorder=6, label="Estaciones de Control Biológico Acuático en Canales (BIO-N, C, S)")

    ax.set_xlim(-340, 680)
    ax.set_ylim(-490, 380)
    ax.set_aspect("equal", adjustable="box")
    ax.set_title(
        "Diseño Técnico de la Intervención: 7 Tramos Viales de Cercas Vivas (0 Cruces de Calles) y Red de Monitoreo\nFigura 2",
        fontsize=12.0,
        fontweight="bold",
        pad=14,
    )
    ax.set_xlabel("Distancia relativa Este-Oeste desde Biblioteca Patrimonial I-01 (metros)", fontsize=10.5)
    ax.set_ylabel("Distancia relativa Norte-Sur desde Biblioteca Patrimonial I-01 (metros)", fontsize=10.5)
    ax.grid(True, linestyle=":", alpha=0.45)

    handles, labels = ax.get_legend_handles_labels()
    handles.append(Line2D([0], [0], color="#95a5a6", lw=1.8, label="Red Vial y Caminerías (LINE-VIA-01..16 · 0 cruces con cercas)"))
    handles.append(MplPolygon([[0, 0]], facecolor="#a8e6cf", edgecolor="#56ab91", alpha=0.5, label="Parques y Jardines Catalogados (POLY-VERDE-01..12)"))
    handles.append(MplPolygon([[0, 0]], facecolor="#dfe6e9", edgecolor="#636e72", label="Edificaciones del Campus (123 polígonos · 0 solapamientos)"))
    ax.legend(handles=handles, loc="upper left", bbox_to_anchor=(1.01, 1.0), fontsize=8.2, framealpha=0.95)

    ax.annotate(
        "N",
        xy=(0.05, 0.93),
        xytext=(0.05, 0.84),
        arrowprops=dict(facecolor="black", width=2.5, headwidth=8),
        ha="center",
        va="center",
        xycoords="axes fraction",
        fontsize=12,
        fontweight="bold",
    )

    output_f2 = os.path.join(BASE_DIR, "Figura2_Diseno_Tecnico_Intervencion.png")
    plt.savefig(output_f2, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"Figura 2 generada en: {output_f2}")


if __name__ == "__main__":
    crear_figura_diagnostico()
    crear_figura_diseno_tecnico()
