"""
Generador de la Presentación Oficial PDF (12 Diapositivas · Widescreen 16:9)
Archivo de salida: Ideaton_Reto6_AlgoritmoVerdeYT.pdf
Equipo: Algoritmo Verde YT | Yachay Open Science Week 2026 (Ideatón)
Tipografía de Gran Tamaño (Auditorium-Ready) para lectura clara a distancia.
"""

import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.backends.backend_pdf import PdfPages
from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))
OUT_PDF = os.path.join(BASE_DIR, "Ideaton_Reto6_AlgoritmoVerdeYT.pdf")
ROOT_PDF = os.path.join(ROOT_DIR, "Ideaton_Reto6_AlgoritmoVerdeYT.pdf")
CHAT_PDF = os.path.join(ROOT_DIR, "WhatsApp Chat with Ideaton", "Ideaton_Reto6_AlgoritmoVerdeYT.pdf")

plt.rcParams["font.family"] = "DejaVu Sans"

# Paleta Institucional Algoritmo Verde YT
C_NAVY = "#0f172a"
C_BLUE = "#1e3799"
C_GREEN = "#10ac84"
C_GREEN_DARK = "#0b7a5e"
C_GREEN_LIGHT = "#e8f8f5"
C_BLUE_LIGHT = "#eef2ff"
C_AMBER = "#d35400"
C_AMBER_LIGHT = "#fef5e7"
C_RED = "#c0392b"
C_RED_LIGHT = "#fdedec"
C_TEXT = "#1e293b"
C_MUTED = "#475569"
C_BG = "#f8fafc"
C_WHITE = "#ffffff"
C_BORDER = "#cbd5e1"


def new_slide(slide_num, total_slides=12, title="", subtitle="", badge=""):
    """Crea un lienzo Widescreen 16:9 estándar PowerPoint (13.333 x 7.5 in) con coordenadas [0..16, 0..9]."""
    fig = plt.figure(figsize=(13.333, 7.5), dpi=220)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)
    ax.axis("off")

    ax.add_patch(patches.Rectangle((0, 0), 16, 9, facecolor=C_BG, edgecolor="none"))

    if slide_num > 1:
        # Barra superior institucional
        ax.add_patch(patches.Rectangle((0, 7.92), 16, 1.08, facecolor=C_NAVY, edgecolor="none"))
        ax.add_patch(patches.Rectangle((0, 7.84), 16, 0.08, facecolor=C_GREEN, edgecolor="none"))

        if badge:
            ax.add_patch(patches.FancyBboxPatch(
                (0.40, 8.24), 2.35, 0.48,
                boxstyle="round,pad=0.03,rounding_size=0.12",
                facecolor=C_GREEN, edgecolor="none"
            ))
            ax.text(1.575, 8.48, badge, color=C_WHITE, fontsize=12.0, fontweight="bold", ha="center", va="center")
            title_x = 2.95
        else:
            title_x = 0.45

        ax.text(title_x, 8.60, title, color=C_WHITE, fontsize=17.5, fontweight="bold", ha="left", va="center")
        if subtitle:
            ax.text(title_x, 8.16, subtitle, color="#cbd5e1", fontsize=12.0, ha="left", va="center")

        # Pie de diapositiva
        ax.add_patch(patches.Rectangle((0, 0), 16, 0.46, facecolor="#e2e8f0", edgecolor="none"))
        ax.text(0.45, 0.23, "◆ Algoritmo Verde YT  |  Universidad Yachay Tech · Ideatón YOSW 2026",
                color=C_NAVY, fontsize=11.0, fontweight="bold", ha="left", va="center")
        ax.text(15.55, 0.23, f"{slide_num} / {total_slides}",
                color=C_NAVY, fontsize=11.5, fontweight="bold", ha="right", va="center")

    return fig, ax


def draw_card(ax, x, y, w, h, title="", title_color=C_BLUE, bg=C_WHITE, ec=C_BORDER, accent_left=None, title_size=14.5):
    """Dibuja una tarjeta con encabezados grandes y legibles."""
    card = patches.FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.02,rounding_size=0.15",
        facecolor=bg, edgecolor=ec, linewidth=1.5
    )
    ax.add_patch(card)
    if accent_left:
        bar = patches.FancyBboxPatch(
            (x, y + 0.05), 0.13, h - 0.10,
            boxstyle="round,pad=0.0,rounding_size=0.05",
            facecolor=accent_left, edgecolor="none"
        )
        ax.add_patch(bar)
    if title:
        tx = x + (0.32 if accent_left else 0.24)
        ax.text(tx, y + h - 0.40, title, color=title_color, fontsize=title_size, fontweight="bold", ha="left", va="center")


def place_image(fig, img_path, rect):
    """Inserta una imagen dentro de rect = [left_in_16, bottom_in_9, w_in_16, h_in_9]."""
    if not os.path.exists(img_path):
        return
    ax_img = fig.add_axes([rect[0] / 16.0, rect[1] / 9.0, rect[2] / 16.0, rect[3] / 9.0])
    img = Image.open(img_path)
    ax_img.imshow(img)
    ax_img.axis("off")


