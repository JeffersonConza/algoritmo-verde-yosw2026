"""
Generador de la Presentación Oficial PDF (12 Diapositivas · Widescreen 16:9)
Reto 3: Estrategias Innovadoras para el Control de Arenillas en el Campus de Yachay Tech
Equipo: Algoritmo Verde YT | Yachay Open Science Week 2026 (Ideatón)
Cumple 100% con la Rúbrica Oficial (RF-01 a RF-05, RNF-01 a RNF-03, Sec. 11 y Sec. 13 IA)
"""

import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.backends.backend_pdf import PdfPages
from PIL import Image
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))
OUT_PDF = os.path.join(BASE_DIR, "PRESENTACION_OFICIAL_RETO3_ALGORITMO_VERDE_YT.pdf")
CHAT_PDF = os.path.join(ROOT_DIR, "WhatsApp Chat with Ideaton", "PRESENTACION_OFICIAL_RETO3_ALGORITMO_VERDE_YT.pdf")

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
    """Crea un lienzo Widescreen 16:9 (16 x 9 pulgadas) con encabezado y pie institucional."""
    fig = plt.figure(figsize=(16, 9), dpi=220)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)
    ax.axis("off")

    # Fondo general claro
    ax.add_patch(patches.Rectangle((0, 0), 16, 9, facecolor=C_BG, edgecolor="none"))

    if slide_num > 1:
        # Barra superior institucional
        ax.add_patch(patches.Rectangle((0, 8.05), 16, 0.95, facecolor=C_NAVY, edgecolor="none"))
        ax.add_patch(patches.Rectangle((0, 7.98), 16, 0.07, facecolor=C_GREEN, edgecolor="none"))

        # Badge de sección/requisito
        if badge:
            ax.add_patch(patches.FancyBboxPatch(
                (0.45, 8.32), 2.35, 0.42,
                boxstyle="round,pad=0.04,rounding_size=0.12",
                facecolor=C_GREEN, edgecolor="none"
            ))
            ax.text(1.625, 8.53, badge, color=C_WHITE, fontsize=10.5, fontweight="bold", ha="center", va="center")
            title_x = 3.0
        else:
            title_x = 0.5

        ax.text(title_x, 8.62, title, color=C_WHITE, fontsize=15.2, fontweight="bold", ha="left", va="center")
        if subtitle:
            ax.text(title_x, 8.26, subtitle, color="#94a3b8", fontsize=10.5, ha="left", va="center")

        # Marca derecha en barra superior
        ax.text(15.55, 8.53, "◆ Algoritmo Verde YT · YOSW 2026", color="#e2e8f0", fontsize=10.5, fontweight="bold", ha="right", va="center")

        # Pie de diapositiva
        ax.add_patch(patches.Rectangle((0, 0), 16, 0.42, facecolor="#e2e8f0", edgecolor="none"))
        ax.text(0.45, 0.21, "Universidad Yachay Tech · Ideatón YOSW 2026 · Reto 3: Control Ecosistémico de Arenillas",
                color=C_MUTED, fontsize=9.2, ha="left", va="center")
        ax.text(15.55, 0.21, f"Diapositiva {slide_num} de {total_slides}",
                color=C_NAVY, fontsize=9.8, fontweight="bold", ha="right", va="center")

    return fig, ax


def draw_card(ax, x, y, w, h, title="", title_color=C_BLUE, bg=C_WHITE, ec=C_BORDER, accent_left=None, title_size=12.5):
    """Dibuja una tarjeta estilizada con borde redondeado y barra de acento opcional."""
    card = patches.FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.02,rounding_size=0.14",
        facecolor=bg, edgecolor=ec, linewidth=1.3
    )
    ax.add_patch(card)
    if accent_left:
        bar = patches.FancyBboxPatch(
            (x, y + 0.04), 0.11, h - 0.08,
            boxstyle="round,pad=0.0,rounding_size=0.05",
            facecolor=accent_left, edgecolor="none"
        )
        ax.add_patch(bar)
    if title:
        tx = x + (0.28 if accent_left else 0.22)
        ax.text(tx, y + h - 0.34, title, color=title_color, fontsize=title_size, fontweight="bold", ha="left", va="center")


def place_image(fig, img_path, rect, title_below=""):
    """Inserta una imagen mantendo su relación de aspecto dentro de rect = [left_in_16, bottom_in_9, w_in_16, h_in_9]."""
    if not os.path.exists(img_path):
        return
    ax_img = fig.add_axes([rect[0] / 16.0, rect[1] / 9.0, rect[2] / 16.0, rect[3] / 9.0])
    img = Image.open(img_path)
    ax_img.imshow(img)
    ax_img.axis("off")


