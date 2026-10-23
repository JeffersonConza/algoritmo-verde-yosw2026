"""
Generador del Visor Geoespacial Interactivo - Reto 3: Control de Arenillas
Equipo: Algoritmo Verde YT | Yachay Open Science Week 2026
Enfoque: Humanista, Bilingüe (ES/EN), Tema Claro/Oscuro, Identidad de Marca y Acceso Móvil QR
Calibrado con Coordenadas GPS Oficiales de Google Maps y Capas Base Optimizadas
"""

import os
import base64
import random
import folium
from folium import plugins

def generar_mapa():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Cargar código QR en base64 para inclusión autónoma
    qr_path = os.path.join(base_dir, "qr_algoritmo_verde.png")
    qr_b64 = ""
    if os.path.exists(qr_path):
        with open(qr_path, "rb") as f:
            qr_b64 = base64.b64encode(f.read()).decode("utf-8")

    # Coordenadas centrales calibradas de Yachay Tech
    center_lat = 0.4048
    center_lon = -78.1725
    
    # Crear el mapa base centrado en Yachay Tech
    m = folium.Map(
        location=[center_lat, center_lon],
        zoom_start=16,
        max_zoom=20,
        control_scale=True,
        tiles=None
    )
    
    # -------------------------------------------------------------
    # 1. CAPAS BASE COMPATIBLES OFFLINE, FILE:/// Y MODO NOCHE
    # -------------------------------------------------------------
    # 1. Capa Predeterminada: Google Satélite Híbrido (show=True)
    tile_hybrid = folium.TileLayer(
        tiles='https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}',
        attr='Google Maps Satellite',
        name='🛰️ Google Satélite Híbrido',
        overlay=False,
        control=True,
        show=True,
        max_zoom=20
    ).add_to(m)

    # Capas alternativas (show=False para que Satélite sea el predeterminado activo)
    tile_streets = folium.TileLayer(
        tiles='https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
        attr='Google Maps Streets',
        name='🗺️ Google Callejero Oficial',
        overlay=False,
        control=True,
        show=False,
        max_zoom=20
    ).add_to(m)

    folium.TileLayer(
        tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}',
        attr='Esri World Street Map',
        name='🏙️ Esri Callejero (Calles y Campus)',
        overlay=False,
        control=True,
        show=False,
        max_zoom=19
    ).add_to(m)

    folium.TileLayer(
        tiles='https://{s}.tile.openstreetmap.de/{z}/{x}/{y}.png',
        attr='&copy; OpenStreetMap contributors',
        subdomains='abc',
        name='🌐 OpenStreetMap (FOSSGIS Libre)',
        overlay=False,
        control=True,
        show=False,
        max_zoom=19
    ).add_to(m)

    folium.TileLayer(
        tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        attr='Esri World Imagery',
        name='🌍 Satélite Esri (Fotografía Aérea)',
        overlay=False,
        control=True,
        show=False,
        max_zoom=19
    ).add_to(m)

    folium.TileLayer(
        tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}',
        attr='Esri World Topo Map',
        name='⛰️ Relieve y Topografía (Esri Topo)',
        overlay=False,
        control=True,
        show=False,
        max_zoom=19
    ).add_to(m)

    # 7. Modo Noche (Esri Dark Canvas - Alto contraste para presentaciones nocturnas)
    tile_dark = folium.TileLayer(
        tiles='https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Dark_Gray_Base/MapServer/tile/{z}/{y}/{x}',
        attr='Esri Dark Gray Canvas',
        name='🌌 Modo Noche (Esri Dark)',
        overlay=False,
        control=True,
        show=False,
        max_zoom=19
    ).add_to(m)

    # -------------------------------------------------------------
    # 2. FEATURE GROUPS (CAPAS TEMÁTICAS HUMANIZADAS)
    # -------------------------------------------------------------
    fg_distritos = folium.FeatureGroup(name="🏛️ Zonas Principales: Envolventes Orgánicas Suaves", show=True)
    fg_areas_verdes = folium.FeatureGroup(name="🌳 Áreas Verdes, Jardines Patrimoniales y Parques (12 Polígonos)", show=True)
    fg_vias = folium.FeatureGroup(name="🛣️ Red Vial, Caminerías y Senderos del Campus (16 Ejes)", show=True)
    fg_zonas = folium.FeatureGroup(name="🔥 Diagnóstico: Mapa de Calor de Picaduras y Riesgo (Simulium spp.)", show=False)
    fg_perimetros = folium.FeatureGroup(name="📐 Perímetros de Conjunto Histórico y Delimitaciones", show=False)
    fg_edificios = folium.FeatureGroup(name="🏛️ Vida en el Campus (Residencias, Aulas, Cultura)", show=True)
    fg_canales = folium.FeatureGroup(name="💧 Fuentes de Agua y Red Hídrica (Lóticas y Lénticas)", show=True)
    fg_biocontrol = folium.FeatureGroup(name="🦗 Biocontrol Acuático (Libélulas Nativas + Bti)", show=True)
    fg_cercas = folium.FeatureGroup(name="🌿 Cercas Vivas en 3 Estratos (Algoritmo Verde)", show=True)
    fg_buffer = folium.FeatureGroup(name="🛡️ Espacios Protegidos y Aromaterapia (Buffer 40m)", show=True)
    fg_trampas = folium.FeatureGroup(name="🎯 Bio-Monitoreo Continuo de Bienestar (6 Puntos)", show=True)

    # -------------------------------------------------------------
    # 2.1 ENVOLVENTES ORGÁNICAS CALIBRADAS DE LAS 4 ZONAS PRINCIPALES DEL CAMPUS
    # -------------------------------------------------------------
    # Delimitación biofílica continua mediante suavizado de Chaikin (3 iteraciones).
    # Calibración espacial integral que cubre el 100% de las 124 edificaciones y 69 hitos del campus.
    def chaikin_closed(nodes, iterations=3):
        pts = [list(p) for p in nodes]
        for _ in range(iterations):
            new_pts = []
            n = len(pts)
            for i in range(n):
                p1 = pts[i]
                p2 = pts[(i + 1) % n]
                q = [0.75 * p1[0] + 0.25 * p2[0], 0.75 * p1[1] + 0.25 * p2[1]]
                r = [0.25 * p1[0] + 0.75 * p2[0], 0.25 * p1[1] + 0.75 * p2[1]]
                new_pts.extend([q, r])
            pts = new_pts
        res = [[round(p[0], 7), round(p[1], 7)] for p in pts]
        res.append(res[0])
        return res

    distritos_organicos = [
        {
            "id": "DIST-NORTE",
            "tag_oficial": "[ZONA-1-NORTE]",
            "zona_num": "Zona 1",
            "nombre": "Polo Académico Norte, Residencias Los Bloques y Salud",
            "subtitulo": "Docencia Magna, Rectorado, Complejo ITT, Salud y Alojamiento Modular",
            "tags_secundarios": "#AulasMagnas #Senescyt #LosBloques #CentroMedico #Biblioteca247 #ITT #Container",
            "nodes": [
                [0.40835, -78.17060], [0.40805, -78.16945], [0.40680, -78.16930],
                [0.40590, -78.16950], [0.40520, -78.17050], [0.40525, -78.17120],
                [0.40610, -78.17175], [0.40740, -78.17195], [0.40825, -78.17135]
            ],
            "color": "#1e3799",
            "fill": "#3498db",
            "icono": "graduation-cap",
            "centroid": [0.4068383, -78.1706075],
            "area_m2": 77134.1,
            "poblacion": "~650 estudiantes, docentes y personal",
            "edificios_clave": "Edificio Senescyt (Biblioteca 24/7, Krispan, Comedor Sol del Ecuador), Bloques A-I, Centro Médico Tipo A, Complejo ITT (Bloques 1 y 2, Plaza ITT), Container y Parada Senescyt.",
            "estrategia": "Cerca Viva 3 (320 m) con estrato alto rompevientos (*Schinus molle*) y aromáticas medias."
        },
        {
            "id": "DIST-CENTRAL",
            "tag_oficial": "[ZONA-2-CENTRAL]",
            "zona_num": "Zona 2",
            "nombre": "Casco Histórico, Patrimonio Cultural e Ingenio Azucarero",
            "subtitulo": "Patrimonio San José, Aulas B/I, Plaza Mikuna, Sala Capitular y Paleohumedal",
            "tags_secundarios": "#PatrimonioSanJose #IngenioAzucarero #BibliotecaPatrimonial #PlazaMikuna #SalaCapitular #Paleohumedal",
            "nodes": [
                [0.40605, -78.17340], [0.40565, -78.17220], [0.40460, -78.17220],
                [0.40360, -78.17470], [0.40360, -78.17580], [0.40380, -78.17720],
                [0.40445, -78.17740], [0.40520, -78.17680], [0.40570, -78.17520],
                [0.40595, -78.17430]
            ],
            "color": "#d35400",
            "fill": "#f39c12",
            "icono": "landmark",
            "centroid": [0.4047761, -78.1747386],
            "area_m2": 107418.2,
            "poblacion": "~350 estudiantes en tránsito y comensales en horas pico",
            "edificios_clave": "Torre y Chimenea del Ingenio, Biblioteca Central Patrimonial (24/7), Aulas B e I, Patio Gastronómico Plaza Mikuna (Restaurante El Colibrí), Sala Capitular, Sala de Estar, Baños, Molino de Agua, Canales San José y Capitular, Pozo y Paleohumedal.",
            "estrategia": "Cerca Viva 2 (280 m) de barrera rompevientos y reposición fitoquímica alrededor de terrazas de alimentación."
        },
        {
            "id": "DIST-SUR",
            "tag_oficial": "[ZONA-3-SUR]",
            "zona_num": "Zona 3",
            "nombre": "Gran Distrito Residencial, Complejo Deportivo y Concha Acústica",
            "subtitulo": "Residencias Las Multis, Las Pats, Las T's, Canchas, Gimnasio al Aire Libre y Docentes",
            "tags_secundarios": "#LasMultis #LasPats #LasTs #ComplejoDeportivo #ConchaAcustica #VillasDocentes #Gimnasio",
            "nodes": [
                [0.40435, -78.17270], [0.40410, -78.17060], [0.40260, -78.16980],
                [0.40140, -78.17030], [0.39990, -78.17460], [0.39990, -78.17560],
                [0.40110, -78.17660], [0.40240, -78.17680], [0.40375, -78.17630],
                [0.40400, -78.17420]
            ],
            "color": "#27ae60",
            "fill": "#2ecc71",
            "icono": "home",
            "centroid": [0.4022536, -78.1735068],
            "area_m2": 273735.7,
            "poblacion": "~550 residentes activos (estudiantes y profesores) + deportistas",
            "edificios_clave": "Residencias Las Multis (13 bloques de 3 pisos), Residencias Patrimoniales Las Pats, Módulos Las T's (13 bloques sur), Villas de Docentes, 7 canchas deportivas, Gimnasio al Aire Libre, Concha Acústica, Laboratorios de Carrera y Canal Suroeste.",
            "estrategia": "Cerca Viva 1 (380 m) multiestrato hipoalergénica con sustitución de romero por cedrón/huacatay en dormitorios."
        },
        {
            "id": "DIST-ESTE",
            "tag_oficial": "[ZONA-4-ESTE]",
            "zona_num": "Zona 4",
            "nombre": "Eje Hídrico Agroforestal y Periferia Oriental",
            "subtitulo": "Reservorio Léntico, Canales de Conducción, Esclusa Este y Servicios",
            "tags_secundarios": "#ReservorioLéntico #CanalEste #EsclusaEste #SantuarioOdonatos #SachaHome #ComedorPerci",
            "nodes": [
                [0.40585, -78.16840], [0.40490, -78.16740], [0.40390, -78.16770],
                [0.40300, -78.16920], [0.40360, -78.16995], [0.40420, -78.17120],
                [0.40490, -78.16960], [0.40575, -78.16935]
            ],
            "color": "#00a8ff",
            "fill": "#74b9ff",
            "icono": "tint",
            "centroid": [0.4044449, -78.1689849],
            "area_m2": 66417.2,
            "poblacion": "~120 usuarios y comensales diarios",
            "edificios_clave": "Laguna Artificial / Reservorio Agroforestal (~2,006 m²), Canal Este (34 vértices), Esclusa Este y Canal Conector (15 vértices), Comedor doña Perci, Habitaciones Privadas Sacha Home (Sin Convenio) y Barriada.",
            "estrategia": "Santuario de odonatos (libélulas nativas) + inoculación selectiva con Bti en canal lótico."
        }
    ]

    for dist in distritos_organicos:
        dist["ring"] = chaikin_closed(dist["nodes"], 3)
        # Envolvente orgánica suave con estética pastel translúcida
        folium.Polygon(
            locations=dist["ring"],
            color=dist["color"],
            weight=2.5,
            dash_array="5, 5",
            fill=True,
            fill_color=dist["fill"],
            fill_opacity=0.12,
            tooltip=f"🏛️ {dist['tag_oficial']} · {dist['nombre']}",
            popup=folium.Popup(f"""
                <div style="font-family: 'Segoe UI', Arial, sans-serif; width: 300px; line-height: 1.45;">
                    <div style="background: linear-gradient(135deg, {dist['color']}, {dist['fill']}); color: white; padding: 8px 12px; border-radius: 6px 6px 0 0;">
                        <span style="font-size: 10.5px; text-transform: uppercase; letter-spacing: 0.5px; opacity: 0.95;">{dist['tag_oficial']} · {dist['zona_num']} CALIBRADA</span>
                        <div style="font-weight: bold; font-size: 13.5px; margin-top: 2px;">{dist['nombre']}</div>
                    </div>
                    <div style="padding: 10px 12px; border: 1px solid {dist['color']}; border-top: none; border-radius: 0 0 6px 6px; background: #ffffff; font-size: 12px; color: #2c3e50;">
                        <div style="font-size: 11.5px; color: #576574; margin-bottom: 4px; font-style: italic;">{dist['subtitulo']}</div>
                        <div style="margin: 3px 0 6px 0; font-size: 10.5px; color: #0984e3; font-weight: 600;">{dist['tags_secundarios']}</div>
                        <p style="margin: 4px 0;"><b>👥 Población y Aforo:</b> {dist['poblacion']}</p>
                        <p style="margin: 4px 0;"><b>📐 Superficie Delimitada:</b> ~{dist['area_m2']:,} m² (~{dist['area_m2']/10000:.2f} ha)</p>
                        <p style="margin: 4px 0;"><b>🏛️ Infraestructura Clave:</b> {dist['edificios_clave']}</p>
                        <div style="margin-top: 8px; padding: 6px 8px; background: #ecfdf5; border-left: 3px solid #10ac84; border-radius: 4px; color: #065f46; font-size: 11px;">
                            <b>🌿 Enfoque Ecosistémico:</b> {dist['estrategia']}
                        </div>
                    </div>
                </div>
            """, max_width=320)
        ).add_to(fg_distritos)

        # Macro-Badge circular central de identificación de Zona
        folium.CircleMarker(
            location=dist["centroid"],
            radius=9,
            color=dist["color"],
            weight=2.5,
            fill=True,
            fill_color=dist["fill"],
            fill_opacity=0.85,
            tooltip=f"📍 {dist['tag_oficial']} · {dist['nombre']}",
            popup=folium.Popup(f"""
                <div style="font-family: 'Segoe UI', Arial, sans-serif; width: 260px;">
                    <b style="color: {dist['color']}; font-size: 13px;">{dist['tag_oficial']} · {dist['nombre']}</b><br>
                    <span style="font-size: 11px; color: #0984e3; font-weight: 600;">{dist['tags_secundarios']}</span><br>
                    <span style="font-size: 11.5px; color: #2c3e50;">Centroide: {dist['centroid'][0]:.6f}, {dist['centroid'][1]:.6f}</span><br>
                    <span style="font-size: 11px; color: #7f8c8d;">Área delimitada: ~{dist['area_m2']:,} m² (~{dist['area_m2']/10000:.2f} ha)</span>
                </div>
            """, max_width=280)
        ).add_to(fg_distritos)

    # -------------------------------------------------------------
    # 2.2 RED VIAL Y CORREDORES DEL CAMPUS YACHAY TECH (6 EJES GEOREFERENCIADOS)
    # -------------------------------------------------------------
    red_vial_campus = [
        {
            "id": "LINE-VIA-01",
            "nombre": "Vía a Yachay (Eje Troncal Norte-Sur · Ingenio – Las Pats)",
            "tipo": "Vía Troncal Principal",
            "longitud_m": 671.8,
            "color": "#4b6584",
            "weight": 4.5,
            "dash": "10, 5",
            "coords": [
                [0.4084238, -78.1741618], [0.4082660, -78.1741927], [0.4078673, -78.1742708],
                [0.4072715, -78.1741692], [0.4067812, -78.1742957], [0.4066571, -78.1743311],
                [0.4064648, -78.1743985], [0.4061327, -78.1744380], [0.4059525, -78.1744278],
                [0.4057413, -78.1743894], [0.4056429, -78.1743332], [0.4053810, -78.1741835],
                [0.4052319, -78.1740983], [0.4051363, -78.1740437], [0.4050620, -78.1740209],
                [0.4048954, -78.1739697], [0.4048767, -78.1739640], [0.4047470, -78.1739753],
                [0.4046351, -78.1739851], [0.4045346, -78.1739883], [0.4043184, -78.1739953],
                [0.4043009, -78.1739960], [0.4041101, -78.1739874], [0.4040370, -78.1739948],
                [0.4038327, -78.1740062], [0.4037358, -78.1740257], [0.4036051, -78.1740157],
                [0.4035334, -78.1740064], [0.4032900, -78.1739194], [0.4031836, -78.1738850],
                [0.4030601, -78.1738240], [0.4028205, -78.1737057], [0.4026043, -78.1736018]
            ],
            "desc": "Arteria principal norte-sur que bordea el Casco Histórico e Ingenio Azucarero (Chimenea, Torre, Biblioteca 24/7, Aulas B y Plaza Mikuna) hasta el Arco de Las Pats (BUS-03). Alberga los parqueos en vía P-08, P-09, P-10 y P-11."
        },
        {
            "id": "LINE-VIA-02",
            "nombre": "Vía a Yachay / Proyecto Yachay (Eje Transversal San José – Sala Capitular – Las Pats)",
            "tipo": "Vía Colectora Patrimonial",
            "longitud_m": 466.6,
            "color": "#4b6584",
            "weight": 4.5,
            "dash": "10, 5",
            "coords": [
                [0.4045471, -78.1770499], [0.4045341, -78.1770157], [0.4043661, -78.1764704],
                [0.4040172, -78.1753376], [0.4039373, -78.1751792], [0.4036132, -78.1747903],
                [0.4031498, -78.1746821], [0.4029399, -78.1744892], [0.4026958, -78.1740567],
                [0.4026350, -78.1738397], [0.4026043, -78.1736018]
            ],
            "desc": "Conecta el extremo oeste de San José (Edificio 41, Comedores Analí y Pato Goloso, Parqueaderos P-01, P-02, P-06), pasa frente a la Sala Capitular y su Parada de Buses (BUS-02) y empalma en el Arco de Las Pats."
        },
        {
            "id": "LINE-VIA-03",
            "nombre": "Vía Hacienda San José y Acceso Las Multis / Concha Acústica",
            "tipo": "Vía Asfaltada y Acceso Residencial Sur",
            "longitud_m": 663.4,
            "color": "#596275",
            "weight": 4.0,
            "dash": "8, 4",
            "coords": [
                [0.4039373, -78.1751792], [0.4032949, -78.1753398], [0.4031886, -78.1753670],
                [0.4028186, -78.1754532], [0.4023183, -78.1756609], [0.4010013, -78.1769687],
                [0.4008154, -78.1764895], [0.4008802, -78.1762625], [0.4011971, -78.1753544],
                [0.4013180, -78.1752380], [0.4014418, -78.1752129], [0.4017145, -78.1752174],
                [0.4018678, -78.1752188]
            ],
            "desc": "Desciende desde la intersección de Sala Capitular bordeando las Villas de Docentes y Las Multis hasta la Concha Acústica, e ingresa por el ramal sur paralelo al Canal Suroeste hacia el Parqueadero P-03 y la Plaza de las Multis."
        },
        {
            "id": "LINE-VIA-04",
            "nombre": "Circuito Vial del Polo Académico Norte (Anillo Senescyt y Los Bloques)",
            "tipo": "Anillo Vial Adoquinado y Perimetral Norte",
            "longitud_m": 897.0,
            "color": "#3867d6",
            "weight": 4.2,
            "dash": "8, 4",
            "coords": [
                [0.4056851, -78.1712618], [0.4064579, -78.1714921], [0.4072668, -78.1716068],
                [0.4080157, -78.1716587], [0.4082536, -78.1711806], [0.4074898, -78.1702973],
                [0.4072556, -78.1700264], [0.4067406, -78.1693880], [0.4059124, -78.1700414],
                [0.4064241, -78.1706111], [0.4072556, -78.1700264]
            ],
            "desc": "Circuito vial que envuelve los Bloques A-I, el Centro Médico, el Container y el Edificio Senescyt. Articula la Parada de Buses Senescyt (BUS-01), los parqueos en vía P-12 a P-15 y los estacionamientos P-16, P-17 (Sur) y P-18, P-19 (Este)."
        },
        {
            "id": "LINE-VIA-05",
            "nombre": "Corredor Diagonal Inter-Zonal (Las Pats – Canchas – Invernaderos – ITT – Senescyt)",
            "tipo": "Corredor Interno de Articulación Universitaria",
            "longitud_m": 660.7,
            "color": "#576574",
            "weight": 3.8,
            "dash": "6, 6",
            "coords": [
                [0.4026043, -78.1736018], [0.4025974, -78.1735614], [0.4027072, -78.1734875],
                [0.4036114, -78.1737604], [0.4041898, -78.1724761], [0.4043629, -78.1725395],
                [0.4051128, -78.1726439], [0.4053502, -78.1719272], [0.4056851, -78.1712618],
                [0.4058770, -78.1710562], [0.4060647, -78.1709009], [0.4061614, -78.1708229],
                [0.4064241, -78.1706111]
            ],
            "desc": "Eje interno diagonal que enlaza el Arco de Las Pats, el Complejo Deportivo (P-04), los Laboratorios de Carrera, los Invernaderos Experimentales, el Complejo ITT y el acceso sur del Edificio Senescyt."
        },
        {
            "id": "LINE-VIA-06",
            "nombre": "Vía a Hoja Blanca y Conector Reservorio Este – Senescyt",
            "tipo": "Vía Periférica Sur-Este y Eje Agroforestal",
            "longitud_m": 855.0,
            "color": "#778ca3",
            "weight": 3.8,
            "dash": "6, 6",
            "coords": [
                [0.4025974, -78.1735614], [0.4026156, -78.1734607], [0.4026695, -78.1732853],
                [0.4027138, -78.1731525], [0.4027684, -78.1729520], [0.4028752, -78.1725062],
                [0.4030545, -78.1720939], [0.4031387, -78.1717623], [0.4031076, -78.1712216],
                [0.4030312, -78.1708227], [0.4030078, -78.1704475], [0.4031045, -78.1700939],
                [0.4038071, -78.1693926], [0.4039682, -78.1690738], [0.4040779, -78.1689639],
                [0.4047174, -78.1685938], [0.4059124, -78.1700414]
            ],
            "desc": "Borde sur del Complejo Deportivo y Gimnasio al Aire Libre hacia Barriada, ascendiendo por la Esclusa Hidráulica Este (I-23), la Laguna/Reservorio Agroforestal, Comedor doña Perci y Sacha Home hasta conectar con Senescyt Sur."
        },
        {
            "id": "LINE-VIA-07",
            "nombre": "Anillo Occidental de Servicio y Avenida Diagonal Los Bloques – ITT",
            "tipo": "Vía Interna de Servicio y Diagonal Peatonal-Vehicular",
            "longitud_m": 442.8,
            "color": "#3867d6",
            "weight": 3.6,
            "dash": "6, 4",
            "coords": [
                [0.4080157, -78.1716587], [0.4080119, -78.1725745], [0.4071614, -78.1725099],
                [0.4072668, -78.1716068], [0.4064241, -78.1706111]
            ],
            "desc": "Anillo perimetral occidental de servicio que rodea los Bloques F y D (OSM Ways 360908702 y 360908705) y continúa por la avenida diagonal que separa las Residencias Los Bloques (A–E) del Complejo ITT (OSM Way 863664231)."
        },
        {
            "id": "LINE-VIA-08",
            "nombre": "Caminerías Peatonales Internas de Residencias Los Bloques (A–I) y Centro Médico",
            "tipo": "Red Peatonal Adoquinada Residencial",
            "longitud_m": 165.6,
            "color": "#20bf6b",
            "weight": 3.2,
            "dash": "4, 4",
            "coords": [
                [0.4077550, -78.1715900], [0.4075100, -78.1712800], [0.4071800, -78.1709300],
                [0.4068800, -78.1705900], [0.4072400, -78.1703100], [0.4075800, -78.1706400],
                [0.4078200, -78.1709800]
            ],
            "desc": "Senderos peatonales adoquinados que atraviesan los jardines y patios interiores con palmeras entre los Bloques F/G, D/E, A/B/C, H/I y el Centro Médico Tipo A."
        },
        {
            "id": "LINE-VIA-09",
            "nombre": "Sendero Peatonal y Ciclovía Sinuosa (Los Bloques – Paleohumedal – Ingenio Azucarero)",
            "tipo": "Sendero Ecológico Peatonal / Caminería Blanca",
            "longitud_m": 268.4,
            "color": "#d35400",
            "weight": 3.8,
            "dash": "5, 5",
            "coords": [
                [0.4071614, -78.1725099], [0.4069200, -78.1728200], [0.4064800, -78.1731800],
                [0.4061500, -78.1737500], [0.4059200, -78.1741500], [0.4056429, -78.1743332]
            ],
            "desc": "Camino peatonal sinuoso de lastre blanco que conecta directamente el extremo suroeste de Residencias Los Bloques con el sector norte del Ingenio Azucarero y Vía a Yachay, bordeando la pradera ecológica del Paleohumedal (I-22)."
        },
        {
            "id": "LINE-VIA-10",
            "nombre": "Vía de Acceso Sur a Invernaderos Experimentales, Lab. Idiomas y Plaza Mikuna",
            "tipo": "Vía Interna de Servicio Agrícola y Docencia",
            "longitud_m": 172.9,
            "color": "#576574",
            "weight": 3.5,
            "dash": "6, 4",
            "coords": [
                [0.4040370, -78.1739948], [0.4039500, -78.1734200], [0.4040800, -78.1729200],
                [0.4041898, -78.1724761]
            ],
            "desc": "Vía transversal que parte desde Vía a Yachay (al sur de Plaza Mikuna y Laboratorio de Idiomas), recorre el frente sur de los 4 Invernaderos Experimentales y empalma con la explanada de Laboratorios de Carrera (P-05)."
        },
        {
            "id": "LINE-VIA-11",
            "nombre": "Caminerías Cruciformes de Plaza del Estudiante, Biblioteca Patrimonial y Aulas B",
            "tipo": "Caminería Peatonal Patrimonial (4 Cuadrantes)",
            "longitud_m": 174.2,
            "color": "#c0392b",
            "weight": 3.2,
            "dash": "4, 4",
            "coords": [
                [0.4048342, -78.1740918], [0.4045200, -78.1742800], [0.4043184, -78.1739953],
                [0.4045200, -78.1742800], [0.4044119, -78.1743079], [0.4046800, -78.1744800],
                [0.4049740, -78.1745032]
            ],
            "desc": "Andadores peatonales dispuestos en cruz y diagonal que dividen los 4 jardines cuadrangulares al sur de la Biblioteca Patrimonial (24/7), articulando el flujo estudiantil entre Aulas B Sur, el Laboratorio de Química (I-10) y Plaza Mikuna."
        },
        {
            "id": "LINE-VIA-12",
            "nombre": "Vía Periférica Oriental (Senescyt Este – Parcelas Experimentales – Reservorio Este)",
            "tipo": "Camino Afirmado Agroforestal Oriental",
            "longitud_m": 336.6,
            "color": "#778ca3",
            "weight": 3.4,
            "dash": "6, 6",
            "coords": [
                [0.4067406, -78.1693880], [0.4059500, -78.1684500], [0.4055810, -78.1691651],
                [0.4047174, -78.1685938]
            ],
            "desc": "Camino oriental que desciende desde la esquina este de Senescyt (OSM Way 980670152), pasa junto a la Edificación Abandonada Sin Techo (POLY-ABANDON-TECHO) y las parcelas experimentales hasta la bifurcación del Reservorio Este y Sacha Home."
        },
        {
            "id": "LINE-VIA-13",
            "nombre": "Red de Caminerías Adoquinadas del Complejo Deportivo Sur y Las Pats",
            "tipo": "Caminería Peatonal Deportiva y Residencial",
            "longitud_m": 205.0,
            "color": "#20bf6b",
            "weight": 3.2,
            "dash": "4, 4",
            "coords": [
                [0.4026043, -78.1736018], [0.4022500, -78.1732500], [0.4020500, -78.1728200],
                [0.4022800, -78.1726800], [0.4023200, -78.1723500], [0.4023800, -78.1719500]
            ],
            "desc": "Caminerías adoquinadas en trazado geométrico que enlazan las Residencias Patrimoniales Las Pats con las Canchas de Volley Playa, Básquetbol 1–3, Fútbol Sintético 1–3 y el Gimnasio al Aire Libre."
        },
        {
            "id": "LINE-VIA-14",
            "nombre": "Caminerías Curvas Internas de Las Multis y Acceso Peatonal Concha Acústica",
            "tipo": "Circuito Peatonal Orgánico Multifamiliar",
            "longitud_m": 281.7,
            "color": "#16a085",
            "weight": 3.3,
            "dash": "4, 4",
            "coords": [
                [0.4026518, -78.1749874], [0.4023800, -78.1751200], [0.4021200, -78.1753200],
                [0.4018500, -78.1755800], [0.4015800, -78.1758200], [0.4013200, -78.1761800],
                [0.4010013, -78.1769687]
            ],
            "desc": "Senderos peatonales curvos que recorren las terrazas ajardinadas entre los 13 bloques de Las Multis (RECT-MULTI-01 a 13) y desembocan en la explanada de la Concha Acústica (I-09)."
        },
        {
            "id": "LINE-VIA-15",
            "nombre": "Alameda Peatonal Central de Residencias Patrimoniales Las T's (Bloques 1–13)",
            "tipo": "Sendero Peatonal Residencial Sur",
            "longitud_m": 164.6,
            "color": "#27ae60",
            "weight": 3.2,
            "dash": "4, 4",
            "coords": [
                [0.4004800, -78.1744800], [0.4006200, -78.1748200], [0.4007400, -78.1751500],
                [0.4008100, -78.1755200], [0.4008500, -78.1758700]
            ],
            "desc": "Eje peatonal interno este-oeste que articula los módulos residenciales patrimoniales tipo T (RECT-T-01 a RECT-T-13), protegido en su flanco norte por la Cerca Viva 1 hipoalergénica."
        },
        {
            "id": "LINE-VIA-16",
            "nombre": "Caminería Patrimonial de Sala Capitular, Caballerizas, Villas Docentes y San José",
            "tipo": "Corredor Peatonal Histórico y Docente",
            "longitud_m": 216.1,
            "color": "#8e44ad",
            "weight": 3.3,
            "dash": "4, 4",
            "coords": [
                [0.4043897, -78.1754970], [0.4044200, -78.1758200], [0.4042500, -78.1762500],
                [0.4042100, -78.1766200], [0.4038800, -78.1758200], [0.4035500, -78.1756200]
            ],
            "desc": "Recorrido peatonal que enlaza el Claustro de la Sala Capitular y sus 3 piletas ornamentales con Aulas Caballerizas, la Sala de Estar / Comedores de San José y el sendero interior de las Villas de Docentes (RECT-DOCENTES-01 a 08)."
        }
    ]

    for via in red_vial_campus:
        folium.PolyLine(
            locations=via["coords"],
            color=via["color"],
            weight=via["weight"],
            opacity=0.82,
            dash_array=via["dash"],
            tooltip=f"🛣️ {via['nombre']} (~{via['longitud_m']} m)",
            popup=folium.Popup(f"""
                <div style="font-family: 'Segoe UI', Arial, sans-serif; width: 265px; line-height: 1.4;">
                    <div style="color: #2c3e50; font-weight: bold; font-size: 13.5px; margin-bottom: 3px;">🛣️ {via['nombre']}</div>
                    <span style="background: #eef2f7; color: #4b6584; padding: 2px 7px; border-radius: 4px; font-size: 10.5px; font-weight: 700;">{via['id']} · {via['tipo']}</span>
                    <p style="margin: 8px 0 6px 0; font-size: 11.5px; color: #34495e;">{via['desc']}</p>
                    <div style="font-size: 10.5px; color: #7f8c8d; border-top: 1px solid #ecf0f1; padding-top: 4px;">
                        Longitud trazada: <b>{via['longitud_m']} m</b> | Vértices: <b>{len(via['coords'])} pts</b>
                    </div>
                </div>
            """, max_width=285)
        ).add_to(fg_vias)

    # -------------------------------------------------------------
    # 2.3 ÁREAS VERDES, JARDINES PATRIMONIALES Y PARQUES DEL CAMPUS (12 POLÍGONOS)
    # -------------------------------------------------------------
    areas_verdes_campus = [
        {
            "id": "POLY-VERDE-01",
            "nombre": "Jardín Central y Patios Verdes de Residencias Los Bloques (A–I)",
            "tipo": "Jardín Residencial Universitario y Palmeras",
            "zona": "Zona 1 · Polo Norte",
            "area": 1964.1,
            "centroid": [0.4074, -78.1707517],
            "color": "#27ae60",
            "fill": "#2ecc71",
            "coords": [
                [0.4077100, -78.1712500], [0.4077400, -78.1708800], [0.4074900, -78.1705600],
                [0.4071800, -78.1703900], [0.4069800, -78.1705800], [0.4074800, -78.1711200]
            ],
            "desc": "Patios ajardinados interiores con césped y palmeras ornamentales entre los Bloques A–I y el Centro Médico Tipo A. Protegidos por la Cerca Viva 3 con formulación hipoalergénica libre de romero junto a dormitorios."
        },
        {
            "id": "POLY-VERDE-02",
            "nombre": "Parterres y Jardines Orientales del Edificio Senescyt",
            "tipo": "Jardineras Académicas y Estancia Exterior",
            "zona": "Zona 1 · Polo Norte",
            "area": 1822.2,
            "centroid": [0.406485, -78.1697867],
            "color": "#27ae60",
            "fill": "#58d68d",
            "coords": [
                [0.4069100, -78.1696900], [0.4067300, -78.1694400], [0.4060200, -78.1699900],
                [0.4061400, -78.1701400], [0.4064100, -78.1699400], [0.4067900, -78.1697600]
            ],
            "desc": "Parterres arbolados en la explanada sureste del Edificio Senescyt, contiguos a la Biblioteca 24/7 y al eje de estacionamientos P-16 a P-19."
        },
        {
            "id": "POLY-VERDE-03",
            "nombre": "Corredor Ecológico y Pradera del Paleohumedal (Los Bloques – Ingenio)",
            "tipo": "Pradera de Amortiguamiento y Humedal Estacional",
            "zona": "Inter-Zonal 1–2",
            "area": 35217.9,
            "centroid": [0.4062833, -78.1729683],
            "color": "#1e8449",
            "fill": "#52be80",
            "coords": [
                [0.4071200, -78.1725200], [0.4068800, -78.1717200], [0.4057500, -78.1719500],
                [0.4054800, -78.1735500], [0.4058200, -78.1742200], [0.4066500, -78.1738500]
            ],
            "desc": "Extensa pradera verde que alberga la depresión natural del Paleohumedal (I-22) y es surcada por el sendero peatonal blanco (LINE-VIA-09) que une Los Bloques con el Ingenio Azucarero."
        },
        {
            "id": "POLY-VERDE-04",
            "nombre": "Jardín Patrimonial de la Plaza del Ingenio y Chimenea Histórica",
            "tipo": "Jardín Histórico Patrimonial con Palmeras",
            "zona": "Zona 2 · Casco Histórico",
            "area": 445.5,
            "centroid": [0.40532, -78.1744575],
            "color": "#196f3d",
            "fill": "#2ecc71",
            "coords": [
                [0.4052200, -78.1744800], [0.4052600, -78.1743400], [0.4050100, -78.1742600],
                [0.4049800, -78.1744400]
            ],
            "desc": "Jardín central rectangular con palmeras centenarias en el corazón de la Plaza del Ingenio Azucarero, flanqueado por Aulas I, Biblioteca Patrimonial y el Restaurante Plaza Ingenio."
        },
        {
            "id": "POLY-VERDE-05",
            "nombre": "Parque y Arboleda Patrimonial Oeste del Ingenio (Trapiches y Molino)",
            "tipo": "Arboleda Patrimonial y Explanada de Maquinaria",
            "zona": "Zona 2 · Casco Histórico",
            "area": 1643.8,
            "centroid": [0.405138, -78.174918],
            "color": "#196f3d",
            "fill": "#27ae60",
            "coords": [
                [0.4052900, -78.1750800], [0.4053400, -78.1747900], [0.4050600, -78.1746600],
                [0.4049100, -78.1749200], [0.4050900, -78.1751400]
            ],
            "desc": "Parque arbolado de diseño ovalado al occidente de Aulas I y al sur del Molino de Agua Patrimonial (W-08), donde se exhiben piezas industriales históricas del antiguo ingenio."
        },
        {
            "id": "POLY-VERDE-06",
            "nombre": "Jardines Cuadrangulares de Plaza del Estudiante y Aulas B (4 Cuadrantes)",
            "tipo": "Explanada Verde Universitaria en Cruz",
            "zona": "Zona 2 · Casco Histórico",
            "area": 1833.4,
            "centroid": [0.404568, -78.174248],
            "color": "#27ae60",
            "fill": "#2ecc71",
            "coords": [
                [0.4047300, -78.1744100], [0.4047900, -78.1740300], [0.4043400, -78.1740100],
                [0.4044200, -78.1743100], [0.4045600, -78.1744800]
            ],
            "desc": "Jardín emblemático dividido en 4 cuadrantes de césped por las caminerías en cruz (LINE-VIA-11), situado entre la Biblioteca Patrimonial, el Laboratorio de Química (I-10), Aulas B Sur y Vía a Yachay."
        },
        {
            "id": "POLY-VERDE-07",
            "nombre": "Parque Central Yachay y Pradera Agroecológica de Invernaderos / Plaza Mikuna",
            "tipo": "Parque Universitario y Área Verde Experimental",
            "zona": "Zonas 2–3 · Eje Central",
            "area": 6608.5,
            "centroid": [0.404642, -78.173284],
            "color": "#229954",
            "fill": "#58d68d",
            "coords": [
                [0.4049800, -78.1736200], [0.4050600, -78.1727200], [0.4044800, -78.1728800],
                [0.4041200, -78.1734800], [0.4041500, -78.1737400]
            ],
            "desc": "Área verde que integra el Parque Yachay (OSM Way 550738479) y los jardines contiguos a Plaza Mikuna, Laboratorio de Idiomas (I-07) y los 4 Invernaderos Experimentales (INV-01), donde se propagan las 1,960 plántulas repelentes."
        },
        {
            "id": "POLY-VERDE-08",
            "nombre": "Parcelas Agroecológicas Experimentales y Cinturón Ripario del Reservorio Este",
            "tipo": "Agroforestería Experimental y Refugio de Odonatos",
            "zona": "Zona 4 · Eje Hídrico Este",
            "area": 2565.1,
            "centroid": [0.404605, -78.1688575],
            "color": "#1e8449",
            "fill": "#45b39d",
            "coords": [
                [0.4048800, -78.1689500], [0.4046800, -78.1679500], [0.4038400, -78.1679800],
                [0.4038600, -78.1687800], [0.4044200, -78.1691200]
            ],
            "desc": "Comprende las parcelas agrícolas de trazado geométrico experimental al noroeste del reservorio y el anillo de vegetación riparia que rodea la Laguna Artificial (~2,006.2 m²), hábitat reproductivo de libélulas (Odonata)."
        },
        {
            "id": "POLY-VERDE-09",
            "nombre": "Parque y Arboleda del Complejo Deportivo Sur (Canchas y Gimnasio)",
            "tipo": "Parque Deportivo y Recreación al Aire Libre",
            "zona": "Zona 3 · Distrito Sur",
            "area": 2435.6,
            "centroid": [0.402, -78.172816],
            "color": "#27ae60",
            "fill": "#52be80",
            "coords": [
                [0.4026800, -78.1729800], [0.4027500, -78.1720200], [0.4017800, -78.1717500],
                [0.4016200, -78.1726400], [0.4022200, -78.1730500]
            ],
            "desc": "Pradera arbolada y taludes verdes que envuelven las 7 canchas deportivas (Fútbol Sintético 1–3, Básquetbol 1–3 y Volley Playa) y el Gimnasio al Aire Libre, resguardados por el extremo oriental de la Cerca Viva 1."
        },
        {
            "id": "POLY-VERDE-10",
            "nombre": "Jardines Comunitarios Internos de Residencias Patrimoniales Las Pats",
            "tipo": "Patio Verde Residencial Patrimonial",
            "zona": "Zona 3 · Distrito Sur",
            "area": 3679.7,
            "centroid": [0.401832, -78.17385],
            "color": "#229954",
            "fill": "#58d68d",
            "coords": [
                [0.4023200, -78.1740800], [0.4021200, -78.1735800], [0.4015500, -78.1732200],
                [0.4014500, -78.1737800], [0.4017800, -78.1742800]
            ],
            "desc": "Gran jardín central comunitario delimitado por la herradura arquitectónica de los pabellones Las Pats 1 a 9 (RECT-PATS-01 a 09), con árboles de sombra y senderos peatonales seguros."
        },
        {
            "id": "POLY-VERDE-11",
            "nombre": "Parque Escalonado de Las Multis, Alameda de Las T's y Pradera Concha Acústica",
            "tipo": "Parque Residencial y Explanada Cultural",
            "zona": "Zona 3 · Distrito Sur",
            "area": 872.4,
            "centroid": [0.400995, -78.17655],
            "color": "#16a085",
            "fill": "#48c9b0",
            "coords": [
                [0.4025800, -78.1748800], [0.4022500, -78.1753800], [0.4011800, -78.1766500],
                [0.4008600, -78.1759500], [0.4005500, -78.1748500], [0.4014800, -78.1748200]
            ],
            "desc": "Parques escalonados entre los 13 bloques de Las Multis, la pradera de eventos de la Concha Acústica (I-09) y la alameda ajardinada de las Casas Patrimoniales Las T's (RECT-T-01 a 13), junto al Canal Suroeste."
        },
        {
            "id": "POLY-VERDE-12",
            "nombre": "Jardines Claustrales de Sala Capitular, Caballerizas y Barrio Docente",
            "tipo": "Jardín Histórico, Botánico y Residencial Docente",
            "zona": "Zonas 2–3 · Sector San José",
            "area": 592.9,
            "centroid": [0.4040675, -78.175575],
            "color": "#1e8449",
            "fill": "#52be80",
            "coords": [
                [0.4046200, -78.1751500], [0.4044800, -78.1761200], [0.4034800, -78.1760200],
                [0.4032800, -78.1754800], [0.4040500, -78.1752200]
            ],
            "desc": "Jardines patrimoniales que rodean las 3 piletas ornamentales de la Sala Capitular (W-05 a W-07), el Canal de Jardines (W-03) y el corredor arbolado de las 8 Villas de Docentes (RECT-DOCENTES-01 a 08)."
        }
    ]

    for av in areas_verdes_campus:
        folium.Polygon(
            locations=av["coords"],
            color=av["color"],
            weight=2.0,
            dash_array="4, 4",
            fill=True,
            fill_color=av["fill"],
            fill_opacity=0.22,
            tooltip=f"🌳 {av['nombre']} (~{av['area']:,} m²)",
            popup=folium.Popup(f"""
                <div style="font-family: 'Segoe UI', Arial, sans-serif; width: 265px; line-height: 1.4;">
                    <div style="color: {av['color']}; font-weight: bold; font-size: 13.5px; margin-bottom: 3px;">🌳 {av['nombre']}</div>
                    <span style="background: #e8f8f5; color: #0e6251; padding: 2px 7px; border-radius: 4px; font-size: 10.5px; font-weight: 700;">{av['id']} · {av['tipo']}</span>
                    <p style="margin: 8px 0 6px 0; font-size: 11.5px; color: #34495e;">{av['desc']}</p>
                    <div style="font-size: 10.5px; color: #7f8c8d; border-top: 1px solid #ecf0f1; padding-top: 4px;">
                        Superficie verde: <b>{av['area']:,} m² (~{av['area']/10000:.2f} ha)</b> | {av['zona']}
                    </div>
                </div>
            """, max_width=285)
        ).add_to(fg_areas_verdes)

    # -------------------------------------------------------------
    # COORDENADAS TOPOGRÁFICAS DE LOS CANALES LÓTICOS (FOCOS LARVARIOS)
    # -------------------------------------------------------------
    canal_suroeste = [
        [0.4009199, -78.1764438],
        [0.4012991, -78.1753884]
    ]
    canal_este_topografico_34pts = [
        [0.4031240, -78.1710613],
        [0.4031186, -78.1708376],
        [0.4031018, -78.1707763],
        [0.4030834, -78.1707354],
        [0.4030630, -78.1706915],
        [0.4030583, -78.1706194],
        [0.4030512, -78.1705781],
        [0.4030764, -78.1705517],
        [0.4030700, -78.1705198],
        [0.4030418, -78.1704859],
        [0.4030428, -78.1704541],
        [0.4030526, -78.1704125],
        [0.4030626, -78.1703478],
        [0.4030945, -78.1702814],
        [0.4031364, -78.1702016],
        [0.4031434, -78.1701560],
        [0.4031649, -78.1701269],
        [0.4031914, -78.1700806],
        [0.4032437, -78.1700253],
        [0.4032775, -78.1699897],
        [0.4033355, -78.1699559],
        [0.4033992, -78.1699193],
        [0.4034358, -78.1698828],
        [0.4034780, -78.1698503],
        [0.4035283, -78.1698037],
        [0.4035648, -78.1697641],
        [0.4036433, -78.1696551],
        [0.4037057, -78.1695582],
        [0.4037570, -78.1694912],
        [0.4038066, -78.1694345],
        [0.4039819, -78.1692012],
        [0.4040671, -78.1690939],
        [0.4040768, -78.1690268],
        [0.4041009, -78.1689487]
    ]

    # -------------------------------------------------------------
    # 3. MAPA DE CALOR: DENSIDAD EPIDEMIOLÓGICA DE PICADURAS Y RIESGO
    # -------------------------------------------------------------
    # Se sustituyen los polígonos geométricos con bordes rectos artificiales por un
    # modelado continuo orgánico (HeatMap) calibrado con los focos lóticos y
    # la atracción hematófaga por densidad humana (CO2, gradientes térmicos y microbiota cutánea).
    rng = random.Random(42)
    heat_data = []

    # 1. Puntos a lo largo del Canal Suroeste (Concha Acústica / Multifamiliares)
    for s in range(12):
        alpha = s / 11
        lat = canal_suroeste[0][0] + alpha * (canal_suroeste[1][0] - canal_suroeste[0][0])
        lon = canal_suroeste[0][1] + alpha * (canal_suroeste[1][1] - canal_suroeste[0][1])
        heat_data.append([lat, lon, 0.95])
        heat_data.append([lat + rng.gauss(0, 0.00012), lon + rng.gauss(0, 0.00012), 0.80])

    # 4. Puntos a lo largo del Canal Este Topográfico (34 Vértices)
    for pt in canal_este_topografico_34pts:
        heat_data.append([pt[0], pt[1], 0.92])
        heat_data.append([pt[0] + rng.gauss(0, 0.00010), pt[1] + rng.gauss(0, 0.00010), 0.75])

    # Puntos a lo largo del Canal Jardines Sala Capitular (Foco de picaduras en Parada de Bus)
    canal_capitular_heat = [
        [0.4046421, -78.1751245],
        [0.4048221, -78.1751372],
        [0.4050082, -78.1751801]
    ]
    for pt in canal_capitular_heat:
        heat_data.append([pt[0], pt[1], 0.95])
        heat_data.append([pt[0] + rng.gauss(0, 0.00008), pt[1] + rng.gauss(0, 0.00008), 0.85])

    # Puntos a lo largo del Canal San José (Contiguo a Edificio 20 y Sala de Estar)
    canal_sanjose_heat = [
        [0.4045979, -78.1764123],
        [0.4045743, -78.1764386],
        [0.4045700, -78.1764951],
        [0.4045492, -78.1765761]
    ]
    for pt in canal_sanjose_heat:
        heat_data.append([pt[0], pt[1], 0.90])
        heat_data.append([pt[0] + rng.gauss(0, 0.00008), pt[1] + rng.gauss(0, 0.00008), 0.80])

    # Puntos a lo largo del Canal Conector hacia Esclusa Este (15 vértices)
    canal_esclusa_heat = [
        [0.4046761, -78.1680199], [0.4045333, -78.1681836], [0.4043868, -78.1682822],
        [0.4041962, -78.1686307], [0.4041061, -78.1687743], [0.4040429, -78.1689091],
        [0.4040262, -78.1689233], [0.4040011, -78.1689108], [0.4039983, -78.1689206],
        [0.4040178, -78.1689304], [0.4040123, -78.1689487], [0.4039886, -78.1689348],
        [0.4039831, -78.1689614], [0.4039943, -78.1689726], [0.4039970, -78.1689739]
    ]
    for pt in canal_esclusa_heat:
        heat_data.append([pt[0], pt[1], 0.88])
        heat_data.append([pt[0] + rng.gauss(0, 0.00008), pt[1] + rng.gauss(0, 0.00008), 0.72])

    # Sospecha Hídrica / Antiguo Lago (Foco de humedad y refugio vegetal adulto)
    heat_data.append([0.4058428, -78.1733964, 0.90])
    heat_data.append([0.4058428 + rng.gauss(0, 0.00008), -78.1733964 + rng.gauss(0, 0.00008), 0.75])

    # 5. Epicentros de atracción humana (CO2 y emisión térmica)
    # Sector Sur: Las Multis, Las T's, Las Pats, Concha Acústica (~550 hab.)
    for _ in range(120):
        lat = rng.gauss(0.4022, 0.00075)
        lon = rng.gauss(-78.1745, 0.00095)
        w = rng.uniform(0.75, 1.0)
        heat_data.append([lat, lon, w])

    # Sector Central: Casco Histórico Ingenio Azucarero, Aulas B/I, Biblioteca (~250 hab.)
    for _ in range(90):
        lat = rng.gauss(0.4048, 0.00060)
        lon = rng.gauss(-78.1738, 0.00075)
        w = rng.uniform(0.70, 0.95)
        heat_data.append([lat, lon, w])

    # Sector Norte: Edificio Senescyt, Krispan, Residencias Los Bloques (~450 hab.)
    for _ in range(105):
        lat = rng.gauss(0.4068, 0.00060)
        lon = rng.gauss(-78.1708, 0.00070)
        w = rng.uniform(0.78, 1.0)
        heat_data.append([lat, lon, w])

    # Sector Este: Reservorio Agroforestal y Periferia (~120 hab.)
    for _ in range(45):
        lat = rng.gauss(0.4041, 0.00045)
        lon = rng.gauss(-78.1685, 0.00055)
        w = rng.uniform(0.60, 0.85)
        heat_data.append([lat, lon, w])

    # Capa HeatMap con gradiente térmico continuo de alta visibilidad
    gradient_calor = {
        0.15: '#2ecc71',  # Verde esmeralda: Baja presión / dispersión periférica
        0.35: '#f1c40f',  # Amarillo ámbar: Presión de picaduras moderada
        0.60: '#e67e22',  # Naranja: Alta molestia en caminerías y aulas
        0.85: '#e74c3c',  # Rojo carmesí: Foco lótico crítico y dormitorios contiguos
        1.00: '#8e44ad'   # Púrpura profundo: Máxima densidad larvaria y telmófaga
    }
    plugins.HeatMap(
        heat_data,
        name="🔥 Mapa de Calor Epidemiológico (Simulium spp.)",
        min_opacity=0.35,
        max_zoom=18,
        radius=28,
        blur=20,
        gradient=gradient_calor
    ).add_to(fg_zonas)

    # Marcadores de Epicentros Epidemiológicos (Badges Interactivos con Diagnóstico Completo)
    epicentros_diagnostico = [
        {
            "nombre": "Epicentro Sur: Hogar Estudiantil y Docente",
            "sector": "Las Multis, Las T's y Las Pats",
            "coords": [0.4022, -78.1745],
            "poblacion": "~550 estudiantes, investigadores y docentes residentes",
            "foco": "Canal Suroeste (~124.5 m) y acequia sur de desagüe",
            "impacto": "Ataque diurno en horas de descanso y recreación en la Concha Acústica; interrupción del sueño, pápulas eritematosas y prurito prolongado.",
            "solucion": "Cerca Viva 1 (380 m) con protocolo 100% libre de romero en dormitorios (sustituido por cedrón y huacatay) + aromaterapia basal.",
            "color": "#e74c3c"
        },
        {
            "nombre": "Epicentro Central: Corazón Académico y Patrimonial",
            "sector": "Ingenio Azucarero, Aulas B/I y Biblioteca Patrimonial",
            "coords": [0.4048, -78.1738],
            "poblacion": "~250 estudiantes, docentes y comensales en horas pico",
            "foco": "Arboledas históricas sombreadas, jardines patrimoniales y microclima húmedo de Plaza Mikuna / El Colibrí",
            "impacto": "La alta demanda del Restaurante El Colibrí (almuerzo económico de USD 2.50 frente a USD 3.50 de Senescyt) satura las mesas abiertas de Plaza Mikuna al mediodía, generando un foco concentrado de atracción térmica y picaduras.",
            "solucion": "Cerca Viva 2 (280 m) como cortina rompevientos con molle y lavanda melífera protegiendo las mesas de comida.",
            "color": "#e67e22"
        },
        {
            "nombre": "Epicentro Norte: Aulas Magnas y Residencias",
            "sector": "Edificio Senescyt y Residencias Los Bloques A-I",
            "coords": [0.4068, -78.1708],
            "poblacion": "~450 estudiantes y personal administrativo",
            "foco": "Acequias de coronación y drenajes pluviales del talud norte",
            "impacto": "Imposibilidad de ventilación natural en clases durante horas de la tarde; estrés en exámenes y consultas frecuentes al Centro Médico por dermatitis.",
            "solucion": "Cerca Viva 3 (320 m) con estrato alto rompevientos y reducción proyectada del 82.8% de penetración.",
            "color": "#c0392b"
        },
        {
            "nombre": "Epicentro Este: Recursos Hídricos y Conducción",
            "sector": "Reservorio Agroforestal, Comedor doña Perci y Habitaciones Privadas Sacha Home (Sin Convenio)",
            "coords": [0.4041, -78.1685],
            "poblacion": "~30 a 50 usuarios diarios (baja afluencia en Comedor doña Perci)",
            "foco": "Canal Sinuoso Este (34 vértices) y Laguna Artificial (~2,006 m²)",
            "impacto": "Flujo peatonal reducido hacia Comedor doña Perci por su ubicación periférica; zona ideal de baja perturbación para consolidación de depredadores acuáticos.",
            "solucion": "Santuario de odonatos (libélulas nativas) en reservorio y bio-dosificación con Bti en el canal de alimentación.",
            "color": "#8e44ad"
        }
    ]

    for epi in epicentros_diagnostico:
        folium.CircleMarker(
            location=epi["coords"],
            radius=11,
            color=epi["color"],
            weight=2.5,
            fill=True,
            fill_color=epi["color"],
            fill_opacity=0.80,
            tooltip=f"🔥 {epi['nombre']} ({epi['sector']})",
            popup=folium.Popup(f"""
                <div style="font-family: 'Segoe UI', Arial, sans-serif; width: 280px; line-height: 1.42;">
                    <div style="background: {epi['color']}; color: white; padding: 7px 11px; border-radius: 6px 6px 0 0; font-weight: bold; font-size: 13px;">
                        🔥 {epi['nombre']}
                    </div>
                    <div style="padding: 10px 12px; border: 1px solid {epi['color']}; border-top: none; border-radius: 0 0 6px 6px; background: #fffdfd; font-size: 12px; color: #2c3e50;">
                        <span style="background: #fde8e8; color: #c0392b; padding: 2px 7px; border-radius: 4px; font-weight: 700; font-size: 10.5px;">EPICENTRO EPIDEMIOLÓGICO</span>
                        <p style="margin: 7px 0 4px 0;"><b>👥 Comunidad Afectada:</b> {epi['poblacion']}.</p>
                        <p style="margin: 4px 0;"><b>💧 Foco Hidrológico:</b> {epi['foco']}.</p>
                        <p style="margin: 4px 0; color: #7f1d1d;"><b>💔 Impacto Diario:</b> {epi['impacto']}</p>
                        <div style="margin-top: 8px; padding: 6px 8px; background: #ecfdf5; border-left: 3px solid #10ac84; border-radius: 4px; color: #065f46; font-size: 11.5px;">
                            <b>🌿 Solución Algoritmo Verde:</b> {epi['solucion']}
                        </div>
                    </div>
                </div>
            """, max_width=300)
        ).add_to(fg_zonas)

    # -------------------------------------------------------------
    # 4. ESPACIOS HUMANOS REALES DEL CAMPUS (TRES ZONAS PRINCIPALES)
    # -------------------------------------------------------------
    hitos_humanos = [
        # =============================================================
        # ZONA 1: SENESCYT
        # =============================================================
        ([0.406633, -78.170096], "Edificio Senescyt (Yachay Tech)", "university", "darkblue",
         "🏛️ Edificio Académico de 4 Pisos", "Estructura de 4 pisos que alberga aulas magnas, oficinas de profesores, decanatos, hall principal, biblioteca y minimarket Krispan."),
        ([0.407655, -78.170721], "Centro Médico / Bienestar Estudiantil", "medkit", "red",
         "🏥 Salud y Bienestar Estudiantil", "Centro Médico Tipo A y Promoción de Vida Comunitaria. Atención primaria médica y psicológica."),
        ([0.406950, -78.171150], "Residencias Estudiantiles 'Los Bloques'", "bed", "darkred",
         "🛌 Alojamiento Estudiantil (Bloques A-I)", "Complejo habitacional de 9 bloques modulares (A a I) blindado por la Cerca Viva 3."),
        ([0.406259, -78.170117], "Biblioteca (Edificio Senescyt - 24/7)", "book", "blue",
         "📚 Biblioteca y Sala de Estudio (24/7)", "Sala de lectura, consulta individual y estudio en el primer piso (ala sur) del Edificio Senescyt. Servicio continuo 24/7 para estudiantes e investigadores."),
        ([0.406501, -78.170395], "Minimarket Krispan", "shopping-cart", "orange",
         "☕ Cafetería y Abastecimiento (Primer Piso)", "Local interior de alimentos, café y artículos de primera necesidad en el primer piso (ala oeste) de Senescyt."),
        ([0.407063, -78.169911], "Comedor Sol del Ecuador", "cutlery", "orange",
         "🍲 Restaurante Universitario (Primer Piso)", "Comedor en primer piso (ala norte) de Senescyt. Almuerzo: USD 3.50 (afluencia moderada de docentes, personal administrativo y estudiantes)."),
        ([0.4065590, -78.1701841], "Hall Principal Edificio Senescyt", "users", "darkblue",
         "🏛️ Hall Principal (Planta Baja)", "Vestíbulo cívico y de distribución principal en el primer piso del Edificio Senescyt. Conecta biblioteca, aulas y áreas de convivencia."),

        # =============================================================
        # ZONA 2: INGENIO AZUCARERO
        # =============================================================
        ([0.405060, -78.174257], "Biblioteca Patrimonial Principal (24/7)", "book", "blue",
         "📚 Biblioteca Central Patrimonial (24/7)", "Emblemática biblioteca histórica de la Hacienda San José con atención ininterrumpida 24/7, jardines y salas de lectura."),
        ([0.405220, -78.174354], "Torre del Ingenio Azucarero", "history", "purple",
         "🏛️ Monumento Histórico", "Chimenea y torre histórica de la Hacienda San José. Símbolo patrimonial de Urcuquí y del campus."),
        ([0.405324, -78.174470], "Plaza del Ingenio", "sun-o", "purple",
         "🎭 Explanada Cívica y Cultural", "Gran explanada patrimonial frente a la Chimenea y la Biblioteca Patrimonial."),
        ([0.404933, -78.174292], "Plaza del Estudiante", "users", "green",
         "🤝 Convivencia y Descanso", "Plazoleta peatonal arbolada entre Aulas B y Aulas I."),
        ([0.404415, -78.175230], "Sala Capitular", "landmark", "darkpurple",
         "🏛️ Sala Capitular Patrimonial", "Monumento histórico y sala ceremonial de la Hacienda San José."),
        ([0.404402, -78.175821], "Sala de Defensas San José", "mortar-board", "darkblue",
         "🎓 Sala de Grados y Tesis", "Espacio solemne para sustentación de tesis y actos de titulación universitaria."),
        ([0.404270, -78.174298], "Aulas B (Sur)", "pencil", "cadetblue",
         "✏️ Aulas de Docencia B", "Bloque de aulas teóricas y seminarios junto a la arboleda patrimonial."),
        ([0.405354, -78.174306], "Aulas B (Norte)", "pencil", "cadetblue",
         "✏️ Aulas de Docencia B Norte", "Bloque de aulas B norte, adyacente a la Plaza del Ingenio."),
        ([0.405224, -78.174622], "Aulas I (Antiguo Ingenio)", "university", "cadetblue",
         "🏛️ Aulas y Talleres I", "Nave patrimonial adaptada para laboratorios, docencia técnica y talleres de ingeniería."),
        ([0.404328, -78.173777], "Restaurant El Colibrí", "coffee", "orange",
         "🍲 Comedor Universitario (Alta Demanda)", "Restaurante tradicional en Plaza Mikuna. Almuerzo económico: USD 2.50 (alta afluencia estudiantil en horas pico, foco de atracción humana)."),
        ([0.404211, -78.173869], "Mesas y Sitio de Estar (Plaza Mikuna)", "cutlery", "darkgreen",
         "🍽️ Comedor Cubierto al Aire Libre", "Área de mesas bajo cubierta para consumo de alimentos sin picaduras."),
        ([0.404550, -78.173820], "Restaurant Containers (Plaza Mikuna)", "cutlery", "darkred",
         "🍔 Patio Gastronómico Containers", "Módulos de restaurantes en contenedores ecológicos adaptados."),
        ([0.404419, -78.173849], "Sitio de Fogata (Plaza Mikuna)", "fire", "red",
         "🔥 Espacio Comunitario de Fogata", "Punto tradicional de reunión y fogatas de fin de semestre."),
        ([0.403800, -78.172660], "Laboratorios de Carrera (Ingenierías)", "cogs", "darkpurple",
         "💻 Investigación y Tecnología", "Talleres experimentales de ingeniería junto al canal hídrico central."),
        ([0.404200, -78.173150], "Invernaderos Experimentales", "leaf", "darkgreen",
         "🌱 Investigación Agropecuaria", "Conjunto de cuatro invernaderos de ensayo fitoquímico y botánico."),
        ([0.404900, -78.173900], "Laboratorio de Química", "flask", "darkpurple",
         "🔬 Biotecnología y Química", "Laboratorios para caracterización fitoquímica de terpenos protectores."),
        ([0.4058643, -78.1706952], "Plaza Edificio ITT", "square-o", "cadetblue",
         "🏛️ Plaza Cívica Edificio ITT", "Explanada central peatonal articulada entre los dos bloques de aulas y laboratorios del ITT."),

        # =============================================================
        # ZONA 3: RESIDENCIAS 'LAS PATS' Y 'MULTIFAMILIARES'
        # =============================================================
        ([0.402750, -78.174800], "Residencias Estudiantiles 'Las Multis'", "building", "green",
         "🏢 Complejo Multifamiliar (3 Pisos)", "13 edificios de 3 pisos con ~5 departamentos por piso (2 a 6 personas por depto; ~30-90 residentes/bloque). Máxima densidad estudiantil del campus."),
        ([0.402297, -78.173836], "Residencias Estudiantiles 'Las Pats'", "home", "green",
         "🏡 Residencias Patrimoniales", "Edificios de 1 piso (~6 personas) y de 2 pisos (~8 personas conviviendo) en arquitectura tradicional de teja."),
        ([0.400650, -78.175090], "Residencias Estudiantiles 'Las T\'s'", "home", "gray",
         "🏘️ Módulos en T (Sector Residencial Sur)", "13 estructuras modulares pareadas en T ubicadas en este sector patrimonial sur. Estructuras actualmente desocupadas (sin residentes activos); baja emisión antropogénica."),
        ([0.402150, -78.174500], "Residencias de Docentes", "briefcase", "cadetblue",
         "🏠 Villas Docentes", "Conjunto de viviendas asignadas al cuerpo docente e investigadores residentes."),
        ([0.4018349, -78.1755181], "Concha Acústica Yachay Tech", "music", "darkgreen",
         "🎭 Cultura y Eventos al Aire Libre", "Anfiteatro universitario al aire libre recuperado para conciertos y arte sin picaduras."),
        ([0.402500, -78.171800], "Canchas Deportivas (Fútbol / Múltiples)", "futbol-o", "blue",
         "⚽ Deporte y Actividad Física", "Canchas reglamentarias de césped y vóley junto a la acequia sur protegida."),
        ([0.402550, -78.172800], "Parada (Arco de las Pats)", "bus", "gray",
         "🚌 Transporte Universitario", "Punto principal de arribo y espera de buses universitarios hacia Ibarra y Urcuquí."),
        ([0.4021506, -78.1751864], "Plaza de las Multis", "sun-o", "green",
         "🤝 Espacio Comunitario y Recreación", "Plazoleta central y área de convivencia al aire libre entre los bloques multifamiliares."),
        ([0.4043772, -78.1754463], "Pileta Histórica (Claustro Sala Capitular)", "tint", "blue",
         "⛲ Fuente Ornamental Claustral (Seca)", "Pileta central de piedra en claustro de Sala Capitular. Permanece seca la mayor parte del año; 0% riesgo de cría larvaria de vectores."),
        ([0.4043464, -78.1756891], "Pileta de Jardines (Sala Capitular)", "tint", "cadetblue",
         "⛲ Fuente Ornamental de Jardín (Seca)", "Pileta ornamental en jardines exteriores San José. Permanece seca habitualmente; nulo riesgo de proliferación entomológica."),
        ([0.4042981, -78.1751977], "Pileta de Agua (Sector Sala Capitular)", "tint", "blue",
         "⛲ Fuente Ornamental Exterior", "Pileta ornamental en el sector exterior contiguo a la Sala Capitular; estructura monitoreada sin estancamiento."),
        ([0.4053046, -78.1748750], "Molino de Agua (Patrimonial, Fuera de Uso)", "cog", "purple",
         "⚙️ Patrimonio Industrial Hidráulico (No en Uso)", "Molino hidráulico histórico de la antigua Hacienda San José. Actualmente no está en uso; sin flujo motriz ni molienda activa."),
        ([0.4043885, -78.1759853], "Parqueadero San José 1 (Norte)", "car", "gray",
         "🚗 Estacionamiento Vehicular", "Área de parqueo norte junto a la Sala de Defensas y Sala Capitular."),
        ([0.4044492, -78.1762745], "Parqueadero San José 2 (Central)", "car", "gray",
         "🚗 Estacionamiento Vehicular", "Área de parqueo central para usuarios, docentes y personal en sector San José."),
        ([0.4016694, -78.1749447], "Parqueadero Residencias 'Las Multis'", "car", "gray",
         "🚗 Estacionamiento Residencial", "Zona de aparcamiento para residentes y visitantes de Las Multis."),
        ([0.4034454, -78.1729857], "Parqueadero Complejo Deportivo", "car", "gray",
         "🚗 Estacionamiento Deportivo", "Parqueadero de acceso a canchas de fútbol, básquetbol y vóley de playa."),
        ([0.4020212, -78.1733637], "Parqueadero Sector 'Las Pats'", "car", "gray",
         "🚗 Estacionamiento Residencial", "Área de estacionamiento para las Residencias Patrimoniales Las Pats."),
        ([0.4042475, -78.1770788], "Parqueadero San José 3 (Oeste)", "car", "gray",
         "🚗 Estacionamiento Vehicular", "Parqueadero exterior occidental junto al Edificio 41 y servicios generales."),
        ([0.4074220, -78.1697626], "Depósito de Basura Principal (Senescyt)", "trash", "black",
         "🗑️ Gestión de Residuos Sólidos", "Estación principal de contenedores para reciclaje y desechos en Senescyt."),
        ([0.4022108, -78.1733913], "Depósito de Basura Principal (Las Pats)", "trash", "black",
         "🗑️ Gestión de Residuos Sólidos", "Estación de contenedores de residuos para el sector patrimonial Las Pats."),
        ([0.4057470, -78.1742848], "Depósito de Basura Principal (San José)", "trash", "black",
         "🗑️ Gestión de Residuos Sólidos", "Estación central de acopio de basura del sector Ingenio / San José."),
        ([0.4036513, -78.1751166], "Depósito de Basura (Sector Residencias Docentes / Multis)", "trash", "black",
         "🗑️ Gestión de Residuos Sólidos", "Estación de acopio y contenedores para el sector sur de Residencias de Docentes y Las Multis."),
        ([0.4047478, -78.1743254], "Depósito de Basura (Tachos Aulas B)", "trash", "gray",
         "🗑️ Tachos de Residuos Menores", "Punto ecológico de tachos pequeños para estudiantes en Aulas B."),
        ([0.4049303, -78.1741545], "Depósito de Basura (Tachos Plaza del Estudiante)", "trash", "gray",
         "🗑️ Tachos de Residuos Menores", "Tachos de clasificación de residuos en Plaza del Estudiante."),
        ([0.4043180, -78.1738190], "Depósito de Basura (Tachos Plaza Mikuna)", "trash", "gray",
         "🗑️ Tachos de Residuos Menores", "Punto ecológico de tachos de basura en patio gastronómico Plaza Mikuna."),
        ([0.4041680, -78.1767040], "Tachos de Basura (San José / Restaurantes)", "trash", "gray",
         "🗑️ Tachos de Residuos Menores", "Punto de recolección de residuos orgánicos entre baterías sanitarias y comedores Analí y Pato Goloso."),
        ([0.4044473, -78.1750098], "Pozo Histórico en Desuso (Sala Capitular Este)", "exclamation-triangle", "red",
         "⚠️ Foco Entomológico (Pozo en Mal Estado)", "Estructura de pozo en mal estado con retención de agua y humedad sombría; punto prioritario de inspección y control biológico de Culicoides spp."),
        ([0.4058428, -78.1733964], "Antiguo Humedal / Posible Fuente Hídrica Subterránea", "tint", "darkblue",
         "💧 Sospecha Hídrica / Paleohumedal", "Sector de antiguo lago con presencia persistente de vegetación densa tras labores de poda/fumigación. Evidencia de posible nivel freático alto, paleohumedal o fuente hídrica subterránea; foco prioritario de inspección larvaria y refugio de adultos de Simulium spp."),
        ([0.4039612, -78.1689813], "Esclusa y Compuerta Hidráulica Este", "filter", "blue",
         "⚙️ Infraestructura Hídrica / Esclusa", "Compuerta y esclusa de regulación hídrica conectada al canal de conducción este. Punto neurálgico para dosificación biológica y regulación de flujo laminar contra cría de tábanos y arenillas."),
        ([0.4039391, -78.1767816], "Parqueadero San José 4 (Extremo Oeste)", "car", "gray",
         "🚗 Estacionamiento Vehicular", "Área de parqueo exterior en el extremo occidental de San José / Concha Acústica."),
        ([0.4045529, -78.1739939], "Sitio de Parqueo en Vía (Biblioteca Sur)", "car", "lightgray",
         "🚗 Parqueo en Vía", "Espacio de aparcamiento lateral sobre calzada en el eje vehicular de Biblioteca y Aulas B."),
        ([0.4050925, -78.1740554], "Sitio de Parqueo en Vía (Biblioteca Central)", "car", "lightgray",
         "🚗 Parqueo en Vía", "Espacio de aparcamiento lateral sobre calzada frente a Biblioteca Patrimonial."),
        ([0.4052694, -78.1741467], "Sitio de Parqueo en Vía (Torre del Ingenio)", "car", "lightgray",
         "🚗 Parqueo en Vía", "Espacio de aparcamiento lateral sobre calzada junto a la Torre del Ingenio."),
        ([0.4054657, -78.1742427], "Sitio de Parqueo en Vía (Chimenea Norte)", "car", "lightgray",
         "🚗 Parqueo en Vía", "Espacio de aparcamiento lateral sobre calzada en el acceso norte al casco histórico."),
        ([0.4075754, -78.1703796], "Sitio de Parqueo en Vía (Senescyt Norte 1)", "car", "lightgray",
         "🚗 Parqueo en Vía", "Espacio de aparcamiento lateral sobre vía de acceso norte a Senescyt y Centro Médico."),
        ([0.4074696, -78.1702623], "Sitio de Parqueo en Vía (Senescyt Norte 2)", "car", "lightgray",
         "🚗 Parqueo en Vía", "Espacio de aparcamiento lateral sobre vía norte hacia Edificio Senescyt."),
        ([0.4073308, -78.1701017], "Sitio de Parqueo en Vía (Senescyt Acceso Principal)", "car", "lightgray",
         "🚗 Parqueo en Vía", "Espacio de aparcamiento sobre vía principal frente al acceso a Senescyt."),
        ([0.4069505, -78.1696585], "Sitio de Parqueo en Vía (Senescyt Este / Comedor)", "car", "lightgray",
         "🚗 Parqueo en Vía", "Espacio de aparcamiento lateral sobre vía este junto al Comedor Sol del Ecuador."),
        ([0.4071972, -78.1699859], "Parada de Buses (Edificio Senescyt)", "bus", "purple",
         "🚌 Movilidad y Transporte Universitario", "Parada principal de transporte público y buses universitarios en el acceso oriental del Edificio Senescyt."),
        ([0.4040003, -78.1750936], "Parada de Buses (Sala Capitular)", "bus", "purple",
         "🚌 Movilidad y Transporte Universitario", "Parada de transporte público y buses universitarios en el sector patrimonial San José - Sala Capitular."),
        ([0.4027118, -78.1737212], "Parada de Buses (Frente al Arco de Las Pats)", "bus", "purple",
         "🚌 Movilidad y Transporte Universitario", "Parada de transporte público y buses universitarios frente al arco patrimonial de acceso a Residencias Las Pats."),
        ([0.4060672, -78.1702615], "Parqueadero Senescyt (Sur 1)", "car", "gray",
         "🚗 Estacionamiento Vehicular", "Punto de estacionamiento vehicular en el área de parqueadero sur del Edificio Senescyt."),
        ([0.4062500, -78.1704686], "Parqueadero Senescyt (Sur 2)", "car", "gray",
         "🚗 Estacionamiento Vehicular", "Punto de estacionamiento vehicular en el área de parqueadero sur del Edificio Senescyt."),
        ([0.4061990, -78.1698907], "Parqueadero Senescyt (Este 1)", "car", "gray",
         "🚗 Estacionamiento Vehicular", "Punto de estacionamiento vehicular en el área de parqueadero este del Edificio Senescyt."),
        ([0.4065601, -78.1695897], "Parqueadero Senescyt (Este 2)", "car", "gray",
         "🚗 Estacionamiento Vehicular", "Punto de estacionamiento vehicular en el área de parqueadero este del Edificio Senescyt.")
    ]

    for coord, nombre, icono, color, categoria, descripcion_humana in hitos_humanos:
        folium.Marker(
            location=coord,
            icon=folium.Icon(icon=icono, prefix='fa', color=color),
            popup=folium.Popup(f"""
                <div style="font-family: 'Segoe UI', Arial, sans-serif; width: 250px; line-height: 1.4;">
                    <div style="color: #1e3799; font-weight: bold; font-size: 14px; margin-bottom: 3px;">{nombre}</div>
                    <span style="background: #eef2f7; color: #34495e; padding: 2px 7px; border-radius: 4px; font-size: 11px; font-weight: 600;">{categoria}</span>
                    <p style="margin: 8px 0 6px 0; font-size: 12px; color: #2c3e50;">{descripcion_humana}</p>
                    <div style="font-size: 10px; color: #7f8c8d; border-top: 1px solid #ecf0f1; padding-top: 4px;">
                        📍 GPS Google: {coord[0]:.6f}, {coord[1]:.6f}
                    </div>
                </div>
            """, max_width=270),
            tooltip=f"{nombre} ({categoria})"
        ).add_to(fg_edificios)

    # -------------------------------------------------------------
    # 4.1 HUELLAS ARQUITECTÓNICAS RECTANGULARES (ZONA NORTE)
    # -------------------------------------------------------------
    huellas_arquitectonicas = [
        {
            "id": "RECT-A",
            "nombre": "Bloque A",
            "tipo": "Residencia Estudiantil (Rectangular)",
            "zona": "Senescyt",
            "coords": [[0.40418, -78.17538], [0.40411, -78.17582], [0.40406, -78.17565], [0.40392, -78.17545]],
            "centroid": [0.406809, -78.1705632],
            "area": 599.6,
            "color": "#16a085", "fill": "#1abc9c",
            "interior": False,
            "is_perimeter": False,
            "desc": "Bloque residencial modular estudiantil en zona norte."
        },
        {
            "id": "RECT-B",
            "nombre": "Bloque B",
            "tipo": "Residencia Estudiantil (Rectangular)",
            "zona": "Senescyt",
            "coords": [[0.4069112, -78.1708846], [0.4071388, -78.1706975], [0.4070326, -78.1705683], [0.406805, -78.1707554]],
            "centroid": [0.4069719, -78.1707264],
            "area": 607.1,
            "color": "#16a085", "fill": "#1abc9c",
            "interior": False,
            "is_perimeter": False,
            "desc": "Bloque residencial modular estudiantil en zona norte."
        },
        {
            "id": "RECT-C",
            "nombre": "Bloque C",
            "tipo": "Residencia Estudiantil (Rectangular)",
            "zona": "Senescyt",
            "coords": [[0.4072065, -78.1707382], [0.4069815, -78.170937], [0.4070848, -78.1710539], [0.4073098, -78.1708551]],
            "centroid": [0.4071457, -78.170896],
            "area": 577.1,
            "color": "#16a085", "fill": "#1abc9c",
            "interior": False,
            "is_perimeter": False,
            "desc": "Bloque residencial modular estudiantil en zona norte."
        },
        {
            "id": "RECT-D",
            "nombre": "Bloque D",
            "tipo": "Residencia Estudiantil (Rectangular)",
            "zona": "Senescyt",
            "coords": [[0.4071311, -78.1711226], [0.4073159, -78.1713426], [0.4074547, -78.171226], [0.4072699, -78.171006]],
            "centroid": [0.4072929, -78.1711743],
            "area": 641.7,
            "color": "#16a085", "fill": "#1abc9c",
            "interior": False,
            "is_perimeter": False,
            "desc": "Bloque residencial modular estudiantil en zona norte."
        },
        {
            "id": "RECT-E",
            "nombre": "Bloque E",
            "tipo": "Residencia Estudiantil (Rectangular)",
            "zona": "Senescyt",
            "coords": [[0.4072764, -78.1709972], [0.4074687, -78.1712182], [0.4075913, -78.1711116], [0.407399, -78.1708906]],
            "centroid": [0.4074338, -78.1710544],
            "area": 586.5,
            "color": "#16a085", "fill": "#1abc9c",
            "interior": False,
            "is_perimeter": False,
            "desc": "Bloque residencial modular estudiantil en zona norte."
        },
        {
            "id": "RECT-F",
            "nombre": "Bloque F",
            "tipo": "Residencia Estudiantil (Rectangular Independiente)",
            "zona": "Senescyt",
            "coords": [[0.4075616, -78.1714552], [0.4078955, -78.171474], [0.4079049, -78.1713069], [0.407571, -78.1712881]],
            "centroid": [0.4077333, -78.1713811],
            "area": 689.6,
            "color": "#27ae60", "fill": "#2ecc71",
            "interior": False,
            "is_perimeter": False,
            "desc": "Bloque F independiente (ala occidental del complejo F/G)."
        },
        {
            "id": "RECT-G",
            "nombre": "Bloque G",
            "tipo": "Residencia Estudiantil (Rectangular Independiente)",
            "zona": "Senescyt",
            "coords": [[0.4078877, -78.1713166], [0.4079317, -78.1709736], [0.4077735, -78.1709533], [0.4077295, -78.1712963]],
            "centroid": [0.4078306, -78.1711349],
            "area": 679.6,
            "color": "#27ae60", "fill": "#2ecc71",
            "interior": False,
            "is_perimeter": False,
            "desc": "Bloque G independiente (ala oriental del complejo F/G)."
        },
        {
            "id": "RECT-H",
            "nombre": "Bloque H",
            "tipo": "Residencia Estudiantil (Rectangular)",
            "zona": "Senescyt",
            "coords": [[0.4071925, -78.1703263], [0.4074167, -78.1705805], [0.407533, -78.170478], [0.4073088, -78.1702238]],
            "centroid": [0.4073627, -78.1704022],
            "area": 647.5,
            "color": "#16a085", "fill": "#1abc9c",
            "interior": False,
            "is_perimeter": False,
            "desc": "Bloque residencial modular estudiantil en zona este."
        },
        {
            "id": "RECT-I",
            "nombre": "Bloque I",
            "tipo": "Residencia Estudiantil (Rectangular)",
            "zona": "Senescyt",
            "coords": [[0.4070515, -78.1704146], [0.4073067, -78.1701927], [0.4072116, -78.1700833], [0.4069564, -78.1703052]],
            "centroid": [0.4071315, -78.170249],
            "area": 604.0,
            "color": "#16a085", "fill": "#1abc9c",
            "interior": False,
            "is_perimeter": False,
            "desc": "Bloque residencial modular estudiantil en zona este."
        },
        {
            "id": "RECT-MED",
            "nombre": "Centro Médico / Bienestar Estudiantil",
            "tipo": "Salud y Vida Comunitaria (Rectangular)",
            "zona": "Senescyt",
            "coords": [[0.407518, -78.1706569], [0.407687, -78.1708685], [0.4077926, -78.1707842], [0.4076236, -78.1705726]],
            "centroid": [0.4076553, -78.1707206],
            "area": 450.9,
            "color": "#e74c3c", "fill": "#ff7675",
            "interior": False,
            "is_perimeter": False,
            "desc": "Centro Médico Tipo A y Promoción de Vida Comunitaria."
        },
        {
            "id": "POLY-SENESCYT",
            "nombre": "Edificio Senescyt",
            "tipo": "Edificio Académico y Administrativo de 4 Pisos (8 Vértices)",
            "zona": "Senescyt",
            "coords": [[0.4071147, -78.1699317], [0.4069484, -78.1697289], [0.4068317, -78.1698328], [0.4068019, -78.1698043], [0.4063912, -78.170151], [0.4062218, -78.1699562], [0.4061159, -78.1700531], [0.4064619, -78.1704732]],
            "centroid": [0.4066329, -78.1700962],
            "area": 3474.8,
            "color": "#c0392b", "fill": "#e74c3c",
            "interior": False,
            "is_perimeter": False,
            "desc": "Estructura principal de 4 pisos. En el primer piso concentra el Hall principal, biblioteca universitaria, minimarket Krispan, Comedor Sol del Ecuador y aulas de docencia; los pisos superiores albergan oficinas de profesores, decanatos y aulas adicionales."
        },
        {
            "id": "INT-BIB",
            "nombre": "Biblioteca Universitaria (Senescyt - 24/7)",
            "tipo": "Sala de Estudio y Lectura 24/7 (Primer Piso)",
            "zona": "Senescyt",
            "coords": [[0.4062218, -78.1699562], [0.4061159, -78.1700531], [0.406315, -78.1702949], [0.4063677, -78.1702261], [0.4063425, -78.1701969], [0.4063898, -78.170154], [0.4062959, -78.1700414]],
            "centroid": [0.4062594, -78.1701174],
            "area": 514.6,
            "color": "#1d6fa5", "fill": "#3498db",
            "interior": True,
            "is_perimeter": False,
            "desc": "Biblioteca interior en el primer piso (ala sur) del Edificio Senescyt. Servicio ininterrumpido de estudio e investigación 24/7."
        },
        {
            "id": "INT-KRISPAN",
            "nombre": "Minimarket Krispan",
            "tipo": "Comercial / Cafetería (Primer Piso - Edificio Senescyt)",
            "zona": "Senescyt",
            "coords": [[0.4065494, -78.1703109], [0.4064042, -78.1704011], [0.4064522, -78.1704784], [0.4065974, -78.1703882]],
            "centroid": [0.4065008, -78.1703946],
            "area": 191.7,
            "color": "#d35400", "fill": "#e67e22",
            "interior": True,
            "is_perimeter": False,
            "desc": "Minimarket y cafetería interior situada en el primer piso (ala oeste) de Senescyt."
        },
        {
            "id": "INT-COMEDOR",
            "nombre": "Comedor Sol del Ecuador",
            "tipo": "Restaurante Universitario (Primer Piso - Edificio Senescyt)",
            "zona": "Senescyt",
            "coords": [[0.4071116, -78.1699224], [0.4070583, -78.1698613], [0.4070134, -78.1699005], [0.4070667, -78.1699616]],
            "centroid": [0.4070625, -78.1699114],
            "area": 59.6,
            "color": "#d35400", "fill": "#f39c12",
            "interior": True,
            "is_perimeter": False,
            "desc": "Comedor universitario en el primer piso (ala norte interior) de Senescyt. Almuerzo: USD 3.50 (afluencia moderada de docentes, personal administrativo y estudiantes)."
        },
        {
            "id": "POLY-BIB-PAT",
            "nombre": "Biblioteca Patrimonial Principal (24/7)",
            "tipo": "Biblioteca y Patrimonio Histórico 24/7 (13 Vértices)",
            "zona": "Ingenio Azucarero",
            "coords": [[0.404974, -78.1745032], [0.4050648, -78.1745478], [0.4052466, -78.1741918], [0.4049036, -78.1740328], [0.4048781, -78.1740757], [0.4048509, -78.174063], [0.4048342, -78.1740918], [0.4048677, -78.1741103], [0.4048446, -78.1741485], [0.4049049, -78.174179], [0.4049301, -78.1741401], [0.4051064, -78.1742397], [0.4049746, -78.1745002]],
            "centroid": [0.4050602, -78.1742572],
            "area": 869.5,
            "color": "#2980b9", "fill": "#3498db",
            "interior": False,
            "is_perimeter": False,
            "desc": "Biblioteca patrimonial histórica de la Hacienda San José. Salas de estudio y lectura con atención ininterrumpida 24/7."
        },
        {
            "id": "RECT-BANOS-BIB",
            "nombre": "Baños Biblioteca Patrimonial",
            "tipo": "Servicios Higiénicos",
            "zona": "Ingenio Azucarero",
            "coords": [[0.404742, -78.174346], [0.4048017, -78.1743738], [0.4048203, -78.1743338], [0.4047606, -78.174306]],
            "centroid": [0.4047812, -78.1743399],
            "area": 35.8,
            "color": "#7f8c8d", "fill": "#bdc3c7",
            "interior": False,
            "is_perimeter": False,
            "desc": "Batería sanitaria exterior de la Biblioteca Patrimonial."
        },
        {
            "id": "RECT-AULAS-B-SUR",
            "nombre": "Aulas B (Sur Biblioteca)",
            "tipo": "Docencia y Seminarios",
            "zona": "Ingenio Azucarero",
            "coords": [[0.4044119, -78.1743079], [0.404172, -78.1741934], [0.4041269, -78.1742878], [0.4043668, -78.1744023]],
            "centroid": [0.4042694, -78.1742978],
            "area": 342.6,
            "color": "#1f618d", "fill": "#5dade2",
            "interior": False,
            "is_perimeter": False,
            "desc": "Bloque de aulas al sur de la Biblioteca Patrimonial."
        },
        {
            "id": "RECT-AULAS-B-NORTE",
            "nombre": "Aulas B (Norte)",
            "tipo": "Docencia y Seminarios",
            "zona": "Ingenio Azucarero",
            "coords": [[0.4055181, -78.1743369], [0.4052311, -78.1741944], [0.4051907, -78.1742757], [0.4054777, -78.1744182]],
            "centroid": [0.4053544, -78.1743063],
            "area": 358.5,
            "color": "#1f618d", "fill": "#5dade2",
            "interior": False,
            "is_perimeter": False,
            "desc": "Bloque de aulas B norte, adyacente a la Plaza del Ingenio."
        },
        {
            "id": "RECT-AULAS-I-1",
            "nombre": "Aulas I (Módulo 1 - Antiguo Ingenio)",
            "tipo": "Aulas Técnicas y Talleres",
            "zona": "Ingenio Azucarero",
            "coords": [[0.4051256, -78.1745126], [0.4050769, -78.1746142], [0.4053233, -78.1747322], [0.405372, -78.1746306]],
            "centroid": [0.4052244, -78.1746224],
            "area": 379.3,
            "color": "#6c3483", "fill": "#bb8fce",
            "interior": False,
            "is_perimeter": False,
            "desc": "Módulo patrimonial restaurado para clases técnicas."
        },
        {
            "id": "RECT-AULAS-I-2",
            "nombre": "Aulas I (Módulo 2 - Antiguo Ingenio)",
            "tipo": "Aulas Técnicas y Talleres",
            "zona": "Ingenio Azucarero",
            "coords": [[0.4054504, -78.1746678], [0.4055414, -78.1744942], [0.405489, -78.1744667], [0.405398, -78.1746403]],
            "centroid": [0.4054697, -78.1745673],
            "area": 143.0,
            "color": "#6c3483", "fill": "#bb8fce",
            "interior": False,
            "is_perimeter": False,
            "desc": "Módulo norte de Aulas I."
        },
        {
            "id": "RECT-BANOS-AULAS-I",
            "nombre": "Baños Aulas I",
            "tipo": "Servicios Higiénicos Yuxtapuestos",
            "zona": "Ingenio Azucarero",
            "coords": [[0.405327, -78.1747475], [0.4054, -78.174776], [0.4054449, -78.1746611], [0.4053719, -78.1746326]],
            "centroid": [0.405386, -78.1747043],
            "area": 119.2,
            "color": "#7f8c8d", "fill": "#bdc3c7",
            "interior": False,
            "is_perimeter": False,
            "desc": "Batería de baños yuxtapuesta a las naves de Aulas I."
        },
        {
            "id": "RECT-SALA-DOCENTES",
            "nombre": "Sala de Docentes (Ingenio)",
            "tipo": "Área de Profesores",
            "zona": "Ingenio Azucarero",
            "coords": [[0.4055409, -78.1744952], [0.405607, -78.1743896], [0.405553, -78.1743558], [0.4054869, -78.1744614]],
            "centroid": [0.4055469, -78.1744255],
            "area": 97.8,
            "color": "#16a085", "fill": "#48c9b0",
            "interior": False,
            "is_perimeter": False,
            "desc": "Espacio de trabajo y descanso para cuerpo docente."
        },
        {
            "id": "RECT-LABS-DOCENCIA",
            "nombre": "Laboratorios de Docencia",
            "tipo": "Talleres y Docencia Práctica",
            "zona": "Ingenio Azucarero",
            "coords": [[0.4054855, -78.1748217], [0.4056858, -78.1744248], [0.4056007, -78.1743819], [0.4054004, -78.1747788]],
            "centroid": [0.4055431, -78.1746018],
            "area": 522.2,
            "color": "#2c3e50", "fill": "#566573",
            "interior": False,
            "is_perimeter": False,
            "desc": "Naves de docencia práctica y laboratorios formativos."
        },
        {
            "id": "RECT-COLIBRI",
            "nombre": "Restaurante El Colibrí",
            "tipo": "Comedor Universitario",
            "zona": "Ingenio Azucarero",
            "coords": [[0.4042855, -78.1737925], [0.4043474, -78.1738179], [0.4043707, -78.1737612], [0.4043088, -78.1737358]],
            "centroid": [0.4043281, -78.1737769],
            "area": 50.5,
            "color": "#d35400", "fill": "#e67e22",
            "interior": False,
            "is_perimeter": False,
            "desc": "Restaurante universitario tradicional en Plaza Mikuna. Almuerzo económico: USD 2.50 (alta afluencia estudiantil en horas pico, foco de atracción humana)."
        },
        {
            "id": "RECT-MESAS-MIKUNA",
            "nombre": "Mesas y Sitio de Estar (Plaza Mikuna)",
            "tipo": "Comedor Cubierto al Aire Libre",
            "zona": "Ingenio Azucarero",
            "coords": [[0.4042451, -78.1738246], [0.404176, -78.1738246], [0.404176, -78.1739135], [0.4042451, -78.1739135]],
            "centroid": [0.4042106, -78.173869],
            "area": 75.7,
            "color": "#27ae60", "fill": "#58d68d",
            "interior": False,
            "is_perimeter": False,
            "desc": "Área de mesas bajo cubierta para consumo de alimentos y estancia."
        },
        {
            "id": "RECT-CONTAINERS-1",
            "nombre": "Containers de Comida 1 (Plaza Mikuna)",
            "tipo": "Módulos Gastronómicos",
            "zona": "Ingenio Azucarero",
            "coords": [[0.4046048, -78.1737629], [0.4045036, -78.1737985], [0.4045138, -78.1738274], [0.404615, -78.1737918]],
            "centroid": [0.4045593, -78.1737952],
            "area": 40.5,
            "color": "#b03a2e", "fill": "#ec7063",
            "interior": False,
            "is_perimeter": False,
            "desc": "Módulo norte de contenedores gastronómicos en Plaza Mikuna."
        },
        {
            "id": "RECT-CONTAINERS-2",
            "nombre": "Containers de Comida 2 (Plaza Mikuna)",
            "tipo": "Módulos Gastronómicos",
            "zona": "Ingenio Azucarero",
            "coords": [[0.4045006, -78.1738863], [0.4045461, -78.1739152], [0.4045636, -78.1738877], [0.4045181, -78.1738588]],
            "centroid": [0.4045321, -78.173887],
            "area": 21.7,
            "color": "#b03a2e", "fill": "#ec7063",
            "interior": False,
            "is_perimeter": False,
            "desc": "Módulo sur de contenedores gastronómicos en Plaza Mikuna."
        },
        {
            "id": "RECT-INV-1",
            "nombre": "Invernadero Experimental 1",
            "tipo": "Investigación Agropecuaria",
            "zona": "Ingenio Azucarero",
            "coords": [[0.4041395, -78.1729552], [0.4044119, -78.1730552], [0.4044572, -78.1729319], [0.4041848, -78.1728319]],
            "centroid": [0.4042983, -78.1729436],
            "area": 469.7,
            "color": "#196f3d", "fill": "#52be80",
            "interior": False,
            "is_perimeter": False,
            "desc": "Nave de cultivo protegido e investigación en bio-repelencia."
        },
        {
            "id": "RECT-INV-2",
            "nombre": "Invernadero Experimental 2",
            "tipo": "Investigación Agropecuaria",
            "zona": "Ingenio Azucarero",
            "coords": [[0.4043837, -78.1731279], [0.4041097, -78.1730253], [0.4040881, -78.173083], [0.4043621, -78.1731856]],
            "centroid": [0.4042359, -78.1731054],
            "area": 222.2,
            "color": "#196f3d", "fill": "#52be80",
            "interior": False,
            "is_perimeter": False,
            "desc": "Invernadero experimental para ensayo de especies botánicas."
        },
        {
            "id": "RECT-INV-3",
            "nombre": "Invernadero Experimental 3",
            "tipo": "Investigación Agropecuaria",
            "zona": "Ingenio Azucarero",
            "coords": [[0.4040372, -78.1732037], [0.4043145, -78.1733036], [0.4043367, -78.1732419], [0.4040594, -78.173142]],
            "centroid": [0.4041869, -78.1732228],
            "area": 238.0,
            "color": "#196f3d", "fill": "#52be80",
            "interior": False,
            "is_perimeter": False,
            "desc": "Invernadero botánico experimental."
        },
        {
            "id": "RECT-INV-4",
            "nombre": "Invernadero Experimental 4",
            "tipo": "Investigación Agropecuaria",
            "zona": "Ingenio Azucarero",
            "coords": [[0.4039885, -78.1733332], [0.4042629, -78.173434], [0.4042835, -78.1733779], [0.4040091, -78.1732771]],
            "centroid": [0.404136, -78.1733556],
            "area": 215.3,
            "color": "#196f3d", "fill": "#52be80",
            "interior": False,
            "is_perimeter": False,
            "desc": "Invernadero botánico experimental junto al eje agroforestal."
        },
        {
            "id": "RECT-LABS-CARRERA",
            "nombre": "Laboratorios de Carrera (Ingenierías)",
            "tipo": "Talleres y Naves Tecnológicas",
            "zona": "Ingenio Azucarero",
            "coords": [[0.4038491, -78.1728994], [0.4039735, -78.1724875], [0.4037509, -78.1724203], [0.4036265, -78.1728322]],
            "centroid": [0.4038, -78.1726599],
            "area": 1232.9,
            "color": "#4a235a", "fill": "#a569bd",
            "interior": False,
            "is_perimeter": False,
            "desc": "Naves de ingeniería y laboratorios experimentales de carrera."
        },
        {
            "id": "RECT-BANOS-LABS",
            "nombre": "Baños Laboratorios de Carrera",
            "tipo": "Servicios Higiénicos",
            "zona": "Ingenio Azucarero",
            "coords": [[0.4038265, -78.1728016], [0.4037989, -78.1728845], [0.4038497, -78.1729014], [0.4038773, -78.1728185]],
            "centroid": [0.4038381, -78.1728515],
            "area": 57.6,
            "color": "#7f8c8d", "fill": "#bdc3c7",
            "interior": False,
            "is_perimeter": False,
            "desc": "Batería sanitaria adyacente a los Laboratorios de Carrera."
        },
        {
            "id": "RECT-CAPITULAR",
            "nombre": "Sala Capitular",
            "tipo": "Monumento y Sala Patrimonial",
            "zona": "Ingenio Azucarero",
            "coords": [[0.4044278, -78.1753652], [0.4044453, -78.1752043], [0.4043741, -78.1751966], [0.4043566, -78.1753575]],
            "centroid": [0.404401, -78.1752809],
            "area": 142.8,
            "color": "#7d6608", "fill": "#f4d03f",
            "interior": False,
            "is_perimeter": False,
            "desc": "Sala Capitular histórica de la Hacienda San José."
        },
        {
            "id": "RECT-CABALLERIZAS",
            "nombre": "Aulas Caballerizas",
            "tipo": "Aulas Patrimoniales Adaptadas",
            "zona": "Ingenio Azucarero",
            "coords": [[0.4045321, -78.1756988], [0.4045271, -78.1760378], [0.4045776, -78.1760385], [0.4045826, -78.1756995]],
            "centroid": [0.4045548, -78.1758687],
            "area": 210.8,
            "color": "#7d6608", "fill": "#f5b041",
            "interior": False,
            "is_perimeter": False,
            "desc": "Antiguas caballerizas de la hacienda convertidas en aulas universitarias."
        },
        {
            "id": "RECT-EDIF-SUR-CAB",
            "nombre": "Edificio Sur Caballerizas",
            "tipo": "Edificación Auxiliar",
            "zona": "Ingenio Azucarero",
            "coords": [[0.4042508, -78.1757655], [0.4042153, -78.1756006], [0.4041423, -78.1756163], [0.4041778, -78.1757812]],
            "centroid": [0.4041965, -78.1756909],
            "area": 155.3,
            "color": "#7d6608", "fill": "#f5b041",
            "interior": False,
            "is_perimeter": False,
            "desc": "Edificación auxiliar sur del complejo de caballerizas."
        },
        {
            "id": "RECT-DEFENSAS-SAN-JOSE",
            "nombre": "Sala de Defensas San José",
            "tipo": "Sala de Grado y Defensa de Tesis",
            "zona": "Ingenio Azucarero",
            "coords": [[0.4043876, -78.1758678], [0.4044402, -78.1757886], [0.404417, -78.1757733], [0.4043644, -78.1758524]],
            "centroid": [0.4044023, -78.1758205],
            "area": 32.5,
            "color": "#1b4f72", "fill": "#5499c7",
            "interior": False,
            "is_perimeter": False,
            "desc": "Sala ceremonial para defensa de tesis de grado e investidura."
        },
        {
            "id": "RECT-BANOS-SAN-JOSE",
            "nombre": "Baños Sala de Defensas",
            "tipo": "Servicios Higiénicos",
            "zona": "Ingenio Azucarero",
            "coords": [[0.4044248, -78.175814], [0.4044254, -78.1757722], [0.4043909, -78.1757717], [0.4043903, -78.1758135]],
            "centroid": [0.4044079, -78.1757929],
            "area": 17.8,
            "color": "#7f8c8d", "fill": "#bdc3c7",
            "interior": False,
            "is_perimeter": False,
            "desc": "Servicios higiénicos adjuntos a la Sala San José."
        },
        {
            "id": "RECT-EDIF-ANEXO-DEF",
            "nombre": "Edificio Anexo San José",
            "tipo": "Edificación Administrativa",
            "zona": "Ingenio Azucarero",
            "coords": [[0.4043874, -78.1758643], [0.4044852, -78.1758681], [0.4044887, -78.1757777], [0.4043909, -78.1757739]],
            "centroid": [0.4044381, -78.175821],
            "area": 109.1,
            "color": "#1b4f72", "fill": "#5499c7",
            "interior": False,
            "is_perimeter": False,
            "desc": "Bloque anexo administrativo de la Sala de Defensas."
        },
        {
            "id": "PERIM-INGENIO",
            "nombre": "Polígono Complejo Ingenio Azucarero",
            "tipo": "Perímetro Complejo Histórico",
            "zona": "Ingenio Azucarero",
            "coords": [[0.405489, -78.1748234], [0.4056908, -78.1744328], [0.4048442, -78.1740107], [0.4046374, -78.1744077]],
            "centroid": [0.4051641, -78.1744181],
            "area": 5174.3,
            "color": "#8e44ad", "fill": "#bb8fce",
            "interior": False,
            "is_perimeter": True,
            "desc": "Delimitación general del casco histórico del Antiguo Ingenio Azucarero."
        },
        {
            "id": "PERIM-CAPITULAR",
            "nombre": "Polígono Complejo Sala Capitular y Caballerizas",
            "tipo": "Perímetro Histórico San José",
            "zona": "Ingenio Azucarero",
            "coords": [[0.4046333, -78.1752063], [0.4043752, -78.1751848], [0.4043574, -78.1752489], [0.4043236, -78.1752475], [0.4043115, -78.1752995], [0.4042143, -78.1753032], [0.4042049, -78.1755577], [0.4041271, -78.1755469], [0.4043722, -78.1764415], [0.4045777, -78.1763744], [0.4045733, -78.1756365]],
            "centroid": [0.4044094, -78.1757593],
            "area": 5070.5,
            "color": "#b7950b", "fill": "#f9e79f",
            "interior": False,
            "is_perimeter": True,
            "desc": "Perímetro patrimonial de la Hacienda San José (Sala Capitular y Caballerizas)."
        },
        {
            "id": "RECT-T-01",
            "nombre": "Casa Patrimonial Las T's 1",
            "tipo": "Residencia Estudiantil Patrimonial (Casa T)",
            "zona": "Las T's y Multis",
            "coords": [[0.400474, -78.1746762], [0.400643, -78.1744016], [0.4005601, -78.1743506], [0.4003911, -78.1746252]],
            "centroid": [0.4005171, -78.1745134],
            "area": 386.5,
            "color": "#27ae60", "fill": "#2ecc71",
            "interior": False,
            "is_perimeter": False,
            "desc": "Casa patrimonial tipo T de dos módulos residenciales con línea divisoria medianera central. Teja tradicional y corredores exteriores."
        },
        {
            "id": "RECT-T-02",
            "nombre": "Casa Patrimonial Las T's 2",
            "tipo": "Residencia Estudiantil Patrimonial (Casa T)",
            "zona": "Las T's y Multis",
            "coords": [[0.4003661, -78.1746641], [0.4001941, -78.1749471], [0.4002775, -78.1749978], [0.4004495, -78.1747148]],
            "centroid": [0.4003218, -78.174831],
            "area": 398.2,
            "color": "#27ae60", "fill": "#2ecc71",
            "interior": False,
            "is_perimeter": False,
            "desc": "Casa patrimonial tipo T de dos módulos residenciales con línea divisoria medianera central. Teja tradicional y corredores exteriores."
        },
        {
            "id": "RECT-T-03",
            "nombre": "Casa Patrimonial Las T's 3",
            "tipo": "Residencia Estudiantil Patrimonial (Casa T)",
            "zona": "Las T's y Multis",
            "coords": [[0.4005556, -78.1748175], [0.4007241, -78.1745438], [0.4006395, -78.1744917], [0.400471, -78.1747654]],
            "centroid": [0.4005975, -78.1746546],
            "area": 393.4,
            "color": "#27ae60", "fill": "#2ecc71",
            "interior": False,
            "is_perimeter": False,
            "desc": "Casa patrimonial tipo T de dos módulos residenciales con línea divisoria medianera central. Teja tradicional y corredores exteriores."
        },
        {
            "id": "RECT-T-04",
            "nombre": "Casa Patrimonial Las T's 4",
            "tipo": "Residencia Estudiantil Patrimonial (Casa T)",
            "zona": "Las T's y Multis",
            "coords": [[0.4004492, -78.1748063], [0.4002765, -78.1750826], [0.4003619, -78.175136], [0.4005346, -78.1748597]],
            "centroid": [0.4004056, -78.1749711],
            "area": 404.4,
            "color": "#27ae60", "fill": "#2ecc71",
            "interior": False,
            "is_perimeter": False,
            "desc": "Casa patrimonial tipo T de dos módulos residenciales con línea divisoria medianera central. Teja tradicional y corredores exteriores."
        },
        {
            "id": "RECT-T-05",
            "nombre": "Casa Patrimonial Las T's 5",
            "tipo": "Residencia Estudiantil Patrimonial (Casa T)",
            "zona": "Las T's y Multis",
            "coords": [[0.4007249, -78.1746561], [0.4006393, -78.1748581], [0.400731, -78.174897], [0.4008167, -78.174695]],
            "centroid": [0.400728, -78.1747765],
            "area": 269.5,
            "color": "#27ae60", "fill": "#2ecc71",
            "interior": False,
            "is_perimeter": False,
            "desc": "Módulo residencial patrimonial tipo T (Casa T 5). Sistema constructivo histórico restaurado con tabique divisorio interior."
        },
        {
            "id": "RECT-T-06",
            "nombre": "Casa Patrimonial Las T's 6",
            "tipo": "Residencia Estudiantil Patrimonial (Casa T)",
            "zona": "Las T's y Multis",
            "coords": [[0.4006223, -78.1751363], [0.4007077, -78.1749377], [0.4006141, -78.1748974], [0.4005287, -78.175096]],
            "centroid": [0.4006182, -78.1750168],
            "area": 271.4,
            "color": "#27ae60", "fill": "#2ecc71",
            "interior": False,
            "is_perimeter": False,
            "desc": "Módulo residencial patrimonial tipo T (Casa T 6). Sistema constructivo histórico restaurado con tabique divisorio interior."
        },
        {
            "id": "RECT-T-07",
            "nombre": "Casa Patrimonial Las T's 7",
            "tipo": "Residencia Estudiantil Patrimonial (Casa T)",
            "zona": "Las T's y Multis",
            "coords": [[0.4005132, -78.1751382], [0.4004237, -78.1753434], [0.400513, -78.1753824], [0.4006025, -78.1751772]],
            "centroid": [0.4005131, -78.1752603],
            "area": 268.8,
            "color": "#27ae60", "fill": "#2ecc71",
            "interior": False,
            "is_perimeter": False,
            "desc": "Módulo residencial patrimonial tipo T (Casa T 7). Sistema constructivo histórico restaurado con tabique divisorio interior."
        },
        {
            "id": "RECT-T-08",
            "nombre": "Casa Patrimonial Las T's 8",
            "tipo": "Residencia Estudiantil Patrimonial (Casa T)",
            "zona": "Las T's y Multis",
            "coords": [[0.400812, -78.1750482], [0.4009025, -78.1748415], [0.4008126, -78.1748021], [0.4007221, -78.1750088]],
            "centroid": [0.4008123, -78.1749251],
            "area": 272.7,
            "color": "#27ae60", "fill": "#2ecc71",
            "interior": False,
            "is_perimeter": False,
            "desc": "Módulo residencial patrimonial tipo T (Casa T 8). Sistema constructivo histórico restaurado con tabique divisorio interior."
        },
        {
            "id": "RECT-T-09",
            "nombre": "Casa Patrimonial Las T's 9",
            "tipo": "Residencia Estudiantil Patrimonial (Casa T)",
            "zona": "Las T's y Multis",
            "coords": [[0.400705, -78.1752905], [0.4007905, -78.1750873], [0.4007027, -78.1750504], [0.4006172, -78.1752536]],
            "centroid": [0.4007038, -78.1751704],
            "area": 258.7,
            "color": "#27ae60", "fill": "#2ecc71",
            "interior": False,
            "is_perimeter": False,
            "desc": "Módulo residencial patrimonial tipo T (Casa T 9). Sistema constructivo histórico restaurado con tabique divisorio interior."
        },
        {
            "id": "RECT-T-10",
            "nombre": "Casa Patrimonial Las T's 10",
            "tipo": "Residencia Estudiantil Patrimonial (Casa T)",
            "zona": "Las T's y Multis",
            "coords": [[0.4005981, -78.1752945], [0.4005085, -78.175496], [0.4005981, -78.1755358], [0.4006877, -78.1753343]],
            "centroid": [0.4005981, -78.1754152],
            "area": 266.4,
            "color": "#27ae60", "fill": "#2ecc71",
            "interior": False,
            "is_perimeter": False,
            "desc": "Módulo residencial patrimonial tipo T (Casa T 10). Sistema constructivo histórico restaurado con tabique divisorio interior."
        },
        {
            "id": "RECT-T-11",
            "nombre": "Casa Patrimonial Las T's 11",
            "tipo": "Residencia Estudiantil Patrimonial (Casa T - Módulo Cuádruple)",
            "zona": "Las T's y Multis",
            "coords": [[0.400901, -78.1753736], [0.4010165, -78.1749582], [0.4009201, -78.1749314], [0.4008046, -78.1753468]],
            "centroid": [0.4009106, -78.1751525],
            "area": 531.4,
            "color": "#27ae60", "fill": "#2ecc71",
            "interior": False,
            "is_perimeter": False,
            "desc": "Bloque residencial longitudinal patrimonial (Casa T 11) de 4 departamentos/módulos con 3 tabiques divisorios transversales internos."
        },
        {
            "id": "RECT-T-12",
            "nombre": "Casa Patrimonial Las T's 12",
            "tipo": "Residencia Estudiantil Patrimonial (Casa T - Módulo Cuádruple)",
            "zona": "Las T's y Multis",
            "coords": [[0.4007697, -78.1758188], [0.4008887, -78.1754085], [0.4007908, -78.1753801], [0.4006718, -78.1757904]],
            "centroid": [0.4007803, -78.1755995],
            "area": 536.4,
            "color": "#27ae60", "fill": "#2ecc71",
            "interior": False,
            "is_perimeter": False,
            "desc": "Bloque residencial longitudinal patrimonial (Casa T 12) de 4 departamentos/módulos con 3 tabiques divisorios transversales internos."
        },
        {
            "id": "RECT-T-13",
            "nombre": "Casa Patrimonial Las T's 13",
            "tipo": "Residencia Estudiantil Patrimonial (Casa T)",
            "zona": "Las T's y Multis",
            "coords": [[0.4009273, -78.1757779], [0.4008294, -78.1757511], [0.4007714, -78.1759632], [0.4008693, -78.17599]],
            "centroid": [0.4008493, -78.1758705],
            "area": 275.0,
            "color": "#27ae60", "fill": "#2ecc71",
            "interior": False,
            "is_perimeter": False,
            "desc": "Módulo residencial patrimonial tipo T (Casa T 13, extremo oeste). Sistema constructivo histórico restaurado con tabique divisorio interior."
        },
        {
            "id": "RECT-MULTI-01",
            "nombre": "Bloque Multifamiliar Las Multis 1",
            "tipo": "Residencia Estudiantil Multifamiliar (Escalonada)",
            "zona": "Sector Las Multis",
            "coords": [[0.402326, -78.1749139], [0.402203, -78.1745572], [0.4018942, -78.1746752], [0.4019311, -78.1747802], [0.4021091, -78.1747272], [0.4021936, -78.1749595]],
            "centroid": [0.4021405, -78.174741],
            "area": 936.1,
            "color": "#16a085", "fill": "#1abc9c",
            "interior": False,
            "is_perimeter": False,
            "desc": "Bloque residencial multifamiliar escalonado con tabique de división interior."
        },
        {
            "id": "RECT-MULTI-02",
            "nombre": "Bloque Multifamiliar Las Multis 2",
            "tipo": "Residencia Estudiantil Multifamiliar (Escalonada)",
            "zona": "Sector Las Multis",
            "coords": [[0.40185, -78.1746799], [0.4017048, -78.1747389], [0.4018278, -78.1750879], [0.4021453, -78.17498], [0.4021031, -78.1748657], [0.4019385, -78.174919]],
            "centroid": [0.4018943, -78.1749032],
            "area": 1004.3,
            "color": "#16a085", "fill": "#1abc9c",
            "interior": False,
            "is_perimeter": False,
            "desc": "Bloque residencial multifamiliar escalonado con partición divisoria interna."
        },
        {
            "id": "RECT-MULTI-03",
            "nombre": "Bloque Multifamiliar Las Multis 3",
            "tipo": "Residencia Estudiantil Multifamiliar",
            "zona": "Sector Las Multis",
            "coords": [[0.4023441, -78.1747352], [0.4023891, -78.1748526], [0.4026945, -78.1747476], [0.4026539, -78.1746189]],
            "centroid": [0.4025221, -78.1747377],
            "area": 527.7,
            "color": "#16a085", "fill": "#1abc9c",
            "interior": False,
            "is_perimeter": False,
            "desc": "Bloque residencial multifamiliar en el cuadrante noreste de Las Multis."
        },
        {
            "id": "RECT-MULTI-04",
            "nombre": "Bloque Multifamiliar Las Multis 4",
            "tipo": "Residencia Estudiantil Multifamiliar",
            "zona": "Sector Las Multis",
            "coords": [[0.4024762, -78.1749807], [0.402784, -78.174872], [0.4028293, -78.1749937], [0.4025165, -78.175103]],
            "centroid": [0.4026518, -78.1749874],
            "area": 526.9,
            "color": "#16a085", "fill": "#1abc9c",
            "interior": False,
            "is_perimeter": False,
            "desc": "Bloque residencial multifamiliar en el cuadrante norte de Las Multis."
        },
        {
            "id": "RECT-MULTI-05",
            "nombre": "Bloque Multifamiliar Las Multis 5",
            "tipo": "Residencia Estudiantil Multifamiliar",
            "zona": "Sector Las Multis",
            "coords": [[0.4027056, -78.1752355], [0.4027461, -78.1753495], [0.4024638, -78.1754443], [0.4024323, -78.1753364]],
            "centroid": [0.4025888, -78.175341],
            "area": 425.6,
            "color": "#16a085", "fill": "#1abc9c",
            "interior": False,
            "is_perimeter": False,
            "desc": "Bloque residencial multifamiliar central en Las Multis."
        },
        {
            "id": "RECT-MULTI-06",
            "nombre": "Bloque Multifamiliar Las Multis 6",
            "tipo": "Residencia Estudiantil Multifamiliar",
            "zona": "Sector Las Multis",
            "coords": [[0.4023572, -78.1753669], [0.4024229, -78.1754702], [0.4021778, -78.1756271], [0.4021209, -78.1755339]],
            "centroid": [0.402272, -78.175498],
            "area": 416.1,
            "color": "#16a085", "fill": "#1abc9c",
            "interior": False,
            "is_perimeter": False,
            "desc": "Bloque residencial multifamiliar orientado al suroeste."
        },
        {
            "id": "RECT-MULTI-07",
            "nombre": "Bloque Multifamiliar Las Multis 7",
            "tipo": "Residencia Estudiantil Multifamiliar",
            "zona": "Sector Las Multis",
            "coords": [[0.4019338, -78.1758794], [0.4018517, -78.1757889], [0.4020759, -78.1755855], [0.402158, -78.175676]],
            "centroid": [0.4020048, -78.1757324],
            "area": 458.3,
            "color": "#16a085", "fill": "#1abc9c",
            "interior": False,
            "is_perimeter": False,
            "desc": "Bloque residencial multifamiliar en el sector suroeste de Las Multis."
        },
        {
            "id": "RECT-MULTI-08",
            "nombre": "Bloque Multifamiliar Las Multis 8",
            "tipo": "Residencia Estudiantil Multifamiliar",
            "zona": "Sector Las Multis",
            "coords": [[0.4018174, -78.1758313], [0.4015988, -78.1760321], [0.4016753, -78.1761176], [0.4018888, -78.1759271]],
            "centroid": [0.4017455, -78.1759762],
            "area": 422.0,
            "color": "#16a085", "fill": "#1abc9c",
            "interior": False,
            "is_perimeter": False,
            "desc": "Bloque residencial multifamiliar en el sector suroeste de Las Multis."
        },
        {
            "id": "RECT-MULTI-09",
            "nombre": "Bloque Multifamiliar Las Multis 9",
            "tipo": "Residencia Estudiantil Multifamiliar",
            "zona": "Sector Las Multis",
            "coords": [[0.4016364, -78.1761706], [0.4015532, -78.17608], [0.4013471, -78.1763006], [0.4014339, -78.1763778]],
            "centroid": [0.4014933, -78.176231],
            "area": 437.7,
            "color": "#16a085", "fill": "#1abc9c",
            "interior": False,
            "is_perimeter": False,
            "desc": "Bloque residencial multifamiliar en el extremo sur de Las Multis."
        },
        {
            "id": "RECT-MULTI-10",
            "nombre": "Bloque Multifamiliar Las Multis 10",
            "tipo": "Residencia Estudiantil Multifamiliar",
            "zona": "Sector Las Multis",
            "coords": [[0.4013873, -78.1764358], [0.4013031, -78.1763543], [0.4011053, -78.1765685], [0.4011861, -78.1766446]],
            "centroid": [0.4012463, -78.1764998],
            "area": 411.0,
            "color": "#16a085", "fill": "#1abc9c",
            "interior": False,
            "is_perimeter": False,
            "desc": "Bloque residencial multifamiliar en el extremo sur de Las Multis."
        },
        {
            "id": "RECT-MULTI-11",
            "nombre": "Bloque Multifamiliar Las Multis 11",
            "tipo": "Residencia Estudiantil Multifamiliar",
            "zona": "Sector Las Multis",
            "coords": [[0.401374, -78.175511], [0.401561, -78.175288], [0.401673, -78.175372], [0.401460, -78.175584]],
            "centroid": [0.4015207, -78.1754351],
            "area": 460.1,
            "color": "#16a085", "fill": "#1abc9c",
            "interior": False,
            "is_perimeter": False,
            "desc": "Bloque residencial multifamiliar estudiantil en el flanco este de Las Multis, próximo al canal sur."
        },
        {
            "id": "RECT-MULTI-12",
            "nombre": "Bloque Multifamiliar Las Multis 12",
            "tipo": "Residencia Estudiantil Multifamiliar",
            "zona": "Sector Las Multis",
            "coords": [[0.401332, -78.175933], [0.401540, -78.175720], [0.401436, -78.175639], [0.401249, -78.175855]],
            "centroid": [0.4013919, -78.1757845],
            "area": 441.8,
            "color": "#16a085", "fill": "#1abc9c",
            "interior": False,
            "is_perimeter": False,
            "desc": "Bloque residencial multifamiliar estudiantil en el sector central-sur de Las Multis."
        },
        {
            "id": "RECT-MULTI-13",
            "nombre": "Bloque Multifamiliar Las Multis 13",
            "tipo": "Residencia Estudiantil Multifamiliar",
            "zona": "Sector Las Multis",
            "coords": [[0.401300, -78.175989], [0.401120, -78.176199], [0.401196, -78.176276], [0.401403, -78.176064]],
            "centroid": [0.4012578, -78.1761296],
            "area": 415.1,
            "color": "#16a085", "fill": "#1abc9c",
            "interior": False,
            "is_perimeter": False,
            "desc": "Bloque residencial multifamiliar estudiantil en el flanco suroeste de Las Multis."
        },
        {
            "id": "RECT-MULTI-NORES",
            "nombre": "Edificio Técnico y de Servicios Las Multis",
            "tipo": "Edificio de Servicios / Soporte Técnico",
            "zona": "Sector Las Multis",
            "coords": [[0.4016072, -78.175048], [0.4015167, -78.1750779], [0.4014777, -78.1749597], [0.4015682, -78.1749298]],
            "centroid": [0.4015424, -78.1750039],
            "area": 147.0,
            "color": "#7f8c8d", "fill": "#bdc3c7",
            "interior": False,
            "is_perimeter": False,
            "desc": "Edificación no residencial de apoyo técnico y logístico en Las Multis."
        },
        {
            "id": "RECT-MULTI-CANCHA",
            "nombre": "Cancha Deportiva Las Multis",
            "tipo": "Instalación Deportiva y Recreativa",
            "zona": "Sector Las Multis",
            "coords": [[0.4025336, -78.1744405], [0.4025305, -78.1746075], [0.4023046, -78.1746098], [0.4023086, -78.1744442]],
            "centroid": [0.4024195, -78.1745256],
            "area": 464.5,
            "color": "#27ae60", "fill": "#2ecc71",
            "interior": False,
            "is_perimeter": False,
            "desc": "Cancha deportiva multifuncional de uso estudiantil en Las Multis."
        },
        {
            "id": "RECT-MULTI-TIENDA",
            "nombre": "Tienda / Minimarket Las Multis",
            "tipo": "Comercio Interior en Residencia",
            "zona": "Sector Las Multis",
            "coords": [[0.4015656, -78.1752884], [0.4015418, -78.1753156], [0.4015767, -78.1753438], [0.4016069, -78.1753119]],
            "centroid": [0.4015734, -78.1753152],
            "area": 22.6,
            "color": "#d35400", "fill": "#e67e22",
            "interior": True,
            "is_perimeter": False,
            "desc": "Tienda y bazar de víveres que comparte la planta baja con el bloque residencial."
        },
        {
            "id": "RECT-COMEDOR-PERCI",
            "nombre": "Restaurante Comedor doña Perci",
            "tipo": "Servicio de Alimentación / Gastronomía",
            "zona": "Sector Reservorio Este",
            "coords": [[0.40456, -78.1685081], [0.4046152, -78.1684733], [0.4046456, -78.1685216], [0.4045904, -78.1685564]],
            "centroid": [0.4046028, -78.1685148],
            "area": 46.2,
            "color": "#e67e22", "fill": "#f39c12",
            "interior": False,
            "is_perimeter": False,
            "desc": "Comedor tradicional en inmediaciones del reservorio este. Afluencia reducida/esporádica (~20-30 clientes/día) por su ubicación periférica."
        },
        {
            "id": "RECT-SACHA-HOME",
            "nombre": "Habitaciones Privadas Sacha Home (Sin Convenio)",
            "tipo": "Alojamiento Privado Externo (Sin Convenio)",
            "zona": "Sector Reservorio Este (Externo)",
            "coords": [[0.4046659, -78.1684636], [0.4044948, -78.168285], [0.4045398, -78.1682419], [0.4047109, -78.1684205]],
            "centroid": [0.4046028, -78.1683528],
            "area": 191.0,
            "color": "#16a085", "fill": "#1abc9c",
            "interior": False,
            "is_perimeter": False,
            "desc": "Inmueble privado de habitaciones individuales (8 habitaciones distribuidas en 2 pisos) sin convenio con la universidad, ubicadas en las inmediaciones del límite este del campus."
        },
        {
            "id": "RECT-PATS-01",
            "nombre": "Residencia Patrimonial Las Pats 1",
            "tipo": "Residencia Estudiantil Patrimonial",
            "zona": "Sector Las Pats",
            "coords": [[0.40147, -78.1732153], [0.4013916, -78.1731671], [0.4015606, -78.1728926], [0.401639, -78.1729409]],
            "centroid": [0.4015153, -78.173054],
            "area": 367.8,
            "color": "#27ae60", "fill": "#2ecc71",
            "interior": False,
            "is_perimeter": False,
            "desc": "Bloque residencial estudiantil patrimonial de arquitectura tradicional con 2 tabiques divisorios."
        },
        {
            "id": "RECT-PATS-02",
            "nombre": "Residencia Patrimonial Las Pats 2",
            "tipo": "Residencia Estudiantil Patrimonial",
            "zona": "Sector Las Pats",
            "coords": [[0.4011861, -78.1734779], [0.4013688, -78.1732024], [0.4014493, -78.1732558], [0.4012666, -78.1735313]],
            "centroid": [0.4013177, -78.1733669],
            "area": 395.8,
            "color": "#27ae60", "fill": "#2ecc71",
            "interior": False,
            "is_perimeter": False,
            "desc": "Bloque residencial estudiantil patrimonial de arquitectura tradicional con 2 tabiques divisorios."
        },
        {
            "id": "RECT-PATS-03",
            "nombre": "Residencia Patrimonial Las Pats 3",
            "tipo": "Residencia Estudiantil Patrimonial",
            "zona": "Sector Las Pats",
            "coords": [[0.401227, -78.1735933], [0.4013045, -78.173549], [0.4015137, -78.173915], [0.4014362, -78.1739593]],
            "centroid": [0.4013703, -78.1737541],
            "area": 466.3,
            "color": "#27ae60", "fill": "#2ecc71",
            "interior": False,
            "is_perimeter": False,
            "desc": "Bloque residencial estudiantil patrimonial con 3 divisiones interiores modulares."
        },
        {
            "id": "RECT-PATS-04",
            "nombre": "Residencia Patrimonial Las Pats 4",
            "tipo": "Residencia Estudiantil Patrimonial",
            "zona": "Sector Las Pats",
            "coords": [[0.4017578, -78.1745351], [0.4014684, -78.1740073], [0.4015458, -78.1739649], [0.4018352, -78.1744927]],
            "centroid": [0.4016518, -78.17425],
            "area": 658.0,
            "color": "#27ae60", "fill": "#2ecc71",
            "interior": False,
            "is_perimeter": False,
            "desc": "Bloque residencial estudiantil patrimonial con 5 tabiques divisorios transversales."
        },
        {
            "id": "RECT-PATS-05",
            "nombre": "Residencia Patrimonial Las Pats 5",
            "tipo": "Residencia Estudiantil Patrimonial",
            "zona": "Sector Las Pats",
            "coords": [[0.4025027, -78.1742363], [0.4017966, -78.174643], [0.4017533, -78.1745678], [0.4024594, -78.1741611]],
            "centroid": [0.402128, -78.1744021],
            "area": 876.0,
            "color": "#27ae60", "fill": "#2ecc71",
            "interior": False,
            "is_perimeter": False,
            "desc": "Bloque longitudinal patrimonial de 8 módulos con 7 tabiques divisorios transversales."
        },
        {
            "id": "RECT-PATS-06",
            "nombre": "Residencia Patrimonial Las Pats 6",
            "tipo": "Residencia Estudiantil Patrimonial",
            "zona": "Sector Las Pats",
            "coords": [[0.4023284, -78.1737619], [0.4025212, -78.174114], [0.4024424, -78.1741571], [0.4022496, -78.173805]],
            "centroid": [0.4023854, -78.1739595],
            "area": 446.7,
            "color": "#27ae60", "fill": "#2ecc71",
            "interior": False,
            "is_perimeter": False,
            "desc": "Bloque residencial estudiantil patrimonial con 3 tabiques divisorios transversales."
        },
        {
            "id": "RECT-PATS-07",
            "nombre": "Residencia Patrimonial Las Pats 7",
            "tipo": "Residencia Estudiantil Patrimonial",
            "zona": "Sector Las Pats",
            "coords": [[0.4020997, -78.1733646], [0.4022975, -78.173715], [0.4022201, -78.1737587], [0.4020223, -78.1734083]],
            "centroid": [0.4021599, -78.1735616],
            "area": 443.1,
            "color": "#27ae60", "fill": "#2ecc71",
            "interior": False,
            "is_perimeter": False,
            "desc": "Bloque residencial estudiantil patrimonial con 3 tabiques divisorios transversales."
        },
        {
            "id": "RECT-PATS-08",
            "nombre": "Residencia Patrimonial Las Pats 8",
            "tipo": "Residencia Estudiantil Patrimonial",
            "zona": "Sector Las Pats",
            "coords": [[0.4025969, -78.1740908], [0.4031024, -78.1750656], [0.4030231, -78.1751067], [0.4025176, -78.1741319]],
            "centroid": [0.40281, -78.1745988],
            "area": 1215.0,
            "color": "#27ae60", "fill": "#2ecc71",
            "interior": False,
            "is_perimeter": False,
            "desc": "Bloque longitudinal patrimonial superior de 11 módulos con 10 tabiques divisorios transversales."
        },
        {
            "id": "RECT-PATS-09",
            "nombre": "Residencia Patrimonial Las Pats 9",
            "tipo": "Residencia Estudiantil Patrimonial",
            "zona": "Sector Las Pats",
            "coords": [[0.401931, -78.173188], [0.401974, -78.173282], [0.401686, -78.173438], [0.401646, -78.173357]],
            "centroid": [0.4018124, -78.1733144],
            "area": 393.1,
            "color": "#27ae60", "fill": "#2ecc71",
            "interior": False,
            "is_perimeter": False,
            "desc": "Bloque residencial estudiantil patrimonial de 3 módulos habitacionales con 2 tabiques divisorios transversales."
        },
        {
            "id": "RECT-PATS-LAB",
            "nombre": "Laboratorio de Campo Las Pats",
            "tipo": "Laboratorio / Investigación Científica",
            "zona": "Sector Las Pats",
            "coords": [[0.4017122, -78.1745652], [0.4016589, -78.1745934], [0.401565, -78.174416], [0.4016183, -78.1743878]],
            "centroid": [0.4016386, -78.1744906],
            "area": 150.0,
            "color": "#2980b9", "fill": "#3498db",
            "interior": False,
            "is_perimeter": False,
            "desc": "Edificación no residencial destinada a ensayos biológicos y laboratorio de campo en Las Pats."
        },
        {
            "id": "RECT-PATS-TICS",
            "nombre": "Edificio TICs y Conectividad Las Pats",
            "tipo": "Tecnología / Soporte y Telecomunicaciones",
            "zona": "Sector Las Pats",
            "coords": [[0.4030727, -78.1752435], [0.4029439, -78.1752928], [0.40291, -78.1752042], [0.4030388, -78.1751549]],
            "centroid": [0.4029913, -78.1752238],
            "area": 162.1,
            "color": "#8e44ad", "fill": "#9b59b6",
            "interior": False,
            "is_perimeter": False,
            "desc": "Centro de distribución de datos, telecomunicaciones y soporte informático en Las Pats."
        },
        {
            "id": "RECT-PATS-DOCENTES",
            "nombre": "Villas Residenciales de Docentes",
            "tipo": "Residencia de Docentes e Investigadores",
            "zona": "Sector Las Pats",
            "coords": [[0.4029138, -78.1752754], [0.4029413, -78.1753629], [0.4028382, -78.1753953], [0.4028107, -78.1753078]],
            "centroid": [0.402876, -78.1753353],
            "area": 122.8,
            "color": "#34495e", "fill": "#5d6d7e",
            "interior": False,
            "is_perimeter": False,
            "desc": "Complejo habitacional asignado a personal docente e investigadores visitantes en Las Pats."
        },
        # =============================================================
        # SECTOR SALA CAPITULAR, SAN JOSÉ Y SERVICIOS
        # =============================================================
        {
            "id": "RECT-CAPITULAR-CLAUSTRO",
            "nombre": "Claustro y Galerías Sala Capitular",
            "tipo": "Patrimonio / Claustro Colonial",
            "zona": "Sector San José - Sala Capitular",
            "coords": [
                [0.404240, -78.175332],
                [0.40420902103464523, -78.17559009943265],
                [0.4045625167016313, -78.17563580351128],
                [0.40457700555425363, -78.17552026853677],
                [0.4045318176805893, -78.17551204248113],
                [0.4045468941577039, -78.17536179998498],
                [0.40444834700931, -78.17535273674106],
                [0.4044267281680122, -78.17549822469832],
                [0.4043353137421178, -78.1754867983086],
                [0.40434880702301934, -78.17534002693716]
            ],
            "centroid": [0.4043897, -78.175497],
            "area": 906.9,
            "color": "#6c5ce7", "fill": "#a29bfe",
            "interior": False, "is_perimeter": False,
            "desc": "Edificio claustral y galerías perimetrales en U en el sector patrimonial Sala Capitular."
        },
        {
            "id": "POLY-EDIF-ANEXO-CAPITULAR",
            "nombre": "Edificio Anexo Sala Capitular",
            "tipo": "Patrimonio / Edificación Administrativa",
            "zona": "Sector San José - Sala Capitular",
            "coords": [
                [0.4045396964142846, -78.17526107572444],
                [0.4045260050582979, -78.17534611107887],
                [0.404609840980748, -78.175361761138],
                [0.4046150036913649, -78.1753101170312],
                [0.40463355988830263, -78.1753144049758],
                [0.40463849313901573, -78.17527830353698],
                [0.40461558547259185, -78.17527400021251],
                [0.40462666073768727, -78.17522577523509],
                [0.4046123362828976, -78.17521994200987],
                [0.40461150996838957, -78.17519041498646],
                [0.40447122857397105, -78.1751837268196],
                [0.4044622953106167, -78.17525119795917]
            ],
            "centroid": [0.4045586, -78.1752602],
            "area": 238.3,
            "color": "#6c5ce7", "fill": "#a29bfe",
            "interior": False, "is_perimeter": False,
            "desc": "Edificación anexa en el sector de la Sala Capitular, contigua al canal y área de parada."
        },
        {
            "id": "RECT-EDIF-20",
            "nombre": "Edificio 20 (San José)",
            "tipo": "Infraestructura y Servicios San José",
            "zona": "Sector San José",
            "coords": [
                [0.4042613018403834, -78.1760998960864],
                [0.4043092936161369, -78.17608846041709],
                [0.40434474337116183, -78.17620740414793],
                [0.40430115536149835, -78.17622010330457]
            ],
            "centroid": [0.4043038, -78.1761532],
            "area": 73.0,
            "color": "#4a69bd", "fill": "#6a89cc",
            "interior": False, "is_perimeter": False,
            "desc": "Edificio modular de soporte técnico y oficinas de servicios en el sector San José."
        },
        # =============================================================
        # COMPLEJO DEPORTIVO SUR (CANCHAS REGLAMENTARIAS)
        # =============================================================
        {
            "id": "RECT-CANCHA-VOLLEY",
            "nombre": "Cancha de Volley Playa (Arena)",
            "tipo": "Deporte y Recreación / Cancha de Arena",
            "zona": "Complejo Deportivo Sur",
            "coords": [
                [0.4025861600605359, -78.17299007290745],
                [0.4025842300089088, -78.17286166687853],
                [0.40235194000536745, -78.17285994863846],
                [0.40233825911290455, -78.17299975708694]
            ],
            "centroid": [0.4024635, -78.1729286],
            "area": 396.4,
            "color": "#e67e22", "fill": "#f39c12",
            "interior": False, "is_perimeter": False,
            "desc": "Cancha reglamentaria con superficie de arena para voleibol de playa y acondicionamiento físico."
        },
        {
            "id": "RECT-CANCHA-BASKET-1",
            "nombre": "Cancha de Basketball 1",
            "tipo": "Deporte y Recreación / Cancha de Baloncesto",
            "zona": "Complejo Deportivo Sur",
            "coords": [
                [0.40228557017200245, -78.17262017830531],
                [0.4022828888612006, -78.17279072890534],
                [0.40257329585712437, -78.17278597294019],
                [0.40256714258832177, -78.17261542483678]
            ],
            "centroid": [0.4024272, -78.1727035],
            "area": 601.0,
            "color": "#d35400", "fill": "#e67e22",
            "interior": False, "is_perimeter": False,
            "desc": "Cancha polideportiva pavimentada para básquetbol y actividades formativas (Cancha 1)."
        },
        {
            "id": "RECT-CANCHA-BASKET-2",
            "nombre": "Cancha de Basketball 2",
            "tipo": "Deporte y Recreación / Cancha de Baloncesto",
            "zona": "Complejo Deportivo Sur",
            "coords": [
                [0.4023890144287728, -78.17229870730031],
                [0.4023920568119697, -78.1724493204527],
                [0.40266729410813257, -78.17244629640133],
                [0.4026652204280081, -78.17229713258551]
            ],
            "centroid": [0.4025282, -78.1723728],
            "area": 509.2,
            "color": "#d35400", "fill": "#e67e22",
            "interior": False, "is_perimeter": False,
            "desc": "Cancha polideportiva pavimentada para básquetbol central (Cancha 2)."
        },
        {
            "id": "RECT-CANCHA-BASKET-3",
            "nombre": "Cancha de Basketball 3",
            "tipo": "Deporte y Recreación / Cancha de Baloncesto",
            "zona": "Complejo Deportivo Sur",
            "coords": [
                [0.4027909097980843, -78.17206146245567],
                [0.40279148333782916, -78.17220993324644],
                [0.4025168444205669, -78.17221321915268],
                [0.4025181243070779, -78.17206312374493]
            ],
            "centroid": [0.4026541, -78.172137],
            "area": 503.3,
            "color": "#d35400", "fill": "#e67e22",
            "interior": False, "is_perimeter": False,
            "desc": "Cancha polideportiva pavimentada para básquetbol norte (Cancha 3)."
        },
        {
            "id": "RECT-CANCHA-FUTBOL-1",
            "nombre": "Cancha de Fútbol Sintética 1 (Cercada)",
            "tipo": "Deporte y Recreación / Fútbol Sintético",
            "zona": "Complejo Deportivo Sur",
            "coords": [
                [0.40209252598424083, -78.17236796565483],
                [0.40208233822360445, -78.17260800363452],
                [0.40165628949352405, -78.17260779323227],
                [0.4016526038666191, -78.17237240586813]
            ],
            "centroid": [0.4018716, -78.1724884],
            "area": 1267.9,
            "color": "#27ae60", "fill": "#2ecc71",
            "interior": False, "is_perimeter": False,
            "desc": "Cancha reglamentaria de césped sintético cercada con malla perimetral lateral para fútbol (Cancha 1)."
        },
        {
            "id": "RECT-CANCHA-FUTBOL-2",
            "nombre": "Cancha de Fútbol Sintética 2 (Cercada)",
            "tipo": "Deporte y Recreación / Fútbol Sintético",
            "zona": "Complejo Deportivo Sur",
            "coords": [
                [0.40223108513129635, -78.17230336934185],
                [0.40222409652123897, -78.172062332801],
                [0.40181875311686155, -78.1720683136697],
                [0.401816173567501, -78.17229743361754]
            ],
            "centroid": [0.4020243, -78.1721833],
            "area": 1187.7,
            "color": "#27ae60", "fill": "#2ecc71",
            "interior": False, "is_perimeter": False,
            "desc": "Cancha reglamentaria de césped sintético cercada con malla de tela lateral para fútbol (Cancha 2)."
        },
        {
            "id": "RECT-CANCHA-FUTBOL-3",
            "nombre": "Cancha de Fútbol Sintética 3 (Cercada)",
            "tipo": "Deporte y Recreación / Fútbol Sintético",
            "zona": "Complejo Deportivo Sur",
            "coords": [
                [0.40195721709224796, -78.17197007418827],
                [0.40196081391685234, -78.17179118686657],
                [0.40226137989635063, -78.17178857753838],
                [0.40226750026629277, -78.1719670839912]
            ],
            "centroid": [0.4021117, -78.1718797],
            "area": 672.4,
            "color": "#27ae60", "fill": "#2ecc71",
            "interior": False, "is_perimeter": False,
            "desc": "Cancha de fútbol con césped sintético y cerramiento perimetral este (Cancha 3)."
        },
        # =============================================================
        # SECTOR RESIDENCIAS DE DOCENTES
        # =============================================================
        {
            "id": "RECT-DOCENTES-01",
            "nombre": "Residencia de Docentes 1 (Villa Principal)",
            "tipo": "Residencia de Docentes e Investigadores",
            "zona": "Sector Residencias Docentes",
            "coords": [
                [0.4029675544664514, -78.1757290860798],
                [0.403452951226866, -78.1755941846592],
                [0.4034219996664258, -78.17550799582311],
                [0.403346240240605, -78.1755276638781],
                [0.403326756837941, -78.17545328677666],
                [0.4032590031300809, -78.1754745150326],
                [0.4032845330165297, -78.17554451818032],
                [0.40293582357967284, -78.17563840721435]
            ],
            "centroid": [0.4032036, -78.1756063],
            "area": 644.7,
            "color": "#2980b9", "fill": "#3498db",
            "interior": False, "is_perimeter": False,
            "desc": "Villa docente longitudinal de 8 vértices en el ala suroriental del barrio residencial de profesores."
        },
        {
            "id": "RECT-DOCENTES-02",
            "nombre": "Residencia de Docentes 2",
            "tipo": "Residencia de Docentes e Investigadores",
            "zona": "Sector Residencias Docentes",
            "coords": [
                [0.4035058418082375, -78.17557991761626],
                [0.40368979868839344, -78.17553113679166],
                [0.4036587904803255, -78.17543803362949],
                [0.40348043378653464, -78.17548726709248]
            ],
            "centroid": [0.4035841, -78.1755092],
            "area": 224.3,
            "color": "#2980b9", "fill": "#3498db",
            "interior": False, "is_perimeter": False,
            "desc": "Vivienda unifamiliar docente ubicada en el sendero interior del barrio de profesores."
        },
        {
            "id": "RECT-DOCENTES-03",
            "nombre": "Residencia de Docentes 3",
            "tipo": "Residencia de Docentes e Investigadores",
            "zona": "Sector Residencias Docentes",
            "coords": [
                [0.4037476411895457, -78.1755252375428],
                [0.4038818212547698, -78.17549032201262],
                [0.4038545128083486, -78.17539282014432],
                [0.40372073591745794, -78.17542534823382]
            ],
            "centroid": [0.403801, -78.1754586],
            "area": 174.2,
            "color": "#2980b9", "fill": "#3498db",
            "interior": False, "is_perimeter": False,
            "desc": "Vivienda docente en el sector nororiental de villas universitarias."
        },
        {
            "id": "RECT-DOCENTES-04",
            "nombre": "Residencia de Docentes 4",
            "tipo": "Residencia de Docentes e Investigadores",
            "zona": "Sector Residencias Docentes",
            "coords": [
                [0.4037532394194796, -78.1755999134971],
                [0.40377127893214637, -78.1756951934876],
                [0.40391611473941935, -78.17566177330714],
                [0.4038948400052535, -78.17557179127812]
            ],
            "centroid": [0.4038333, -78.1756325],
            "area": 170.9,
            "color": "#2980b9", "fill": "#3498db",
            "interior": False, "is_perimeter": False,
            "desc": "Villa docente norte contigua al jardín botánico protegido."
        },
        {
            "id": "RECT-DOCENTES-05",
            "nombre": "Residencia de Docentes 5",
            "tipo": "Residencia de Docentes e Investigadores",
            "zona": "Sector Residencias Docentes",
            "coords": [
                [0.40358234289246236, -78.17564059729222],
                [0.40360440058953484, -78.17572338828448],
                [0.4037156117408911, -78.1756997583329],
                [0.40370142023332534, -78.17561677651535]
            ],
            "centroid": [0.4036507, -78.1756697],
            "area": 122.9,
            "color": "#2980b9", "fill": "#3498db",
            "interior": False, "is_perimeter": False,
            "desc": "Villa docente compacta en el corredor peatonal central de profesores."
        },
        {
            "id": "RECT-DOCENTES-NORES",
            "nombre": "Edificio Comunitario / No Residencial (Docentes)",
            "tipo": "Equipamiento Comunitario y Servicios",
            "zona": "Sector Residencias Docentes",
            "coords": [
                [0.40324304597535526, -78.1759031942055],
                [0.4035214193391899, -78.17584776761707],
                [0.40351696828514927, -78.17579067461945],
                [0.40323308002676506, -78.17583935576278]
            ],
            "centroid": [0.4033757, -78.1758457],
            "area": 214.0,
            "color": "#16a085", "fill": "#1abc9c",
            "interior": False, "is_perimeter": False,
            "desc": "Edificio no residencial de administración comunitaria, bodegas y salas de reunión para docentes."
        },
        {
            "id": "RECT-DOCENTES-06",
            "nombre": "Residencia de Docentes 6",
            "tipo": "Residencia de Docentes e Investigadores",
            "zona": "Sector Residencias Docentes",
            "coords": [
                [0.40387879399406623, -78.17587575557651],
                [0.40405620634993067, -78.1758250209943],
                [0.40402705150552726, -78.17573525220743],
                [0.4038527651904324, -78.17578665461019]
            ],
            "centroid": [0.403954, -78.1758057],
            "area": 211.1,
            "color": "#2980b9", "fill": "#3498db",
            "interior": False, "is_perimeter": False,
            "desc": "Villa docente noroccidental con vista a la arboleda patrimonial."
        },
        {
            "id": "RECT-DOCENTES-07",
            "nombre": "Residencia de Docentes 7",
            "tipo": "Residencia de Docentes e Investigadores",
            "zona": "Sector Residencias Docentes",
            "coords": [
                [0.40399083308609157, -78.17593886434996],
                [0.40400638670525724, -78.17601900690731],
                [0.403706932409291, -78.17610106077338],
                [0.40368862851209686, -78.17602027664064]
            ],
            "centroid": [0.4038478, -78.1760199],
            "area": 315.2,
            "color": "#2980b9", "fill": "#3498db",
            "interior": False, "is_perimeter": False,
            "desc": "Villa docente amplia situada en el límite oeste de las residencias de profesores."
        },
        {
            "id": "RECT-DOCENTES-08",
            "nombre": "Residencia de Docentes 8 (Bifamiliar)",
            "tipo": "Residencia de Docentes e Investigadores",
            "zona": "Sector Residencias Docentes",
            "coords": [
                [0.4034709211178097, -78.17616348286064],
                [0.4036378625066064, -78.17611892659224],
                [0.40362256650572353, -78.17605104552078],
                [0.4034521176605463, -78.17609436336367]
            ],
            "centroid": [0.4035454, -78.176107],
            "area": 151.6,
            "color": "#2980b9", "fill": "#3498db",
            "interior": False, "is_perimeter": False,
            "desc": "Residencia docente bifamiliar dotada de tabique transversal divisorio interior."
        },
        # =============================================================
        # EDIFICIOS VARIOS, GASTRONOMÍA Y SERVICIOS SAN JOSÉ
        # =============================================================
        {
            "id": "RECT-SALA-ESTAR",
            "nombre": "Sala de Estar (San José)",
            "tipo": "Área Social y Descanso (Cubierta / Ventanal Polarizado)",
            "zona": "Sector San José",
            "coords": [
                [0.40423891136109147, -78.17639429127263],
                [0.4042568967600418, -78.17643816181554],
                [0.4041600862575909, -78.17646787279462],
                [0.4041503670363246, -78.17641990720087]
            ],
            "centroid": [0.4042014, -78.1764305],
            "area": 57.1,
            "color": "#2c3e50", "fill": "#34495e",
            "interior": False, "is_perimeter": False,
            "desc": "Espacio cubierto para estancia y descanso estudiantil y docente, dotado de cubierta de techo y cerramiento perimetral de ventanales polarizados."
        },
        {
            "id": "INT-BANOS-ESTAR",
            "nombre": "Baños Sala de Estar (San José)",
            "tipo": "Servicios Sanitarios e Higiene (Módulo Interior)",
            "zona": "Sector San José",
            "coords": [
                [0.4042568967600418, -78.17643816181554],
                [0.4042514185740652, -78.17641695162406],
                [0.40421909904079517, -78.17642265098506],
                [0.4042358186948357, -78.17644524108512]
            ],
            "centroid": [0.4042401, -78.1764302],
            "area": 8.1,
            "color": "#16a085", "fill": "#1abc9c",
            "interior": True, "is_perimeter": False,
            "desc": "Módulo sanitario integrado en el sector norte de la Sala de Estar en el complejo San José."
        },
        {
            "id": "RECT-EDIF-38",
            "nombre": "Edificio 38 (San José)",
            "tipo": "Edificio Administrativo y Operativo",
            "zona": "Sector San José",
            "coords": [
                [0.404213301532898, -78.17668579084234],
                [0.40434474337116183, -78.17664338480479],
                [0.40430820746524393, -78.1765556598624],
                [0.4041867832892328, -78.17659284889407]
            ],
            "centroid": [0.4042631, -78.1766201],
            "area": 155.8,
            "color": "#34495e", "fill": "#7f8c8d",
            "interior": False, "is_perimeter": False,
            "desc": "Edificio administrativo y oficinas operativas en el patio gastronómico de San José."
        },
        {
            "id": "RECT-EDIF-39",
            "nombre": "Edificio 39 (San José)",
            "tipo": "Edificio de Servicios y Logística",
            "zona": "Sector San José",
            "coords": [
                [0.4039881695303205, -78.17657909628454],
                [0.40394774317195414, -78.17659349605131],
                [0.4039159568316363, -78.17648654219273],
                [0.4039650048518703, -78.17647615665793]
            ],
            "centroid": [0.4039536, -78.1765325],
            "area": 62.0,
            "color": "#34495e", "fill": "#7f8c8d",
            "interior": False, "is_perimeter": False,
            "desc": "Edificio auxiliar de bodega y almacenamiento técnico en San José sur."
        },
        {
            "id": "RECT-EDIF-40",
            "nombre": "Edificio 40 (San José)",
            "tipo": "Edificio Polivalente San José",
            "zona": "Sector San José",
            "coords": [
                [0.40417029791370934, -78.17668871013962],
                [0.40398480040210594, -78.17674116491273],
                [0.4039591650499329, -78.17662885123883],
                [0.4041368223423578, -78.17657692050491]
            ],
            "centroid": [0.4040631, -78.1766592],
            "area": 269.6,
            "color": "#34495e", "fill": "#7f8c8d",
            "interior": False, "is_perimeter": False,
            "desc": "Instalación polivalente de talleres y logística general en San José."
        },
        {
            "id": "RECT-EDIF-41",
            "nombre": "Edificio 41 (San José)",
            "tipo": "Complejo Edilicio Mayor San José",
            "zona": "Sector San José",
            "coords": [
                [0.404050227323438, -78.1767745594875],
                [0.4041059504735446, -78.17694830796492],
                [0.4043600323994754, -78.1768552994728],
                [0.40434376633858476, -78.17679090716022],
                [0.40439599086775, -78.17677676581192],
                [0.40444369217875803, -78.17690276029923],
                [0.4043033964471817, -78.17695548261383],
                [0.4043141870791176, -78.177001158758],
                [0.404280774987399, -78.17701357549211],
                [0.40427539839671817, -78.17698872299397],
                [0.40408248039094047, -78.17706267168654],
                [0.4039960670941696, -78.17678581728795]
            ],
            "centroid": [0.4042101, -78.1769226],
            "area": 610.8,
            "color": "#2c3e50", "fill": "#57606f",
            "interior": False, "is_perimeter": False,
            "desc": "Complejo arquitectónico escalonado de 12 vértices para laboratorios y talleres San José."
        },
        {
            "id": "RECT-REST-PATO-GOLOSO",
            "nombre": "Restaurante 'Pato Goloso' (Concurrido en las noches)",
            "tipo": "Gastronomía y Alimentación / Restaurante (Nocturno)",
            "zona": "Sector Gastronómico San José",
            "coords": [
                [0.4042956013511884, -78.17665611628786],
                [0.4042846843054159, -78.17661256146175],
                [0.404331228715073, -78.17660118513263],
                [0.4043448855288352, -78.17664481704243]
            ],
            "centroid": [0.4043142, -78.1766288],
            "area": 27.4,
            "color": "#d35400", "fill": "#e67e22",
            "interior": False, "is_perimeter": False,
            "desc": "Restaurante y cafetería universitaria tradicional 'Pato Goloso' en el patio gastronómico San José. Alta concurrencia en horario nocturno."
        },
        {
            "id": "RECT-REST-COMEDOR-ANALI",
            "nombre": "Restaurante 'Comedor Analí'",
            "tipo": "Gastronomía y Alimentación / Restaurante",
            "zona": "Sector Gastronómico San José",
            "coords": [
                [0.4042956013511884, -78.17665611628786],
                [0.4042846843054159, -78.17661256146175],
                [0.4042187098924085, -78.17663000363017],
                [0.40423812982681984, -78.176677545081]
            ],
            "centroid": [0.4042585, -78.1766439],
            "area": 38.3,
            "color": "#d35400", "fill": "#e67e22",
            "interior": False, "is_perimeter": False,
            "desc": "Comedor estudiantil y docente 'Analí' con servicio de almuerzos y mesas protegidas."
        },
        {
            "id": "RECT-BANOS-SANJOSE-1",
            "nombre": "Batería Sanitaria 1 (Sector Analí / Pato Goloso)",
            "tipo": "Servicios Sanitarios e Higiene",
            "zona": "Sector San José",
            "coords": [
                [0.4042187098924085, -78.17663000363017],
                [0.40423812982681984, -78.176677545081],
                [0.4042106691286265, -78.17668492325618],
                [0.4041981534608102, -78.17663813939762]
            ],
            "centroid": [0.4042169, -78.1766586],
            "area": 15.5,
            "color": "#7f8c8d", "fill": "#95a5a6",
            "interior": False, "is_perimeter": False,
            "desc": "Módulo de baños públicos y lavamanos junto al Comedor Analí y Pato Goloso."
        },
        {
            "id": "RECT-BANOS-SANJOSE-2",
            "nombre": "Batería Sanitaria 2 (Sector Sur San José)",
            "tipo": "Servicios Sanitarios e Higiene",
            "zona": "Sector San José",
            "coords": [
                [0.40397770829273366, -78.17669053334565],
                [0.4040335081217475, -78.17667322278062],
                [0.4040111203343552, -78.17660955551632],
                [0.40394965649017067, -78.17662843796816]
            ],
            "centroid": [0.4039928, -78.1766499],
            "area": 51.0,
            "color": "#7f8c8d", "fill": "#95a5a6",
            "interior": False, "is_perimeter": False,
            "desc": "Batería sanitaria de servicio público en el sector sur de talleres y oficinas San José."
        },
        {
            "id": "RECT-REST-INGENIO",
            "nombre": "Restaurante Patrimonial Plaza Ingenio",
            "tipo": "Gastronomía y Alimentación / Restaurante Patrimonial",
            "zona": "Ingenio",
            "coords": [
                [0.40497164971995137, -78.17449059422302],
                [0.4049389695943836, -78.17455568309286],
                [0.40476277701161273, -78.17446256966684],
                [0.4047912653573043, -78.17440493895086]
            ],
            "centroid": [0.404868, -78.1744794],
            "area": 168.3,
            "color": "#d35400", "fill": "#e67e22",
            "interior": False, "is_perimeter": False,
            "desc": "Establecimiento gastronómico tradicional ubicado en el flanco de la Plaza del Ingenio Azucarero."
        },
        {
            "id": "POLY-ABANDON-TECHO",
            "nombre": "Edificación Abandonada (Sin Techo)",
            "tipo": "Estructura Abandonada / Sin Cobertura",
            "zona": "Periferia Este",
            "coords": [
                [0.4055451275729653, -78.16916152255357],
                [0.40558123378924427, -78.16920179161598],
                [0.4056159597151692, -78.16916702300554],
                [0.4055825733687857, -78.16912945471526]
            ],
            "centroid": [0.405581, -78.1691651],
            "area": 31.6,
            "color": "#7f8c8d", "fill": "#95a5a6",
            "interior": False, "is_perimeter": False,
            "desc": "Estructura muraria antigua en ruinas y desprovista de cubierta de techo en la periferia este del campus."
        },
        {
            "id": "POLY-BARRIADA",
            "nombre": "Asentamiento Perimetral Barriada",
            "tipo": "Asentamiento Residencial Periférico",
            "zona": "Periferia Este",
            "coords": [
                [0.403416800675225, -78.16975950913621],
                [0.4033017886549784, -78.16987596542849],
                [0.40318353501394316, -78.16996936841555],
                [0.4031364550298862, -78.16992066140911],
                [0.4031239251155644, -78.1697504579221],
                [0.4031141663469189, -78.1696423080254],
                [0.40311687517375067, -78.16944922544191],
                [0.4031696420512379, -78.16944064273751],
                [0.40320304039785515, -78.16942229016715],
                [0.4034510338335197, -78.16932705956306],
                [0.403479290504302, -78.16939685733432],
                [0.4034087632991755, -78.16942535276313],
                [0.40344100688154433, -78.16948265262258],
                [0.40341423304313534, -78.16950516538711],
                [0.4034987173863257, -78.16965614342064]
            ],
            "centroid": [0.4032816, -78.1696338],
            "area": 1956.0,
            "color": "#b9770e", "fill": "#f5b041",
            "interior": False, "is_perimeter": True,
            "desc": "Sector habitacional y viviendas del asentamiento barrial en la periferia este del campus."
        },
        {
            "id": "POLY-EDIF-ITT-1",
            "nombre": "Edificio ITT (No en Uso) - Bloque Norte",
            "tipo": "Infraestructura Educativa Inconclusa / No en Uso",
            "zona": "Eje Tecnológico",
            "coords": [
                [0.40568742119572077, -78.17043643393573],
                [0.40577778324982705, -78.17053811999169],
                [0.40586489852537144, -78.1704741928856],
                [0.40609968508828403, -78.17076873212748],
                [0.4063098792007305, -78.17060367389932],
                [0.4059471837862516, -78.17020232873084]
            ],
            "centroid": [0.4060091, -78.1704836],
            "area": 1835.8,
            "color": "#7f8c8d", "fill": "#bdc3c7",
            "interior": False, "is_perimeter": False,
            "desc": "Bloque norte del Instituto Tecnológico Territorial (ITT), edificación de gran escala actualmente desocupada y no en uso."
        },
        {
            "id": "POLY-EDIF-ITT-2",
            "nombre": "Edificio ITT (No en Uso) - Bloque Sur",
            "tipo": "Infraestructura Educativa Inconclusa / No en Uso",
            "zona": "Eje Tecnológico",
            "coords": [
                [0.40564432486800545, -78.17065867740455],
                [0.4058919916215835, -78.17095544242314],
                [0.40569193733932163, -78.17111620230816],
                [0.4053582225741319, -78.17071015491132],
                [0.40564693557948556, -78.17046058095627],
                [0.4057528083127586, -78.17055970662256]
            ],
            "centroid": [0.4056269, -78.1707963],
            "area": 1909.7,
            "color": "#7f8c8d", "fill": "#bdc3c7",
            "interior": False, "is_perimeter": False,
            "desc": "Bloque sur del Instituto Tecnológico Territorial (ITT), edificación de gran volumen actualmente desocupada y no en uso."
        },
        {
            "id": "POLY-ABANDON-01",
            "nombre": "Edificio Abandonado (Sector Intermedio Este)",
            "tipo": "Estructura Abandonada / Obra Inconclusa",
            "zona": "Sector Intermedio",
            "coords": [
                [0.40365346426669096, -78.17125960309245],
                [0.4040465980124745, -78.17150253007814],
                [0.40407184687028974, -78.17148316413493],
                [0.40422491818431067, -78.17157319198544],
                [0.40427010643396466, -78.1713867979584],
                [0.4041895600147244, -78.17131776560983],
                [0.4041882815323957, -78.17129234893221],
                [0.4041402707897744, -78.1712430836846],
                [0.4037233844233991, -78.17104780748441]
            ],
            "centroid": [0.4039664, -78.1713058],
            "area": 1868.4,
            "color": "#7f8c8d", "fill": "#bdc3c7",
            "interior": False, "is_perimeter": False,
            "desc": "Estructura inconclusa y deshabitada en el sector intermedio este del campus Yachay Tech."
        },
        {
            "id": "POLY-ABANDON-02",
            "nombre": "Edificio Abandonado (Sector Intermedio Oeste)",
            "tipo": "Estructura Abandonada / Obra Inconclusa",
            "zona": "Sector Intermedio",
            "coords": [
                [0.4035130158607125, -78.17176742545003],
                [0.40382321809887034, -78.17185335921086],
                [0.40378204630646614, -78.1719856399383],
                [0.40346753223031806, -78.1718985761575],
                [0.4034062852079537, -78.17212640804205],
                [0.40402779033033714, -78.1722987939844],
                [0.40421829192713976, -78.17173257684784],
                [0.40358177314045884, -78.17155460198654]
            ],
            "centroid": [0.4038277, -78.1719331],
            "area": 4274.0,
            "color": "#7f8c8d", "fill": "#bdc3c7",
            "interior": False, "is_perimeter": False,
            "desc": "Macromanzana de hormigón armado inconclusa en el sector intermedio; no alberga población activa."
        },
        {
            "id": "POLY-ABANDON-AUDITORIO",
            "nombre": "Edificio Abandonado (Proyecto Auditorio)",
            "tipo": "Estructura Abandonada / Obra Inconclusa",
            "zona": "Sector Central",
            "coords": [
                [0.40473562332417545, -78.17251673234806],
                [0.4050808675267319, -78.17261476322064],
                [0.40524213053362224, -78.1721051767315],
                [0.40493515885630726, -78.17187461532733]
            ],
            "centroid": [0.4049924, -78.1722743],
            "area": 2676.3,
            "color": "#7f8c8d", "fill": "#bdc3c7",
            "interior": False, "is_perimeter": False,
            "desc": "Estructura que originalmente iba a albergar el Gran Auditorio Universitario, actualmente desocupada y en obra gris."
        },
        {
            "id": "POLY-ABANDON-SUR",
            "nombre": "Edificio Abandonado (Sector Sur)",
            "tipo": "Estructura Abandonada / Obra Inconclusa",
            "zona": "Sector Sur",
            "coords": [
                [0.40198661472022046, -78.17018494333783],
                [0.40197939986354697, -78.17015896664411],
                [0.4018014059681932, -78.17014905901726],
                [0.4016457134467513, -78.17039303735463],
                [0.40139340789967926, -78.17091625315602],
                [0.40150833806372377, -78.17098671074227],
                [0.4015331078693194, -78.17095079335678],
                [0.40155968867380226, -78.17098383852725],
                [0.4018828040275859, -78.17049047158272],
                [0.4018368499539993, -78.17046120356976],
                [0.40190674515631897, -78.17035997422332],
                [0.4019967199907882, -78.17032866383832],
                [0.40201035768468407, -78.17041042529293],
                [0.4024179041088888, -78.17039486933922],
                [0.40242027729676116, -78.17019680936544]
            ],
            "centroid": [0.4018584, -78.1704689],
            "area": 3521.5,
            "color": "#7f8c8d", "fill": "#bdc3c7",
            "interior": False, "is_perimeter": False,
            "desc": "Edificación de gran perímetro en obra gris desocupada en el cuadrante sureste del campus."
        },
        {
            "id": "POLY-GIMNASIO-AIRE-LIBRE",
            "nombre": "Área de Gimnasia al Aire Libre",
            "tipo": "Instalación Deportiva y Calistenia",
            "zona": "Complejo Deportivo Sur",
            "coords": [
                [0.4021387444371405, -78.17252282884651],
                [0.402149242762423, -78.1723480258741],
                [0.4022851637956411, -78.17234637947526],
                [0.402285096053807, -78.17238344901638],
                [0.4022178859242461, -78.17251937191773],
                [0.4021387493835701, -78.17252422790877]
            ],
            "centroid": [0.4022032, -78.1724260],
            "area": 244.9,
            "color": "#16a085", "fill": "#1abc9c",
            "interior": False, "is_perimeter": False,
            "desc": "Espacio deportivo y circuito biosaludable de calistenia al aire libre, contiguo a las canchas deportivas y residencias estudiantiles del sector sur."
        },
        {
            "id": "POLY-CONTAINER-DESUSO",
            "nombre": "Container Modular (En Desuso Mantenido)",
            "tipo": "Infraestructura Logística y Almacén",
            "zona": "Senescyt",
            "coords": [
                [0.4077409361522614, -78.1702754359314],
                [0.4077590220797426, -78.17025461179638],
                [0.4078325724502306, -78.17034346961663],
                [0.407814481699854, -78.17036009172537]
            ],
            "centroid": [0.4077862, -78.1703076],
            "area": 36.3,
            "color": "#7f8c8d", "fill": "#95a5a6",
            "interior": False, "is_perimeter": False,
            "desc": "Estructura modular tipo contenedor en desuso operativo pero con mantenimiento exterior, ubicada al norte del Edificio Senescyt."
        }
    ]

    for h in huellas_arquitectonicas:
        if h.get("is_perimeter"):
            # Perímetros de conjunto histórico y delimitaciones mayores:
            # Se asignan a fg_perimetros (desactivada por defecto) con fill=False (solo trazo discontinuo),
            # de modo que el interior sea 100% transparente al ratón y permita seleccionar libremente
            # cualquier edificio individual contenido (Biblioteca Patrimonial, Sala Capitular, Aulas, etc.).
            folium.Polygon(
                locations=h["coords"],
                color=h["color"],
                weight=2.5,
                dash_array="8, 8",
                fill=False,
                tooltip=f"📐 {h['nombre']} ({h['tipo']})",
                popup=folium.Popup(f"""
                    <div style="font-family: 'Segoe UI', Arial, sans-serif; width: 260px; line-height: 1.4;">
                        <div style="color: {h['color']}; font-weight: bold; font-size: 13.5px; margin-bottom: 2px;">📐 {h['nombre']}</div>
                        <span style="background: #fdf2e9; color: #d35400; padding: 2px 6px; border-radius: 4px; font-size: 10px; font-weight: 600;">{h['tipo']}</span>
                        <p style="margin: 6px 0 4px 0; font-size: 11.5px; color: #34495e;">
                            {h.get('desc', '')}
                        </p>
                        <div style="font-size: 10.5px; color: #7f8c8d; border-top: 1px solid #ecf0f1; padding-top: 4px;">
                            Área total del conjunto: <b>{h.get('area', 'N/D')} m²</b> | Zona: <b>{h.get('zona', '')}</b><br>
                            <i>💡 Nota: Haz clic en los edificios interiores para ver sus detalles individuales.</i>
                        </div>
                    </div>
                """, max_width=280)
            ).add_to(fg_perimetros)
        else:
            if h.get("interior"):
                dash = "3, 3"
                weight = 2.5
                opacity = 0.55
            else:
                dash = None
                weight = 2
                opacity = 0.38
            folium.Polygon(
                locations=h["coords"],
                color=h["color"],
                weight=weight,
                dash_array=dash,
                fill=True,
                fill_color=h["fill"],
                fill_opacity=opacity,
                tooltip=f"🏛️ {h['nombre']} ({h['tipo']})",
                popup=folium.Popup(f"""
                    <div style="font-family: 'Segoe UI', Arial, sans-serif; width: 250px; line-height: 1.4;">
                        <div style="color: {h['color']}; font-weight: bold; font-size: 13px; margin-bottom: 2px;">{h['nombre']}</div>
                        <span style="background: #eef2f7; color: #2c3e50; padding: 2px 6px; border-radius: 4px; font-size: 10px; font-weight: 600;">{h['tipo']}</span>
                        <p style="margin: 6px 0 4px 0; font-size: 11px; color: #34495e;">
                            {h.get('desc', '')}
                        </p>
                        <div style="font-size: 10px; color: #7f8c8d; border-top: 1px solid #ecf0f1; padding-top: 3px;">
                            Superficie aprox: <b>{h.get('area', 'N/D')} m²</b> | Zona: <b>{h.get('zona', '')}</b>
                        </div>
                    </div>
                """, max_width=270)
            ).add_to(fg_edificios)

    # Líneas divisorias arquitectónicas interiores
    lineas_divisorias = [
        {
            "nombre": "División Bloques F y G",
            "coords": [[0.4078891, -78.1713060], [0.4077295, -78.1712963]],
            "color": "#1e8449",
            "desc": "Separación modular y pasillo técnico entre el Bloque F y Bloque G."
        },
        {
            "nombre": "División de Ambientes Biblioteca Patrimonial",
            "coords": [[0.4052026, -78.1742789], [0.4051054, -78.1742367]],
            "color": "#1b4f72",
            "desc": "Tabique divisorio interior entre sala de lectura histórica y acervo patrimonial."
        },
        {
            "nombre": "División Casa Patrimonial Las T's 1",
            "coords": [[0.4004985, -78.1744459], [0.4004445, -78.1745398]],
            "color": "#27ae60",
            "desc": "Línea de división medianera interior de Casa Patrimonial Las T's 1."
        },
        {
            "nombre": "División Casa Patrimonial Las T's 2",
            "coords": [[0.4003, -78.1747604], [0.4002447, -78.1748556]],
            "color": "#27ae60",
            "desc": "Línea de división medianera interior de Casa Patrimonial Las T's 2."
        },
        {
            "nombre": "División Casa Patrimonial Las T's 3",
            "coords": [[0.4006698, -78.1746367], [0.4006158, -78.1747255]],
            "color": "#27ae60",
            "desc": "Línea de división medianera interior de Casa Patrimonial Las T's 3."
        },
        {
            "nombre": "División Casa Patrimonial Las T's 4",
            "coords": [[0.40048, -78.1749512], [0.4004207, -78.1750387]],
            "color": "#27ae60",
            "desc": "Línea de división medianera interior de Casa Patrimonial Las T's 4."
        },
        {
            "nombre": "División Casa Patrimonial Las T's 5",
            "coords": [[0.4006813, -78.174759], [0.400773, -78.1747979]],
            "color": "#27ae60",
            "desc": "Tabique transversal divisorio interior en punto topográfico [0.4006775, -78.1747574]."
        },
        {
            "nombre": "División Casa Patrimonial Las T's 6",
            "coords": [[0.4006643, -78.1750387], [0.4005707, -78.1749984]],
            "color": "#27ae60",
            "desc": "Tabique transversal divisorio interior en punto topográfico [0.4005722, -78.1749991]."
        },
        {
            "nombre": "División Casa Patrimonial Las T's 7",
            "coords": [[0.4004717, -78.1752334], [0.400561, -78.1752724]],
            "color": "#27ae60",
            "desc": "Tabique transversal divisorio interior en punto topográfico [0.4004703, -78.1752328]."
        },
        {
            "nombre": "División Casa Patrimonial Las T's 8",
            "coords": [[0.4008564, -78.1749468], [0.4007665, -78.1749074]],
            "color": "#27ae60",
            "desc": "Tabique transversal divisorio interior en punto topográfico [0.4008586, -78.1749478]."
        },
        {
            "nombre": "División Casa Patrimonial Las T's 9",
            "coords": [[0.4007488, -78.1751863], [0.400661, -78.1751494]],
            "color": "#27ae60",
            "desc": "Tabique transversal divisorio interior en punto topográfico [0.4007509, -78.1751872]."
        },
        {
            "nombre": "División Casa Patrimonial Las T's 10",
            "coords": [[0.400553, -78.175396], [0.4006426, -78.1754358]],
            "color": "#27ae60",
            "desc": "Tabique transversal divisorio interior en punto topográfico [0.4006437, -78.1754363]."
        },
        {
            "nombre": "División Casa Patrimonial Las T's 11 (Módulo 1)",
            "coords": [[0.4009843, -78.175074], [0.4008879, -78.1750472]],
            "color": "#27ae60",
            "desc": "Tabique transversal divisorio interior 1/3 en punto topográfico [0.4008861, -78.1750467]."
        },
        {
            "nombre": "División Casa Patrimonial Las T's 11 (Módulo 2)",
            "coords": [[0.400956, -78.175176], [0.4008596, -78.1751492]],
            "color": "#27ae60",
            "desc": "Tabique transversal divisorio interior 2/3 en punto topográfico [0.4008529, -78.1751473]."
        },
        {
            "nombre": "División Casa Patrimonial Las T's 11 (Módulo 3)",
            "coords": [[0.4009283, -78.1752755], [0.4008319, -78.1752487]],
            "color": "#27ae60",
            "desc": "Tabique transversal divisorio interior 3/3 en punto topográfico [0.4008274, -78.1752475]."
        },
        {
            "nombre": "División Casa Patrimonial Las T's 12 (Módulo 1)",
            "coords": [[0.4007985, -78.1757194], [0.4007006, -78.175691]],
            "color": "#27ae60",
            "desc": "Tabique transversal divisorio interior 1/3 en punto topográfico [0.4007043, -78.1756921]."
        },
        {
            "nombre": "División Casa Patrimonial Las T's 12 (Módulo 2)",
            "coords": [[0.4008287, -78.1756154], [0.4007308, -78.175587]],
            "color": "#27ae60",
            "desc": "Tabique transversal divisorio interior 2/3 en punto topográfico [0.4007292, -78.1755865]."
        },
        {
            "nombre": "División Casa Patrimonial Las T's 12 (Módulo 3)",
            "coords": [[0.4008572, -78.175517], [0.4007593, -78.1754886]],
            "color": "#27ae60",
            "desc": "Tabique transversal divisorio interior 3/3 en punto topográfico [0.400757, -78.1754879]."
        },
        {
            "nombre": "División Casa Patrimonial Las T's 13",
            "coords": [[0.4008969, -78.175889], [0.400799, -78.1758622]],
            "color": "#27ae60",
            "desc": "Tabique transversal divisorio interior en punto topográfico [0.4008941, -78.1758882]."
        },
        {
            "nombre": "División Bloque Multifamiliar 1",
            "coords": [[0.4021158, -78.174749], [0.402256, -78.1747041]],
            "color": "#16a085",
            "desc": "Línea de partición medianera interior del Bloque Multifamiliar 1."
        },
        {
            "nombre": "División Bloque Multifamiliar 2",
            "coords": [[0.4019849, -78.1750345], [0.4019449, -78.1749169]],
            "color": "#16a085",
            "desc": "Tabique transversal divisorio interior en el quiebre escalonado del Bloque Multifamiliar 2."
        },
        {
            "nombre": "División Residencia Patrimonial Las Pats 1 (Línea 1)",
            "coords": [[0.4015244, -78.1731259], [0.401449, -78.1730776]],
            "color": "#27ae60",
            "desc": "Tabique divisorio interior 1 en Residencia Patrimonial Las Pats 1."
        },
        {
            "nombre": "División Residencia Patrimonial Las Pats 1 (Línea 2)",
            "coords": [[0.4015838, -78.1730381], [0.4015043, -78.1729858]],
            "color": "#27ae60",
            "desc": "Tabique divisorio interior 2 en Residencia Patrimonial Las Pats 1."
        },
        {
            "nombre": "División Residencia Patrimonial Las Pats 2 (Línea 1)",
            "coords": [[0.401335, -78.173425], [0.4012639, -78.1733764]],
            "color": "#27ae60",
            "desc": "Tabique divisorio interior 1 en Residencia Patrimonial Las Pats 2."
        },
        {
            "nombre": "División Residencia Patrimonial Las Pats 2 (Línea 2)",
            "coords": [[0.4013953, -78.1733361], [0.4013202, -78.1732909]],
            "color": "#27ae60",
            "desc": "Tabique divisorio interior 2 en Residencia Patrimonial Las Pats 2."
        },
        {
            "nombre": "División Residencia Patrimonial Las Pats 3 (Línea 1)",
            "coords": [[0.401462, -78.1738283], [0.4013796, -78.1738618]],
            "color": "#27ae60",
            "desc": "Tabique divisorio interior 1 en Residencia Patrimonial Las Pats 3."
        },
        {
            "nombre": "División Residencia Patrimonial Las Pats 3 (Línea 2)",
            "coords": [[0.4014171, -78.1737321], [0.401335, -78.17378]],
            "color": "#27ae60",
            "desc": "Tabique divisorio interior 2 en Residencia Patrimonial Las Pats 3."
        },
        {
            "nombre": "División Residencia Patrimonial Las Pats 3 (Línea 3)",
            "coords": [[0.4013608, -78.1736526], [0.4012874, -78.1736952]],
            "color": "#27ae60",
            "desc": "Tabique divisorio interior 3 en Residencia Patrimonial Las Pats 3."
        },
        {
            "nombre": "División Residencia Patrimonial Las Pats 4 (Módulo 1)",
            "coords": [[0.4015206, -78.1741025], [0.401598, -78.1740601]],
            "color": "#27ae60",
            "desc": "Tabique transversal divisorio 1 en punto topográfico [0.4016008, -78.1740586]."
        },
        {
            "nombre": "División Residencia Patrimonial Las Pats 4 (Módulo 2)",
            "coords": [[0.4015675, -78.174188], [0.4016449, -78.1741456]],
            "color": "#27ae60",
            "desc": "Tabique transversal divisorio 2 en punto topográfico [0.4016451, -78.1741455]."
        },
        {
            "nombre": "División Residencia Patrimonial Las Pats 4 (Módulo 3)",
            "coords": [[0.4016123, -78.1742697], [0.4016897, -78.1742273]],
            "color": "#27ae60",
            "desc": "Tabique transversal divisorio 3 en punto topográfico [0.401691, -78.1742266]."
        },
        {
            "nombre": "División Residencia Patrimonial Las Pats 4 (Módulo 4)",
            "coords": [[0.4016626, -78.1743615], [0.40174, -78.1743191]],
            "color": "#27ae60",
            "desc": "Tabique transversal divisorio 4 en punto topográfico [0.4017393, -78.1743195]."
        },
        {
            "nombre": "División Residencia Patrimonial Las Pats 4 (Módulo 5)",
            "coords": [[0.4017108, -78.1744493], [0.4017881, -78.174407]],
            "color": "#27ae60",
            "desc": "Tabique transversal divisorio 5 en punto topográfico [0.4017886, -78.1744067]."
        },
        {
            "nombre": "División Residencia Patrimonial Las Pats 5 (Módulo 1)",
            "coords": [[0.4018832, -78.1745931], [0.4018399, -78.1745179]],
            "color": "#27ae60",
            "desc": "Tabique transversal divisorio 1 en punto topográfico [0.4018386, -78.1745156]."
        },
        {
            "nombre": "División Residencia Patrimonial Las Pats 5 (Módulo 2)",
            "coords": [[0.4019767, -78.1745393], [0.4019334, -78.1744641]],
            "color": "#27ae60",
            "desc": "Tabique transversal divisorio 2 en punto topográfico [0.4019324, -78.1744623]."
        },
        {
            "nombre": "División Residencia Patrimonial Las Pats 5 (Módulo 3)",
            "coords": [[0.4020605, -78.174491], [0.4020173, -78.1744158]],
            "color": "#27ae60",
            "desc": "Tabique transversal divisorio 3 en punto topográfico [0.4020149, -78.1744117]."
        },
        {
            "nombre": "División Residencia Patrimonial Las Pats 5 (Módulo 4)",
            "coords": [[0.4021501, -78.1744394], [0.4021068, -78.1743642]],
            "color": "#27ae60",
            "desc": "Tabique transversal divisorio 4 en punto topográfico [0.4021058, -78.1743624]."
        },
        {
            "nombre": "División Residencia Patrimonial Las Pats 5 (Módulo 5)",
            "coords": [[0.4022366, -78.1743895], [0.4021934, -78.1743144]],
            "color": "#27ae60",
            "desc": "Tabique transversal divisorio 5 en punto topográfico [0.4021913, -78.1743108]."
        },
        {
            "nombre": "División Residencia Patrimonial Las Pats 5 (Módulo 6)",
            "coords": [[0.4023263, -78.1743379], [0.402283, -78.1742627]],
            "color": "#27ae60",
            "desc": "Tabique transversal divisorio 6 en punto topográfico [0.4022821, -78.1742612]."
        },
        {
            "nombre": "División Residencia Patrimonial Las Pats 5 (Módulo 7)",
            "coords": [[0.4024105, -78.1742894], [0.4023672, -78.1742142]],
            "color": "#27ae60",
            "desc": "Tabique transversal divisorio 7 en punto topográfico [0.4023653, -78.1742109]."
        },
        {
            "nombre": "División Residencia Patrimonial Las Pats 6 (Módulo 1)",
            "coords": [[0.4024759, -78.1740312], [0.4023971, -78.1740743]],
            "color": "#27ae60",
            "desc": "Tabique transversal divisorio 1 en punto topográfico [0.4023974, -78.1740741]."
        },
        {
            "nombre": "División Residencia Patrimonial Las Pats 6 (Módulo 2)",
            "coords": [[0.4024283, -78.1739444], [0.4023495, -78.1739875]],
            "color": "#27ae60",
            "desc": "Tabique transversal divisorio 2 en punto topográfico [0.4023482, -78.1739882]."
        },
        {
            "nombre": "División Residencia Patrimonial Las Pats 6 (Módulo 3)",
            "coords": [[0.402381, -78.1738579], [0.4023022, -78.173901]],
            "color": "#27ae60",
            "desc": "Tabique transversal divisorio 3 en punto topográfico [0.4023002, -78.1739021]."
        },
        {
            "nombre": "División Residencia Patrimonial Las Pats 7 (Módulo 1)",
            "coords": [[0.4021519, -78.173457], [0.4020745, -78.1735007]],
            "color": "#27ae60",
            "desc": "Tabique transversal divisorio 1 en punto topográfico [0.4020732, -78.1735014]."
        },
        {
            "nombre": "División Residencia Patrimonial Las Pats 7 (Módulo 2)",
            "coords": [[0.4022001, -78.1735424], [0.4021227, -78.1735861]],
            "color": "#27ae60",
            "desc": "Tabique transversal divisorio 2 en punto topográfico [0.4021195, -78.1735879]."
        },
        {
            "nombre": "División Residencia Patrimonial Las Pats 7 (Módulo 3)",
            "coords": [[0.4022494, -78.1736297], [0.402172, -78.1736734]],
            "color": "#27ae60",
            "desc": "Tabique transversal divisorio 3 en punto topográfico [0.4021695, -78.1736748]."
        },
        {
            "nombre": "División Residencia Patrimonial Las Pats 8 (Módulo 1)",
            "coords": [[0.4030519, -78.1749682], [0.4029726, -78.1750093]],
            "color": "#27ae60",
            "desc": "Tabique transversal divisorio 1 en punto topográfico [0.4029728, -78.1750092]."
        },
        {
            "nombre": "División Residencia Patrimonial Las Pats 8 (Módulo 2)",
            "coords": [[0.4030107, -78.1748889], [0.4029315, -78.17493]],
            "color": "#27ae60",
            "desc": "Tabique transversal divisorio 2 en punto topográfico [0.4029345, -78.1749284]."
        },
        {
            "nombre": "División Residencia Patrimonial Las Pats 8 (Módulo 3)",
            "coords": [[0.4029686, -78.1748076], [0.4028893, -78.1748487]],
            "color": "#27ae60",
            "desc": "Tabique transversal divisorio 3 en punto topográfico [0.4028903, -78.1748482]."
        },
        {
            "nombre": "División Residencia Patrimonial Las Pats 8 (Módulo 4)",
            "coords": [[0.4029226, -78.1747189], [0.4028433, -78.17476]],
            "color": "#27ae60",
            "desc": "Tabique transversal divisorio 4 en punto topográfico [0.402842, -78.1747607]."
        },
        {
            "nombre": "División Residencia Patrimonial Las Pats 8 (Módulo 5)",
            "coords": [[0.4028764, -78.1746299], [0.4027972, -78.174671]],
            "color": "#27ae60",
            "desc": "Tabique transversal divisorio 5 en punto topográfico [0.4027961, -78.1746715]."
        },
        {
            "nombre": "División Residencia Patrimonial Las Pats 8 (Módulo 6)",
            "coords": [[0.4028257, -78.1745321], [0.4027464, -78.1745732]],
            "color": "#27ae60",
            "desc": "Tabique transversal divisorio 6 en punto topográfico [0.4027448, -78.174574]."
        },
        {
            "nombre": "División Residencia Patrimonial Las Pats 8 (Módulo 7)",
            "coords": [[0.4027797, -78.1744434], [0.4027005, -78.1744845]],
            "color": "#27ae60",
            "desc": "Tabique transversal divisorio 7 en punto topográfico [0.4026985, -78.1744855]."
        },
        {
            "nombre": "División Residencia Patrimonial Las Pats 8 (Módulo 8)",
            "coords": [[0.4027352, -78.1743575], [0.4026559, -78.1743986]],
            "color": "#27ae60",
            "desc": "Tabique transversal divisorio 8 en punto topográfico [0.4026539, -78.1743996]."
        },
        {
            "nombre": "División Residencia Patrimonial Las Pats 8 (Módulo 9)",
            "coords": [[0.4026889, -78.1742682], [0.4026096, -78.1743093]],
            "color": "#27ae60",
            "desc": "Tabique transversal divisorio 9 en punto topográfico [0.402608, -78.1743101]."
        },
        {
            "nombre": "División Residencia Patrimonial Las Pats 8 (Módulo 10)",
            "coords": [[0.4026424, -78.1741785], [0.4025631, -78.1742196]],
            "color": "#27ae60",
            "desc": "Tabique transversal divisorio 10 en punto topográfico [0.4025651, -78.1742186]."
        },
        {
            "nombre": "División Residencia Patrimonial Las Pats 9 (Módulo 1)",
            "coords": [[0.401784, -78.173383], [0.4017430, -78.1732995]],
            "color": "#27ae60",
            "desc": "Tabique transversal divisorio 1 en punto topográfico [0.401784, -78.173383]."
        },
        {
            "nombre": "División Residencia Patrimonial Las Pats 9 (Módulo 2)",
            "coords": [[0.401877, -78.173330], [0.4018350, -78.1732449]],
            "color": "#27ae60",
            "desc": "Tabique transversal divisorio 2 en punto topográfico [0.401877, -78.173330]."
        },
        {
            "nombre": "División Residencia de Docentes 8 (Medianera)",
            "coords": [[0.4035530, -78.1761398], [0.4035359, -78.1760731]],
            "color": "#1b4f72",
            "desc": "Tabique transversal medianero interior que independiza las dos unidades de la Residencia de Docentes 8."
        }
    ]
    for ld in lineas_divisorias:
        folium.PolyLine(
            locations=ld["coords"],
            color=ld["color"],
            weight=3,
            dash_array="4, 4",
            tooltip=f"📏 {ld['nombre']}",
            popup=folium.Popup(f"<b>{ld['nombre']}</b><br>{ld['desc']}", max_width=220)
        ).add_to(fg_edificios)

    # -------------------------------------------------------------
    # 5. RECURSOS HÍDRICOS (CANALES LÓTICOS Y RESERVORIO LÉNTICO)
    # -------------------------------------------------------------
    # 5.1. Canal de Agua Suroeste (Sector Concha Acústica / Multifamiliares)
    folium.PolyLine(
        locations=canal_suroeste,
        color="#00cec9",
        weight=3.5,
        dash_array='6, 6',
        popup=folium.Popup("""
            <div style="font-family: 'Segoe UI', Arial, sans-serif; width: 250px;">
                <h4 style="color: #00cec9; margin: 0 0 4px 0;">💧 Canal de Agua Suroeste</h4>
                <span style="background: #e0f2fe; color: #0369a1; padding: 2px 6px; border-radius: 4px; font-size: 10px; font-weight: 600;">Sector Concha Acústica</span>
                <p style="font-size: 11.5px; color: #34495e; margin: 6px 0 0 0;">
                    Flujo hídrico lotiforme de ~124.5 m que discurre en el flanco sur de las Residencias. Blindado perimetralmente por la Cerca Viva 1.
                </p>
            </div>
        """, max_width=270),
        tooltip="💧 Canal de Agua Suroeste (~124.5 m)"
    ).add_to(fg_canales)

    # 5.4. Canal de Agua Este (Conducción hacia el Reservorio - 34 Vértices Topográficos Relevados)
    # Suavizado de curva mediante interpolación spline cúbica (120 puntos)
    try:
        from scipy.interpolate import splprep, splev
        _lats = [p[0] for p in canal_este_topografico_34pts]
        _lons = [p[1] for p in canal_este_topografico_34pts]
        _tck, _u = splprep([_lats, _lons], s=0.0000000005, k=3)
        _u_fine = np.linspace(0, 1, 120)
        _lats_f, _lons_f = splev(_u_fine, _tck)
        canal_este_suave = [[round(float(la), 7), round(float(lo), 7)] for la, lo in zip(_lats_f, _lons_f)]
    except Exception:
        canal_este_suave = canal_este_topografico_34pts

    # PolyLine del Canal Este
    folium.PolyLine(
        locations=canal_este_suave,
        color="#0abde3",
        weight=3.5,
        dash_array='4, 4',
        popup=folium.Popup("""
            <div style="font-family: 'Segoe UI', Arial, sans-serif; width: 260px;">
                <h4 style="color: #0abde3; margin: 0 0 4px 0;">💧 Canal de Agua Este (Hacia Reservorio)</h4>
                <span style="background: #e0f2fe; color: #0369a1; padding: 2px 6px; border-radius: 4px; font-size: 10px; font-weight: 600;">Conducción Hidráulica ~280.6 m</span>
                <p style="font-size: 11.5px; color: #34495e; margin: 6px 0 0 0;">
                    Canal sinuoso de 34 vértices topográficos modelado con interpolación spline continua. Transporta caudal gravitacional hacia el reservorio agroforestal.
                </p>
            </div>
        """, max_width=280),
        tooltip="💧 Canal de Agua Este: Conducción a Reservorio (~280.6 m)"
    ).add_to(fg_canales)

    # 5.5. Laguna Artificial de Agua o Reservorio (Cuerpo Léntico)
    laguna_coords = [[0.4043551, -78.1682684], [0.4043551, -78.1681642], [0.4042595, -78.1681065], [0.4041402, -78.1681031], [0.4040329, -78.1681142], [0.4039035, -78.1681725], [0.4039088, -78.1682983], [0.4039638, -78.1685078], [0.4040483, -78.168541], [0.4040812, -78.1685544], [0.4040684, -78.1685806], [0.4040919, -78.1686181], [0.4041271, -78.1685953], [0.4041489, -78.1685705], [0.4041596, -78.1685403], [0.4042129, -78.1685363]]
    folium.Polygon(
        locations=laguna_coords,
        color="#0984e3",
        weight=2.5,
        fill=True,
        fill_color="#00cec9",
        fill_opacity=0.62,
        popup=folium.Popup("""
            <div style="font-family: 'Segoe UI', Arial, sans-serif; width: 270px; line-height: 1.4;">
                <div style="color: #0984e3; font-weight: bold; font-size: 14px; margin-bottom: 3px;">🌊 Laguna Artificial / Reservorio de Agua</div>
                <span style="background: #e0f2fe; color: #0369a1; padding: 2px 7px; border-radius: 4px; font-size: 10.5px; font-weight: 600;">Cuerpo Léntico · ~2,006.2 m² de Espejo de Agua</span>
                <p style="margin: 8px 0 6px 0; font-size: 11.5px; color: #2c3e50;">
                    <b>Ecosistema Libre de Arenillas:</b> Las hembras de <i>Simulium</i> spp. no ovipositan en aguas estancadas/lénticas. Este reservorio actúa como santuario y vivero natural de <b>libélulas y caballitos del diablo (Odonata)</b>, principales depredadores biológicos de los simúlidos en vuelo.
                </p>
                <div style="font-size: 10px; color: #7f8c8d; border-top: 1px solid #ecf0f1; padding-top: 4px;">
                    📍 Centroide GPS: 0.404121, -78.168316 | Polígono de 16 vértices
                </div>
            </div>
        """, max_width=290),
        tooltip="🌊 Laguna Artificial / Reservorio de Agua (~2,006 m² - Refugio de Odonatos)"
    ).add_to(fg_canales)

    # Marcador en el centro de la Laguna
    folium.Marker(
        location=[0.404122, -78.1683157],
        icon=folium.Icon(icon='tint', prefix='fa', color='darkblue'),
        popup=folium.Popup("""
            <div style="font-family: 'Segoe UI', Arial, sans-serif; width: 230px;">
                <b style="color: #0984e3;">💧 Reservorio Central</b><br>
                <span style="font-size: 11px; color: #57606f;">Espejo de agua artificial de ~2,006 m² para fomento de fauna depredadora nativa.</span>
            </div>
        """, max_width=250),
        tooltip="💧 Centroide: Laguna y Reservorio de Agua"
    ).add_to(fg_canales)

    # 5.7. Canal de Agua Jardines Sala Capitular / Ingenio
    canal_capitular = [
        [0.4046421, -78.1751245],
        [0.4048221, -78.1751372],
        [0.4050082, -78.1751801]
    ]
    folium.PolyLine(
        locations=canal_capitular,
        color="#0984e3",
        weight=3.5,
        dash_array='5, 5',
        popup=folium.Popup("""
            <div style="font-family: 'Segoe UI', Arial, sans-serif; width: 250px;">
                <h4 style="color: #0984e3; margin: 0 0 5px 0;">💧 Canal Jardines Sala Capitular</h4>
                <p style="font-size: 12px; color: #34495e; margin: 0;">
                    Acequia lótica descubierta que fluye por los jardines del sector patrimonial. Su cercanía a la <b>Parada de la Sala Capitular</b> explica la elevada tasa de picaduras observada en usuarios en espera.<br>
                    <b>Intervención Verde:</b> Tratamiento biológico selectivo con Bti e interceptación de vuelo mediante la barrera vegetal.
                </p>
                <div style="font-size: 10px; color: #7f8c8d; border-top: 1px solid #ecf0f1; padding-top: 3px; margin-top: 5px;">
                    Longitud: <b>41.1 m</b> | Sector Sala Capitular / Ingenio
                </div>
            </div>
        """, max_width=270),
        tooltip="💧 Canal de Agua Jardines Sala Capitular (Cercano a Parada de Bus)"
    ).add_to(fg_canales)

    # 5.8. Canal de Agua Sector San José (Contiguo a Edificio 20 y Sala de Estar)
    canal_sanjose = [
        [0.4045979, -78.1764123],
        [0.4045743, -78.1764386],
        [0.4045700, -78.1764951],
        [0.4045492, -78.1765761]
    ]
    folium.PolyLine(
        locations=canal_sanjose,
        color="#0984e3",
        weight=3.5,
        dash_array='5, 5',
        popup=folium.Popup("""
            <div style="font-family: 'Segoe UI', Arial, sans-serif; width: 250px;">
                <h4 style="color: #0984e3; margin: 0 0 5px 0;">💧 Canal de Agua Sector San José</h4>
                <p style="font-size: 12px; color: #34495e; margin: 0;">
                    Acequia lótica activa descubierta que discurre en la retaguardia del Edificio 20 y la Sala de Estar de San José.<br>
                    <b>Intervención Verde:</b> Bio-mitigación con barrera vegetal tri-estrato CV-07 y control biológico con Bti.
                </p>
                <div style="font-size: 10px; color: #7f8c8d; border-top: 1px solid #ecf0f1; padding-top: 3px; margin-top: 5px;">
                    Longitud: <b>19.5 m</b> | Sector San José / Casco Histórico
                </div>
            </div>
        """, max_width=270),
        tooltip="💧 Canal de Agua Sector San José (Contiguo a Edificio 20 y Sala de Estar)"
    ).add_to(fg_canales)

    # 5.9. Canal de Agua Conector hacia Esclusa Este (15 Vértices Topográficos)
    canal_esclusa_este = [
        [0.4046761, -78.1680199],
        [0.4045333, -78.1681836],
        [0.4043868, -78.1682822],
        [0.4041962, -78.1686307],
        [0.4041061, -78.1687743],
        [0.4040429, -78.1689091],
        [0.4040262, -78.1689233],
        [0.4040011, -78.1689108],
        [0.4039983, -78.1689206],
        [0.4040178, -78.1689304],
        [0.4040123, -78.1689487],
        [0.4039886, -78.1689348],
        [0.4039831, -78.1689614],
        [0.4039943, -78.1689726],
        [0.4039970, -78.1689739]
    ]
    folium.PolyLine(
        locations=canal_esclusa_este,
        color="#0abde3",
        weight=3.5,
        dash_array='4, 4',
        popup=folium.Popup("""
            <div style="font-family: 'Segoe UI', Arial, sans-serif; width: 260px;">
                <h4 style="color: #0abde3; margin: 0 0 4px 0;">💧 Canal Conector hacia Esclusa Este</h4>
                <p style="margin: 0; font-size: 11.5px; color: #555;">
                    Longitud: <b>~142.8 m</b> | 15 vértices topográficos.<br>
                    Ramal hídrico de conducción conectado a la esclusa de regulación este. Tramo activo monitoreado para biocontrol con Bti y hábitat de libélulas.
                </p>
            </div>
        """, max_width=270),
        tooltip="💧 Canal Conector hacia Esclusa Este (~142.8 m)"
    ).add_to(fg_canales)

    # 5.6. Fuentes de Agua Ornamentales e Infraestructura Hidráulica
    # Pileta Histórica (Claustro Sala Capitular)
    folium.Marker(
        location=[0.4043772, -78.1754463],
        icon=folium.Icon(icon='tint', prefix='fa', color='blue'),
        popup=folium.Popup("""
            <div style="font-family: 'Segoe UI', Arial, sans-serif; width: 260px; line-height: 1.4;">
                <div style="color: #0984e3; font-weight: bold; font-size: 13.5px; margin-bottom: 2px;">⛲ Pileta Histórica (Claustro Sala Capitular)</div>
                <span style="background: #e0f2fe; color: #0369a1; padding: 2px 6px; border-radius: 4px; font-size: 10px; font-weight: 600;">Fuente Ornamental / Patrimonio Hidráulico</span>
                <p style="margin: 6px 0 4px 0; font-size: 11.5px; color: #34495e;">
                    <b>Estado Físico:</b> Permanece seca la mayor parte del año.<br>
                    <b>Riesgo Entomológico:</b> Nulo para <i>Simulium</i> (no genera hábitat larvario al carecer de agua corriente y permanecer seca).
                </p>
                <div style="font-size: 10px; color: #7f8c8d; border-top: 1px solid #ecf0f1; padding-top: 3px;">
                    📍 GPS: 0.404377, -78.175446 | Patio Central Sala Capitular
                </div>
            </div>
        """, max_width=280),
        tooltip="⛲ Pileta Histórica: Fuente Ornamental Claustral (Seca)"
    ).add_to(fg_canales)

    # Pileta de Jardines (Sala Capitular)
    folium.Marker(
        location=[0.4043464, -78.1756891],
        icon=folium.Icon(icon='tint', prefix='fa', color='cadetblue'),
        popup=folium.Popup("""
            <div style="font-family: 'Segoe UI', Arial, sans-serif; width: 260px; line-height: 1.4;">
                <div style="color: #0984e3; font-weight: bold; font-size: 13.5px; margin-bottom: 2px;">⛲ Pileta de Jardines (Sala Capitular)</div>
                <span style="background: #e0f2fe; color: #0369a1; padding: 2px 6px; border-radius: 4px; font-size: 10px; font-weight: 600;">Fuente Ornamental Exterior</span>
                <p style="margin: 6px 0 4px 0; font-size: 11.5px; color: #34495e;">
                    <b>Estado Físico:</b> Permanece seca habitualmente.<br>
                    <b>Riesgo Entomológico:</b> Nulo para vectores (estructura ornamental seca sin estancamiento).
                </p>
                <div style="font-size: 10px; color: #7f8c8d; border-top: 1px solid #ecf0f1; padding-top: 3px;">
                    📍 GPS: 0.404346, -78.175689 | Jardines Exteriores San José
                </div>
            </div>
        """, max_width=280),
        tooltip="⛲ Pileta de Jardines: Fuente Ornamental Exterior (Seca)"
    ).add_to(fg_canales)

    # Pileta de Agua (Sector Sala Capitular)
    folium.Marker(
        location=[0.4042981, -78.1751977],
        icon=folium.Icon(icon='tint', prefix='fa', color='blue'),
        popup=folium.Popup("""
            <div style="font-family: 'Segoe UI', Arial, sans-serif; width: 260px; line-height: 1.4;">
                <div style="color: #0984e3; font-weight: bold; font-size: 13.5px; margin-bottom: 2px;">⛲ Pileta de Agua (Sector Sala Capitular)</div>
                <span style="background: #e0f2fe; color: #0369a1; padding: 2px 6px; border-radius: 4px; font-size: 10px; font-weight: 600;">Fuente Ornamental Exterior</span>
                <p style="margin: 6px 0 4px 0; font-size: 11.5px; color: #34495e;">
                    <b>Estado Físico:</b> Fuente ornamental exterior contigua a la Sala Capitular.<br>
                    <b>Riesgo Entomológico:</b> Nulo para vectores si se mantiene limpia y sin acumulación de agua estancada.
                </p>
                <div style="font-size: 10px; color: #7f8c8d; border-top: 1px solid #ecf0f1; padding-top: 3px;">
                    📍 GPS: 0.404298, -78.175198 | Sector Sala Capitular
                </div>
            </div>
        """, max_width=280),
        tooltip="⛲ Pileta de Agua: Fuente Ornamental (Sector Sala Capitular)"
    ).add_to(fg_canales)

    # Molino de Agua (Patrimonial, Fuera de Uso)
    folium.Marker(
        location=[0.4053046, -78.1748750],
        icon=folium.Icon(icon='cog', prefix='fa', color='purple'),
        popup=folium.Popup("""
            <div style="font-family: 'Segoe UI', Arial, sans-serif; width: 260px; line-height: 1.4;">
                <div style="color: #8e44ad; font-weight: bold; font-size: 13.5px; margin-bottom: 2px;">⚙️ Molino de Agua (Patrimonial, Fuera de Uso)</div>
                <span style="background: #f3e5f5; color: #7b1fa2; padding: 2px 6px; border-radius: 4px; font-size: 10px; font-weight: 600;">Patrimonio Industrial Hidráulico (No en Uso)</span>
                <p style="margin: 6px 0 4px 0; font-size: 11.5px; color: #34495e;">
                    <b>Régimen Hidráulico:</b> Rueda y canaleta histórica de la antigua Hacienda San José. Actualmente no está en uso; sin flujo motriz ni molienda activa.
                </p>
                <div style="font-size: 10px; color: #7f8c8d; border-top: 1px solid #ecf0f1; padding-top: 3px;">
                    📍 GPS: 0.405305, -78.174875 | Sector Aulas I / Biblioteca
                </div>
            </div>
        """, max_width=280),
        tooltip="⚙️ Molino de Agua: Patrimonio Hidráulico del Ingenio (No en Uso)"
    ).add_to(fg_canales)

    # -------------------------------------------------------------
    # 6. BIOCONTROL ACUÁTICO (LIBÉLULAS + Bti)
    # -------------------------------------------------------------
    puntos_biocontrol = [
        ([0.4072, -78.1705], "Bio-Estación Hídrica Norte", "Sector Canal Senescyt"),
        ([0.4048, -78.1720], "Bio-Estación Hídrica Central", "Sector Canal Laboratorios"),
        ([0.4028, -78.1726], "Bio-Estación Hídrica Sur", "Sector Canal Canchas y Residencias")
    ]
    for pt, titulo, detalle in puntos_biocontrol:
        folium.CircleMarker(
            location=pt,
            radius=8,
            color="#0984e3",
            fill=True,
            fill_color="#74b9ff",
            fill_opacity=0.9,
            popup=folium.Popup(f"""
                <div style="font-family: 'Segoe UI', Arial, sans-serif; width: 250px;">
                    <h4 style="color: #0984e3; margin: 0 0 4px 0;">🦗 {titulo}</h4>
                    <span style="color: #636e72; font-size: 11px;">{detalle}</span>
                    <p style="font-size: 12px; color: #2d3436; margin: 8px 0 0 0;">
                        • <b>Ninfas de Libélula (Odonata):</b> Depredador voraz y natural de larvas acuáticas.<br>
                        • <b>Micro-larvicida Bti:</b> <i>Bacillus thuringiensis israelensis</i>, 100% inocuo para humanos, peces, aves y abejas.
                    </p>
                </div>
            """, max_width=270),
            tooltip=f"🦗 {titulo} (Depredación Natural y Bti)"
        ).add_to(fg_biocontrol)

    # -------------------------------------------------------------
    # 7. CERCAS VIVAS EN 3 ESTRATOS (980 METROS ÓPTIMOS)
    # -------------------------------------------------------------
    cerca1 = [
        [0.4031, -78.1750],
        [0.4030, -78.1738],
        [0.4024, -78.1730]
    ]
    folium.PolyLine(
        locations=cerca1,
        color="#10ac84",
        weight=6,
        popup=folium.Popup("""
            <div style="font-family: 'Segoe UI', Arial, sans-serif; width: 280px;">
                <div style="background: #10ac84; color: white; padding: 6px 10px; border-radius: 6px 6px 0 0; font-weight: bold; font-size: 13px;">
                    🌿 Cerca Viva 1 · Sector Residencial (380m)
                </div>
                <div style="padding: 10px; border: 1px solid #10ac84; border-top: none; border-radius: 0 0 6px 6px; font-size: 12px;">
                    <b>🌱 Arquitectura en 3 Estratos Hipoalergénica:</b><br>
                    • <b>Alto (3.5-5m):</b> <i>Schinus molle</i> (Molle andino) - Cortina rompeviento y sombra.<br>
                    • <b>Medio (1.2-2m · Buffer Hipoalergénico):</b> <i>Myrcianthes hallii</i> (Arrayán nativo) combinado con <i>Aloysia citrodora</i> (Cedrón) y <i>Tagetes minuta</i> (Huacatay). <b>100% libre de Romero a <5m de dormitorios</b> para proteger a residentes con alergias respiratorias o asma.<br>
                    • <b>Bajo (0.4-0.8m):</b> <i>Cymbopogon citratus</i> (Hierba luisa) - Perfume cítrico y barrera basal de citronelal.<br>
                    <div style="margin-top: 6px; padding: 5px; background: #e8f8f5; border-radius: 4px; color: #0e6251;">
                        <b>🛡️ Inclusión Médica:</b> Blindaje fitoquímico seguro para Las Multis, Las T's y Las Pats con cero irritación bronquial.
                    </div>
                </div>
            </div>
        """, max_width=300),
        tooltip="🌿 Cerca Viva 1: Corredor Residencial (380m) - Confort y Protección"
    ).add_to(fg_cercas)

    cerca2 = [
        [0.4055, -78.1734],
        [0.4048, -78.1728],
        [0.4040, -78.1726]
    ]
    folium.PolyLine(
        locations=cerca2,
        color="#10ac84",
        weight=6,
        popup=folium.Popup("""
            <div style="font-family: 'Segoe UI', Arial, sans-serif; width: 280px;">
                <div style="background: #10ac84; color: white; padding: 6px 10px; border-radius: 6px 6px 0 0; font-weight: bold; font-size: 13px;">
                    🌿 Cerca Viva 2 · Sector Ingenio / Laboratorios (280m)
                </div>
                <div style="padding: 10px; border: 1px solid #10ac84; border-top: none; border-radius: 0 0 6px 6px; font-size: 12px;">
                    <b>🌱 Arquitectura en 3 Estratos:</b><br>
                    • <b>Alto:</b> <i>Schinus molle</i> (Cortina contra vientos del valle).<br>
                    • <b>Medio:</b> <i>Lantana camara</i> y Lavanda (Flores melíferas para polinizadores).<br>
                    • <b>Bajo:</b> <i>Cymbopogon citratus</i> (Aroma cítrico continuo).<br>
                    <div style="margin-top: 6px; padding: 5px; background: #e8f8f5; border-radius: 4px; color: #0e6251;">
                        <b>✨ Impacto en el Estudio:</b> Permite disfrutar las caminerías históricas y estudiar en áreas abiertas del Ingenio.
                    </div>
                </div>
            </div>
        """, max_width=300),
        tooltip="🌿 Cerca Viva 2: Corredor Histórico / Laboratorios (280m)"
    ).add_to(fg_cercas)

    cerca3 = [
        [0.4072, -78.1718],
        [0.4066, -78.1710],
        [0.4060, -78.1702]
    ]
    folium.PolyLine(
        locations=cerca3,
        color="#10ac84",
        weight=6,
        popup=folium.Popup("""
            <div style="font-family: 'Segoe UI', Arial, sans-serif; width: 280px;">
                <div style="background: #10ac84; color: white; padding: 6px 10px; border-radius: 6px 6px 0 0; font-weight: bold; font-size: 13px;">
                    🌿 Cerca Viva 3 · Sector Senescyt / Los Bloques (320m)
                </div>
                <div style="padding: 10px; border: 1px solid #10ac84; border-top: none; border-radius: 0 0 6px 6px; font-size: 12px;">
                    <b>🌱 Arquitectura en 3 Estratos:</b><br>
                    • <b>Alto:</b> <i>Schinus molle</i>.<br>
                    • <b>Medio:</b> <i>Myrcianthes hallii</i> (Arrayán) con Cedrón en dormitorios y Romero confinado al talud abierto del canal.<br>
                    • <b>Bajo:</b> <i>Cymbopogon citratus</i>.<br>
                    <div style="margin-top: 6px; padding: 5px; background: #e8f8f5; border-radius: 4px; color: #0e6251;">
                        <b>✨ Impacto Académico:</b> Ventilación natural en aulas Senescyt y descanso protegido sin alérgenos en Los Bloques.
                    </div>
                </div>
            </div>
        """, max_width=300),
        tooltip="🌿 Cerca Viva 3: Corredor Académico Senescyt / Los Bloques (320m)"
    ).add_to(fg_cercas)

    # -------------------------------------------------------------
    # 8. BUFFERS DE COBERTURA Y AROMATERAPIA (40 METROS)
    # -------------------------------------------------------------
    for c_coords, c_name, c_desc in [
        (cerca1, "Zona Protegida Residencias", "Cubre Las Multis, Patrimoniales y Concha Acústica"),
        (cerca2, "Zona Protegida Ingenio", "Cubre Biblioteca, Chimenea y Caminerías"),
        (cerca3, "Zona Protegida Senescyt", "Cubre Aulas Ed. Senescyt y Residencias Los Bloques")
    ]:
        folium.PolyLine(
            locations=c_coords,
            color="#2ecc71",
            weight=36,
            opacity=0.25,
            popup=folium.Popup(f"""
                <div style="font-family: 'Segoe UI', Arial, sans-serif; width: 240px;">
                    <b style="color: #27ae60;">🛡️ {c_name} (Buffer 40m)</b><br>
                    <span style="font-size: 12px; color: #2c3e50;">{c_desc}</span><br>
                    <p style="font-size: 11px; color: #555; margin: 4px 0 0 0;">
                        Los monoterpenos volátiles (citronelal, cineol, pineno) saturan los receptores olfativos de las arenillas, impidiendo que ubiquen a las personas.
                    </p>
                </div>
            """, max_width=260),
            tooltip=f"🛡️ Área de Confort y Protección Aromática ({c_name})"
        ).add_to(fg_buffer)

    # -------------------------------------------------------------
    # 9. RED DE BIO-MONITOREO DE BIENESTAR COMUNITARIO
    # -------------------------------------------------------------
    trampas_humanas = [
        ([0.4024, -78.1730], "Estación Sur 1", "Residencias Patrimoniales y Canchas Deportivas"),
        ([0.4028, -78.1750], "Estación Sur 2", "Las Multis y Concha Acústica"),
        ([0.4052, -78.1742], "Estación Central 1", "Biblioteca Patrimonial y Jardines"),
        ([0.4047, -78.1724], "Estación Central 2", "Acceso a Laboratorios de Carrera"),
        ([0.4067, -78.1702], "Estación Norte 1", "Edificio Senescyt (Fachada Aulas)"),
        ([0.4070, -78.1714], "Estación Norte 2", "Residencias Los Bloques y Vida Comunitaria")
    ]
    for pt, codigo, ubicacion in trampas_humanas:
        folium.Marker(
            location=pt,
            icon=folium.Icon(icon="crosshairs", prefix="fa", color="darkblue"),
            popup=folium.Popup(f"""
                <div style="font-family: 'Segoe UI', Arial, sans-serif; width: 240px;">
                    <div style="color: #1e3799; font-weight: bold; font-size: 13px;">🎯 {codigo}</div>
                    <b>Lugar:</b> {ubicacion}<br>
                    <p style="font-size: 11px; color: #333; margin: 6px 0 0 0;">
                        <b>Cebo Ecológico:</b> Ácido L-láctico y fermentación bio-orgánica de CO2.<br>
                        <b>Misión:</b> Comprobar semanalmente la disminución del 82% en la molestia por picaduras reportada por la comunidad.
                    </p>
                </div>
            """, max_width=260),
            tooltip=f"🎯 {codigo}: Monitoreo de Bienestar ({ubicacion})"
        ).add_to(fg_trampas)

    # Agregar capas al mapa (fg_areas_verdes debajo de fg_edificios para preservar clicabilidad total de edificios)
    fg_distritos.add_to(m)
    fg_areas_verdes.add_to(m)
    fg_vias.add_to(m)
    fg_zonas.add_to(m)
    fg_canales.add_to(m)
    fg_biocontrol.add_to(m)
    fg_perimetros.add_to(m)
    fg_edificios.add_to(m)
    fg_cercas.add_to(m)
    fg_buffer.add_to(m)
    fg_trampas.add_to(m)

    # Controles estándar de Folium (collapsed=True evita colisión visual con la barra superior)
    folium.LayerControl(position='topright', collapsed=True).add_to(m)

    # Inyectar Favicon vectorial oficial en el <head>
    m.get_root().header.add_child(folium.Element('<link rel="icon" type="image/svg+xml" href="favicon.svg">'))

    mini_tile = folium.TileLayer(
        tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}',
        attr='Esri'
    )
    plugins.MiniMap(tile_layer=mini_tile, toggle_display=True, position='bottomleft').add_to(m)
    plugins.MeasureControl(position='topleft', primary_length_unit='meters', primary_area_unit='sqmeters').add_to(m)

    # Nombres de variables JS para interactividad directa
    map_var = m.get_name()
    distritos_var = fg_distritos.get_name()
    zonas_var = fg_zonas.get_name()
    cercas_var = fg_cercas.get_name()
    buffer_var = fg_buffer.get_name()
    canales_var = fg_canales.get_name()
    biocontrol_var = fg_biocontrol.get_name()
    trampas_var = fg_trampas.get_name()
    edificios_var = fg_edificios.get_name()
    dark_var = tile_dark.get_name()
    streets_var = tile_streets.get_name()

    # -------------------------------------------------------------
    # 10. INTERFAZ HUMANISTA, BILINGÜE, DARK/LIGHT Y QR (HTML + CSS + JS)
    # -------------------------------------------------------------
    interfaz_humanista_html = f"""
    <!-- ESTILOS ADAPTABLES: CLARO / OSCURO / MÓVIL -->
    <style>
        :root {{
            --bg-body: #ffffff;
            --bg-navbar: rgba(255, 255, 255, 0.94);
            --bg-panel: rgba(255, 255, 255, 0.96);
            --bg-card: #f8fafc;
            --border-color: #dcdde1;
            --border-accent: rgba(16, 172, 132, 0.35);
            --text-color: #2f3640;
            --text-muted: #57606f;
            --primary-color: #10ac84;
            --secondary-color: #1e3799;
            --shadow-card: 0 4px 20px rgba(0, 0, 0, 0.16);
            --btn-bg: #ffffff;
            --btn-text: #2f3640;
            --btn-hover: #f1f2f6;
        }}

        body[data-theme="dark"] {{
            --bg-body: #0f172a;
            --bg-navbar: rgba(15, 23, 42, 0.94);
            --bg-panel: rgba(30, 41, 59, 0.96);
            --bg-card: #1e293b;
            --border-color: #334155;
            --border-accent: rgba(46, 213, 115, 0.45);
            --text-color: #f1f2f6;
            --text-muted: #94a3b8;
            --primary-color: #2ed573;
            --secondary-color: #4a69bd;
            --shadow-card: 0 6px 25px rgba(0, 0, 0, 0.55);
            --btn-bg: #1e293b;
            --btn-text: #f1f2f6;
            --btn-hover: #334155;
        }}

        /* Adaptación de controles Leaflet en Modo Oscuro */
        body[data-theme="dark"] .leaflet-bar a {{
            background-color: #1e293b !important;
            color: #f1f2f6 !important;
            border-bottom: 1px solid #334155 !important;
        }}
        body[data-theme="dark"] .leaflet-bar a:hover {{
            background-color: #334155 !important;
            color: #2ed573 !important;
        }}
        body[data-theme="dark"] .leaflet-control-layers {{
            background: #1e293b !important;
            color: #f1f2f6 !important;
            border: 1px solid #334155 !important;
        }}
        body[data-theme="dark"] .leaflet-control-layers-expanded {{
            background: #1e293b !important;
            color: #f1f2f6 !important;
        }}
        /* Ventanas Emergentes (Popups) Semitransparentes con Glassmorphism */
        .leaflet-popup-content-wrapper {{
            background: rgba(255, 255, 255, 0.84) !important;
            backdrop-filter: blur(14px) saturate(180%) !important;
            -webkit-backdrop-filter: blur(14px) saturate(180%) !important;
            color: var(--text-color) !important;
            border-radius: 14px !important;
            box-shadow: 0 10px 32px rgba(0, 0, 0, 0.22) !important;
            padding: 4px 6px !important;
            border: 1px solid rgba(255, 255, 255, 0.65) !important;
        }}
        .leaflet-popup-tip {{
            background: rgba(255, 255, 255, 0.84) !important;
            backdrop-filter: blur(14px) !important;
            -webkit-backdrop-filter: blur(14px) !important;
        }}
        body[data-theme="dark"] .leaflet-popup-content-wrapper {{
            background: rgba(15, 23, 42, 0.86) !important;
            backdrop-filter: blur(14px) saturate(180%) !important;
            -webkit-backdrop-filter: blur(14px) saturate(180%) !important;
            color: #f1f2f6 !important;
            border: 1px solid rgba(255, 255, 255, 0.15) !important;
            box-shadow: 0 12px 35px rgba(0, 0, 0, 0.65) !important;
        }}
        body[data-theme="dark"] .leaflet-popup-tip {{
            background: rgba(15, 23, 42, 0.86) !important;
        }}
        /* Botón de Cierre Fácil y Prominente en Popups */
        .leaflet-popup-close-button {{
            width: 30px !important;
            height: 30px !important;
            line-height: 28px !important;
            font-size: 20px !important;
            font-weight: 700 !important;
            color: #475569 !important;
            background: rgba(0, 0, 0, 0.08) !important;
            border-radius: 50% !important;
            top: 8px !important;
            right: 8px !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            text-decoration: none !important;
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
            padding: 0 !important;
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.15) !important;
            z-index: 1000 !important;
            border: 1px solid rgba(255, 255, 255, 0.6) !important;
            cursor: pointer !important;
        }}
        .leaflet-popup-close-button:hover {{
            background: #ef4444 !important;
            color: #ffffff !important;
            transform: scale(1.12) rotate(90deg) !important;
            box-shadow: 0 4px 12px rgba(239, 68, 68, 0.45) !important;
            border-color: #ef4444 !important;
        }}
        body[data-theme="dark"] .leaflet-popup-close-button {{
            background: rgba(255, 255, 255, 0.14) !important;
            color: #cbd5e1 !important;
            border-color: rgba(255, 255, 255, 0.2) !important;
        }}
        body[data-theme="dark"] .leaflet-popup-close-button:hover {{
            background: #ef4444 !important;
            color: #ffffff !important;
        }}

        /* Transparencia en tarjetas interiores dentro de los popups */
        .leaflet-popup-content div[style*="background: #fff"],
        .leaflet-popup-content div[style*="background:#fff"],
        .leaflet-popup-content div[style*="background: #fffdfa"],
        .leaflet-popup-content div[style*="background: #fbfdff"],
        .leaflet-popup-content div[style*="background: #fffcfc"] {{
            background: rgba(255, 255, 255, 0.55) !important;
            backdrop-filter: blur(4px) !important;
            border-radius: 8px !important;
        }}
        body[data-theme="dark"] .leaflet-popup-content div[style*="background: #fff"],
        body[data-theme="dark"] .leaflet-popup-content div[style*="background:#fff"],
        body[data-theme="dark"] .leaflet-popup-content div[style*="background: #fffdfa"],
        body[data-theme="dark"] .leaflet-popup-content div[style*="background: #fbfdff"],
        body[data-theme="dark"] .leaflet-popup-content div[style*="background: #fffcfc"],
        body[data-theme="dark"] .leaflet-popup-content div[style*="background: #e8f8f5"],
        body[data-theme="dark"] .leaflet-popup-content div[style*="background: #eef2f7"] {{
            background: rgba(15, 23, 42, 0.65) !important;
            border-color: #334155 !important;
            color: #f1f2f6 !important;
            border-radius: 8px !important;
        }}
        body[data-theme="dark"] .leaflet-popup-content p,
        body[data-theme="dark"] .leaflet-popup-content span,
        body[data-theme="dark"] .leaflet-popup-content b,
        body[data-theme="dark"] .leaflet-popup-content div {{
            color: #f1f2f6 !important;
        }}

        .leaflet-container {{
            font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif !important;
            background: var(--bg-body);
        }}

        /* Barra de navegación superior (Storytelling Bar) */
        #story-nav-bar {{
            position: fixed;
            top: 14px;
            left: 50%;
            transform: translateX(-50%);
            z-index: 1000;
            background: var(--bg-navbar);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            padding: 6px 14px;
            border-radius: 30px;
            box-shadow: var(--shadow-card);
            border: 1px solid var(--border-accent);
            display: flex;
            align-items: center;
            gap: 6px;
            flex-wrap: wrap;
            max-width: 96vw;
            color: var(--text-color);
            transition: all 0.3s ease;
        }}

        .nav-btn {{
            background: var(--btn-bg);
            border: 1px solid var(--border-color);
            color: var(--btn-text);
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.25s ease;
            display: inline-flex;
            align-items: center;
            gap: 5px;
            outline: none;
            box-shadow: 0 1px 3px rgba(0,0,0,0.06);
        }}
        .nav-btn:hover {{
            background: var(--btn-hover);
            transform: translateY(-1px);
            box-shadow: 0 3px 8px rgba(0,0,0,0.12);
        }}
        .nav-btn-highlight {{
            background: var(--primary-color) !important;
            color: #ffffff !important;
            border-color: var(--primary-color) !important;
        }}
        .nav-btn-highlight:hover {{
            filter: brightness(0.95);
        }}
        .nav-btn-alert {{
            background: #f39c12 !important;
            color: #ffffff !important;
            border-color: #e67e22 !important;
        }}
        .nav-btn-alert:hover {{
            background: #d68910 !important;
        }}
        .nav-btn-info {{
            background: var(--secondary-color) !important;
            color: #ffffff !important;
            border-color: var(--secondary-color) !important;
        }}
        .nav-btn-info:hover {{
            filter: brightness(0.9);
        }}

        /* Leyenda visual intuitiva (Inferior Izquierda, sobre minimapa sin colisión) */
        #panel-leyenda {{
            position: fixed;
            bottom: 195px;
            left: 15px;
            z-index: 1001;
            background: var(--bg-panel);
            backdrop-filter: blur(8px);
            border-radius: 10px;
            box-shadow: var(--shadow-card);
            border: 1px solid var(--primary-color);
            width: 235px;
            font-size: 11px;
            overflow: hidden;
            transition: all 0.3s ease;
            color: var(--text-color);
        }}
        .leyenda-header {{
            background: var(--primary-color);
            color: white;
            padding: 6px 10px;
            font-weight: bold;
            display: flex;
            justify-content: space-between;
            align-items: center;
            cursor: pointer;
            font-size: 12px;
        }}
        .leyenda-content {{
            padding: 8px 10px;
            line-height: 1.6;
            color: var(--text-color);
        }}
        .leyenda-item {{
            display: flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 4px;
        }}
        .leyenda-badge {{
            width: 14px;
            height: 14px;
            border-radius: 3px;
            display: inline-block;
            flex-shrink: 0;
        }}

        /* Dashboard flotante humanista (Inferior Derecha) */
        #dashboard-flotante {{
            position: fixed;
            bottom: 25px;
            right: 25px;
            width: 330px;
            z-index: 9999;
            background: var(--bg-panel);
            border: 2px solid var(--primary-color);
            border-radius: 14px;
            box-shadow: var(--shadow-card);
            font-family: 'Segoe UI', -apple-system, sans-serif;
            overflow: hidden;
            transition: all 0.3s ease;
            color: var(--text-color);
        }}
        .dash-header {{
            background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
            color: white;
            padding: 10px 14px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .dash-body {{
            padding: 12px 16px;
        }}
        .toggle-btn {{
            background: rgba(255, 255, 255, 0.25);
            border: none;
            color: white;
            font-weight: bold;
            border-radius: 50%;
            width: 22px;
            height: 22px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 12px;
        }}
        .toggle-btn:hover {{
            background: rgba(255, 255, 255, 0.4);
        }}

        /* Modales (Bienvenida y Código QR) */
        .modal-overlay {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background: rgba(12, 36, 97, 0.65);
            backdrop-filter: blur(6px);
            z-index: 10000;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
            animation: fadeIn 0.3s ease;
        }}
        .modal-card {{
            background: rgba(255, 255, 255, 0.88) !important;
            backdrop-filter: blur(16px) saturate(180%) !important;
            -webkit-backdrop-filter: blur(16px) saturate(180%) !important;
            color: var(--text-color);
            max-width: 620px;
            width: 100%;
            border-radius: 18px;
            box-shadow: 0 20px 50px rgba(0,0,0,0.35);
            border: 1px solid rgba(255, 255, 255, 0.65);
            overflow: hidden;
            animation: slideUp 0.35s ease;
            position: relative;
        }}
        body[data-theme="dark"] .modal-card {{
            background: rgba(15, 23, 42, 0.88) !important;
            backdrop-filter: blur(16px) saturate(180%) !important;
            -webkit-backdrop-filter: blur(16px) saturate(180%) !important;
            border: 1px solid rgba(255, 255, 255, 0.15);
        }}
        /* Botón de Cierre Circular Prominente y Accesible (Solo icono X para sencillez de uso) */
        .btn-modal-close-round {{
            position: absolute;
            top: 14px;
            right: 16px;
            width: 36px;
            height: 36px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.22);
            border: 2px solid rgba(255, 255, 255, 0.85);
            color: #ffffff;
            font-size: 19px;
            font-weight: 700;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            z-index: 50;
            transition: all 0.2s ease;
            box-shadow: 0 3px 10px rgba(0, 0, 0, 0.25);
            line-height: 1;
            padding: 0;
            outline: none;
        }}
        .btn-modal-close-round:hover {{
            background: #ef4444;
            border-color: #ef4444;
            transform: scale(1.12) rotate(90deg);
            box-shadow: 0 4px 14px rgba(239, 68, 68, 0.5);
        }}
        .modal-header {{
            background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
            color: white;
            padding: 18px 24px;
            position: relative;
        }}
        .modal-body {{
            padding: 22px 24px;
            line-height: 1.55;
            font-size: 13.5px;
            max-height: 70vh;
            overflow-y: auto;
        }}
        .card-pilar {{
            background: var(--bg-card);
            border-left: 4px solid var(--primary-color);
            padding: 10px 14px;
            margin: 10px 0;
            border-radius: 0 8px 8px 0;
            border-top: 1px solid var(--border-color);
            border-right: 1px solid var(--border-color);
            border-bottom: 1px solid var(--border-color);
        }}
        .modal-btn-close {{
            background: var(--primary-color);
            color: white;
            border: none;
            padding: 10px 22px;
            border-radius: 25px;
            font-weight: 700;
            cursor: pointer;
            font-size: 13.5px;
            box-shadow: 0 4px 12px rgba(16, 172, 132, 0.35);
            transition: all 0.2s ease;
        }}
        .modal-btn-close:hover {{
            filter: brightness(0.92);
            transform: translateY(-1px);
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; }}
            to {{ opacity: 1; }}
        }}
        @keyframes slideUp {{
            from {{ transform: translateY(20px); opacity: 0; }}
            to {{ transform: translateY(0); opacity: 1; }}
        }}

        @media (max-width: 860px) {{
            #story-nav-bar {{
                top: 8px;
                padding: 5px 8px;
                gap: 5px;
                overflow-x: auto;
                white-space: nowrap;
                flex-wrap: nowrap;
                justify-content: flex-start;
                max-width: 95vw;
                -webkit-overflow-scrolling: touch;
                scrollbar-width: none;
            }}
            #story-nav-bar::-webkit-scrollbar {{
                display: none;
            }}
            .nav-btn {{
                padding: 5px 10px;
                font-size: 11px;
                flex-shrink: 0;
            }}
            #dashboard-flotante {{
                width: 280px;
                bottom: 15px;
                right: 15px;
            }}
            #panel-leyenda {{
                width: 200px;
                bottom: 185px;
            }}
        }}
    </style>

    <!-- BARRA SUPERIOR DE NAVEGACIÓN Y STORYTELLING -->
    <div id="story-nav-bar">
        <!-- Logo / Marca: Abre modal del equipo -->
        <div id="nav-brand" style="display: flex; align-items: center; gap: 7px; padding: 2px 10px 2px 4px; border-right: 1px solid var(--border-color); cursor: pointer; border-radius: 8px; transition: background 0.2s;" onclick="toggleModalEquipo(true)" title="Clic para ver Integrantes del Equipo y Detalles" onmouseover="this.style.background='rgba(16,172,132,0.12)'" onmouseout="this.style.background='transparent'">
            <svg width="24" height="24" viewBox="0 0 100 100">
                <rect width="100" height="100" rx="26" fill="url(#brandGrad)"/>
                <defs>
                    <linearGradient id="brandGrad" x1="0%" y1="100%" x2="100%" y2="0%">
                        <stop offset="0%" stop-color="#1e3799"/>
                        <stop offset="50%" stop-color="#10ac84"/>
                        <stop offset="100%" stop-color="#2ecc71"/>
                    </linearGradient>
                </defs>
                <path d="M 50 14 C 28 32, 22 66, 50 86 C 78 66, 72 32, 50 14 Z" fill="#ffffff" opacity="0.95"/>
                <path d="M 50 20 L 50 80" stroke="#10ac84" stroke-width="4" stroke-linecap="round"/>
                <circle cx="36" cy="50" r="4.5" fill="#1e3799"/>
                <circle cx="64" cy="50" r="4.5" fill="#1e3799"/>
                <circle cx="50" cy="22" r="5" fill="#f39c12"/>
            </svg>
            <div style="display: flex; flex-direction: column; line-height: 1.15;">
                <span style="font-weight: 800; font-size: 13px; color: var(--text-color); letter-spacing: -0.3px;">Algoritmo Verde (YT)</span>
                <span style="font-size: 9.5px; font-weight: 700; color: #10ac84;">👥 Conoce al Equipo &raquo;</span>
            </div>
        </div>

        <button id="btn-info" class="nav-btn nav-btn-info" onclick="toggleModalBienvenida(true)" title="Conocer el propósito humano del proyecto">
            ℹ️ <span data-i18n="nav_vision">Visión y Propósito</span>
        </button>
        <button id="btn-solucion" class="nav-btn nav-btn-highlight" onclick="activarModoSolucion()" title="Ver la solución ecológica activa">
            🌿 <span data-i18n="nav_solution">Solución Verde (Activa)</span>
        </button>
        <button id="btn-diagnostico" class="nav-btn" onclick="activarModoDiagnostico()" title="Ver mapa de calor continuo y focos epidemiológicos de picaduras">
            🔥 <span data-i18n="nav_diagnosis">Ver Mapa de Calor</span>
        </button>
        <span style="color: var(--border-color); margin: 0 2px;">|</span>
        <button class="nav-btn" onclick="irAZona('senescyt')" title="Enfocar Sector Senescyt (Aulas, Bloques, Centro Médico)">
            🏛️ <span data-i18n="nav_senescyt">1. Senescyt</span>
        </button>
        <button class="nav-btn" onclick="irAZona('ingenio')" title="Enfocar Sector Ingenio Azucarero (Aulas B/I, Biblioteca, Mikuna)">
            🏭 <span data-i18n="nav_ingenio">2. Ingenio Azucarero</span>
        </button>
        <button class="nav-btn" onclick="irAZona('residencias')" title="Enfocar Sector Las Pats y Multis (T's, Docentes, Deportes)">
            🏡 <span data-i18n="nav_residencias">3. Las Pats y Multis</span>
        </button>
        <button class="nav-btn" onclick="irAZona('general')" title="Restablecer vista completa del campus">
            🔭 <span data-i18n="nav_campus">Vista Campus</span>
        </button>
        <span style="color: var(--border-color); margin: 0 2px;">|</span>
        <!-- Botón Código QR para celular / Pitch -->
        <button id="btn-qr" class="nav-btn" onclick="toggleModalQR(true)" title="Escanear con celular o descargar para presentación">
            📱 <span data-i18n="nav_qr">Código QR</span>
        </button>
        <!-- Alternador Tema Claro / Oscuro -->
        <button id="btn-theme" class="nav-btn" onclick="toggleTema()" title="Cambiar Tema Claro / Oscuro">
            <span id="theme-icon">🌙</span> <span id="theme-label" data-i18n="nav_theme">Oscuro</span>
        </button>
        <!-- Selector Bilingüe ES / EN -->
        <button id="btn-lang" class="nav-btn" onclick="toggleIdioma()" title="Switch Language / Cambiar Idioma" style="font-weight: 700; color: var(--primary-color);">
            🌐 <span id="lang-label">EN</span>
        </button>
    </div>

    <!-- LEYENDA VISUAL ACCESIBLE (Encima del minimapa) -->
    <div id="panel-leyenda">
        <div class="leyenda-header" onclick="toggleLeyenda()">
            <span data-i18n="leyenda_title">📋 Simbología Humanista</span>
            <span id="leyenda-icon-toggle">−</span>
        </div>
        <div id="leyenda-body" class="leyenda-content">
            <div class="leyenda-item">
                <span class="leyenda-badge" style="background: linear-gradient(to right, #2ecc71, #f1c40f, #e67e22, #e74c3c, #8e44ad); border-radius: 2px;"></span>
                <span data-i18n="leyenda_heat"><b>Mapa de Calor:</b> Presión hematófaga (Simulium spp.)</span>
            </div>
            <div class="leyenda-item">
                <span class="leyenda-badge" style="background: rgba(46, 204, 113, 0.4); border: 1px solid #27ae60;"></span>
                <span data-i18n="leyenda_safe"><b>Zona Segura:</b> Aromaterapia natural y aire limpio</span>
            </div>
            <div class="leyenda-item">
                <span class="leyenda-badge" style="background: #10ac84;"></span>
                <span data-i18n="leyenda_fences"><b>Cercas Vivas:</b> 3 estratos (Molle, Arrayán, H. Luisa)</span>
            </div>
            <div class="leyenda-item">
                <span class="leyenda-badge" style="background: #0abde3;"></span>
                <span data-i18n="leyenda_canals"><b>Canales Hídricos:</b> Biocontrol con Libélulas + Bti</span>
            </div>
            <div class="leyenda-item">
                <span class="leyenda-badge" style="background: #1e3799;"></span>
                <span data-i18n="leyenda_monitoring"><b>Bio-Monitoreo:</b> Validación continua del confort</span>
            </div>
            <div class="leyenda-item">
                <span class="leyenda-badge" style="background: #e74c3c;"></span>
                <span data-i18n="leyenda_life"><b>Hitos de Vida:</b> Residencias, aulas y cultura</span>
            </div>
            <div class="leyenda-item">
                <span class="leyenda-badge" style="background: #4b6584;"></span>
                <span data-i18n="leyenda_roads"><b>Red Vial (16):</b> Vías troncales y caminerías</span>
            </div>
            <div class="leyenda-item">
                <span class="leyenda-badge" style="background: rgba(82, 190, 128, 0.55); border: 1px dashed #1e8449;"></span>
                <span data-i18n="leyenda_greens"><b>Áreas Verdes (12):</b> Jardines y parques (~5.97 ha)</span>
            </div>
        </div>
    </div>

    <!-- DASHBOARD FLOTANTE HUMANISTA -->
    <div id="dashboard-flotante">
        <div class="dash-header">
            <div>
                <span style="font-weight: 700; font-size: 14px; letter-spacing: 0.3px;" data-i18n="dash_title">🌱 Algoritmo Verde YT</span><br>
                <span style="font-size: 11px; opacity: 0.9;" data-i18n="dash_sub">Yachay Open Science Week 2026</span>
            </div>
            <button class="toggle-btn" onclick="toggleDashboard()" title="Minimizar / Expandir panel" id="btn-dash-toggle">−</button>
        </div>
        <div id="dash-content" class="dash-body">
            <p style="margin: 0 0 8px 0; font-size: 11.5px; color: var(--text-muted); line-height: 1.35;" data-i18n="dash_desc">
                Reto 3: Manejo ecológico de arenillas que prioriza la salud, el estudio y la vida al aire libre en Yachay Tech.
            </p>
            <table style="width: 100%; font-size: 11.5px; line-height: 1.65; color: var(--text-color); border-collapse: collapse;">
                <tr>
                    <td data-i18n="dash_community">👥 <b>Comunidad Protegida:</b></td>
                    <td style="text-align: right; font-weight: 700; color: var(--secondary-color);" data-i18n="dash_community_val">~800+ personas</td>
                </tr>
                <tr>
                    <td data-i18n="dash_fences">🌿 <b>Cercas en 3 Estratos:</b></td>
                    <td style="text-align: right; font-weight: 700; color: var(--primary-color);" data-i18n="dash_fences_val">980 m lineales</td>
                </tr>
                <tr>
                    <td data-i18n="dash_comfort">🛡️ <b>Área de Confort:</b></td>
                    <td style="text-align: right; font-weight: 700; color: #009432;" data-i18n="dash_comfort_val">~39,200 m²</td>
                </tr>
                <tr>
                    <td data-i18n="dash_seedlings">🌳 <b>Plántulas Repelentes:</b></td>
                    <td style="text-align: right; font-weight: 700; color: var(--primary-color);" data-i18n="dash_seedlings_val">~1,960 plantas</td>
                </tr>
                <tr>
                    <td data-i18n="dash_chemicals">🚫 <b>Insecticidas Químicos:</b></td>
                    <td style="text-align: right; font-weight: 700; color: var(--primary-color);" data-i18n="dash_chemicals_val">0% (Cero toxicidad)</td>
                </tr>
                <tr>
                    <td data-i18n="dash_biocontrol">🦗 <b>Control Biológico:</b></td>
                    <td style="text-align: right; font-weight: 700; color: #0984e3;" data-i18n="dash_biocontrol_val">Libélulas + Bti</td>
                </tr>
                <tr>
                    <td data-i18n="dash_monitoring">🎯 <b>Bio-Monitoreo:</b></td>
                    <td style="text-align: right; font-weight: 700; color: var(--secondary-color);" data-i18n="dash_monitoring_val">6 estaciones GPS</td>
                </tr>
                <tr style="border-top: 1px dashed var(--border-color);">
                    <td data-i18n="dash_reduction">📉 <b>Mitigación Picaduras:</b></td>
                    <td style="text-align: right; font-weight: 800; color: #e74c3c; font-size: 12.5px;" data-i18n="dash_reduction_val">82% efectividad</td>
                </tr>
            </table>
            <div style="margin-top: 10px; font-size: 10.5px; color: var(--text-muted); text-align: center;" data-i18n="dash_hint">
                💡 <i>Usa los botones superiores para recorrer el campus</i>
            </div>
        </div>
    </div>

    <!-- MODAL DE BIENVENIDA Y PROPÓSITO HUMANISTA -->
    <!-- MODAL DE VISIÓN Y PROPÓSITO (CON BOTÓN DE CIERRE PROMINENTE Y FÁCIL) -->
    <div id="modal-bienvenida" class="modal-overlay" style="display: none;" onclick="if(event.target===this) toggleModalBienvenida(false)">
        <div class="modal-card">
            <div class="modal-header">
                <!-- Botón de Cierre Fácil y Prominente (Solo icono X) -->
                <button onclick="toggleModalBienvenida(false)" class="btn-modal-close-round" title="Cerrar ventana (Esc)" aria-label="Cerrar">✕</button>
                <h2 style="margin: 0; font-size: 19px; font-weight: 700; padding-right: 40px;" data-i18n="modal_title">🌱 Algoritmo Verde: Un Campus para Vivir y Estudiar en Paz</h2>
                <div style="font-size: 12px; opacity: 0.95; margin-top: 4px;" data-i18n="modal_sub">
                    Propuesta Multidisciplinar · YOSW 2026 Ideatón (Reto 3 - Control de Arenillas)
                </div>
            </div>
            <div class="modal-body">
                <p style="margin-top: 0; font-size: 13.5px;" data-i18n="modal_p1">
                    <b>¿Por qué existe este proyecto?</b><br>
                    En el campus de Yachay Tech, las picaduras diurnas de arenillas (<i>Simulium</i> spp.) afectan la concentración en clases, el descanso en residencias y el uso de espacios culturales. Nuestra propuesta <b>no es llenar el campus de venenos sintéticos</b>, sino devolverle la armonía al territorio mediante ciencia aplicada, ecología y diseño paisajístico.
                </p>

                <div class="card-pilar">
                    <b style="color: var(--primary-color); font-size: 13.5px;" data-i18n="modal_card1_title">👥 Las Personas Primero (Salud y Confort)</b><br>
                    <span data-i18n="modal_card1_desc">Protegemos a más de 800 residentes, docentes y trabajadores. Eliminamos el uso de pesticidas tóxicos protegiendo el aire que respiran los estudiantes en Las Multis, Los Bloques y aulas.</span>
                </div>

                <div class="card-pilar" style="border-left-color: #3498db;">
                    <b style="color: #2980b9; font-size: 13.5px;" data-i18n="modal_card2_title">🌿 Naturaleza que Protege e Inclusión Hipoalergénica</b><br>
                    <span data-i18n="modal_card2_desc">980 metros de barreras vivas blindando 124 edificaciones e infraestructuras. Diseño con <b>zonificación hipoalergénica</b>: en proximidad inmediata a dormitorios (Las Multis, Las T's, Las Pats y Los Bloques) el romero es sustituido por <b>Cedrón (Aloysia citrodora)</b> y <b>Huacatay (Tagetes minuta)</b> para resguardar a residentes con asma, rinitis o alergias a Lamiaceae.</span>
                </div>

                <div class="card-pilar" style="border-left-color: #0abde3;">
                    <b style="color: #0abde3; font-size: 13.5px;" data-i18n="modal_card3_title">💧 Agua Limpia y Biocontrol Respetuoso</b><br>
                    <span data-i18n="modal_card3_desc">Los canales de riego que cruzan Yachay alimentan los cultivos de Urcuquí. Nuestro control biológico usa <b>ninfas de libélulas nativas</b> y micro-larvicidas biológicos (Bti) que preservan la calidad del agua para las comunidades vecinas.</span>
                </div>

                <!-- Botones Inferiores Fáciles de Cerrar -->
                <div style="display: flex; gap: 12px; justify-content: center; margin-top: 22px; flex-wrap: wrap;">
                    <button class="modal-btn-close" onclick="toggleModalBienvenida(false)" style="background: linear-gradient(135deg, #10ac84, #1dd1a1); color: white; border: none; padding: 11px 22px; border-radius: 25px; font-weight: 700; font-size: 13.5px; cursor: pointer; box-shadow: 0 4px 14px rgba(16,172,132,0.4); display: flex; align-items: center; gap: 6px;">
                        <span>✨</span> <span data-i18n="modal_btn_explore">¡Explorar el Campus Protegido!</span>
                    </button>
                    <button onclick="toggleModalBienvenida(false)" style="background: #e2e8f0; color: #1e293b; border: 1px solid #cbd5e1; padding: 11px 20px; border-radius: 25px; font-weight: 700; font-size: 13.5px; cursor: pointer; display: flex; align-items: center; gap: 6px; transition: background 0.2s;" onmouseover="this.style.background='#cbd5e1'" onmouseout="this.style.background='#e2e8f0'">
                        <span>✕</span> <span>Cerrar Ventana</span>
                    </button>
                </div>
            </div>
        </div>
    </div>

    <!-- MODAL DE INTEGRANTES DEL EQUIPO Y DETALLES DEL PROYECTO -->
    <div id="modal-equipo" class="modal-overlay" style="display: none;" onclick="if(event.target===this) toggleModalEquipo(false)">
        <div class="modal-card" style="max-width: 640px;">
            <div class="modal-header" style="background: linear-gradient(135deg, #1e3799, #10ac84); position: relative; padding: 20px 24px;">
                <button onclick="toggleModalEquipo(false)" class="btn-modal-close-round" title="Cerrar ventana (Esc)" aria-label="Cerrar">✕</button>
                <div style="display: flex; align-items: center; gap: 12px;">
                    <div style="background: white; border-radius: 12px; padding: 6px; display: flex; align-items: center; justify-content: center; box-shadow: 0 3px 8px rgba(0,0,0,0.2);">
                        <svg width="32" height="32" viewBox="0 0 100 100">
                            <rect width="100" height="100" rx="26" fill="url(#brandGradModal)"/>
                            <defs>
                                <linearGradient id="brandGradModal" x1="0%" y1="100%" x2="100%" y2="0%">
                                    <stop offset="0%" stop-color="#1e3799"/>
                                    <stop offset="50%" stop-color="#10ac84"/>
                                    <stop offset="100%" stop-color="#2ecc71"/>
                                </linearGradient>
                            </defs>
                            <path d="M 50 18 C 36 28, 26 44, 26 62 C 26 76, 36 84, 50 84 C 64 84, 74 76, 74 62 C 74 44, 64 28, 50 18 Z" fill="#ffffff" opacity="0.95"/>
                            <path d="M 50 30 L 50 74 M 50 46 L 64 38 M 50 56 L 66 48 M 50 46 L 36 38 M 50 56 L 34 48" stroke="#10ac84" stroke-width="3.5" stroke-linecap="round"/>
                            <circle cx="50" cy="30" r="4.5" fill="#1e3799"/>
                            <circle cx="64" cy="38" r="3.5" fill="#1e3799"/>
                            <circle cx="66" cy="48" r="3.5" fill="#1e3799"/>
                            <circle cx="36" cy="38" r="3.5" fill="#1e3799"/>
                            <circle cx="34" cy="48" r="3.5" fill="#1e3799"/>
                        </svg>
                    </div>
                    <div>
                        <h2 style="margin: 0; font-size: 19px; font-weight: 800; color: white;">Equipo: Algoritmo Verde YT</h2>
                        <div style="font-size: 12px; opacity: 0.95; color: #e0f2fe; margin-top: 2px;">
                            Yachay Open Science Week 2026 · Reto 3 (Control Ecosistémico de Arenillas)
                        </div>
                    </div>
                </div>
            </div>

            <div class="modal-body" style="padding: 20px 24px; max-height: 72vh; overflow-y: auto;">
                <!-- Breve Resumen Ejecutivo del Proyecto -->
                <div style="background: var(--bg-card); border-left: 4px solid #10ac84; padding: 12px 16px; border-radius: 8px; margin-bottom: 16px;">
                    <div style="font-size: 13px; color: var(--text-color); line-height: 1.45;">
                        <b>🌱 Breves detalles del proyecto:</b> Estrategia de Manejo Integrado Ecosistémico estructurada en 3 pilares: (1) <b>Cercas vivas multiestrato repelentes</b> (980 m; Molle, Arrayán, Romero y Hierba Luisa); (2) <b>Biocontrol acuático</b> con odonatos nativos + microdosificación de <i>Bacillus thuringiensis israelensis</i> (Bti) en canales de riego; y (3) <b>Optimización matemática SLSQP</b> y bio-monitoreo telemétrico continuo.
                    </div>
                </div>

                <!-- Métricas Clave de Eficacia -->
                <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin-bottom: 18px; text-align: center;">
                    <div style="background: rgba(16,172,132,0.1); border: 1px solid rgba(16,172,132,0.3); border-radius: 8px; padding: 10px 6px;">
                        <div style="font-size: 18px; font-weight: 800; color: #10ac84;">-82.8%</div>
                        <div style="font-size: 10.5px; color: var(--text-muted); font-weight: 600;">Eficacia (p &lt; 0.001)</div>
                    </div>
                    <div style="background: rgba(41,128,185,0.1); border: 1px solid rgba(41,128,185,0.3); border-radius: 8px; padding: 10px 6px;">
                        <div style="font-size: 18px; font-weight: 800; color: #2980b9;">39,200 m²</div>
                        <div style="font-size: 10.5px; color: var(--text-muted); font-weight: 600;">Área de Confort</div>
                    </div>
                    <div style="background: rgba(230,126,34,0.1); border: 1px solid rgba(230,126,34,0.3); border-radius: 8px; padding: 10px 6px;">
                        <div style="font-size: 18px; font-weight: 800; color: #d35400;">$1,470 USD</div>
                        <div style="font-size: 10.5px; color: var(--text-muted); font-weight: 600;">Inversión ($1.50/m)</div>
                    </div>
                </div>

                <!-- Integrantes del Equipo -->
                <h3 style="margin: 0 0 10px 0; font-size: 14px; font-weight: 700; color: var(--text-color); display: flex; align-items: center; gap: 6px;">
                    <span>👥</span> <span>Integrantes del Equipo y Roles</span>
                </h3>

                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 10px; margin-bottom: 16px;">
                    <!-- Jefferson Conza -->
                    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 10px; padding: 11px 13px; display: flex; gap: 10px; align-items: flex-start;">
                        <div style="background: #1e3799; color: white; width: 34px; height: 34px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 13px; flex-shrink: 0;">JC</div>
                        <div style="line-height: 1.25;">
                            <div style="font-weight: 700; font-size: 13px; color: var(--text-color);">Jefferson Conza</div>
                            <div style="font-size: 11px; color: #10ac84; font-weight: 600;">Líder Técnico & Modelado Espacial</div>
                            <div style="font-size: 10.5px; color: var(--text-muted); margin-top: 2px;">Matemáticas / Computación</div>
                        </div>
                    </div>

                    <!-- Christopher Picuasi -->
                    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 10px; padding: 11px 13px; display: flex; gap: 10px; align-items: flex-start;">
                        <div style="background: #10ac84; color: white; width: 34px; height: 34px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 13px; flex-shrink: 0;">CP</div>
                        <div style="line-height: 1.25;">
                            <div style="font-weight: 700; font-size: 13px; color: var(--text-color);">Christopher Picuasi</div>
                            <div style="font-size: 11px; color: #10ac84; font-weight: 600;">Desarrollo de Software & SIG</div>
                            <div style="font-size: 10.5px; color: var(--text-muted); margin-top: 2px;">Computación (3.º sem.)</div>
                        </div>
                    </div>

                    <!-- Francisco Ibujes -->
                    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 10px; padding: 11px 13px; display: flex; gap: 10px; align-items: flex-start;">
                        <div style="background: #e67e22; color: white; width: 34px; height: 34px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 13px; flex-shrink: 0;">FI</div>
                        <div style="line-height: 1.25;">
                            <div style="font-weight: 700; font-size: 13px; color: var(--text-color);">Francisco Ibujes</div>
                            <div style="font-size: 11px; color: #e67e22; font-weight: 600;">Investigación Química & Bio-Repelencia</div>
                            <div style="font-size: 10.5px; color: var(--text-muted); margin-top: 2px;">Química (2.º sem.)</div>
                        </div>
                    </div>

                    <!-- Luis Collaguazo -->
                    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 10px; padding: 11px 13px; display: flex; gap: 10px; align-items: flex-start;">
                        <div style="background: #9b59b6; color: white; width: 34px; height: 34px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 13px; flex-shrink: 0;">LC</div>
                        <div style="line-height: 1.25;">
                            <div style="font-weight: 700; font-size: 13px; color: var(--text-color);">Luis Collaguazo</div>
                            <div style="font-size: 11px; color: #9b59b6; font-weight: 600;">Investigación Biológica & Salud</div>
                            <div style="font-size: 10.5px; color: var(--text-muted); margin-top: 2px;">Biomedicina (2.º sem.)</div>
                        </div>
                    </div>
                </div>

                <!-- Mentoría -->
                <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 10px; padding: 11px 16px; margin-bottom: 18px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;">
                    <div>
                        <span style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; color: var(--text-muted); font-weight: 700;">Mentor Asignado:</span>
                        <div style="font-size: 13px; font-weight: 700; color: var(--text-color);">Ing. José Luis Flores M.Sc.</div>
                    </div>
                    <div>
                        <span style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; color: var(--text-muted); font-weight: 700;">Institución:</span>
                        <div style="font-size: 13px; font-weight: 700; color: #1e3799;">Universidad Yachay Tech</div>
                    </div>
                </div>

                <!-- Botones Inferiores -->
                <div style="display: flex; gap: 10px; justify-content: center; flex-wrap: wrap;">
                    <button onclick="toggleModalEquipo(false); toggleModalBienvenida(true);" style="background: #10ac84; color: white; border: none; padding: 10px 18px; border-radius: 20px; font-size: 13px; font-weight: 600; cursor: pointer; display: flex; align-items: center; gap: 6px;">
                        <span>ℹ️</span> <span>Ver Visión y Propósito</span>
                    </button>
                    <button onclick="toggleModalEquipo(false)" style="background: #e2e8f0; color: #1e293b; border: 1px solid #cbd5e1; padding: 10px 18px; border-radius: 20px; font-size: 13px; font-weight: 600; cursor: pointer;">
                        ✕ Cerrar
                    </button>
                </div>
            </div>
        </div>
    </div>

    <!-- MODAL DE CÓDIGO QR PARA CELULAR Y PITCH -->
    <div id="modal-qr" class="modal-overlay" style="display: none;" onclick="if(event.target===this) toggleModalQR(false)">
        <div class="modal-card" style="max-width: 440px; text-align: center;">
            <div class="modal-header">
                <button onclick="toggleModalQR(false)" class="btn-modal-close-round" title="Cerrar ventana (Esc)" aria-label="Cerrar">✕</button>
                <h2 style="margin: 0; font-size: 18px; font-weight: 700;" data-i18n="qr_title">📱 Escanea con tu Celular</h2>
                <div style="font-size: 12px; opacity: 0.95; margin-top: 4px;" data-i18n="qr_sub">
                    Accede al Prototipo Interactivo en tiempo real
                </div>
            </div>
            <div class="modal-body" style="padding: 24px;">
                <div style="background: white; padding: 14px; border-radius: 12px; display: inline-block; box-shadow: 0 4px 15px rgba(0,0,0,0.12); border: 2px solid var(--primary-color);">
                    <img src="data:image/png;base64,{qr_b64}" alt="QR Algoritmo Verde" style="width: 210px; height: 210px; display: block; margin: 0 auto;">
                </div>
                <p style="margin: 14px 0 6px 0; font-size: 12.5px; color: var(--text-color);" data-i18n="qr_desc">
                    Apunta con la cámara de tu smartphone para explorar el mapa en vivo durante la presentación.
                </p>
                <div style="margin: 10px 0; font-family: monospace; font-size: 11px; background: var(--bg-card); padding: 8px; border-radius: 6px; word-break: break-all; color: var(--primary-color);">
                    https://jeffersonconza.github.io/algoritmo-verde-yosw2026/
                </div>
                <div style="margin-top: 16px; display: flex; gap: 10px; justify-content: center;">
                    <a href="data:image/png;base64,{qr_b64}" download="QR_Algoritmo_Verde_YT.png" class="modal-btn-close" style="text-decoration: none; display: inline-flex; align-items: center; gap: 6px; font-size: 12px; padding: 8px 18px;">
                        ⬇️ <span data-i18n="qr_download">Descargar PNG para Diapositivas</span>
                    </a>
                </div>
            </div>
        </div>
    </div>

    <!-- JAVASCRIPT DE INTERACTIVIDAD DINÁMICA, I18N Y TEMAS -->
    <script>
        // Getters perezosos y seguros para acceder a las instancias de Leaflet una vez inicializadas
        function getMap() {{ return window['{map_var}']; }}
        function getFGDistritos() {{ return window['{distritos_var}']; }}
        function getFGZonas() {{ return window['{zonas_var}']; }}
        function getFGCercas() {{ return window['{cercas_var}']; }}
        function getFGBuffer() {{ return window['{buffer_var}']; }}
        function getFGCanales() {{ return window['{canales_var}']; }}
        function getFGBiocontrol() {{ return window['{biocontrol_var}']; }}
        function getFGTrampas() {{ return window['{trampas_var}']; }}
        function getFGEdificios() {{ return window['{edificios_var}']; }}
        function getDarkLayer() {{ return window['{dark_var}']; }}
        function getStreetsLayer() {{ return window['{streets_var}']; }}

        // 1. Alternar modo Solución Verde
        function activarModoSolucion() {{
            var foliumMap = getMap();
            var fgCercas = getFGCercas();
            var fgBuffer = getFGBuffer();
            var fgBiocontrol = getFGBiocontrol();
            var fgTrampas = getFGTrampas();
            var fgEdificios = getFGEdificios();
            var fgZonas = getFGZonas();
            var fgDistritos = getFGDistritos();
            if (!foliumMap) return;

            if (fgDistritos && !foliumMap.hasLayer(fgDistritos)) foliumMap.addLayer(fgDistritos);

            if (fgCercas && !foliumMap.hasLayer(fgCercas)) foliumMap.addLayer(fgCercas);
            if (fgBuffer && !foliumMap.hasLayer(fgBuffer)) foliumMap.addLayer(fgBuffer);
            if (fgBiocontrol && !foliumMap.hasLayer(fgBiocontrol)) foliumMap.addLayer(fgBiocontrol);
            if (fgTrampas && !foliumMap.hasLayer(fgTrampas)) foliumMap.addLayer(fgTrampas);
            if (fgEdificios && !foliumMap.hasLayer(fgEdificios)) foliumMap.addLayer(fgEdificios);
            if (fgZonas && foliumMap.hasLayer(fgZonas)) foliumMap.removeLayer(fgZonas);

            var btnSol = document.getElementById('btn-solucion');
            var btnDiag = document.getElementById('btn-diagnostico');
            if (btnSol) btnSol.classList.add('nav-btn-highlight');
            if (btnDiag) btnDiag.classList.remove('nav-btn-alert');
        }}

        // 2. Alternar modo Diagnóstico de Afectación
        function activarModoDiagnostico() {{
            var foliumMap = getMap();
            var fgZonas = getFGZonas();
            var fgCanales = getFGCanales();
            var fgEdificios = getFGEdificios();
            var fgBuffer = getFGBuffer();
            if (!foliumMap) return;

            if (fgZonas && !foliumMap.hasLayer(fgZonas)) foliumMap.addLayer(fgZonas);
            if (fgCanales && !foliumMap.hasLayer(fgCanales)) foliumMap.addLayer(fgCanales);
            if (fgEdificios && !foliumMap.hasLayer(fgEdificios)) foliumMap.addLayer(fgEdificios);
            if (fgBuffer && foliumMap.hasLayer(fgBuffer)) foliumMap.removeLayer(fgBuffer);

            var btnSol = document.getElementById('btn-solucion');
            var btnDiag = document.getElementById('btn-diagnostico');
            if (btnDiag) btnDiag.classList.add('nav-btn-alert');
            if (btnSol) btnSol.classList.remove('nav-btn-highlight');
        }}

        // 3. Vuelos suaves a sectores clave (Storytelling)
        function irAZona(zona) {{
            var foliumMap = getMap();
            if (!foliumMap) return;
            if (zona === 'residencias') {{
                foliumMap.flyTo([0.4024, -78.1740], 17.5, {{ animate: true, duration: 1.2 }});
            }} else if (zona === 'ingenio') {{
                foliumMap.flyTo([0.4050, -78.1738], 17.5, {{ animate: true, duration: 1.2 }});
            }} else if (zona === 'senescyt') {{
                foliumMap.flyTo([0.4068, -78.1708], 17.5, {{ animate: true, duration: 1.2 }});
            }} else if (zona === 'general') {{
                foliumMap.flyTo([0.4048, -78.1725], 16, {{ animate: true, duration: 1.2 }});
            }}
        }}

        // 4. Modales
        function toggleModalBienvenida(show) {{
            var modal = document.getElementById('modal-bienvenida');
            if (modal) modal.style.display = show ? 'flex' : 'none';
        }}

        function toggleModalEquipo(show) {{
            var modal = document.getElementById('modal-equipo');
            if (modal) modal.style.display = show ? 'flex' : 'none';
        }}

        function toggleModalQR(show) {{
            var modal = document.getElementById('modal-qr');
            if (modal) modal.style.display = show ? 'flex' : 'none';
        }}

        // 5. Minimizar/Expandir Dashboard
        function toggleDashboard() {{
            var content = document.getElementById('dash-content');
            var btn = document.getElementById('btn-dash-toggle');
            if (!content || !btn) return;
            if (content.style.display === 'none') {{
                content.style.display = 'block';
                btn.innerHTML = '−';
            }} else {{
                content.style.display = 'none';
                btn.innerHTML = '+';
            }}
        }}

        // 6. Plegar/Desplegar Leyenda
        function toggleLeyenda() {{
            var body = document.getElementById('leyenda-body');
            var icon = document.getElementById('leyenda-icon-toggle');
            if (!body || !icon) return;
            if (body.style.display === 'none') {{
                body.style.display = 'block';
                icon.innerHTML = '−';
            }} else {{
                body.style.display = 'none';
                icon.innerHTML = '+';
            }}
        }}

        // 7. Alternador de Tema Claro / Oscuro
        function toggleTema() {{
            var body = document.body;
            var isDark = body.getAttribute('data-theme') === 'dark';
            var newTheme = isDark ? 'light' : 'dark';
            body.setAttribute('data-theme', newTheme);
            
            var icon = document.getElementById('theme-icon');
            var label = document.getElementById('theme-label');
            var foliumMap = getMap();
            var darkL = getDarkLayer();
            var streetL = getStreetsLayer();

            if (newTheme === 'dark') {{
                if (icon) icon.textContent = '☀️';
                if (label) label.textContent = (currentLang === 'es') ? 'Claro' : 'Light';
                if (foliumMap && darkL && !foliumMap.hasLayer(darkL)) {{
                    foliumMap.addLayer(darkL);
                }}
            }} else {{
                if (icon) icon.textContent = '🌙';
                if (label) label.textContent = (currentLang === 'es') ? 'Oscuro' : 'Dark';
                if (foliumMap && darkL && foliumMap.hasLayer(darkL)) {{
                    foliumMap.removeLayer(darkL);
                    if (streetL && !foliumMap.hasLayer(streetL)) foliumMap.addLayer(streetL);
                }}
            }}
        }}

        // 8. Motor de Internacionalización Bilingüe (i18n)
        var currentLang = 'es';
        var i18nDict = {{
            es: {{
                nav_vision: "Visión y Propósito",
                nav_solution: "Solución Verde (Activa)",
                nav_diagnosis: "Ver Mapa de Calor",
                nav_senescyt: "1. Senescyt",
                nav_ingenio: "2. Ingenio Azucarero",
                nav_residencias: "3. Las Pats y Multis",
                nav_campus: "Vista Campus",
                nav_qr: "Código QR",
                nav_theme: document.body.getAttribute('data-theme') === 'dark' ? "Claro" : "Oscuro",
                
                leyenda_title: "📋 Simbología Humanista",
                leyenda_heat: "<b>Mapa de Calor:</b> Presión hematófaga (Simulium spp.)",
                leyenda_safe: "<b>Zona Segura:</b> Aromaterapia natural y aire limpio",
                leyenda_fences: "<b>Cercas Vivas:</b> 3 estratos (Molle, Arrayán, H. Luisa)",
                leyenda_canals: "<b>Canales Hídricos:</b> Biocontrol con Libélulas + Bti",
                leyenda_monitoring: "<b>Bio-Monitoreo:</b> Validación continua del confort",
                leyenda_life: "<b>Hitos de Vida:</b> Residencias, aulas y cultura",
                leyenda_roads: "<b>Red Vial (16):</b> Vías troncales y caminerías",
                leyenda_greens: "<b>Áreas Verdes (12):</b> Jardines y parques (~5.97 ha)",
                
                dash_title: "🌱 Algoritmo Verde YT",
                dash_sub: "Yachay Open Science Week 2026",
                dash_desc: "Reto 3: Manejo ecológico de arenillas que prioriza la salud, el estudio y la vida al aire libre en Yachay Tech.",
                dash_community: "👥 <b>Comunidad Protegida:</b>",
                dash_community_val: "~800+ personas",
                dash_fences: "🌿 <b>Cercas en 3 Estratos:</b>",
                dash_fences_val: "980 m lineales",
                dash_comfort: "🛡️ <b>Área de Confort:</b>",
                dash_comfort_val: "~39,200 m²",
                dash_seedlings: "🌳 <b>Plántulas Repelentes:</b>",
                dash_seedlings_val: "~1,960 plantas",
                dash_chemicals: "🚫 <b>Insecticidas Químicos:</b>",
                dash_chemicals_val: "0% (Cero toxicidad)",
                dash_biocontrol: "🦗 <b>Control Biológico:</b>",
                dash_biocontrol_val: "Libélulas + Bti",
                dash_monitoring: "🎯 <b>Bio-Monitoreo:</b>",
                dash_monitoring_val: "6 estaciones GPS",
                dash_reduction: "📉 <b>Mitigación Picaduras:</b>",
                dash_reduction_val: "82% efectividad",
                dash_hint: "💡 <i>Usa los botones superiores para recorrer el campus</i>",

                modal_title: "🌱 Algoritmo Verde: Un Campus para Vivir y Estudiar en Paz",
                modal_sub: "Propuesta Multidisciplinar · YOSW 2026 Ideatón (Reto 3 - Control de Arenillas)",
                modal_p1: "<b>¿Por qué existe este proyecto?</b><br>En el campus de Yachay Tech, las picaduras diurnas de arenillas (<i>Simulium</i> spp.) afectan la concentración en clases, el descanso en residencias y el uso de espacios culturales. Nuestra propuesta <b>no es llenar el campus de venenos sintéticos</b>, sino devolverle la armonía al territorio mediante ciencia aplicada, ecología y diseño paisajístico.",
                modal_card1_title: "👥 Las Personas Primero (Salud y Confort)",
                modal_card1_desc: "Protegemos a más de 800 residentes, docentes y trabajadores. Eliminamos el uso de pesticidas tóxicos protegiendo el aire que respiran los estudiantes en Las Multis, Los Bloques y aulas.",
                modal_card2_title: "🌿 Naturaleza que Protege e Inclusión Hipoalergénica",
                modal_card2_desc: "980 metros de barreras vivas blindando 124 edificaciones con zonificación hipoalergénica: en proximidad a dormitorios (Las Multis, Las T's, Las Pats y Los Bloques) el romero se sustituye por Cedrón y Huacatay para proteger a residentes alérgicos o asmáticos.",
                modal_card3_title: "💧 Agua Limpia y Biocontrol Respetuoso",
                modal_card3_desc: "Los canales de riego que cruzan Yachay alimentan los cultivos de Urcuquí. Nuestro control biológico usa <b>ninfas de libélulas nativas</b> y micro-larvicidas biológicos (Bti) que preservan la calidad del agua para las comunidades vecinas.",
                modal_btn_explore: "✨ ¡Explorar el Campus Protegido!",

                qr_title: "📱 Escanea con tu Celular",
                qr_sub: "Accede al Prototipo Interactivo en tiempo real",
                qr_desc: "Apunta con la cámara de tu smartphone para explorar el mapa en vivo durante la presentación.",
                qr_download: "Descargar PNG para Diapositivas"
            }},
            en: {{
                nav_vision: "Vision & Purpose",
                nav_solution: "Green Solution (Active)",
                nav_diagnosis: "View Heatmap",
                nav_senescyt: "1. Senescyt",
                nav_ingenio: "2. Sugar Mill",
                nav_residencias: "3. Pats & Multis",
                nav_campus: "Campus Overview",
                nav_qr: "QR Code",
                nav_theme: document.body.getAttribute('data-theme') === 'dark' ? "Light" : "Dark",
                
                leyenda_title: "📋 Human-Centered Legend",
                leyenda_heat: "<b>Heatmap:</b> Biting pressure (Simulium spp.)",
                leyenda_safe: "<b>Safe Zone:</b> Natural aromatherapy & clean air",
                leyenda_fences: "<b>Living Fences:</b> 3 strata (Molle, Arrayan, Lemongrass)",
                leyenda_canals: "<b>Waterways:</b> Biocontrol with Dragonflies + Bti",
                leyenda_monitoring: "<b>Bio-Monitoring:</b> Continuous comfort tracking",
                leyenda_life: "<b>Campus Life:</b> Housing, classrooms & culture",
                leyenda_roads: "<b>Road Network (16):</b> Main roads & walkways",
                leyenda_greens: "<b>Green Areas (12):</b> Gardens & parks (~5.97 ha)",
                
                dash_title: "🌱 Algoritmo Verde YT",
                dash_sub: "Yachay Open Science Week 2026",
                dash_desc: "Challenge 3: Ecological blackfly management prioritizing health, study and outdoor living at Yachay Tech.",
                dash_community: "👥 <b>Protected Community:</b>",
                dash_community_val: "~800+ people",
                dash_fences: "🌿 <b>3-Strata Living Fences:</b>",
                dash_fences_val: "980 linear meters",
                dash_comfort: "🛡️ <b>Comfort Area:</b>",
                dash_comfort_val: "~39,200 m²",
                dash_seedlings: "🌳 <b>Repellent Seedlings:</b>",
                dash_seedlings_val: "~1,960 plants",
                dash_chemicals: "🚫 <b>Chemical Insecticides:</b>",
                dash_chemicals_val: "0% (Zero toxicity)",
                dash_biocontrol: "🦗 <b>Biological Control:</b>",
                dash_biocontrol_val: "Dragonflies + Bti",
                dash_monitoring: "🎯 <b>Bio-Monitoring:</b>",
                dash_monitoring_val: "6 GPS stations",
                dash_reduction: "📉 <b>Bite Reduction:</b>",
                dash_reduction_val: "82% effectiveness",
                dash_hint: "💡 <i>Use top buttons to explore the campus</i>",

                modal_title: "🌱 Algoritmo Verde: A Campus to Live and Study in Peace",
                modal_sub: "Multidisciplinary Proposal · YOSW 2026 Ideathon (Challenge 3 - Blackfly Control)",
                modal_p1: "<b>Why does this project exist?</b><br>At Yachay Tech campus, daytime blackfly bites (<i>Simulium</i> spp.) disrupt classroom concentration, residential sleep, and the use of cultural spaces. Our proposal <b>is not to drench the campus in synthetic poisons</b>, but to restore territorial harmony through applied science, ecology, and landscape design.",
                modal_card1_title: "👥 People First (Health & Comfort)",
                modal_card1_desc: "We protect over 800 residents, professors, and staff. We eliminate toxic pesticides, safeguarding the air students breathe in student housing and lecture halls.",
                modal_card2_title: "🌿 Nature that Protects & Hypoallergenic Inclusion",
                modal_card2_desc: "980 meters of living barriers shielding 124 buildings with hypoallergenic zoning: near dormitories (Multis, T's, Pats, Blocks), rosemary is replaced by Lemon Verbena and Huacatay to protect residents with asthma or allergies.",
                modal_card3_title: "💧 Clean Water & Respectful Biocontrol",
                modal_card3_desc: "The irrigation canals crossing Yachay nourish the agriculture of Urcuqui. Our biocontrol employs <b>native dragonfly nymphs</b> and microbial bio-larvicides (Bti) that preserve water quality for neighboring communities.",
                modal_btn_explore: "✨ Explore the Protected Campus!",

                qr_title: "📱 Scan with your Phone",
                qr_sub: "Access the Interactive Prototype in real time",
                qr_desc: "Point your smartphone camera to explore the live map during the pitch presentation.",
                qr_download: "Download PNG for Slides"
            }}
        }};

        function toggleIdioma() {{
            currentLang = (currentLang === 'es') ? 'en' : 'es';
            var langLabel = document.getElementById('lang-label');
            if (langLabel) langLabel.textContent = (currentLang === 'es') ? 'EN' : 'ES';
            aplicarIdioma(currentLang);
        }}

        function aplicarIdioma(lang) {{
            var dict = i18nDict[lang];
            if (!dict) return;
            
            var elements = document.querySelectorAll('[data-i18n]');
            elements.forEach(function(el) {{
                var key = el.getAttribute('data-i18n');
                if (key === 'nav_theme') {{
                    var isDark = document.body.getAttribute('data-theme') === 'dark';
                    el.innerHTML = isDark ? (lang === 'es' ? 'Claro' : 'Light') : (lang === 'es' ? 'Oscuro' : 'Dark');
                }} else if (dict[key]) {{
                    el.innerHTML = dict[key];
                }}
            }});
        }}

        // Cerrar modales con tecla Escape
        document.addEventListener('keydown', function(e) {{
            if (e.key === 'Escape') {{
                toggleModalBienvenida(false);
                toggleModalEquipo(false);
                toggleModalQR(false);
            }}
        }});

        // Mostrar bienvenida automáticamente cuando la ventana haya cargado
        window.addEventListener('load', function() {{
            setTimeout(function() {{
                toggleModalBienvenida(true);
            }}, 350);
        }});
    </script>
    """

    m.get_root().html.add_child(folium.Element(interfaz_humanista_html))

    output_path = os.path.join(base_dir, "mapa_interactivo_control_arenillas.html")
    m.save(output_path)
    print(f"Mapa generado exitosamente con Interfaz Humanista, Bilingüe y Dark Mode en: {output_path}")

if __name__ == "__main__":
    generar_mapa()
