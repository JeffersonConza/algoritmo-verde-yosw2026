"""
Generador del Visor Geoespacial Interactivo - Reto 3: Control de Arenillas
Equipo: Algoritmo Verde YT | Yachay Open Science Week 2026
Enfoque: Humanista, Bilingüe (ES/EN), Tema Claro/Oscuro, Identidad de Marca y Acceso Móvil QR
Calibrado con Coordenadas GPS Oficiales de Google Maps y Capas Base Optimizadas
"""

import os
import base64
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
    tile_hybrid = folium.TileLayer(
        tiles='https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}',
        attr='Google Maps Satellite',
        name='🛰️ Google Satélite Híbrido',
        overlay=False,
        control=True,
        max_zoom=20
    ).add_to(m)

    tile_streets = folium.TileLayer(
        tiles='https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
        attr='Google Maps Streets',
        name='🗺️ Google Callejero Oficial',
        overlay=False,
        control=True,
        max_zoom=20
    ).add_to(m)

    folium.TileLayer(
        tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}',
        attr='Esri World Street Map',
        name='🏙️ Esri Callejero (Calles y Campus)',
        overlay=False,
        control=True,
        max_zoom=19
    ).add_to(m)

    folium.TileLayer(
        tiles='https://{s}.tile.openstreetmap.de/{z}/{x}/{y}.png',
        attr='&copy; OpenStreetMap contributors',
        subdomains='abc',
        name='🌐 OpenStreetMap (FOSSGIS Libre)',
        overlay=False,
        control=True,
        max_zoom=19
    ).add_to(m)

    folium.TileLayer(
        tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        attr='Esri World Imagery',
        name='🌍 Satélite Esri (Fotografía Aérea)',
        overlay=False,
        control=True,
        max_zoom=19
    ).add_to(m)

    folium.TileLayer(
        tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}',
        attr='Esri World Topo Map',
        name='⛰️ Relieve y Topografía (Esri Topo)',
        overlay=False,
        control=True,
        max_zoom=19
    ).add_to(m)

    # 7. Modo Noche (Esri Dark Canvas - Alto contraste para presentaciones nocturnas)
    tile_dark = folium.TileLayer(
        tiles='https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Dark_Gray_Base/MapServer/tile/{z}/{y}/{x}',
        attr='Esri Dark Gray Canvas',
        name='🌌 Modo Noche (Esri Dark)',
        overlay=False,
        control=True,
        max_zoom=19
    ).add_to(m)

    # -------------------------------------------------------------
    # 2. FEATURE GROUPS (CAPAS TEMÁTICAS HUMANIZADAS)
    # -------------------------------------------------------------
    fg_zonas = folium.FeatureGroup(name="⚠️ Diagnóstico: Zonas de Molestia y Picaduras", show=False)
    fg_edificios = folium.FeatureGroup(name="🏛️ Vida en el Campus (Residencias, Aulas, Cultura)", show=True)
    fg_canales = folium.FeatureGroup(name="💧 Red Hídrica y Acequias (Focos Lóticos)", show=True)
    fg_biocontrol = folium.FeatureGroup(name="🦗 Biocontrol Acuático (Libélulas Nativas + Bti)", show=True)
    fg_cercas = folium.FeatureGroup(name="🌿 Cercas Vivas en 3 Estratos (Algoritmo Verde)", show=True)
    fg_buffer = folium.FeatureGroup(name="🛡️ Espacios Protegidos y Aromaterapia (Buffer 40m)", show=True)
    fg_trampas = folium.FeatureGroup(name="🎯 Bio-Monitoreo Continuo de Bienestar (6 Puntos)", show=True)

    # -------------------------------------------------------------
    # 3. POLÍGONOS DE ZONAS CRÍTICAS (CON ENFOQUE HUMANO)
    # -------------------------------------------------------------
    poly_z1 = [
        [0.4032, -78.1755],
        [0.4034, -78.1742],
        [0.4025, -78.1725],
        [0.4014, -78.1730],
        [0.4010, -78.1750],
        [0.4018, -78.1762]
    ]
    folium.Polygon(
        locations=poly_z1,
        color="#e67e22",
        weight=2,
        dash_array="6, 6",
        fill=True,
        fill_color="#f39c12",
        fill_opacity=0.20,
        popup=folium.Popup("""
            <div style="font-family: 'Segoe UI', Arial, sans-serif; width: 270px; line-height: 1.4;">
                <div style="background: #e67e22; color: white; padding: 6px 10px; border-radius: 6px 6px 0 0; font-weight: bold; font-size: 13px;">
                    ⚠️ Diagnóstico: Zona 1 - Hogar Estudiantil
                </div>
                <div style="padding: 10px; border: 1px solid #e67e22; border-top: none; border-radius: 0 0 6px 6px; background: #fffdfa;">
                    <b>👥 Comunidad Afectada:</b> ~320 estudiantes en Residencias Patrimoniales y Las Multis.<br>
                    <b>💔 Impacto Humano:</b> Picaduras dolorosas en horas de descanso y recreación en la Concha Acústica; interrupción del sueño y dermatitis.<br>
                    <b>🌿 Solución Verde:</b> Cerca Viva 1 (380m) de protección perimetral + aromaterapia con arrayán y molle.
                </div>
            </div>
        """, max_width=290),
        tooltip="Zona 1: Multifamiliares y Pats (Diagnóstico de Afectación)"
    ).add_to(fg_zonas)

    poly_z2 = [
        [0.4058, -78.1748],
        [0.4057, -78.1735],
        [0.4045, -78.1720],
        [0.4038, -78.1730],
        [0.4043, -78.1755]
    ]
    folium.Polygon(
        locations=poly_z2,
        color="#3498db",
        weight=2,
        dash_array="6, 6",
        fill=True,
        fill_color="#3498db",
        fill_opacity=0.20,
        popup=folium.Popup("""
            <div style="font-family: 'Segoe UI', Arial, sans-serif; width: 270px; line-height: 1.4;">
                <div style="background: #2980b9; color: white; padding: 6px 10px; border-radius: 6px 6px 0 0; font-weight: bold; font-size: 13px;">
                    ⚠️ Diagnóstico: Zona 2 - Corazón Académico
                </div>
                <div style="padding: 10px; border: 1px solid #2980b9; border-top: none; border-radius: 0 0 6px 6px; background: #fbfdff;">
                    <b>👥 Comunidad Afectada:</b> Estudiantes, docentes e investigadores en Biblioteca y Laboratorios.<br>
                    <b>💔 Impacto Humano:</b> Pérdida de concentración por ataque diurno constante de jejenes en caminerías patrimoniales.<br>
                    <b>🌿 Solución Verde:</b> Cerca Viva 2 (280m) que aísla las acequias y crea senderos perfumados con lavanda y hierba luisa.
                </div>
            </div>
        """, max_width=290),
        tooltip="Zona 2: Ingenio Azucarero (Diagnóstico de Afectación)"
    ).add_to(fg_zonas)

    poly_z3 = [
        [0.4076, -78.1720],
        [0.4076, -78.1698],
        [0.4060, -78.1695],
        [0.4058, -78.1712],
        [0.4068, -78.1718]
    ]
    folium.Polygon(
        locations=poly_z3,
        color="#e74c3c",
        weight=2,
        dash_array="6, 6",
        fill=True,
        fill_color="#e74c3c",
        fill_opacity=0.20,
        popup=folium.Popup("""
            <div style="font-family: 'Segoe UI', Arial, sans-serif; width: 270px; line-height: 1.4;">
                <div style="background: #c0392b; color: white; padding: 6px 10px; border-radius: 6px 6px 0 0; font-weight: bold; font-size: 13px;">
                    ⚠️ Diagnóstico: Zona 3 - Aulas y Comunidad
                </div>
                <div style="padding: 10px; border: 1px solid #c0392b; border-top: none; border-radius: 0 0 6px 6px; background: #fffcfc;">
                    <b>👥 Comunidad Afectada:</b> ~450 estudiantes y personal docente en Edificio Senescyt y Los Bloques.<br>
                    <b>💔 Impacto Humano:</b> Imposibilidad de abrir ventanas en clases por invasión de arenillas; estrés en exámenes y áreas de estudio.<br>
                    <b>🌿 Solución Verde:</b> Cerca Viva 3 (320m) con estrato alto rompevientos y reducción del 82% del ingreso de insectos.
                </div>
            </div>
        """, max_width=290),
        tooltip="Zona 3: Bloques y Senescyt (Diagnóstico de Afectación)"
    ).add_to(fg_zonas)

    # -------------------------------------------------------------
    # 4. ESPACIOS HUMANOS REALES DEL CAMPUS (HITOS GOOGLE MAPS)
    # -------------------------------------------------------------
    hitos_humanos = [
        # Zona 1: Vida Residencial y Recreativa
        ([0.402297, -78.173836], "Residencias Patrimoniales", "home", "green",
         "🏡 Hogar Estudiantil", "Alojamiento universitario patrimonial. Con el buffer verde, los estudiantes descansan sin zumbidos ni picaduras nocturnas."),
        ([0.402750, -78.174800], "Las Multis (Residencias)", "home", "green",
         "🏡 Residencias Las Multis", "Alta concentración juvenil. La barrera vegetal disminuye en 85% la presencia de arenillas en balcones y entradas."),
        ([0.402350, -78.175500], "Concha Acústica Yachay Tech", "music", "darkgreen",
         "🎭 Cultura y Esparcimiento", "Espacio emblemático al aire libre recuperado para conciertos, debates y actividades culturales sin picaduras."),
        ([0.402500, -78.171800], "Canchas Deportivas", "futbol-o", "cadetblue",
         "⚽ Salud y Deporte", "Área para fútbol y básquetbol. Los deportistas disfrutan de aire limpio sin necesidad de aplicarse repelentes pegajosos."),
        ([0.402550, -78.172800], "Parada Fasta (Arco Pats)", "bus", "gray",
         "🚌 Transporte Seguro", "Punto neurálgico de espera de buses. Espera cómoda bajo sombra vegetal."),
        
        # Zona 2: Investigación, Estudio y Patrimonio
        ([0.405072, -78.174159], "Biblioteca Patrimonial 'Yachay Tech'", "book", "blue",
         "📚 Sabiduría y Concentración", "Templo del estudio e investigación. Lectura tranquila en jardines y terrazas sin la distracción de insectos picadores."),
        ([0.405320, -78.174000], "Chimenea Ingenio Azucarero", "history", "purple",
         "🏛️ Patrimonio Histórico", "Símbolo de la memoria de Urcuquí. Integrado paisajísticamente con árboles de molle y flores melíferas."),
        ([0.404900, -78.173900], "Laboratorio de Química", "flask", "darkpurple",
         "🔬 Ciencia e Innovación", "Espacio donde la biotecnología se aplica para caracterizar los monoterpenos protectores."),
        ([0.404780, -78.172450], "Laboratorios de Carrera", "cogs", "darkpurple",
         "💻 Práctica Tecnológica", "Tránsito seguro entre naves de laboratorios y áreas experimentales."),

        # Zona 3: Aulas, Bienestar y Convivencia
        ([0.406691, -78.170214], "Edificio Senescyt (Yachay Tech)", "graduation-cap", "red",
         "🎓 Aulas y Aprendizaje", "Salas de clase con ventilación natural abierta, sin calor sofocante ni ingreso de plagas."),
        ([0.406950, -78.171150], "Residencias 'Los Bloques'", "bed", "darkred",
         "🛌 Descanso Juvenil", "Habitaciones tranquilas y seguras para el descanso y estudio individual."),
        ([0.407400, -78.171500], "Vida Comunitaria", "heart", "orange",
         "🤝 Bienestar y Convivencia", "Centro de apoyo emocional y social universitario en un entorno natural y armónico."),
        ([0.406500, -78.170500], "Minimarket Krispan", "shopping-cart", "orange",
         "☕ Encuentro y Servicios", "Punto de café y descanso estudiantil al aire libre en un ambiente fresco y perfumado.")
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
    # 5. CANALES HÍDRICOS (CONVIVENCIA ECOLÓGICA)
    # -------------------------------------------------------------
    canal_coords = [
        [0.4085, -78.1690],
        [0.4072, -78.1705],
        [0.4058, -78.1715],
        [0.4048, -78.1720],
        [0.4035, -78.1725],
        [0.4015, -78.1728]
    ]
    folium.PolyLine(
        locations=canal_coords,
        color="#0abde3",
        weight=4,
        dash_array='7, 7',
        popup=folium.Popup("""
            <div style="font-family: 'Segoe UI', Arial, sans-serif; width: 250px;">
                <h4 style="color: #0abde3; margin: 0 0 5px 0;">💧 Canal de Riego Principal</h4>
                <p style="font-size: 12px; color: #34495e; margin: 0;">
                    Agua corriente que nutre la agricultura del valle. Es el hábitat lótico donde se fija la larva de <i>Simulium</i>.<br>
                    <b>Tratamiento Verde:</b> No usamos venenos químicos. Se introduce control biológico con ninfas de libélulas y Bti ecológico.
                </p>
            </div>
        """, max_width=270),
        tooltip="💧 Canal de Riego: Hábitat Hídrico (Intervención Limpia)"
    ).add_to(fg_canales)

    acequia_ingenio = [
        [0.4056, -78.1738],
        [0.4050, -78.1732],
        [0.4045, -78.1728]
    ]
    folium.PolyLine(
        locations=acequia_ingenio,
        color="#0abde3",
        weight=3,
        dash_array='5, 5',
        popup=folium.Popup("""
            <div style="font-family: 'Segoe UI', Arial, sans-serif; width: 240px;">
                <h4 style="color: #0abde3; margin: 0 0 5px 0;">💧 Acequia Secundaria Ingenio</h4>
                <p style="font-size: 12px; color: #34495e; margin: 0;">
                    Flujo patrimonial intervenido con micro-dosificación selectiva y barrera arbórea perimetral.
                </p>
            </div>
        """, max_width=260),
        tooltip="💧 Acequia Secundaria Ingenio"
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
                    <b>🌱 Arquitectura en 3 Estratos:</b><br>
                    • <b>Alto (3.5-5m):</b> <i>Schinus molle</i> (Molle andino) - Sombra fresca y rompevientos con pineno.<br>
                    • <b>Medio (1.2-2m):</b> <i>Myrcianthes hallii</i> (Arrayán) & Romero - Aroma relajante y bloqueo de vuelo.<br>
                    • <b>Bajo (0.4-0.8m):</b> <i>Cymbopogon citratus</i> (Hierba luisa) - Perfume cítrico y barrera basal de citronelal.<br>
                    <div style="margin-top: 6px; padding: 5px; background: #e8f8f5; border-radius: 4px; color: #0e6251;">
                        <b>✨ Impacto Estudiantil:</b> Transforma los accesos a residencias en paseos aromáticos seguros.
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
                    • <b>Medio:</b> <i>Myrcianthes hallii</i> (Arrayán) & Romero.<br>
                    • <b>Bajo:</b> <i>Cymbopogon citratus</i>.<br>
                    <div style="margin-top: 6px; padding: 5px; background: #e8f8f5; border-radius: 4px; color: #0e6251;">
                        <b>✨ Impacto Académico:</b> Ventilación natural en las aulas y descanso profundo en las habitaciones de Los Bloques.
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

    # Agregar capas al mapa
    fg_zonas.add_to(m)
    fg_canales.add_to(m)
    fg_biocontrol.add_to(m)
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

        /* Tipografía y accesibilidad general */
        .leaflet-popup-content-wrapper {{
            background: var(--bg-panel);
            color: var(--text-color);
            border-radius: 12px;
            box-shadow: var(--shadow-card);
            padding: 2px;
            border: 1px solid var(--border-color);
        }}
        .leaflet-popup-tip {{
            background: var(--bg-panel);
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

        /* Leyenda visual intuitiva (Inferior Izquierda, sobre minimapa) */
        #panel-leyenda {{
            position: fixed;
            bottom: 165px;
            left: 15px;
            z-index: 998;
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
            background: var(--bg-panel);
            color: var(--text-color);
            max-width: 620px;
            width: 100%;
            border-radius: 16px;
            box-shadow: 0 15px 40px rgba(0,0,0,0.35);
            border: 1px solid var(--border-color);
            overflow: hidden;
            animation: slideUp 0.35s ease;
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
                padding: 5px 10px;
                gap: 4px;
            }}
            .nav-btn {{
                padding: 4px 8px;
                font-size: 10px;
            }}
            #dashboard-flotante {{
                width: 280px;
                bottom: 15px;
                right: 15px;
            }}
            #panel-leyenda {{
                width: 200px;
                bottom: 145px;
            }}
        }}
    </style>

    <!-- BARRA SUPERIOR DE NAVEGACIÓN Y STORYTELLING -->
    <div id="story-nav-bar">
        <!-- Logo / Marca -->
        <div id="nav-brand" style="display: flex; align-items: center; gap: 7px; padding-right: 8px; border-right: 1px solid var(--border-color); cursor: pointer;" onclick="toggleModalBienvenida(true)" title="Algoritmo Verde YT">
            <svg width="22" height="22" viewBox="0 0 100 100">
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
            <span style="font-weight: 800; font-size: 12.5px; color: var(--primary-color); letter-spacing: 0.3px;">Algoritmo Verde</span>
        </div>

        <button id="btn-info" class="nav-btn nav-btn-info" onclick="toggleModalBienvenida(true)" title="Conocer el propósito humano del proyecto">
            ℹ️ <span data-i18n="nav_vision">Visión y Propósito</span>
        </button>
        <button id="btn-solucion" class="nav-btn nav-btn-highlight" onclick="activarModoSolucion()" title="Ver la solución ecológica activa">
            🌿 <span data-i18n="nav_solution">Solución Verde (Activa)</span>
        </button>
        <button id="btn-diagnostico" class="nav-btn" onclick="activarModoDiagnostico()" title="Ver zonas críticas y canales originales">
            ⚠️ <span data-i18n="nav_diagnosis">Ver Diagnóstico</span>
        </button>
        <span style="color: var(--border-color); margin: 0 2px;">|</span>
        <button class="nav-btn" onclick="irAZona('residencias')" title="Enfocar Residencias Las Multis y Patrimoniales">
            🏡 <span data-i18n="nav_residencias">Residencias</span>
        </button>
        <button class="nav-btn" onclick="irAZona('ingenio')" title="Enfocar Biblioteca y Laboratorios">
            📚 <span data-i18n="nav_biblioteca">Biblioteca / Aulas</span>
        </button>
        <button class="nav-btn" onclick="irAZona('senescyt')" title="Enfocar Senescyt y Los Bloques">
            🎓 <span data-i18n="nav_senescyt">Senescyt / Bloques</span>
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
    <div id="modal-bienvenida" class="modal-overlay" style="display: none;" onclick="if(event.target===this) toggleModalBienvenida(false)">
        <div class="modal-card">
            <div class="modal-header">
                <button onclick="toggleModalBienvenida(false)" style="position: absolute; top: 16px; right: 18px; background: rgba(255,255,255,0.2); border: none; color: white; font-size: 18px; font-weight: bold; width: 32px; height: 32px; border-radius: 50%; cursor: pointer; display: flex; align-items: center; justify-content: center; transition: all 0.2s;" onmouseover="this.style.background='rgba(255,255,255,0.35)'" onmouseout="this.style.background='rgba(255,255,255,0.2)'" title="Cerrar modal (Esc)">✕</button>
                <h2 style="margin: 0; font-size: 19px; font-weight: 700; padding-right: 35px;" data-i18n="modal_title">🌱 Algoritmo Verde: Un Campus para Vivir y Estudiar en Paz</h2>
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
                    <b style="color: #2980b9; font-size: 13.5px;" data-i18n="modal_card2_title">🌿 Naturaleza que Protege (3 Estratos Vegetales)</b><br>
                    <span data-i18n="modal_card2_desc">980 metros de barreras vivas con especies andinas: <b>Molle</b> (sombra y rompeviento), <b>Arrayán y Romero</b> (bloqueo físico y fragancia relajante) y <b>Hierba Luisa</b> (repelente cítrico basal). Aromaterapia natural que disminuye el estrés académico.</span>
                </div>

                <div class="card-pilar" style="border-left-color: #0abde3;">
                    <b style="color: #0abde3; font-size: 13.5px;" data-i18n="modal_card3_title">💧 Agua Limpia y Biocontrol Respetuoso</b><br>
                    <span data-i18n="modal_card3_desc">Los canales de riego que cruzan Yachay alimentan los cultivos de Urcuquí. Nuestro control biológico usa <b>ninfas de libélulas nativas</b> y micro-larvicidas biológicos (Bti) que preservan la calidad del agua para las comunidades vecinas.</span>
                </div>

                <div style="text-align: center; margin-top: 20px;">
                    <button class="modal-btn-close" onclick="toggleModalBienvenida(false)" data-i18n="modal_btn_explore">
                        ✨ ¡Explorar el Campus Protegido!
                    </button>
                </div>
            </div>
        </div>
    </div>

    <!-- MODAL DE CÓDIGO QR PARA CELULAR Y PITCH -->
    <div id="modal-qr" class="modal-overlay" style="display: none;" onclick="if(event.target===this) toggleModalQR(false)">
        <div class="modal-card" style="max-width: 440px; text-align: center;">
            <div class="modal-header">
                <button onclick="toggleModalQR(false)" style="position: absolute; top: 16px; right: 18px; background: rgba(255,255,255,0.2); border: none; color: white; font-size: 18px; font-weight: bold; width: 32px; height: 32px; border-radius: 50%; cursor: pointer; display: flex; align-items: center; justify-content: center; transition: all 0.2s;" onmouseover="this.style.background='rgba(255,255,255,0.35)'" onmouseout="this.style.background='rgba(255,255,255,0.2)'" title="Cerrar (Esc)">✕</button>
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
            if (!foliumMap) return;

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
                nav_diagnosis: "Ver Diagnóstico",
                nav_residencias: "Residencias",
                nav_biblioteca: "Biblioteca / Aulas",
                nav_senescyt: "Senescyt / Bloques",
                nav_campus: "Vista Campus",
                nav_qr: "Código QR",
                nav_theme: document.body.getAttribute('data-theme') === 'dark' ? "Claro" : "Oscuro",
                
                leyenda_title: "📋 Simbología Humanista",
                leyenda_safe: "<b>Zona Segura:</b> Aromaterapia natural y aire limpio",
                leyenda_fences: "<b>Cercas Vivas:</b> 3 estratos (Molle, Arrayán, H. Luisa)",
                leyenda_canals: "<b>Canales Hídricos:</b> Biocontrol con Libélulas + Bti",
                leyenda_monitoring: "<b>Bio-Monitoreo:</b> Validación continua del confort",
                leyenda_life: "<b>Hitos de Vida:</b> Residencias, aulas y cultura",
                
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
                modal_card2_title: "🌿 Naturaleza que Protege (3 Estratos Vegetales)",
                modal_card2_desc: "980 metros de barreras vivas con especies andinas: <b>Molle</b> (sombra y rompeviento), <b>Arrayán y Romero</b> (bloqueo físico y fragancia relajante) y <b>Hierba Luisa</b> (repelente cítrico basal). Aromaterapia natural que disminuye el estrés académico.",
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
                nav_diagnosis: "View Diagnosis",
                nav_residencias: "Student Housing",
                nav_biblioteca: "Library & Labs",
                nav_senescyt: "Classrooms & Blocks",
                nav_campus: "Campus Overview",
                nav_qr: "QR Code",
                nav_theme: document.body.getAttribute('data-theme') === 'dark' ? "Light" : "Dark",
                
                leyenda_title: "📋 Human-Centered Legend",
                leyenda_safe: "<b>Safe Zone:</b> Natural aromatherapy & clean air",
                leyenda_fences: "<b>Living Fences:</b> 3 strata (Molle, Arrayan, Lemongrass)",
                leyenda_canals: "<b>Waterways:</b> Biocontrol with Dragonflies + Bti",
                leyenda_monitoring: "<b>Bio-Monitoring:</b> Continuous comfort tracking",
                leyenda_life: "<b>Campus Life:</b> Housing, classrooms & culture",
                
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
                modal_card2_title: "🌿 Nature that Protects (3 Plant Strata)",
                modal_card2_desc: "980 meters of living barriers with Andean native species: <b>Molle</b> (shade and windbreak), <b>Arrayan & Rosemary</b> (physical flight barrier and relaxing fragrance), and <b>Lemongrass</b> (citronellal basal repellent). Natural aromatherapy reducing academic stress.",
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