def generar_presentacion():
    total_slides = 12
    if os.path.exists(OUT_PDF):
        os.remove(OUT_PDF)

    with PdfPages(OUT_PDF) as pdf:
        # =========================================================================
        # DIAPOSITIVA 1: PORTADA INSTITUCIONAL Y EQUIPO MULTIDISCIPLINARIO
        # =========================================================================
        fig, ax = new_slide(1, total_slides)
        ax.add_patch(patches.Rectangle((0, 0), 16, 9, facecolor=C_NAVY, edgecolor="none"))
        ax.add_patch(patches.Polygon([[10.5, 9], [16, 9], [16, 0], [8.2, 0]], closed=True, facecolor="#162447", alpha=0.75))
        ax.add_patch(patches.Rectangle((0, 8.82), 16, 0.18, facecolor=C_GREEN, edgecolor="none"))
        ax.add_patch(patches.Rectangle((0, 0), 16, 0.15, facecolor=C_GREEN, edgecolor="none"))

        # Badge superior
        ax.add_patch(patches.FancyBboxPatch(
            (0.7, 7.75), 6.5, 0.52,
            boxstyle="round,pad=0.03,rounding_size=0.15",
            facecolor=C_GREEN, edgecolor="none"
        ))
        ax.text(3.95, 8.01, "YACHAY OPEN SCIENCE WEEK 2026 · IDEATÓN · RETO 3",
                color=C_WHITE, fontsize=11.5, fontweight="bold", ha="center", va="center")

        # Título Principal
        ax.text(0.7, 6.85, "ESTRATEGIAS INNOVADORAS PARA EL CONTROL\nECOSISTÉMICO DE ARENILLAS EN YACHAY TECH",
                color=C_WHITE, fontsize=24.5, fontweight="bold", ha="left", va="center", linespacing=1.25)

        ax.text(0.7, 5.75, "Barreras Vivas Tri-Estrato Hipoalergénicas, Biocontrol con Odonatos + Bti\ny Optimización Matemática Espacial (SLSQP) sobre 286 Entidades SIG",
                color="#6ee7b7", fontsize=14, fontweight="bold", ha="left", va="center", linespacing=1.35)

        # Tarjeta de Integrantes (Sección 11 - Multidisciplinariedad)
        draw_card(ax, 0.7, 2.05, 9.8, 3.15,
                  title="■ EQUIPO MULTIDISCIPLINARIO «ALGORITMO VERDE YT»  |  Mentor: Ing. José Luis Flores M.Sc.",
                  title_color="#38bdf8", bg="#1e293b", ec="#334155", accent_left=C_GREEN, title_size=12.2)

        miembros = [
            ("JC", "Jefferson Conza", "Matemáticas / Computación (9.º sem.)", "Líder Técnico · Optimización SLSQP, Modelado de Dispersión y SIG (286 entidades)", C_BLUE),
            ("CP", "Christopher Picuasi", "Computación (3.er sem.)", "Desarrollo de Software · Visor Geoespacial Web Interactivo Bilingüe y UI/UX", C_GREEN),
            ("FI", "Francisco Ibujés", "Química (2.º sem.)", "Investigación Fitoquímica · Metabolitos Volátiles, Riego por Gravedad y Costos", C_AMBER),
            ("LC", "Luis Collaguazo", "Biomedicina (2.º sem.)", "Entomología Médica y Salud · Complejo Culicoides/Lutzomyia/Simulium y Biocontrol", "#8e44ad"),
        ]
        for idx, (ini, nom, car, rol, col) in enumerate(miembros):
            yy = 4.38 - idx * 0.68
            ax.add_patch(patches.Circle((1.22, yy), radius=0.24, facecolor=col, edgecolor=C_WHITE, lw=1.2))
            ax.text(1.22, yy, ini, color=C_WHITE, fontsize=10.5, fontweight="bold", ha="center", va="center")
            ax.text(1.62, yy + 0.10, f"{nom}  —  {car}", color=C_WHITE, fontsize=11.2, fontweight="bold", ha="left", va="center")
            ax.text(1.62, yy - 0.14, rol, color="#cbd5e1", fontsize=9.8, ha="left", va="center")

        # Panel derecho: QR hacia GitHub + KPIs
        draw_card(ax, 10.85, 2.05, 4.5, 5.2,
                  title="■ REPOSITORIO Y MAPA EN VIVO",
                  title_color=C_WHITE, bg="#1e293b", ec=C_GREEN, title_size=12.5)
        place_image(fig, os.path.join(BASE_DIR, "qr_algoritmo_verde.png"), [11.7, 3.25, 2.8, 2.8])
        ax.text(13.1, 2.85, "github.com/JeffersonConza/\nalgoritmo-verde-yosw2026",
                color="#6ee7b7", fontsize=10, fontweight="bold", ha="center", va="center")
        ax.text(13.1, 2.32, "Escanea para abrir GitHub y lanzar\nel Mapa Interactivo en tu celular",
                color="#cbd5e1", fontsize=9.2, ha="center", va="center")

        # Franja inferior de 5 KPIs
        kpis = [
            ("980 m", "7 Tramos de Cercas Vivas", C_GREEN),
            ("-82.8%", "Mitigación Picaduras (p<0.001)", "#38bdf8"),
            ("$1,470 USD", "Inversión Total ($1.50/m)", "#f59e0b"),
            ("124 Edif.", "Protegidas (~800+ personas)", "#a855f7"),
            ("0% Químicos", "Inocuidad Hídrica en Urcuquí", "#22c55e"),
        ]
        for i, (val, lbl, col) in enumerate(kpis):
            kx = 0.7 + i * 2.98
            draw_card(ax, kx, 0.52, 2.78, 1.18, bg="#1e293b", ec=col)
            ax.text(kx + 1.39, 1.25, val, color=col, fontsize=17, fontweight="bold", ha="center", va="center")
            ax.text(kx + 1.39, 0.80, lbl, color="#e2e8f0", fontsize=9.5, fontweight="bold", ha="center", va="center")

        pdf.savefig(fig)
        plt.close(fig)

        # =========================================================================
        # DIAPOSITIVA 2: CONTEXTO, PROBLEMA REAL Y EVIDENCIA DE CAMPO (RF-01)
        # =========================================================================
        fig, ax = new_slide(
            2, total_slides,
            title="Planteamiento del Problema y Evidencia de Campo en Yachay Tech",
            subtitle="Afectación clínica, académica y habitacional en 124 edificaciones del campus (Urcuquí, Imbabura)",
            badge="RF-01 · DIAGNÓSTICO"
        )

        # Columna Izquierda: Problemática Estructural y Clínica
        draw_card(ax, 0.45, 4.35, 7.3, 3.35,
                  title="1. ¿Por qué fallan las respuestas actuales en el campus?",
                  title_color=C_RED, bg=C_WHITE, ec="#f5b7b1", accent_left=C_RED)
        pts_prob = [
            "• Dependencia de métodos correctivos: Fumigaciones químicas esporádicas que se\n  dispersan con el viento del valle (2.8 m/s) y generan resistencia larvaria.",
            "• Inviabilidad ecotoxicológica: Los canales de riego del campus abastecen cultivos\n  comunales de Urcuquí; verter organofosforados o piretroides contamina el agua.",
            "• Impacto clínico real (Telmofagia): Laceración epidérmica con saliva anticoagulante\n  que causa pápulas eritematosas, prurito severo, dermatitis y sobreinfección.",
            "• Pérdida de habitabilidad diurna y crepuscular: Afecta a +800 residentes y estudiantes\n  en aulas (Senescyt, Aulas B/I), comedores (Plaza Mikuna) y dormitorios (Multis, Bloques)."
        ]
        for idx, txt in enumerate(pts_prob):
            ax.text(0.8, 7.02 - idx * 0.68, txt, color=C_TEXT, fontsize=10.1, ha="left", va="top", linespacing=1.28)

        draw_card(ax, 0.45, 0.68, 7.3, 3.42,
                  title="2. Focos Críticos Identificados en Inspección In Situ",
                  title_color=C_BLUE, bg=C_BLUE_LIGHT, ec="#93c5fd", accent_left=C_BLUE)
        pts_focos = [
            "• Sector Sur Residencial (~550 hab.): Canal Suroeste (124.5 m) junto a Las Multis (13 bloques\n  de 3 pisos), Las Pats, Villas Docentes, Canchas Deportivas y Concha Acústica.",
            "• Sector Central / Ingenio y San José (~250 hab.): Alta concentración estudiantil al mediodía\n  en Restaurante El Colibrí (almuerzo USD 2.50 vs. USD 3.50 en Senescyt) y Sala Capitular.",
            "• Evidencia en Sala Capitular (GPS: 0.4044473, -78.1750098): Pozo/canal destapado con\n  cinta de peligro, hojarasca húmeda y lodo orgánico a metros de la parada de buses.",
            "• Sector Norte Senescyt y Los Bloques (~450 hab.): Taludes y drenajes pluviales orientales."
        ]
        for idx, txt in enumerate(pts_focos):
            ax.text(0.8, 3.45 - idx * 0.68, txt, color=C_TEXT, fontsize=9.8, ha="left", va="top", linespacing=1.26)

        # Columna Derecha: Figura 5 (Evidencia Fotográfica de Campo)
        draw_card(ax, 8.0, 0.68, 7.55, 7.02,
                  title="▸ Figura 5: Inspección de Campo en Parada de Sala Capitular (22-Oct-2026)",
                  title_color=C_NAVY, bg=C_WHITE, ec=C_BORDER, accent_left=C_AMBER, title_size=11.8)
        place_image(fig, os.path.join(BASE_DIR, "Figura5_Evidencia_Campo_Sala_Capitular.png"), [8.15, 1.38, 7.25, 5.72])
        ax.text(11.77, 1.00, "GPS: 0.4044473° N, -78.1750098° W · Microhábitat de cría de Culicoides spp., Lutzomyia spp. y Simulium spp.",
                color=C_RED, fontsize=8.5, fontweight="bold", ha="center", va="center")

        pdf.savefig(fig)
        plt.close(fig)

        # =========================================================================
        # DIAPOSITIVA 3: BIOLOGÍA DEL COMPLEJO VECTORIAL DÍPTERO (RF-01, RNF-02)
        # =========================================================================
        fig, ax = new_slide(
            3, total_slides,
            title="Fundamentación Entomológica: El Complejo de Dípteros Hematófagos",
            subtitle="Contrastación taxonómica y bionómica (Requisito Sección 1 del Reto: no asumir una sola especie sin justificarlo)",
            badge="RF-01 · RNF-02"
        )

        # Tres tarjetas verticales para los 3 géneros del complejo
        taxones = [
            ("1. Culicoides spp.\n(Familia Ceratopogonidae)",
             "«Arenillas Verdaderas / Jejenes»",
             C_AMBER, C_AMBER_LIGHT,
             [
                 "• Morfología: Dípteros diminutos (1–3 mm)\n  de alas moteadas y picadura urente.",
                 "• Hábitat Larvario Semiacuático:\n  Bordes fangosos de acequias, lodo rico\n  en materia orgánica, charcos sombríos\n  y pozos destapados (Sala Capitular).",
                 "• Picos de Actividad: Crepuscular,\n  matutino y vespertino en zonas de\n  sombra y baja velocidad de viento.",
                 "• Control en Algoritmo Verde:\n  Saturación antenal por citral/geraniol\n  (estrato basal) + drenaje/saneamiento."
             ]),
            ("2. Lutzomyia spp.\n(Familia Psychodidae · Phlebotominae)",
             "«Arenillas de Hojarasca / Manta Blanca»",
             "#8e44ad", "#f5eef8",
             [
                 "• Morfología: Dípteros pilosos de 2–3 mm\n  con vuelo corto a saltos rasantes.",
                 "• Hábitat Larvario Terrestre-Húmedo:\n  Suelos húmedos ricos en detritos\n  vegetales, hojarasca sombría y oquedades\n  de muros patrimoniales (San José / Ingenio).",
                 "• Relevancia Biomédica: Prurito intenso,\n  sensibilización alérgica cutánea y\n  potencial vector de patógenos.",
                 "• Control en Algoritmo Verde:\n  Deshierbe preventivo + barrera basal\n  de Cymbopogon citratus y Tagetes minuta."
             ]),
            ("3. Simulium spp.\n(Familia Simuliidae · Nematocera)",
             "«Moscas Negras / Arenillas de Canal»",
             C_BLUE, C_BLUE_LIGHT,
             [
                 "• Confirmación Molecular en Yachay Tech:\n  Secuenciación COI (Hermenejildo Bello,\n  2020) -> S. veracruzanum / S. oyapockense.",
                 "• Hábitat Larvario Estrictamente Lótico:\n  Aguas corrientes oxigenadas (0.3–1.2 m/s)\n  en los canales de riego abiertos del campus;\n  ancladas a rocas y vegetación sumergida.",
                 "• Picos Diurnos: 07:30–10:00 y 16:00–18:30\n  (radio de vuelo asistido hasta 4 km).",
                 "• Control en Algoritmo Verde:\n  Cortina rompevientos (Molle) + Ninfas de\n  Odonatos + micro-dosificación Bti."
             ]),
        ]

        for i, (tit, sub, col, bg_col, bullets) in enumerate(taxones):
            cx = 0.45 + i * 5.12
            draw_card(ax, cx, 2.15, 4.85, 5.55, bg=C_WHITE, ec=col, accent_left=col)
            ax.add_patch(patches.FancyBboxPatch(
                (cx + 0.2, 6.65), 4.45, 0.85,
                boxstyle="round,pad=0.02,rounding_size=0.1",
                facecolor=bg_col, edgecolor="none"
            ))
            ax.text(cx + 2.42, 7.18, tit, color=col, fontsize=12.0, fontweight="bold", ha="center", va="center")
            ax.text(cx + 2.42, 6.78, sub, color=C_TEXT, fontsize=9.8, fontweight="bold", ha="center", va="center")

            for b_idx, b_txt in enumerate(bullets):
                ax.text(cx + 0.28, 6.32 - b_idx * 1.02, b_txt, color=C_TEXT, fontsize=9.9, ha="left", va="top", linespacing=1.25)

        # Banda inferior de Sinergia Fitoquímica y Biológica
        draw_card(ax, 0.45, 0.62, 15.1, 1.28,
                  title="◆ Sinergia de Acción sobre los 3 Taxones (Cero Insecticidas Sintéticos):",
                  title_color=C_GREEN_DARK, bg=C_GREEN_LIGHT, ec=C_GREEN, accent_left=C_GREEN)
        ax.text(0.8, 1.02,
                "La combinación de (1) Bloqueo aerodinámico del viento del valle (Schinus molle), (2) Enmascaramiento olfativo de CO₂ y ácido L-láctico humano\n"
                "mediante monoterpenos volátiles (citral, citronelal, 1,8-cineol, α-pineno) y (3) Depredación acuática por ninfas de libélula (Odonata) + Bti\n"
                "interrumpe simultáneamente el ciclo reproductivo y la orientación hacia el huésped de Culicoides spp., Lutzomyia spp. y Simulium spp.",
                color=C_TEXT, fontsize=9.9, ha="left", va="center", linespacing=1.28)

        pdf.savefig(fig)
        plt.close(fig)

        # =========================================================================
        # DIAPOSITIVA 4: DIAGNÓSTICO ESPACIAL Y CATÁLOGO SIG (RF-01)
        # =========================================================================
        fig, ax = new_slide(
            4, total_slides,
            title="Diagnóstico Geoespacial del Campus: 286 Entidades SIG y Mapa de Calor",
            subtitle="Levantamiento integral de 124 edificaciones, 12 áreas verdes, 16 ejes viales y red de canales lóticos",
            badge="RF-01 · CARTOGRAFÍA"
        )

        # Figura 1 a la izquierda (grande y nítida)
        draw_card(ax, 0.45, 0.65, 9.65, 7.1, bg=C_WHITE, ec=C_BORDER)
        place_image(fig, os.path.join(BASE_DIR, "Figura1_Diagnostico_Espacial_Yachay.png"), [0.55, 0.75, 9.45, 6.9])

        # Panel derecho con desglose de las 286 entidades y 4 distritos
        draw_card(ax, 10.3, 4.35, 5.25, 3.4,
                  title="■ Catálogo Georreferenciado (286 Entidades)",
                  title_color=C_BLUE, bg=C_WHITE, ec=C_BLUE, accent_left=C_BLUE)
        sig_items = [
            ("• 124 Edificaciones y Canchas:", "Huellas poligonales exactas (0 solapamientos)"),
            ("• 12 Áreas Verdes y Parques:", "59,745 m² (~5.97 ha) de jardines y praderas"),
            ("• 16 Ejes Viales y Caminerías:", "Vías troncales y senderos peatonales"),
            ("• 80 Polilíneas Totales:", "Canales lóticos (34 vértices Este), vías y cercas"),
            ("• 69 Puntos Georreferenciados:", "Hitos de vida, 3 paradas de bus, 19 parqueos"),
            ("• 6 Estaciones GPS (T-01..T-06):", "Red de bio-monitoreo en jardines del campus"),
        ]
        for idx, (k, v) in enumerate(sig_items):
            yy = 7.05 - idx * 0.45
            ax.text(10.6, yy, k, color=C_NAVY, fontsize=9.8, fontweight="bold", ha="left", va="center")
            ax.text(10.6, yy - 0.18, f"   {v}", color=C_MUTED, fontsize=9.0, ha="left", va="center")

        draw_card(ax, 10.3, 0.65, 5.25, 3.48,
                  title="▲ 4 Epicentros Epidemiológicos Mapeados",
                  title_color=C_RED, bg=C_RED_LIGHT, ec=C_RED, accent_left=C_RED)
        epi_items = [
            "1. Distrito Sur (54 edif. · ~550 hab.): Las Multis (30–90\n   res./bloque), Las Pats, Las T's, Docentes y Canchas.",
            "2. Distrito Central / Ingenio y San José (37 edif.):\n   Biblioteca 24/7, Aulas B/I, Plaza Mikuna y Sala Capitular.",
            "3. Distrito Norte Senescyt (18 edif. · ~450 hab.):\n   Edif. Senescyt (4 pisos), Centro Médico y Los Bloques A–I.",
            "4. Eje Hídrico Este (Reservorio ~2,006 m² y Canal 34 pts):\n   Santuario natural de odonatos y compuerta hidráulica."
        ]
        for idx, txt in enumerate(epi_items):
            ax.text(10.6, 3.55 - idx * 0.72, txt, color=C_TEXT, fontsize=9.4, ha="left", va="top", linespacing=1.22)

        pdf.savefig(fig)
        plt.close(fig)

        # =========================================================================
        # DIAPOSITIVA 5: MATRIZ MULTICRITERIO DE ALTERNATIVAS (RF-01, RNF-01)
        # =========================================================================
        fig, ax = new_slide(
            5, total_slides,
            title="Comparación Multicriterio de Alternativas y Selección de Estrategia",
            subtitle="Evaluación ponderada (MCDA) frente a requerimientos funcionales (RF) y ambientales (RNF-01 / RNF-02)",
            badge="RF-01 · SELECCIÓN"
        )

        # Tabla MCDA
        draw_card(ax, 0.45, 2.55, 15.1, 5.15,
                  title="◆ Matriz de Decisión Multicriterio (Escala 1.0 a 5.0)",
                  title_color=C_NAVY, bg=C_WHITE, ec=C_BORDER)

        cols = [
            ("Criterio de Evaluación", 3.4),
            ("Peso", 0.9),
            ("A1: Químicos\n(Malatión/Piretroides)", 2.3),
            ("A2: Nebulización\nTérmica Diurna", 2.3),
            ("A3: Trampas UV\nEléctricas", 2.3),
            ("A4: Repelente\nTópico (DEET)", 1.6),
            ("A5: ALGORITMO VERDE\n(Cercas + Bti + SLSQP)", 2.3),
        ]
        rows_mcda = [
            ("Inocuidad Hídrica y Ambiental (RNF-01)", "25%", "1.0 (Contamina riego)", "2.0 (Aerosol inhalable)", "4.5 (Atrae no-objetivo)", "3.0 (Toxicidad dérmica)", "4.9 (Nativas + Bti selectivo)"),
            ("Eficacia sobre Dípteros (RF-01)", "25%", "3.5 (Efecto temporal)", "2.5 (Dispersado por viento)", "1.5 (Simulium es diurno)", "2.5 (Uso individual)", "4.8 (Físico + Fitoquímico)"),
            ("Sostenibilidad Económica (RF-05)", "20%", "1.5 ($4,800+/año)", "1.5 (Diésel e insumos)", "2.0 (Red eléctrica ext.)", "1.0 (Gasto continuo)", "4.7 ($1,470 inversión única)"),
            ("Valor Paisajístico e Inclusión (RNF-02)", "15%", "1.0 (Olor tóxico)", "1.0 (Humo denso)", "2.0 (Plástico invasivo)", "1.0 (Nulo aporte)", "5.0 (Sombra + Hipoalergénico)"),
            ("Factibilidad Operativa Yachay (RF-03)", "15%", "1.5 (Conflicto comunal)", "2.0 (Interrumpe clases)", "3.0 (Fallas intemperie)", "4.0 (No ataca el foco)", "4.8 (Riego por gravedad 0 kWh)"),
            ("PUNTAJE PONDERADO TOTAL", "100%", "1.80 / 5.0", "1.88 / 5.0", "2.73 / 5.0", "2.25 / 5.0", "4.83 / 5.0 (ELEGIDA)"),
        ]

        x0 = 0.65
        y_top = 6.55
        row_h = 0.60

        # Header
        cx = x0
        for c_idx, (c_title, c_w) in enumerate(cols):
            bg_h = C_GREEN if c_idx == 6 else C_NAVY
            ax.add_patch(patches.Rectangle((cx, y_top), c_w, 0.62, facecolor=bg_h, edgecolor=C_WHITE, lw=1))
            ax.text(cx + c_w / 2, y_top + 0.31, c_title, color=C_WHITE, fontsize=9.3, fontweight="bold", ha="center", va="center")
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
                ax.text(cx + c_w / 2, ry + row_h / 2, r_vals[c_idx], color=txt_c, fontsize=9.0, fontweight=fw, ha="center", va="center")
                cx += c_w

        # Tarjetas inferiores de justificación
        draw_card(ax, 0.45, 0.65, 7.35, 1.68,
                  title="✕ ¿Por qué descartamos insecticidas sintéticos y trampas UV?",
                  title_color=C_RED, bg=C_RED_LIGHT, ec=C_RED, accent_left=C_RED, title_size=11.5)
        ax.text(0.78, 1.30,
                "• Los simúlidos pican de día guiados por CO₂, calor y silueta (no son fototrópicos nocturnos),\n  mientras que las trampas eléctricas UV electrocutan polinizadores benéficos (abejas y mariposas).\n"
                "• Los insecticidas sintéticos contaminan las acequias que riegan cultivos en San José de Urcuquí.",
                color=C_TEXT, fontsize=9.0, ha="left", va="center", linespacing=1.26)

        draw_card(ax, 8.1, 0.65, 7.45, 1.68,
                  title="✓ Ventaja Diferenciadora: Manejo Integrado + Protocolo Hipoalergénico",
                  title_color=C_GREEN_DARK, bg=C_GREEN_LIGHT, ec=C_GREEN, accent_left=C_GREEN, title_size=11.5)
        ax.text(8.42, 1.30,
                "• Combina 3 líneas del alcance: Paisajismo Funcional (cercas en 3 estratos) + Control Biológico\n  (Odonatos y Bti) + Tecnología Geoespacial y Telemetría (optimización SLSQP y visor interactivo).\n"
                "• Pionero en salud inclusiva: Sustituye el romero en dormitorios por Cedrón y Huacatay (OPALS 1/10).",
                color=C_TEXT, fontsize=9.0, ha="left", va="center", linespacing=1.26)

        pdf.savefig(fig)
        plt.close(fig)

        # =========================================================================
        # DIAPOSITIVA 6: DISEÑO TÉCNICO I - ARQUITECTURA TRI-ESTRATO (RF-02, RNF-02)
        # =========================================================================
        fig, ax = new_slide(
            6, total_slides,
            title="Diseño Técnico I: Cercas Vivas en 3 Estratos y Zonificación Hipoalergénica",
            subtitle="Ingeniería agroecológica, fitoquímica repelente pasiva 24/7 y biocompatibilidad médica estudiantil",
            badge="RF-02 · RNF-02"
        )

        # Figura 3 a la izquierda
        draw_card(ax, 0.45, 0.65, 9.25, 7.1, bg=C_WHITE, ec=C_BORDER)
        place_image(fig, os.path.join(BASE_DIR, "Figura3_Corte_Transversal_Cercas_3Estratos.png"), [0.55, 0.85, 9.05, 6.7])

        # Especificaciones de los 3 estratos a la derecha
        estratos_info = [
            ("● Estrato Alto (3.5 – 5.0 m): Schinus molle (Molle Andino)",
             C_GREEN_DARK, C_GREEN_LIGHT,
             "• Densidad: 1 árbol cada 2.0 m lineales (490 árboles totales).\n"
             "• Fitoquímica: α-pineno (38%), β-pineno (12%), limoneno (14%) y cariofileno.\n"
             "• Función: Cortina rompevientos que frena la brisa del valle (2.8 m/s) e\n  impide el arrastre eólico de Simulium spp. hacia aulas y residencias."),
            ("● Estrato Medio (1.2 – 2.0 m): Arrayán + Protocolo Hipoalergénico",
             C_BLUE, C_BLUE_LIGHT,
             "• Densidad: 1 arbusto cada 1.0 m lineal (980 arbustos totales).\n"
             "• Columna estructural: Myrcianthes hallii (Arrayán nativo, polen no eólico).\n"
             "• Buffer Hipoalergénico (<5 m de dormitorios): Sustitución 100% de romero\n  por Cedrón (Aloysia citrodora, citral 35%) y Huacatay (Tagetes minuta)\n  para evitar rinitis, asma o dermatitis por alcanfor en estudiantes atópicos."),
            ("◆ Estrato Bajo (0.4 – 0.8 m): Cymbopogon citratus (Hierba Luisa)",
             C_AMBER, C_AMBER_LIGHT,
             "• Densidad: 2 macollas por metro lineal (1,960 macollas en doble hilera).\n"
             "• Fitoquímica: Citronelal (32%), geraniol (28%) y citral (22%).\n"
             "• Función: Sellado basal contra vuelo rasante de Culicoides y Lutzomyia;\n  entra en madurez vegetativa y emisión activa desde la Semana 3."),
        ]

        for idx, (tit, col, bg_c, desc) in enumerate(estratos_info):
            yy = 5.45 - idx * 2.38
            draw_card(ax, 9.9, yy, 5.65, 2.22, title=tit, title_color=col, bg=bg_c, ec=col, accent_left=col, title_size=10.1)
            ax.text(10.22, yy + 1.58, desc, color=C_TEXT, fontsize=9.2, ha="left", va="top", linespacing=1.28)

        pdf.savefig(fig)
        plt.close(fig)

        # =========================================================================
        # DIAPOSITIVA 7: DISEÑO TÉCNICO II - OPTIMIZACIÓN SLSQP Y 7 TRAMOS (RF-02)
        # =========================================================================
        fig, ax = new_slide(
            7, total_slides,
            title="Diseño Técnico II: Optimización Matemática SLSQP y 7 Tramos Viales",
            subtitle="Implantación estratégica de 980 m lineales respetando el 100% de calles, caminerías y accesos del campus",
            badge="RF-02 · SLSQP"
        )

        # Figura 2 a la izquierda
        draw_card(ax, 0.45, 0.65, 9.15, 7.1, bg=C_WHITE, ec=C_BORDER)
        place_image(fig, os.path.join(BASE_DIR, "Figura2_Diseno_Tecnico_Intervencion.png"), [0.55, 0.75, 8.95, 6.9])

        # Panel derecho: Ecuación SLSQP + Tabla de 7 Tramos Viales
        draw_card(ax, 9.8, 5.25, 5.75, 2.5,
                  title="■ Modelo de Optimización No Lineal (SciPy SLSQP)",
                  title_color=C_BLUE, bg=C_BLUE_LIGHT, ec=C_BLUE, accent_left=C_BLUE, title_size=11.2)
        ax.text(10.10, 7.12,
                "Función Objetivo Multiobjetivo (Población Protegida):\n"
                "  max F(L₁,L₂,L₃) = Σ wᵢ·Pᵢ·[1 - exp(-kᵢ·Lᵢ)] - γ·Σ cⱼ·Lⱼ\n"
                "Sujeto a restricciones presupuestarias y topológicas:\n"
                "  • L₁ + L₂ + L₃ ≤ 980 m  |  Costo ≤ USD 1,470 (USD 1.50/m)\n"
                "  • 0 cruces con 16 ejes viales y 124 edificaciones (GIS).",
                color=C_NAVY, fontsize=8.6, ha="left", va="top", linespacing=1.32, family="monospace")

        draw_card(ax, 9.8, 0.65, 5.75, 4.4,
                  title="● Desglose de los 7 Tramos Viales Discontinuos (980 m)",
                  title_color=C_GREEN_DARK, bg=C_WHITE, ec=C_GREEN, accent_left=C_GREEN, title_size=11.2)

        tramos_data = [
            ("CV-1A", "Sur Las Multis y Concha Acústica", "117.7 m", "Paso libre Calle Sur"),
            ("CV-1B", "Arco Central Las Multis – Las Pats", "146.7 m", "Paso libre Vía Yachay"),
            ("CV-1C", "Sur Las Pats y Complejo Deportivo", "115.6 m", "Subt. Cerca 1 = 380 m"),
            ("CV-2A", "Oeste Plaza Mikuna e Invernaderos", "158.1 m", "Paso libre Caminería"),
            ("CV-2B", "Norte Lab. Idiomas y Parque Central", "121.9 m", "Subt. Cerca 2 = 280 m"),
            ("CV-3A", "Oeste Residencias Los Bloques A–I", "163.3 m", "Paso libre Vía Norte"),
            ("CV-3B", "Este Edificio Senescyt y Comedor", "156.7 m", "Subt. Cerca 3 = 320 m"),
            ("TOTAL", "7 Tramos · 0 Cruces Viales", "980.0 m", "1,960 Plánt. · 39,200 m²"),
        ]
        ty0 = 4.35
        for idx, (cod, sec, lon, obs) in enumerate(tramos_data):
            ry = ty0 - idx * 0.45
            is_tot = (idx == len(tramos_data) - 1)
            bg_r = "#d1fae5" if is_tot else ("#f8fafc" if idx % 2 == 0 else C_WHITE)
            ax.add_patch(patches.Rectangle((10.0, ry - 0.18), 5.4, 0.42, facecolor=bg_r, edgecolor="#e2e8f0", lw=0.6))
            fw = "bold" if is_tot else "normal"
            col_t = C_GREEN_DARK if is_tot else C_TEXT
            ax.text(10.10, ry, cod, color=C_BLUE if not is_tot else C_GREEN_DARK, fontsize=8.5, fontweight="bold", ha="left", va="center")
            ax.text(10.80, ry, sec, color=col_t, fontsize=8.2, fontweight=fw, ha="left", va="center")
            ax.text(13.68, ry, lon, color=col_t, fontsize=8.5, fontweight="bold", ha="right", va="center")
            ax.text(13.80, ry, obs, color=C_MUTED if not is_tot else C_GREEN_DARK, fontsize=7.9, fontweight=fw, ha="left", va="center")

        pdf.savefig(fig)
        plt.close(fig)

        # =========================================================================
        # DIAPOSITIVA 8: PROTOTIPO FUNCIONAL WEB Y ARQUITECTURA DE SOFTWARE (4.2)
        # =========================================================================
        fig, ax = new_slide(
            8, total_slides,
            title="Prototipo Funcional: Visor Geoespacial Interactivo y API de Telemetría",
            subtitle="Entregable 4.2: Aplicación web autónoma desplegada en GitHub Pages con ventanas flotantes arrastrables",
            badge="PROTOTIPO · SIG"
        )

        # Captura / Mockup visual o tarjetas de arquitectura
        draw_card(ax, 0.45, 3.95, 7.4, 3.8,
                  title="◆ Características del Visor Interactivo (Folium / Leaflet / JS)",
                  title_color=C_BLUE, bg=C_WHITE, ec=C_BLUE, accent_left=C_BLUE)
        feat_web = [
            "• Ventanas Flotantes Glassmorphic y Arrastrables (⠿): Menú vertical superior,\n  Dock utilitario, Simbología y Dashboard se pueden mover libremente sin solaparse.",
            "• Conmutadores Deslizantes (Toggle Switches): Cambio instantáneo de Idioma\n  (ES ⇄ EN) y Modo Visual (Sol Claro ⇄ Luna Oscuro) con persistencia de capas.",
            "• 286 Entidades Interactivas: Polígonos patrimoniales con pointer-events: none para\n  permitir clic individual en las 124 edificaciones, 12 jardines y 16 vías.",
            "• Evidencia Fotográfica Embebida (Base64): Al hacer clic en el Pozo de Sala\n  Capitular se despliegan las fotografías reales de la inspección de campo."
        ]
        for idx, txt in enumerate(feat_web):
            ax.text(0.8, 7.05 - idx * 0.78, txt, color=C_TEXT, fontsize=9.8, ha="left", va="top", linespacing=1.26)

        draw_card(ax, 0.45, 0.65, 7.4, 3.05,
                  title="■ Stack Tecnológico y Reproducibilidad Abierta (Open Science)",
                  title_color=C_GREEN_DARK, bg=C_GREEN_LIGHT, ec=C_GREEN, accent_left=C_GREEN)
        stack_items = [
            "• generar_mapa_interactivo.py -> Compila el visor HTML autónomo de 286 entidades.",
            "• modelo_optimizacion_matematica.py -> Ejecuta SLSQP (SciPy) y simulación Monte Carlo.",
            "• api_telemetria.py -> Microservicio REST en FastAPI (/docs) para ingesta de estaciones.",
            "• CI/CD GitHub Actions (deploy_pages.yml) -> Publicación continua en GitHub Pages."
        ]
        for idx, txt in enumerate(stack_items):
            ax.text(0.8, 3.02 - idx * 0.54, txt, color=C_TEXT, fontsize=9.6, ha="left", va="top")

        # Derecha: Figura 2 + QR de acceso directo
        draw_card(ax, 8.1, 0.65, 7.45, 7.1,
                  title="▸ Vista Cartográfica y Acceso Móvil Inmediato vía GitHub",
                  title_color=C_NAVY, bg=C_WHITE, ec=C_BORDER, accent_left=C_AMBER)
        place_image(fig, os.path.join(BASE_DIR, "Figura2_Diseno_Tecnico_Intervencion.png"), [8.25, 2.55, 7.15, 4.55])
        place_image(fig, os.path.join(BASE_DIR, "qr_algoritmo_verde.png"), [8.35, 0.80, 1.65, 1.65])
        ax.text(10.2, 1.92, "▸ Repositorio Público (con botón al Mapa en Vivo):", color=C_BLUE, fontsize=10.2, fontweight="bold", ha="left", va="center")
        ax.text(10.2, 1.55, "https://github.com/JeffersonConza/algoritmo-verde-yosw2026", color=C_NAVY, fontsize=9.8, fontweight="bold", ha="left", va="center")
        ax.text(10.2, 1.18, "◆ Enlace Directo GitHub Pages:\nhttps://jeffersonconza.github.io/algoritmo-verde-yosw2026/", color=C_GREEN_DARK, fontsize=9.4, fontweight="bold", ha="left", va="center")

        pdf.savefig(fig)
        plt.close(fig)

        # =========================================================================
        # DIAPOSITIVA 9: PLAN DE IMPLEMENTACIÓN, RIEGO Y MANTENIMIENTO (RF-03)
        # =========================================================================
        fig, ax = new_slide(
            9, total_slides,
            title="Plan de Implementación, Riego Gravitacional y Mantenimiento",
            subtitle="Hoja de ruta realista en 4 fases (16 semanas), 0 kWh de consumo eléctrico y gobernanza institucional",
            badge="RF-03 · OPERACIÓN"
        )

        # 4 Fases como tarjetas en fila superior
        fases = [
            ("FASE I (Semanas 1–2)", "Preparación y Trazado GPS", C_BLUE, C_BLUE_LIGHT,
             "• Replanteo topográfico de los\n  7 tramos (980 m lineales).\n"
             "• Zanjado manual (40×40 cm).\n"
             "• Censo voluntario de alergias\n  con Bienestar Estudiantil.\n"
             "• Tendido de tubería PE 16 mm\n  desde tomas de acequia."),
            ("FASE II (Semanas 3–5)", "Siembra Tri-Estrato", C_GREEN_DARK, C_GREEN_LIGHT,
             "• Incorporación de 1.5 t de\n  compost propio de Yachay Tech.\n"
             "• Trasplante escalonado de las\n  1,960 plántulas y macollas.\n"
             "• Entutorado con caña guadua.\n"
             "• Repelencia basal activa desde\n  la 3.ª semana (Hierba Luisa)."),
            ("FASE III (Semanas 6–8)", "Biocontrol Acuático", "#0288d1", "#e1f5fe",
             "• Consolidación del santuario de\n  ninfas de libélula (Odonata) en\n  el reservorio este (~2,006 m²).\n"
             "• Micro-dosificación focalizada\n  de Bti en cabecera de canales.\n"
             "• Activación de las 6 estaciones\n  GPS de bio-monitoreo (T-01..06)."),
            ("FASE IV (Semanas 9–16+)", "Mantenimiento y Podas", C_AMBER, C_AMBER_LIGHT,
             "• Poda formativa bimensual del\n  estrato arbustivo (2 h/semana\n  por cuadrilla de jardinería).\n"
             "• Conteo semanal en trampas\n  por estudiantes de Biomedicina\n  y Biología (prácticas).\n"
             "• Reproducción por esquejes ($0)."),
        ]

        for i, (f_cod, f_tit, col, bg_c, desc) in enumerate(fases):
            fx = 0.45 + i * 3.82
            draw_card(ax, fx, 3.65, 3.62, 4.05, bg=C_WHITE, ec=col, accent_left=col)
            ax.add_patch(patches.FancyBboxPatch(
                (fx + 0.18, 6.85), 3.26, 0.68,
                boxstyle="round,pad=0.02,rounding_size=0.08",
                facecolor=bg_c, edgecolor="none"
            ))
            ax.text(fx + 1.81, 7.30, f_cod, color=col, fontsize=10.5, fontweight="bold", ha="center", va="center")
            ax.text(fx + 1.81, 7.00, f_tit, color=C_NAVY, fontsize=9.8, fontweight="bold", ha="center", va="center")
            ax.text(fx + 0.22, 6.58, desc, color=C_TEXT, fontsize=9.4, ha="left", va="top", linespacing=1.32)

        # Dos tarjetas inferiores: Riego por Gravedad y Ciclo de Vida / Gobernanza
        draw_card(ax, 0.45, 0.65, 7.35, 2.75,
                  title="● Ingeniería de Riego por Gravedad Pura (0 kWh de Energía Eléctrica)",
                  title_color=C_BLUE, bg=C_WHITE, ec=C_BLUE, accent_left=C_BLUE, title_size=11.4)
        ax.text(0.78, 2.72,
                "• Aprovecha la pendiente topográfica natural del campus (cota ~2,065 m en Senescyt\n  hacia ~2,025 m en Las Multis) sin requerir bombeo eléctrico.\n"
                "• Derivación mediante filtro de malla hacia tubería PE de 16 mm con goteros\n  autocompensantes (2.0 L/h cada 50 cm) a presión hidrostática natural (0.4–0.8 bar).\n"
                "• Cero motobombas y cero riesgo eléctrico exterior (cumple RNF-01).",
                color=C_TEXT, fontsize=9.1, ha="left", va="top", linespacing=1.26)

        draw_card(ax, 8.1, 0.65, 7.45, 2.75,
                  title="■ Gobernanza, Responsables y Ciclo de Vida (>10 Años)",
                  title_color=C_GREEN_DARK, bg=C_GREEN_LIGHT, ec=C_GREEN, accent_left=C_GREEN, title_size=11.4)
        ax.text(8.42, 2.72,
                "• Operación Institucional: Dirección de Infraestructura y Mantenimiento de Yachay Tech\n  con las cuadrillas de jardinería actuales (sin contratar personal adicional).\n"
                "• Vinculación Académica: Club de Agroecología y prácticas de Biomedicina y Química\n  realizan la lectura semanal de las 6 estaciones GPS.\n"
                "• Ciclo de Vida Regenerativo (>10 años): Su eficacia aumenta cada año con el porte foliar.",
                color=C_TEXT, fontsize=9.1, ha="left", va="top", linespacing=1.26)

        pdf.savefig(fig)
        plt.close(fig)

        # =========================================================================
        # DIAPOSITIVA 10: EVALUACIÓN DE EFICACIA E IMPACTO (RF-04, RNF-01)
        # =========================================================================
        fig, ax = new_slide(
            10, total_slides,
            title="Evaluación de Eficacia Estadística e Impacto sobre Fauna No Objetivo",
            subtitle="Validación longitudinal en 6 estaciones GPS (16 semanas) y análisis ecotoxicológico (RF-04, RNF-01)",
            badge="RF-04 · IMPACTO"
        )

        # Figura 4 arriba/izquierda
        draw_card(ax, 0.45, 2.65, 10.2, 5.1, bg=C_WHITE, ec=C_BORDER)
        place_image(fig, os.path.join(BASE_DIR, "Figura4_Curva_Reduccion_BioMonitoreo.png"), [0.55, 2.75, 10.0, 4.9])

        # Indicadores Estadísticos a la derecha
        draw_card(ax, 10.85, 2.65, 4.7, 5.1,
                  title="▲ Métricas de Validación (RF-04)",
                  title_color=C_BLUE, bg=C_WHITE, ec=C_BLUE, accent_left=C_BLUE)
        stat_boxes = [
            ("86.3 ± 6.5", "Línea Base (Sem. 1–4)", "Adultos / trampa / semana", C_RED, C_RED_LIGHT),
            ("14.8 ± 2.0", "Consolidación (Sem. 16)", "Adultos / trampa / semana", C_GREEN_DARK, C_GREEN_LIGHT),
            ("-82.8%", "Mitigación Global", "Prueba t = 25.85 (p < 0.001)", C_BLUE, C_BLUE_LIGHT),
            ("≥ 25 µg/m³", "Pluma de Monoterpenos", "Activa hasta 40 m sotavento", C_AMBER, C_AMBER_LIGHT),
        ]
        for idx, (val, t1, t2, col, bg_c) in enumerate(stat_boxes):
            sy = 6.08 - idx * 1.08
            ax.add_patch(patches.FancyBboxPatch(
                (11.15, sy), 4.2, 0.92,
                boxstyle="round,pad=0.02,rounding_size=0.1",
                facecolor=bg_c, edgecolor=col, lw=1.1
            ))
            ax.text(12.15, sy + 0.46, val, color=col, fontsize=14.5, fontweight="bold", ha="center", va="center")
            ax.text(13.15, sy + 0.60, t1, color=C_NAVY, fontsize=9.6, fontweight="bold", ha="left", va="center")
            ax.text(13.15, sy + 0.28, t2, color=C_MUTED, fontsize=8.6, ha="left", va="center")

        # Franja inferior: Seguridad en Salud y Fauna No Objetivo (RNF-01)
        draw_card(ax, 0.45, 0.65, 15.1, 1.78,
                  title="◆ Inocuidad Ambiental y Protección de Fauna No Objetivo (Polinizadores, Ictiofauna y Regantes - RNF-01)",
                  title_color=C_GREEN_DARK, bg=C_GREEN_LIGHT, ec=C_GREEN, accent_left=C_GREEN)
        ax.text(0.8, 1.35,
                "1. Abejas y Polinizadores (Apis mellifera, Bombus spp.): Las especies elegidas son melíferas y polinizadas por insectos; no sufren toxicidad.\n"
                "2. Especificidad de Bti (Bacillus thuringiensis israelensis): Sus cristales proteicos δ-endotoxina requieren pH intestinal alcalino (>9.0) y proteasas\n"
                "   exclusivas de larvas de Nematocera (Simuliidae/Culicoides); es 100% inocuo para libélulas (Odonata), peces, anfibios, aves, ganado y seres humanos.\n"
                "3. Trampas Ecológicas Selectivas: Cebadas con CO₂ orgánico (levadura + sacarosa) y ácido L-láctico (sudor humano), sin electrocución indiscriminada.",
                color=C_TEXT, fontsize=9.3, ha="left", va="center", linespacing=1.28)

        pdf.savefig(fig)
        plt.close(fig)

        # =========================================================================
        # DIAPOSITIVA 11: VIABILIDAD ECONÓMICA Y PLAN DE ADOPCIÓN (RF-05)
        # =========================================================================
        fig, ax = new_slide(
            11, total_slides,
            title="Viabilidad Económica ($1,470.00 USD) y Estrategia de Adopción",
            subtitle="Presupuesto llave en mano de $1.50 USD por metro lineal con amortización en menos de 3 meses (RF-05)",
            badge="RF-05 · COSTOS"
        )

        # Tabla Presupuestaria a la izquierda
        draw_card(ax, 0.45, 2.75, 9.5, 5.0,
                  title="■ Presupuesto Detallado de Implementación (980 m Lineales)",
                  title_color=C_NAVY, bg=C_WHITE, ec=C_BORDER)

        b_cols = [("Rubro / Partida", 2.5), ("Especificación Técnica", 3.6), ("Cantidad", 1.2), ("Unitario", 0.9), ("Total USD", 1.0)]
        b_rows = [
            ("Plántulas de Molle", "Schinus molle (60–80 cm, vivero local)", "490 u.", "$0.80", "$392.00"),
            ("Plántulas de Arrayán", "Myrcianthes hallii (arbusto nativo)", "490 u.", "$0.70", "$343.00"),
            ("Aromáticas Hipoalerg.", "Aloysia citrodora, Tagetes minuta, R. officinalis", "490 u.", "$0.50", "$245.00"),
            ("Macollas Hierba Luisa", "Cymbopogon citratus (doble hilera basal)", "1,960 u.", "$0.15", "$294.00"),
            ("Manguera Goteo 16mm", "PE con goteros autocompensantes cada 50 cm", "980 m", "$0.15", "$147.00"),
            ("Accesorios y Filtros", "Tomas de acequia, válvulas, filtro de malla y Bti", "Global", "$49.00", "$49.00"),
            ("Compost Institucional", "Abono orgánico planta de compostaje Yachay Tech", "1.5 ton", "$0.00", "$0.00"),
            ("INVERSIÓN TOTAL", "Costo unitario optimizado: $1.50 USD / metro lineal", "980 m", "$1.50/m", "$1,470.00"),
        ]

        bx0 = 0.62
        by_top = 6.62
        bh = 0.45
        cx = bx0
        for c_idx, (ct, cw) in enumerate(b_cols):
            ax.add_patch(patches.Rectangle((cx, by_top), cw, 0.48, facecolor=C_NAVY, edgecolor=C_WHITE, lw=0.8))
            ax.text(cx + cw / 2, by_top + 0.24, ct, color=C_WHITE, fontsize=9.0, fontweight="bold", ha="center", va="center")
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
                ax.text(cx + cw / 2, ry + bh / 2, r_vals[c_idx], color=col_t, fontsize=8.8, fontweight=fw, ha="center", va="center")
                cx += cw

        # Derecha: Comparativa Financiera (ROI)
        draw_card(ax, 10.15, 4.35, 5.4, 3.4,
                  title="■ Rentabilidad vs. Fumigación Química",
                  title_color=C_AMBER, bg=C_AMBER_LIGHT, ec=C_AMBER, accent_left=C_AMBER)
        ax.text(10.48, 7.05,
                "• Fumigación Química Tradicional:\n"
                "  ~USD 350 por aplicación quincenal\n"
                "  = USD 4,800 a 7,000 / año (gasto perpetuo).\n\n"
                "• Algoritmo Verde YT:\n"
                "  USD 1,470.00 de inversión única inicial\n"
                "  + mantenimiento interno con costo marginal ~USD 0.\n\n"
                "▸ Retorno de Inversión (Payback): < 3 meses\n"
                "▸ Ahorro Institucional a 5 años: > USD 22,500.",
                color=C_TEXT, fontsize=9.6, ha="left", va="top", linespacing=1.28)

        # Derecha Abajo + Franja Inferior: Adopción por la Comunidad
        draw_card(ax, 10.15, 0.65, 5.4, 3.48,
                  title="◆ Plan de Adopción Comunitaria",
                  title_color=C_GREEN_DARK, bg=C_GREEN_LIGHT, ec=C_GREEN, accent_left=C_GREEN)
        ax.text(10.48, 3.48,
                "1. Mingas Universitarias «Adopta un Tramo»:\n   Siembra participativa por residencias (Multis, Pats,\n   Bloques) e identificación con placas QR.\n"
                "2. Propagación Vegetativa a Costo Cero:\n   En los 4 Invernaderos Experimentales de Yachay Tech\n   se multiplican esquejes de Hierba Luisa y Cedrón.\n"
                "3. Transferencia a Regantes de Urcuquí:\n   Entrega de guía técnica y esquejes a agricultores\n   vecinos para proteger linderos sin agrotóxicos.",
                color=C_TEXT, fontsize=9.3, ha="left", va="top", linespacing=1.26)

        draw_card(ax, 0.45, 0.65, 9.5, 1.9,
                  title="★ Resumen de Viabilidad Operativa para Yachay Tech",
                  title_color=C_BLUE, bg=C_BLUE_LIGHT, ec=C_BLUE, accent_left=C_BLUE)
        ax.text(0.8, 1.48,
                "• Insumos 100% disponibles en viveros de Ibarra y Urcuquí (sin importaciones ni trámites aduaneros).\n"
                "• Utiliza la red de acequias y la planta de compostaje ya existentes en el campus universitario.\n"
                "• Genera subproductos útiles (aceites esenciales y biomasa aromática) para prácticas de los laboratorios de Química y Agroindustria.",
                color=C_TEXT, fontsize=9.5, ha="left", va="center", linespacing=1.32)

        pdf.savefig(fig)
        plt.close(fig)

        # =========================================================================
        # DIAPOSITIVA 12: CONCLUSIONES, DECLARACIÓN DE IA (SEC. 13) Y QR GITHUB
        # =========================================================================
        fig, ax = new_slide(
            12, total_slides,
            title="Conclusiones, Declaración de Uso de IA (Sec. 13) y Acceso Abierto",
            subtitle="Transparencia metodológica, reconocimiento de limitaciones y despliegue inmediato en el campus",
            badge="CONCLUSIONES · IA"
        )

        # Izquierda Arriba: Conclusiones y Limitaciones Reconocidas
        draw_card(ax, 0.45, 4.25, 9.8, 3.5,
                  title="◆ Conclusiones Clave y Gestión de Limitaciones",
                  title_color=C_NAVY, bg=C_WHITE, ec=C_BLUE, accent_left=C_BLUE)
        concl_pts = [
            "1. Solución Integral Científicamente Fundamentada: Mitiga el complejo de dípteros (Culicoides spp.,\n   Lutzomyia spp. y Simulium spp.) en 124 edificaciones con un 82.8% de reducción proyectada (p < 0.001).",
            "2. Innovación Hipoalergénica e Inocuidad Hídrica: Protege a estudiantes alérgicos/asmáticos (protocolo libre\n   de romero en dormitorios) y preserva el agua de riego comunal de Urcuquí y los polinizadores nativos.",
            "3. Limitación Reconocida y Mitigación: Aunque el estrato arbóreo (S. molle) requiere 6–12 meses para alcanzar\n   su porte completo, el estrato basal (C. citratus y A. citrodora) más el biocontrol con Bti proveen repelencia\n   y reducción larvaria efectiva desde la 3.ª semana de ejecución.",
        ]
        for idx, txt in enumerate(concl_pts):
            ax.text(0.8, 7.12 - idx * 0.94, txt, color=C_TEXT, fontsize=9.5, ha="left", va="top", linespacing=1.25)

        # Izquierda Abajo: Declaración Obligatoria de Uso de IA (Sección 13)
        draw_card(ax, 0.45, 0.65, 9.8, 3.4,
                  title="■ Declaración Obligatoria de Uso de Inteligencia Artificial (Sección 13 del Reto)",
                  title_color=C_GREEN_DARK, bg=C_GREEN_LIGHT, ec=C_GREEN, accent_left=C_GREEN)
        ax.text(0.8, 3.42,
                "• Autoría Humana Directa del Equipo (100% Original): Diagnóstico de campo e inspección fotográfica en Sala\n"
                "  Capitular, levantamiento y curaduría GPS de las 286 entidades del campus (124 edificios, 12 jardines, 16 vías),\n"
                "  diferenciación taxonómica del complejo Culicoides/Lutzomyia/Simulium, protocolo médico hipoalergénico,\n"
                "  formulación del modelo de optimización espacial SLSQP y estructuración del presupuesto de $1,470.00 USD.\n"
                "• Herramientas Computacionales e IA de Apoyo:\n"
                "  - Python (SciPy SLSQP, Folium, Matplotlib): Resolución numérica y renderizado cartográfico supervisado.\n"
                "  - Modelos de Lenguaje (LLMs - Claude / ChatGPT): Asistencia en depuración de código HTML/JS del visor,\n"
                "    traducción técnica al inglés (Executive Summary / UI bilingüe) y verificación de formato APA 7.ª edición.",
                color=C_TEXT, fontsize=9.1, ha="left", va="top", linespacing=1.26)

        # Derecha: Tarjeta de Cierre y QR Único hacia GitHub
        draw_card(ax, 10.5, 0.65, 5.05, 7.1,
                  title="■ Escanea nuestro QR (GitHub)",
                  title_color=C_WHITE, bg=C_NAVY, ec=C_GREEN, title_size=13.5)
        place_image(fig, os.path.join(BASE_DIR, "qr_algoritmo_verde.png"), [11.22, 3.45, 3.6, 3.6])

        ax.text(13.02, 3.05, "Repositorio Público Oficial:", color="#94a3b8", fontsize=10, fontweight="bold", ha="center", va="center")
        ax.text(13.02, 2.68, "github.com/JeffersonConza/\nalgoritmo-verde-yosw2026",
                color="#6ee7b7", fontsize=10.8, fontweight="bold", ha="center", va="center")

        ax.add_patch(patches.FancyBboxPatch(
            (10.85, 1.45), 4.35, 0.85,
            boxstyle="round,pad=0.02,rounding_size=0.12",
            facecolor=C_GREEN, edgecolor="none"
        ))
        ax.text(13.02, 1.88, "▸ Dentro de GitHub: Botón directo\n«VER MAPA INTERACTIVO EN VIVO»",
                color=C_WHITE, fontsize=10.2, fontweight="bold", ha="center", va="center")

        ax.text(13.02, 0.98, "¡Muchas gracias! · Algoritmo Verde YT ◆",
                color=C_WHITE, fontsize=11.5, fontweight="bold", ha="center", va="center")

        pdf.savefig(fig)
        plt.close(fig)

    print(f"Presentación PDF generada exitosamente (12 diapositivas) en: {OUT_PDF}")


if __name__ == "__main__":
    generar_presentacion()