def generar_presentacion():
    import shutil
    import tempfile
    total_slides = 12
    tmp_pdf = os.path.join(tempfile.gettempdir(), "Ideaton_Reto6_AlgoritmoVerdeYT.pdf")

    with PdfPages(tmp_pdf) as pdf:
        # =========================================================================
        # DIAPOSITIVA 1: PORTADA INSTITUCIONAL Y EQUIPO MULTIDISCIPLINARIO
        # =========================================================================
        fig, ax = new_slide(1, total_slides)
        ax.add_patch(patches.Rectangle((0, 0), 16, 9, facecolor=C_NAVY, edgecolor="none"))
        ax.add_patch(patches.Polygon([[10.2, 9], [16, 9], [16, 0], [8.0, 0]], closed=True, facecolor="#162447", alpha=0.80))
        ax.add_patch(patches.Rectangle((0, 8.80), 16, 0.20, facecolor=C_GREEN, edgecolor="none"))
        ax.add_patch(patches.Rectangle((0, 0), 16, 0.16, facecolor=C_GREEN, edgecolor="none"))

        # Badge superior
        ax.add_patch(patches.FancyBboxPatch(
            (0.65, 7.72), 7.2, 0.56,
            boxstyle="round,pad=0.03,rounding_size=0.15",
            facecolor=C_GREEN, edgecolor="none"
        ))
        ax.text(4.25, 8.00, "YACHAY OPEN SCIENCE WEEK 2026 · IDEATÓN",
                color=C_WHITE, fontsize=13.5, fontweight="bold", ha="center", va="center")

        # Título Principal Grande
        ax.text(0.65, 6.72, "CONTROL ECOSISTÉMICO DE ARENILLAS\nEN EL CAMPUS DE YACHAY TECH",
                color=C_WHITE, fontsize=25.5, fontweight="bold", ha="left", va="center", linespacing=1.22)

        ax.text(0.65, 5.55, "Cercas Vivas en 3 Estratos, Biocontrol (Odonatos + Bti)\ny Optimización Espacial SLSQP sobre 286 Entidades SIG",
                color="#6ee7b7", fontsize=15.0, fontweight="bold", ha="left", va="center", linespacing=1.30)

        # Tarjeta de Integrantes (Letra grande)
        draw_card(ax, 0.65, 1.95, 9.85, 3.15,
                  title="■ EQUIPO «ALGORITMO VERDE YT»  |  Mentor: Ing. José Luis Flores M.Sc.",
                  title_color="#38bdf8", bg="#1e293b", ec="#334155", accent_left=C_GREEN, title_size=13.5)

        miembros = [
            ("JC", "Jefferson Conza", "Matemáticas / Computación", "Líder Técnico · Optimización SLSQP y Catálogo SIG", C_BLUE),
            ("CP", "Christopher Picuasi", "Computación, 3.er sem.", "Desarrollo de Software · Visor Web Interactivo y UI/UX", C_GREEN),
            ("FI", "Francisco Ibujés", "Química, 2.º sem.", "Fitoquímica · Monoterpenos, Riego a Gravedad y Costos", C_AMBER),
            ("LC", "Luis Collaguazo", "Biomedicina, 2.º sem.", "Entomología y Salud · Complejo Díptero y Biocontrol", "#8e44ad"),
        ]
        for idx, (ini, nom, car, rol, col) in enumerate(miembros):
            yy = 4.25 - idx * 0.68
            ax.add_patch(patches.Circle((1.18, yy), radius=0.25, facecolor=col, edgecolor=C_WHITE, lw=1.3))
            ax.text(1.18, yy, ini, color=C_WHITE, fontsize=11.5, fontweight="bold", ha="center", va="center")
            ax.text(1.58, yy + 0.11, f"{nom}  ({car})", color=C_WHITE, fontsize=12.5, fontweight="bold", ha="left", va="center")
            ax.text(1.58, yy - 0.15, rol, color="#cbd5e1", fontsize=11.0, ha="left", va="center")

        # Panel derecho: QR hacia GitHub
        draw_card(ax, 10.80, 1.95, 4.55, 5.45,
                  title="■ ESCANEA EL QR (GITHUB)",
                  title_color=C_WHITE, bg="#1e293b", ec=C_GREEN, title_size=14.0)
        place_image(fig, os.path.join(BASE_DIR, "qr_algoritmo_verde.png"), [11.62, 3.22, 2.9, 2.9])
        ax.text(13.07, 2.75, "github.com/JeffersonConza/\nalgoritmo-verde-yosw2026",
                color="#6ee7b7", fontsize=11.5, fontweight="bold", ha="center", va="center")
        ax.text(13.07, 2.18, "Incluye botón directo al\nMapa Interactivo en Vivo",
                color="#f1f5f9", fontsize=11.0, ha="center", va="center")

        # Franja inferior de 5 KPIs con números grandes
        kpis = [
            ("980 m", "7 Tramos Viales", C_GREEN),
            ("-82.8%", "Mitigación (p<0.001)", "#38bdf8"),
            ("USD 1,470", "Costo Total ($1.50/m)", "#f59e0b"),
            ("124 Edif.", "+800 Personas", "#a855f7"),
            ("0% Químicos", "Agua Limpia", "#22c55e"),
        ]
        for i, (val, lbl, col) in enumerate(kpis):
            kx = 0.65 + i * 2.98
            draw_card(ax, kx, 0.42, 2.80, 1.25, bg="#1e293b", ec=col)
            ax.text(kx + 1.40, 1.22, val, color=col, fontsize=19.5, fontweight="bold", ha="center", va="center")
            ax.text(kx + 1.40, 0.72, lbl, color="#f1f5f9", fontsize=11.5, fontweight="bold", ha="center", va="center")

        pdf.savefig(fig)
        plt.close(fig)

        # =========================================================================
        # DIAPOSITIVA 2: PROBLEMA REAL Y EVIDENCIA EN CAMPUS (RF-01)
        # =========================================================================
        fig, ax = new_slide(
            2, total_slides,
            title="Planteamiento del Problema y Evidencia en el Campus",
            subtitle="Afectación en 124 edificaciones y más de 800 estudiantes, docentes y trabajadores",
            badge="RF-01 · PROBLEMA"
        )

        draw_card(ax, 0.40, 4.30, 7.35, 3.32,
                  title="1. ¿Por qué fallan los métodos actuales?",
                  title_color=C_RED, bg=C_WHITE, ec="#f5b7b1", accent_left=C_RED, title_size=15.0)
        pts_prob = [
            "▸ Fumigación ineficaz: El viento del valle (2.8 m/s) dispersa\n   los aerosoles y genera resistencia larvaria.",
            "▸ Riesgo hídrico comunal: Las acequias del campus riegan\n   cultivos de Urcuquí; no se pueden verter pesticidas.",
            "▸ Daño clínico (Telmofagia): Picaduras lacerantes que causan\n   dermatitis, pápulas, prurito severo e insomnio.",
        ]
        for idx, txt in enumerate(pts_prob):
            ax.text(0.78, 6.92 - idx * 0.85, txt, color=C_TEXT, fontsize=12.4, ha="left", va="top", linespacing=1.28)

        draw_card(ax, 0.40, 0.65, 7.35, 3.42,
                  title="2. Focos Críticos Detectados en Campo",
                  title_color=C_BLUE, bg=C_BLUE_LIGHT, ec="#93c5fd", accent_left=C_BLUE, title_size=15.0)
        pts_focos = [
            "▸ Sector Sur (~550 hab.): Canal Suroeste junto a Las Multis\n   (13 bloques), Las Pats, Docentes, Canchas y Concha Acústica.",
            "▸ Sector Central (~250 hab.): Alta demanda al mediodía en\n   Restaurante El Colibrí (USD 2.50 vs. USD 3.50 en Senescyt).",
            "▸ Parada Sala Capitular (GPS 0.404447, -78.175010):\n   Pozo y canal destapado con cinta de peligro y lodo húmedo.",
        ]
        for idx, txt in enumerate(pts_focos):
            ax.text(0.78, 3.38 - idx * 0.88, txt, color=C_TEXT, fontsize=12.2, ha="left", va="top", linespacing=1.28)

        draw_card(ax, 8.00, 0.65, 7.60, 6.97,
                  title="▸ Figura 5: Evidencia en Sala Capitular (22-Oct-2026)",
                  title_color=C_NAVY, bg=C_WHITE, ec=C_BORDER, accent_left=C_AMBER, title_size=13.8)
        place_image(fig, os.path.join(BASE_DIR, "Figura5_Evidencia_Campo_Sala_Capitular.png"), [8.15, 1.45, 7.30, 5.50])
        ax.text(11.80, 1.02, "GPS: 0.404447° N, -78.175010° W · Cría de Culicoides, Lutzomyia y Simulium",
                color=C_RED, fontsize=10.0, fontweight="bold", ha="center", va="center")

        pdf.savefig(fig)
        plt.close(fig)

        # =========================================================================
        # DIAPOSITIVA 3: BIOLOGÍA DEL COMPLEJO DÍPTERO (RF-01, RNF-02)
        # =========================================================================
        fig, ax = new_slide(
            3, total_slides,
            title="Biología de la Plaga: El Complejo de Dípteros Hematófagos",
            subtitle="Contrastación taxonómica rigurosa: Arenillas verdaderas vs. Moscas negras de canal",
            badge="RF-01 · BIOLOGÍA"
        )

        taxones = [
            ("1. Culicoides spp.\n(Ceratopogonidae)",
             "«Arenillas Verdaderas / Jejenes»",
             C_AMBER, C_AMBER_LIGHT,
             [
                 "▸ Tamaño: 1 a 3 mm (alas moteadas).\n   Picadura muy dolorosa y pruriginosa.",
                 "▸ Cría Semiacuática:\n   Lodo orgánico, bordes fangosos de\n   acequias y pozos húmedos sombríos.",
                 "▸ Horario Crítico:\n   Picos al amanecer y atardecer en\n   zonas húmedas de bajo viento.",
                 "▸ Control:\n   Barrera basal de Hierba Luisa\n   (citral/geraniol) + saneamiento."
             ]),
            ("2. Lutzomyia spp.\n(Psychodidae · Phlebotominae)",
             "«Arenillas de Hojarasca»",
             "#8e44ad", "#f5eef8",
             [
                 "▸ Tamaño: 2 a 3 mm (cuerpo piloso).\n   Vuelo corto y silencioso a saltos.",
                 "▸ Cría Terrestre-Húmeda:\n   Hojarasca en descomposición y\n   muros antiguos (San José / Ingenio).",
                 "▸ Relevancia en Salud:\n   Dermatitis papular intensa y\n   riesgo vectorial en zonas andinas.",
                 "▸ Control:\n   Limpieza de hojarasca + estrato\n   de Cedrón y Huacatay."
             ]),
            ("3. Simulium spp.\n(Simuliidae · Nematocera)",
             "«Moscas Negras de Canal»",
             C_BLUE, C_BLUE_LIGHT,
             [
                 "▸ Confirmado en Yachay Tech:\n   Gen COI (Hermenejildo Bello, 2020):\n   S. veracruzanum / S. oyapockense.",
                 "▸ Cría Estrictamente Lótica:\n   Agua corriente oxigenada (0.3–1.2 m/s)\n   en canales de riego del campus.",
                 "▸ Horario Diurno:\n   07:30–10:00 y 16:00–18:30\n   (vuelo asistido hasta 4 km).",
                 "▸ Control:\n   Cortina de Molle + Libélulas + Bti."
             ]),
        ]

        for i, (tit, sub, col, bg_col, bullets) in enumerate(taxones):
            cx = 0.40 + i * 5.15
            draw_card(ax, cx, 2.05, 4.90, 5.55, bg=C_WHITE, ec=col, accent_left=col)
            ax.add_patch(patches.FancyBboxPatch(
                (cx + 0.20, 6.45), 4.50, 0.98,
                boxstyle="round,pad=0.02,rounding_size=0.10",
                facecolor=bg_col, edgecolor="none"
            ))
            ax.text(cx + 2.45, 7.08, tit, color=col, fontsize=13.5, fontweight="bold", ha="center", va="center")
            ax.text(cx + 2.45, 6.62, sub, color=C_TEXT, fontsize=11.2, fontweight="bold", ha="center", va="center")

            for b_idx, b_txt in enumerate(bullets):
                ax.text(cx + 0.28, 6.18 - b_idx * 1.02, b_txt, color=C_TEXT, fontsize=11.4, ha="left", va="top", linespacing=1.24)

        draw_card(ax, 0.40, 0.62, 15.20, 1.25,
                  title="◆ Sinergia Multi-Taxón (Bloqueo Físico + Enmascaramiento Olfativo + Biocontrol Larvario):",
                  title_color=C_GREEN_DARK, bg=C_GREEN_LIGHT, ec=C_GREEN, accent_left=C_GREEN, title_size=13.5)
        ax.text(0.78, 0.98,
                "Los monoterpenos volátiles (citral, citronelal, 1,8-cineol y α-pineno) saturan los receptores antenales de CO₂ y ácido L-láctico\n"
                "de los tres géneros simultáneamente, mientras las ninfas de libélula (Odonata) y el Bti abaten las larvas en canales y reservorio.",
                color=C_TEXT, fontsize=11.6, ha="left", va="center", linespacing=1.28)

        pdf.savefig(fig)
        plt.close(fig)

        # =========================================================================
        # DIAPOSITIVA 4: DIAGNÓSTICO ESPACIAL Y CATÁLOGO SIG (RF-01)
        # =========================================================================
        fig, ax = new_slide(
            4, total_slides,
            title="Diagnóstico Geoespacial: 286 Entidades SIG y Mapa de Calor",
            subtitle="Levantamiento de precisión en los 4 distritos del campus (0 solapamientos topológicos)",
            badge="RF-01 · SIG"
        )

        draw_card(ax, 0.40, 0.65, 9.55, 6.97, bg=C_WHITE, ec=C_BORDER)
        place_image(fig, os.path.join(BASE_DIR, "Figura1_Diagnostico_Espacial_Yachay.png"), [0.50, 0.75, 9.35, 6.77])

        draw_card(ax, 10.15, 4.25, 5.45, 3.37,
                  title="■ Catálogo SIG (286 Entidades)",
                  title_color=C_BLUE, bg=C_WHITE, ec=C_BLUE, accent_left=C_BLUE, title_size=14.5)
        sig_items = [
            "▸ 124 Edificaciones y Canchas catalogadas",
            "▸ 12 Áreas Verdes y Parques (~5.97 ha)",
            "▸ 16 Ejes Viales y Caminerías peatonales",
            "▸ 80 Polilíneas (canales, vías y cercas)",
            "▸ 69 Puntos (3 paradas bus, 19 parqueos)",
            "▸ 6 Estaciones GPS bio-monitoreo (T-01..06)",
        ]
        for idx, txt in enumerate(sig_items):
            ax.text(10.45, 6.82 - idx * 0.42, txt, color=C_TEXT, fontsize=11.4, fontweight="bold", ha="left", va="center")

        draw_card(ax, 10.15, 0.65, 5.45, 3.40,
                  title="▲ 4 Epicentros de Afectación",
                  title_color=C_RED, bg=C_RED_LIGHT, ec=C_RED, accent_left=C_RED, title_size=14.5)
        epi_items = [
            "1. Sur Residencial (54 edif. · ~550 hab.):\n   Las Multis, Las Pats, Las T's, Docentes y Canchas.",
            "2. Central / Ingenio y San José (37 edif.):\n   Biblioteca 24/7, Aulas B/I, Mikuna y Capitular.",
            "3. Norte Senescyt (18 edif. · ~450 hab.):\n   Edif. Senescyt, Centro Médico y Los Bloques A–I.",
            "4. Este Hídrico: Reservorio (~2,006 m²) y Canal.",
        ]
        for idx, txt in enumerate(epi_items):
            ax.text(10.48, 3.45 - idx * 0.68, txt, color=C_TEXT, fontsize=11.2, ha="left", va="top", linespacing=1.22)

        pdf.savefig(fig)
        plt.close(fig)

        # =========================================================================
        # DIAPOSITIVA 5: MATRIZ MULTICRITERIO DE ALTERNATIVAS (RF-01, RNF-01)
        # =========================================================================
        fig, ax = new_slide(
            5, total_slides,
            title="Comparación de Alternativas y Selección de Estrategia",
            subtitle="Matriz de Decisión Multicriterio (MCDA) frente a eficacia, costo e inocuidad ambiental",
            badge="RF-01 · MCDA"
        )

        draw_card(ax, 0.40, 2.45, 15.20, 5.17,
                  title="◆ Matriz de Evaluación Multicriterio (Escala 1.0 a 5.0)",
                  title_color=C_NAVY, bg=C_WHITE, ec=C_BORDER, title_size=14.5)

        cols = [
            ("Criterio", 3.2),
            ("Peso", 0.95),
            ("A1: Químicos\nSintéticos", 2.05),
            ("A2: Termo-\nNebulización", 2.05),
            ("A3: Trampas\nEléctricas UV", 2.05),
            ("A4: Repelente\nDEET Tópico", 2.00),
            ("A5: ALGORITMO\nVERDE YT (MIP)", 2.60),
        ]
        rows_mcda = [
            ("Inocuidad Hídrica (RNF-01)", "25%", "1.0 (Tóxico)", "2.0 (Aerosol)", "4.5 (No-objetivo)", "3.0 (Dérmico)", "4.9 (100% Inocuo)"),
            ("Eficacia en Dípteros (RF-01)", "25%", "3.5 (Temporal)", "2.5 (Viento)", "1.5 (Diurnos)", "2.5 (Parcial)", "4.8 (-82.8% SLSQP)"),
            ("Viabilidad Costo (RF-05)", "20%", "1.5 ($4,800/año)", "1.5 (Diésel)", "2.0 (Cableado)", "1.0 (Continuo)", "4.7 ($1,470 único)"),
            ("Paisaje y Salud (RNF-02)", "15%", "1.0 (Irritante)", "1.0 (Humo)", "2.0 (Invasivo)", "1.0 (Nulo)", "5.0 (Hipoalergénico)"),
            ("Operación Campus (RF-03)", "15%", "1.5 (Regantes)", "2.0 (Clases)", "3.0 (Intemperie)", "4.0 (Individual)", "4.8 (Riego 0 kWh)"),
            ("PUNTAJE PONDERADO", "100%", "1.80 / 5.0", "1.88 / 5.0", "2.73 / 5.0", "2.25 / 5.0", "4.83 / 5.0 (ÓPTIMA)"),
        ]

        x0 = 0.55
        y_top = 6.38
        row_h = 0.60

        cx = x0
        for c_idx, (c_title, c_w) in enumerate(cols):
            bg_h = C_GREEN if c_idx == 6 else C_NAVY
            ax.add_patch(patches.Rectangle((cx, y_top), c_w, 0.65, facecolor=bg_h, edgecolor=C_WHITE, lw=1))
            ax.text(cx + c_w / 2, y_top + 0.325, c_title, color=C_WHITE, fontsize=11.0, fontweight="bold", ha="center", va="center")
            cx += c_w

        for r_idx, r_vals in enumerate(rows_mcda):
            ry = y_top - (r_idx + 1) * row_h
            is_last = (r_idx == len(rows_mcda) - 1)
            cx = x0
            for c_idx, (_, c_w) in enumerate(cols):
                if c_idx == 6:
                    bg_c = "#d1fae5" if not is_last else C_GREEN
                    txt_c = C_GREEN_DARK if not is_last else C_WHITE
                else:
                    bg_c = "#e2e8f0" if is_last else ("#f8fafc" if r_idx % 2 == 0 else C_WHITE)
                    txt_c = C_NAVY if is_last else C_TEXT
                ax.add_patch(patches.Rectangle((cx, ry), c_w, row_h, facecolor=bg_c, edgecolor="#cbd5e1", lw=0.8))
                fw = "bold" if (is_last or c_idx in [0, 1, 6]) else "normal"
                ax.text(cx + c_w / 2, ry + row_h / 2, r_vals[c_idx], color=txt_c, fontsize=11.0, fontweight=fw, ha="center", va="center")
                cx += c_w

        draw_card(ax, 0.40, 0.62, 7.40, 1.65,
                  title="✕ ¿Por qué descartamos químicos y trampas UV?",
                  title_color=C_RED, bg=C_RED_LIGHT, ec=C_RED, accent_left=C_RED, title_size=13.2)
        ax.text(0.75, 1.20,
                "▸ Simulium pica de día guiado por CO₂ y calor; las trampas UV matan\n  abejas y los químicos contaminan las acequias agrícolas de Urcuquí.",
                color=C_TEXT, fontsize=10.8, ha="left", va="center", linespacing=1.28)

        draw_card(ax, 8.05, 0.62, 7.55, 1.65,
                  title="✓ Ventaja de Algoritmo Verde YT (Manejo Integrado)",
                  title_color=C_GREEN_DARK, bg=C_GREEN_LIGHT, ec=C_GREEN, accent_left=C_GREEN, title_size=13.2)
        ax.text(8.40, 1.20,
                "▸ Combina Paisajismo Repelente + Biocontrol + Optimización SLSQP.\n"
                "▸ Salud Inclusiva: Sustituye el romero en dormitorios por Cedrón.",
                color=C_TEXT, fontsize=10.8, ha="left", va="center", linespacing=1.28)

        pdf.savefig(fig)
        plt.close(fig)

        # =========================================================================
        # DIAPOSITIVA 6: DISEÑO TÉCNICO I - ARQUITECTURA EN 3 ESTRATOS (RF-02)
        # =========================================================================
        fig, ax = new_slide(
            6, total_slides,
            title="Diseño Técnico I: Cercas Vivas en 3 Estratos",
            subtitle="Cortina aerodinámica, fitoquímica repelente 24/7 y protocolo hipoalergénico",
            badge="RF-02 · DISEÑO"
        )

        draw_card(ax, 0.40, 0.65, 8.95, 6.97, bg=C_WHITE, ec=C_BORDER)
        place_image(fig, os.path.join(BASE_DIR, "Figura3_Corte_Transversal_Cercas_3Estratos.png"), [0.50, 0.80, 8.75, 6.67])

        estratos_info = [
            ("● Estrato Alto (3.5 – 5.0 m): Molle Andino",
             C_GREEN_DARK, C_GREEN_LIGHT,
             "▸ Siembra: 1 árbol cada 2.0 m (490 árboles S. molle).\n"
             "▸ Compuestos: α-pineno (38%), limoneno y cariofileno.\n"
             "▸ Función: Cortina rompevientos (frena brisa de 2.8 m/s)."),
            ("● Estrato Medio (1.2 – 2.0 m): Arrayán + Cedrón",
             C_BLUE, C_BLUE_LIGHT,
             "▸ Siembra: 1 arbusto cada 1.0 m (980 arbustos M. hallii).\n"
             "▸ Buffer Dormitorios (<5 m): Cero romero; se emplea\n"
             "  Cedrón y Huacatay para proteger residentes asmáticos."),
            ("● Estrato Bajo (0.4 – 0.8 m): Hierba Luisa",
             C_AMBER, C_AMBER_LIGHT,
             "▸ Siembra: 2 macollas por metro (1,960 macollas).\n"
             "▸ Compuestos: Citronelal (32%), geraniol (28%), citral.\n"
             "▸ Función: Bloquea vuelo rasante desde la 3.ª semana."),
        ]

        for idx, (tit, col, bg_c, desc) in enumerate(estratos_info):
            yy = 5.38 - idx * 2.36
            draw_card(ax, 9.55, yy, 6.05, 2.22, title=tit, title_color=col, bg=bg_c, ec=col, accent_left=col, title_size=12.2)
            ax.text(9.88, yy + 1.56, desc, color=C_TEXT, fontsize=10.9, ha="left", va="top", linespacing=1.26)

        pdf.savefig(fig)
        plt.close(fig)

        # =========================================================================
        # DIAPOSITIVA 7: DISEÑO TÉCNICO II - OPTIMIZACIÓN SLSQP Y 7 TRAMOS (RF-02)
        # =========================================================================
        fig, ax = new_slide(
            7, total_slides,
            title="Diseño Técnico II: Optimización SLSQP y 7 Tramos Viales",
            subtitle="980 metros lineales distribuidos en 7 segmentos que respetan el 100% de calles y accesos",
            badge="RF-02 · SLSQP"
        )

        draw_card(ax, 0.40, 0.65, 8.95, 6.97, bg=C_WHITE, ec=C_BORDER)
        place_image(fig, os.path.join(BASE_DIR, "Figura2_Diseno_Tecnico_Intervencion.png"), [0.50, 0.75, 8.75, 6.77])

        draw_card(ax, 9.55, 5.20, 6.05, 2.42,
                  title="■ Optimización Matemática (SciPy SLSQP)",
                  title_color=C_BLUE, bg=C_BLUE_LIGHT, ec=C_BLUE, accent_left=C_BLUE, title_size=13.5)
        ax.text(9.90, 6.98,
                "max F(L₁,L₂,L₃) = Σ wᵢ·Pᵢ·[1 - exp(-kᵢ·Lᵢ)] - γ·Σ cⱼ·Lⱼ\n"
                "▸ Sujeto a: L₁ + L₂ + L₃ ≤ 980 m (USD 1,470.00)\n"
                "▸ Topología: 0 cruces con las 16 vías y 124 edificios.",
                color=C_NAVY, fontsize=11.2, fontweight="bold", ha="left", va="top", linespacing=1.35)

        draw_card(ax, 9.55, 0.65, 6.05, 4.38,
                  title="● 7 Tramos Viales Discontinuos (980.0 m)",
                  title_color=C_GREEN_DARK, bg=C_WHITE, ec=C_GREEN, accent_left=C_GREEN, title_size=13.5)

        tramos_data = [
            ("CV-1A", "Sur Las Multis / Concha Acústica", "117.7 m"),
            ("CV-1B", "Arco Central Multis – Las Pats", "146.7 m"),
            ("CV-1C", "Sur Las Pats / Canchas (C1 = 380 m)", "115.6 m"),
            ("CV-2A", "Oeste Plaza Mikuna e Invernaderos", "158.1 m"),
            ("CV-2B", "Norte Lab. Idiomas (C2 = 280 m)", "121.9 m"),
            ("CV-3A", "Oeste Residencias Los Bloques A–I", "163.3 m"),
            ("CV-3B", "Este Edif. Senescyt (C3 = 320 m)", "156.7 m"),
            ("TOTAL", "7 Tramos · 1,960 Plántulas", "980.0 m"),
        ]
        ty0 = 4.30
        for idx, (cod, sec, lon) in enumerate(tramos_data):
            ry = ty0 - idx * 0.45
            is_tot = (idx == len(tramos_data) - 1)
            bg_r = "#d1fae5" if is_tot else ("#f8fafc" if idx % 2 == 0 else C_WHITE)
            ax.add_patch(patches.Rectangle((9.75, ry - 0.19), 5.65, 0.42, facecolor=bg_r, edgecolor="#cbd5e1", lw=0.7))
            fw = "bold" if is_tot else "normal"
            col_t = C_GREEN_DARK if is_tot else C_TEXT
            ax.text(9.90, ry, cod, color=C_BLUE if not is_tot else C_GREEN_DARK, fontsize=10.8, fontweight="bold", ha="left", va="center")
            ax.text(10.85, ry, sec, color=col_t, fontsize=10.6, fontweight=fw, ha="left", va="center")
            ax.text(15.25, ry, lon, color=col_t, fontsize=10.8, fontweight="bold", ha="right", va="center")

        pdf.savefig(fig)
        plt.close(fig)

        # =========================================================================
        # DIAPOSITIVA 8: PROTOTIPO FUNCIONAL WEB Y TELEMETRÍA (ENTREGABLE 4.2)
        # =========================================================================
        fig, ax = new_slide(
            8, total_slides,
            title="Prototipo Funcional: Visor Geoespacial Web Interactivo",
            subtitle="Aplicación Bilingüe (ES/EN) con Modo Claro/Oscuro, ventanas flotantes arrastrables y API REST",
            badge="PROTOTIPO · WEB"
        )

        draw_card(ax, 0.40, 3.85, 7.45, 3.77,
                  title="◆ Interfaz y Usabilidad (Folium / Leaflet)",
                  title_color=C_BLUE, bg=C_WHITE, ec=C_BLUE, accent_left=C_BLUE, title_size=13.8)
        feat_web = [
            "▸ Ventanas Flotantes Transparentes y Arrastrables (⠿):\n   Menú vertical, Simbología y Dashboard sin solaparse.",
            "▸ Toggles Deslizantes (ES ⇄ EN  y  Sol ⇄ Luna):\n   Cambio instantáneo de idioma y modo oscuro adaptativo.",
            "▸ Evidencia de Campo en Popups (Base64):\n   Clic en Pozo Sala Capitular muestra fotos in situ.",
        ]
        for idx, txt in enumerate(feat_web):
            ax.text(0.78, 6.88 - idx * 0.96, txt, color=C_TEXT, fontsize=11.6, ha="left", va="top", linespacing=1.26)

        draw_card(ax, 0.40, 0.65, 7.45, 2.98,
                  title="■ Arquitectura de Software Abierto",
                  title_color=C_GREEN_DARK, bg=C_GREEN_LIGHT, ec=C_GREEN, accent_left=C_GREEN, title_size=13.8)
        stack_items = [
            "▸ generar_mapa_interactivo.py -> Visor HTML (286 ent.).",
            "▸ modelo_optimizacion_matematica.py -> SLSQP + Monte Carlo.",
            "▸ api_telemetria.py -> API REST FastAPI (/docs).",
            "▸ GitHub Actions CI/CD -> Despliegue en GitHub Pages.",
        ]
        for idx, txt in enumerate(stack_items):
            ax.text(0.78, 2.95 - idx * 0.54, txt, color=C_TEXT, fontsize=11.2, fontweight="bold", ha="left", va="top")

        draw_card(ax, 8.05, 0.65, 7.55, 6.97,
                  title="▸ Acceso Móvil Directo desde GitHub",
                  title_color=C_NAVY, bg=C_WHITE, ec=C_BORDER, accent_left=C_AMBER, title_size=14.2)
        place_image(fig, os.path.join(BASE_DIR, "Figura2_Diseno_Tecnico_Intervencion.png"), [8.20, 2.65, 7.25, 4.35])
        place_image(fig, os.path.join(BASE_DIR, "qr_algoritmo_verde.png"), [8.30, 0.80, 1.75, 1.75])
        ax.text(10.25, 2.05, "▸ Repositorio Oficial GitHub:", color=C_BLUE, fontsize=12.0, fontweight="bold", ha="left", va="center")
        ax.text(10.25, 1.62, "github.com/JeffersonConza/algoritmo-verde-yosw2026", color=C_NAVY, fontsize=11.0, fontweight="bold", ha="left", va="center")
        ax.text(10.25, 1.12, "▸ Visor Web en Vivo (GitHub Pages):\njeffersonconza.github.io/algoritmo-verde-yosw2026", color=C_GREEN_DARK, fontsize=10.8, fontweight="bold", ha="left", va="center")

        pdf.savefig(fig)
        plt.close(fig)

        # =========================================================================
        # DIAPOSITIVA 9: PLAN DE IMPLEMENTACIÓN Y RIEGO POR GRAVEDAD (RF-03)
        # =========================================================================
        fig, ax = new_slide(
            9, total_slides,
            title="Plan de Implementación, Riego a Gravedad y Mantenimiento",
            subtitle="Ejecución en 4 fases (16 semanas), 0 kWh de consumo eléctrico y gobernanza universitaria",
            badge="RF-03 · GESTIÓN"
        )

        fases = [
            ("FASE I (Sem. 1–2)", "Trazado y Riego", C_BLUE, C_BLUE_LIGHT,
             "▸ Replanteo GPS de los\n   7 tramos (980 m).\n\n"
             "▸ Censo de alergias con\n   Bienestar Estudiantil.\n\n"
             "▸ Tendido de manguera\n   de goteo PE 16 mm."),
            ("FASE II (Sem. 3–5)", "Siembra 3 Estratos", C_GREEN_DARK, C_GREEN_LIGHT,
             "▸ Abonado con 1.5 t de\n   compost Yachay Tech.\n\n"
             "▸ Siembra de las 1,960\n   plántulas y macollas.\n\n"
             "▸ Repelencia activa desde\n   la 3.ª semana."),
            ("FASE III (Sem. 6–8)", "Biocontrol Acuático", "#0288d1", "#e1f5fe",
             "▸ Santuario de libélulas\n   (Odonata) en reservorio\n   este (~2,006 m²).\n\n"
             "▸ Micro-dosificación de\n   Bti en canales lóticos.\n\n"
             "▸ 6 estaciones GPS activas."),
            ("FASE IV (Sem. 9–16+)", "Mantenimiento", C_AMBER, C_AMBER_LIGHT,
             "▸ Poda bimensual (2 h/sem\n   cuadrilla jardinería).\n\n"
             "▸ Conteo semanal por\n   estudiantes (Biomedicina).\n\n"
             "▸ Esquejes en invernadero\n   a costo USD 0."),
        ]

        for i, (f_cod, f_tit, col, bg_c, desc) in enumerate(fases):
            fx = 0.40 + i * 3.84
            draw_card(ax, fx, 3.55, 3.64, 4.07, bg=C_WHITE, ec=col, accent_left=col)
            ax.add_patch(patches.FancyBboxPatch(
                (fx + 0.18, 6.68), 3.28, 0.76,
                boxstyle="round,pad=0.02,rounding_size=0.08",
                facecolor=bg_c, edgecolor="none"
            ))
            ax.text(fx + 1.82, 7.22, f_cod, color=col, fontsize=12.5, fontweight="bold", ha="center", va="center")
            ax.text(fx + 1.82, 6.86, f_tit, color=C_NAVY, fontsize=11.8, fontweight="bold", ha="center", va="center")
            ax.text(fx + 0.24, 6.38, desc, color=C_TEXT, fontsize=11.4, ha="left", va="top", linespacing=1.25)

        draw_card(ax, 0.40, 0.65, 7.45, 2.68,
                  title="● Riego por Gravedad Pura (0 kWh Eléctricos)",
                  title_color=C_BLUE, bg=C_WHITE, ec=C_BLUE, accent_left=C_BLUE, title_size=13.5)
        ax.text(0.75, 2.62,
                "▸ Aprovecha el desnivel natural (~2,065 m a ~2,025 m).\n"
                "▸ Tubería PE 16 mm con goteros autocompensantes (2.0 L/h\n  cada 50 cm) a gravedad (0.4–0.8 bar): 0 bombas eléctricas.",
                color=C_TEXT, fontsize=10.8, ha="left", va="top", linespacing=1.28)

        draw_card(ax, 8.05, 0.65, 7.55, 2.68,
                  title="■ Gobernanza y Ciclo de Vida (>10 Años)",
                  title_color=C_GREEN_DARK, bg=C_GREEN_LIGHT, ec=C_GREEN, accent_left=C_GREEN, title_size=13.5)
        ax.text(8.38, 2.62,
                "▸ Operado por Dirección de Mantenimiento + Club de\n  Agroecología y prácticas académicas (costo personal $0).\n"
                "▸ Barrera perenne que aumenta su eficacia cada año.",
                color=C_TEXT, fontsize=10.8, ha="left", va="top", linespacing=1.28)

        pdf.savefig(fig)
        plt.close(fig)

        # =========================================================================
        # DIAPOSITIVA 10: EVALUACIÓN DE EFICACIA E IMPACTO (RF-04, RNF-01)
        # =========================================================================
        fig, ax = new_slide(
            10, total_slides,
            title="Evaluación de Eficacia y Seguridad Ambiental",
            subtitle="Validación estadística en 6 estaciones GPS (16 semanas) e inocuidad sobre polinizadores",
            badge="RF-04 · EFICACIA"
        )

        draw_card(ax, 0.40, 2.55, 10.05, 5.07, bg=C_WHITE, ec=C_BORDER)
        place_image(fig, os.path.join(BASE_DIR, "Figura4_Curva_Reduccion_BioMonitoreo.png"), [0.50, 2.65, 9.85, 4.87])

        draw_card(ax, 10.65, 2.55, 4.95, 5.07,
                  title="▲ Resultados (RF-04)",
                  title_color=C_BLUE, bg=C_WHITE, ec=C_BLUE, accent_left=C_BLUE, title_size=14.5)
        stat_boxes = [
            ("86.3 ± 6.5", "Línea Base (Sem. 1–4)", "Adultos / trampa / sem.", C_RED, C_RED_LIGHT),
            ("14.8 ± 2.0", "Consolidación (Sem. 16)", "Adultos / trampa / sem.", C_GREEN_DARK, C_GREEN_LIGHT),
            ("-82.8%", "Mitigación Lograda", "t = 25.85 (p < 0.001)", C_BLUE, C_BLUE_LIGHT),
            ("≥ 25 µg/m³", "Pluma Terpénica", "Buffer activo de 40 m", C_AMBER, C_AMBER_LIGHT),
        ]
        for idx, (val, t1, t2, col, bg_c) in enumerate(stat_boxes):
            sy = 5.95 - idx * 1.06
            ax.add_patch(patches.FancyBboxPatch(
                (10.92, sy), 4.45, 0.90,
                boxstyle="round,pad=0.02,rounding_size=0.10",
                facecolor=bg_c, edgecolor=col, lw=1.2
            ))
            ax.text(11.88, sy + 0.45, val, color=col, fontsize=14.5, fontweight="bold", ha="center", va="center")
            ax.text(12.88, sy + 0.60, t1, color=C_NAVY, fontsize=10.2, fontweight="bold", ha="left", va="center")
            ax.text(12.88, sy + 0.26, t2, color=C_MUTED, fontsize=9.6, ha="left", va="center")

        draw_card(ax, 0.40, 0.62, 15.20, 1.72,
                  title="◆ Protección de Fauna No Objetivo (Abejas, Libélulas y Agua de Riego - RNF-01)",
                  title_color=C_GREEN_DARK, bg=C_GREEN_LIGHT, ec=C_GREEN, accent_left=C_GREEN, title_size=14.0)
        ax.text(0.78, 1.25,
                "▸ Polinizadores (Apis mellifera, Bombus): Flora melífera sin agroquímicos. El Bti requiere pH intestinal alcalino (>9.0) exclusivo\n"
                "  de larvas de Nematocera; es 100% inocuo para abejas, libélulas (Odonata), peces, aves y cultivos de Urcuquí.",
                color=C_TEXT, fontsize=11.8, ha="left", va="center", linespacing=1.30)

        pdf.savefig(fig)
        plt.close(fig)

        # =========================================================================
        # DIAPOSITIVA 11: VIABILIDAD ECONÓMICA Y ADOPCIÓN (RF-05)
        # =========================================================================
        fig, ax = new_slide(
            11, total_slides,
            title="Viabilidad Económica (USD 1,470) y Adopción Comunitaria",
            subtitle="Inversión optimizada de USD 1.50 por metro lineal con retorno en menos de 3 meses",
            badge="RF-05 · COSTOS"
        )

        draw_card(ax, 0.40, 2.55, 9.65, 5.07,
                  title="■ Presupuesto Detallado (980 m Lineales)",
                  title_color=C_NAVY, bg=C_WHITE, ec=C_BORDER, title_size=14.5)

        b_cols = [("Rubro", 2.6), ("Especificación", 3.5), ("Cant.", 1.2), ("Unit.", 0.9), ("Total", 1.15)]
        b_rows = [
            ("Molle (S. molle)", "Árbol nativo 60–80 cm", "490 u.", "$0.80", "$392.00"),
            ("Arrayán (M. hallii)", "Arbusto nativo andino", "490 u.", "$0.70", "$343.00"),
            ("Cedrón / Huacatay", "Especies hipoalergénicas", "490 u.", "$0.50", "$245.00"),
            ("Hierba Luisa", "Macollas doble hilera", "1,960 u.", "$0.15", "$294.00"),
            ("Manguera PE 16mm", "Goteo integrado cada 50 cm", "980 m", "$0.15", "$147.00"),
            ("Filtros / Válvulas / Bti", "Conexión a gravedad e inóculo", "Global", "$49.00", "$49.00"),
            ("Compost Yachay Tech", "Planta de compostaje propia", "1.5 ton", "$0.00", "$0.00"),
            ("INVERSIÓN TOTAL", "Costo unitario: USD 1.50 / m", "980 m", "$1.50/m", "$1,470.00"),
        ]

        bx0 = 0.55
        by_top = 6.45
        bh = 0.46
        cx = bx0
        for c_idx, (ct, cw) in enumerate(b_cols):
            ax.add_patch(patches.Rectangle((cx, by_top), cw, 0.50, facecolor=C_NAVY, edgecolor=C_WHITE, lw=0.8))
            ax.text(cx + cw / 2, by_top + 0.25, ct, color=C_WHITE, fontsize=11.0, fontweight="bold", ha="center", va="center")
            cx += cw

        for r_idx, r_vals in enumerate(b_rows):
            ry = by_top - (r_idx + 1) * bh
            is_tot = (r_idx == len(b_rows) - 1)
            cx = bx0
            for c_idx, (_, cw) in enumerate(b_cols):
                bg_c = "#d1fae5" if is_tot else ("#f8fafc" if r_idx % 2 == 0 else C_WHITE)
                ax.add_patch(patches.Rectangle((cx, ry), cw, bh, facecolor=bg_c, edgecolor="#cbd5e1", lw=0.7))
                fw = "bold" if (is_tot or c_idx in [0, 4]) else "normal"
                col_t = C_GREEN_DARK if is_tot else C_TEXT
                ax.text(cx + cw / 2, ry + bh / 2, r_vals[c_idx], color=col_t, fontsize=10.8, fontweight=fw, ha="center", va="center")
                cx += cw

        draw_card(ax, 10.25, 4.25, 5.35, 3.37,
                  title="■ Ahorro vs. Fumigación Química",
                  title_color=C_AMBER, bg=C_AMBER_LIGHT, ec=C_AMBER, accent_left=C_AMBER, title_size=14.2)
        ax.text(10.60, 6.92,
                "▸ Fumigación Química Recurrente:\n"
                "  USD 4,800 a 7,000 / año (gasto perpetuo).\n\n"
                "▸ Algoritmo Verde YT:\n"
                "  USD 1,470.00 inversión única inicial.\n\n"
                "★ Amortización: < 3 meses\n"
                "★ Ahorro en 5 años: > USD 22,500.",
                color=C_TEXT, fontsize=11.6, fontweight="bold", ha="left", va="top", linespacing=1.26)

        draw_card(ax, 10.25, 0.62, 5.35, 3.42,
                  title="◆ Adopción por la Comunidad",
                  title_color=C_GREEN_DARK, bg=C_GREEN_LIGHT, ec=C_GREEN, accent_left=C_GREEN, title_size=14.2)
        ax.text(10.60, 3.38,
                "1. Programa «Adopta un Tramo»:\n   Mingas por residencias (Multis, Pats, Bloques).\n"
                "2. Autopropagación en Invernaderos:\n   Esquejes de Hierba Luisa y Cedrón a USD 0.\n"
                "3. Vinculación con Urcuquí:\n   Entrega de esquejes a agricultores vecinos.",
                color=C_TEXT, fontsize=11.2, ha="left", va="top", linespacing=1.26)

        draw_card(ax, 0.40, 0.62, 9.65, 1.72,
                  title="★ Viabilidad Inmediata con Recursos de Yachay Tech",
                  title_color=C_BLUE, bg=C_BLUE_LIGHT, ec=C_BLUE, accent_left=C_BLUE, title_size=13.5)
        ax.text(0.75, 1.22,
                "▸ Plántulas de viveros locales (Ibarra/Urcuquí) + compost propio de Yachay Tech (USD 0).\n"
                "▸ Genera biomasa aromática para prácticas de laboratorio de Química y Agroindustria.",
                color=C_TEXT, fontsize=10.6, ha="left", va="center", linespacing=1.28)

        pdf.savefig(fig)
        plt.close(fig)

        # =========================================================================
        # DIAPOSITIVA 12: CONCLUSIONES, DECLARACIÓN DE IA (SEC. 13) Y QR GITHUB
        # =========================================================================
        fig, ax = new_slide(
            12, total_slides,
            title="Conclusiones, Declaración de IA (Sec. 13) y Acceso QR",
            subtitle="Propuesta lista para ejecución inmediata, transparente y escalable en Yachay Tech",
            badge="CIERRE · IA"
        )

        draw_card(ax, 0.40, 4.20, 9.85, 3.42,
                  title="◆ Conclusiones y Gestión de Limitaciones",
                  title_color=C_NAVY, bg=C_WHITE, ec=C_BLUE, accent_left=C_BLUE, title_size=14.5)
        concl_pts = [
            "1. Impacto Comprobado: Mitigación del 82.8% (p < 0.001) sobre el complejo Culicoides,\n   Lutzomyia y Simulium, protegiendo 124 edificaciones y 39,200 m² sin agrotóxicos.",
            "2. Diseño Vial e Hipoalergénico: 7 tramos (980 m) con 0 cruces de calles y protocolo\n   libre de romero en dormitorios (Cedrón y Huacatay) para proteger a estudiantes alérgicos.",
            "3. Limitación y Mitigación: Mientras el Molle consolida su porte arbóreo (6–12 meses), el\n   estrato basal de Hierba Luisa y el Bti brindan control efectivo desde la 3.ª semana.",
        ]
        for idx, txt in enumerate(concl_pts):
            ax.text(0.78, 6.95 - idx * 0.90, txt, color=C_TEXT, fontsize=11.4, ha="left", va="top", linespacing=1.24)

        draw_card(ax, 0.40, 0.62, 9.85, 3.38,
                  title="■ Declaración Obligatoria de Uso de IA (Sección 13 del Reto)",
                  title_color=C_GREEN_DARK, bg=C_GREEN_LIGHT, ec=C_GREEN, accent_left=C_GREEN, title_size=14.5)
        ax.text(0.78, 3.35,
                "▸ Autoría Humana Directa (100% Original del Equipo): Inspección de campo en Sala Capitular,\n"
                "  levantamiento GPS de las 286 entidades SIG (124 edificios, 12 jardines, 16 vías), taxonomía\n"
                "  del complejo díptero, protocolo hipoalergénico, modelo SLSQP y presupuesto de USD 1,470.\n"
                "▸ Asistencia Computacional e IA Supervisada:\n"
                "  • Python (SciPy SLSQP, Folium, Matplotlib): Optimización numérica y cartografía.\n"
                "  • LLMs (Claude / ChatGPT / Antigravity): Depuración de código JS/HTML, traducción al inglés\n"
                "    y formato APA 7.ª ed. Todos los datos y cálculos fueron verificados por los 4 autores.",
                color=C_TEXT, fontsize=11.0, ha="left", va="top", linespacing=1.25)

        draw_card(ax, 10.50, 0.62, 5.10, 7.00,
                  title="■ Escanea el QR (GitHub)",
                  title_color=C_WHITE, bg=C_NAVY, ec=C_GREEN, title_size=15.0)
        place_image(fig, os.path.join(BASE_DIR, "qr_algoritmo_verde.png"), [11.25, 3.40, 3.60, 3.60])

        ax.text(13.05, 3.00, "Repositorio Público Oficial:", color="#94a3b8", fontsize=11.5, fontweight="bold", ha="center", va="center")
        ax.text(13.05, 2.55, "github.com/JeffersonConza/\nalgoritmo-verde-yosw2026",
                color="#6ee7b7", fontsize=12.0, fontweight="bold", ha="center", va="center")

        ax.add_patch(patches.FancyBboxPatch(
            (10.82, 1.38), 4.46, 0.86,
            boxstyle="round,pad=0.02,rounding_size=0.12",
            facecolor=C_GREEN, edgecolor="none"
        ))
        ax.text(13.05, 1.81, "▸ En GitHub: Botón directo a\n«VER MAPA INTERACTIVO EN VIVO»",
                color=C_WHITE, fontsize=11.5, fontweight="bold", ha="center", va="center")

        ax.text(13.05, 0.95, "¡Muchas gracias! · Algoritmo Verde YT ◆",
                color=C_WHITE, fontsize=12.5, fontweight="bold", ha="center", va="center")

        pdf.savefig(fig)
        plt.close(fig)

    shutil.copy2(tmp_pdf, OUT_PDF)
    print(f"Presentación PDF generada exitosamente con letra grande en: {OUT_PDF}")


if __name__ == "__main__":
    generar_presentacion()
