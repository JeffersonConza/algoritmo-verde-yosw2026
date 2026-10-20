"""
Generador del Visor Geoespacial Interactivo - Reto 3: Control de Arenillas
Equipo: Algoritmo Verde YT | Yachay Open Science Week 2026
Enfoque: Humanista, Amigable, Intuitivo y Fácil de Usar
Calibrado con Coordenadas GPS Oficiales de Google Maps y Capas Base Optimizadas
"""

import folium
from folium import plugins

def generar_mapa():
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
    # 1. CAPAS BASE COMPATIBLES OFFLINE Y PROTOCOLO FILE:///
    # -------------------------------------------------------------
    folium.TileLayer(
        tiles='https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}',
        attr='Google Maps Satellite',
        name='🛰️ Google Satélite Híbrido',
        overlay=False,
        control=True,
        max_zoom=20
    ).add_to(m)

    folium.TileLayer(
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
    # 7. CERCAS VIVAS EN 3 ESTRATOS (CORREDORES PAISAJÍSTICOS)
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

    # Controles estándar de Folium
    folium.LayerControl(position='topright', collapsed=False).add_to(m)

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

    # -------------------------------------------------------------
    # 10. INTERFAZ HUMANISTA, AMIGABLE Y FÁCIL DE USAR (HTML + CSS + JS)
    # -------------------------------------------------------------
    interfaz_humanista_html = f"""
    <!-- ESTILOS HUMANISTAS Y MODERNOS -->
    <style>
        /* Tipografía y accesibilidad general */
        .leaflet-popup-content-wrapper {{
            border-radius: 12px;
            box-shadow: 0 6px 25px rgba(0,0,0,0.22);
            padding: 2px;
        }}
        .leaflet-container {{
            font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif !important;
        }}

        /* Barra de navegación superior (Storytelling Bar) */
        #story-nav-bar {{
            position: fixed;
            top: 14px;
            left: 50%;
            transform: translateX(-50%);
            z-index: 1000;
            background: rgba(255, 255, 255, 0.94);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            padding: 6px 12px;
            border-radius: 30px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.18);
            border: 1px solid rgba(16, 172, 132, 0.35);
            display: flex;
            align-items: center;
            gap: 6px;
            flex-wrap: wrap;
            max-width: 95vw;
        }}

        .nav-btn {{
            background: #ffffff;
            border: 1px solid #dcdde1;
            color: #2f3640;
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
            background: #f1f2f6;
            transform: translateY(-1px);
            box-shadow: 0 3px 8px rgba(0,0,0,0.12);
        }}
        .nav-btn-highlight {{
            background: #10ac84 !important;
            color: #ffffff !important;
            border-color: #10ac84 !important;
        }}
        .nav-btn-highlight:hover {{
            background: #0e9673 !important;
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
            background: #1e3799 !important;
            color: #ffffff !important;
            border-color: #1e3799 !important;
        }}
        .nav-btn-info:hover {{
            background: #0c2461 !important;
        }}

        /* Leyenda visual intuitiva (Inferior Izquierda, sobre minimapa) */
        #panel-leyenda {{
            position: fixed;
            bottom: 165px;
            left: 15px;
            z-index: 998;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(8px);
            border-radius: 10px;
            box-shadow: 0 3px 12px rgba(0,0,0,0.18);
            border: 1px solid #10ac84;
            width: 230px;
            font-size: 11px;
            overflow: hidden;
            transition: all 0.3s ease;
        }}
        .leyenda-header {{
            background: #10ac84;
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
            color: #2f3542;
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
            width: 325px;
            z-index: 9999;
            background: rgba(255, 255, 255, 0.97);
            border: 2px solid #10ac84;
            border-radius: 14px;
            box-shadow: 0 6px 25px rgba(0,0,0,0.22);
            font-family: 'Segoe UI', -apple-system, sans-serif;
            overflow: hidden;
            transition: all 0.3s ease;
        }}
        .dash-header {{
            background: linear-gradient(135deg, #10ac84 0%, #1e3799 100%);
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

        /* Modal de Bienvenida Humanista */
        #modal-bienvenida {{
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
            background: white;
            max-width: 620px;
            width: 100%;
            border-radius: 16px;
            box-shadow: 0 15px 40px rgba(0,0,0,0.3);
            overflow: hidden;
            animation: slideUp 0.35s ease;
        }}
        .modal-header {{
            background: linear-gradient(135deg, #10ac84 0%, #1e3799 100%);
            color: white;
            padding: 20px 24px;
            position: relative;
        }}
        .modal-body {{
            padding: 22px 24px;
            color: #2f3640;
            line-height: 1.55;
            font-size: 13.5px;
            max-height: 70vh;
            overflow-y: auto;
        }}
        .card-pilar {{
            background: #f8fafc;
            border-left: 4px solid #10ac84;
            padding: 10px 14px;
            margin: 10px 0;
            border-radius: 0 8px 8px 0;
        }}
        .modal-btn-close {{
            background: #10ac84;
            color: white;
            border: none;
            padding: 10px 22px;
            border-radius: 25px;
            font-weight: 700;
            cursor: pointer;
            font-size: 14px;
            box-shadow: 0 4px 12px rgba(16, 172, 132, 0.35);
            transition: all 0.2s ease;
        }}
        .modal-btn-close:hover {{
            background: #0e9673;
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

        @media (max-width: 768px) {{
            #story-nav-bar {{
                top: 8px;
                padding: 4px 8px;
                gap: 4px;
            }}
            .nav-btn {{
                padding: 4px 8px;
                font-size: 10px;
            }}
            #dashboard-flotante {{
                width: 270px;
                bottom: 15px;
                right: 15px;
            }}
        }}
    </style>

    <!-- BARRA SUPERIOR DE NAVEGACIÓN Y STORYTELLING -->
    <div id="story-nav-bar">
        <button class="nav-btn nav-btn-info" onclick="toggleModalBienvenida(true)" title="Conocer el propósito humano del proyecto">
            ℹ️ Visión y Propósito
        </button>
        <button id="btn-solucion" class="nav-btn nav-btn-highlight" onclick="activarModoSolucion()" title="Ver la solución ecológica activa">
            🌿 Solución Verde (Activa)
        </button>
        <button id="btn-diagnostico" class="nav-btn" onclick="activarModoDiagnostico()" title="Ver zonas críticas y canales originales">
            ⚠️ Ver Diagnóstico
        </button>
        <span style="color: #dcdde1; margin: 0 2px;">|</span>
        <button class="nav-btn" onclick="irAZona('residencias')" title="Enfocar Residencias Las Multis y Patrimoniales">
            🏡 Residencias
        </button>
        <button class="nav-btn" onclick="irAZona('ingenio')" title="Enfocar Biblioteca y Laboratorios">
            📚 Biblioteca / Aulas
        </button>
        <button class="nav-btn" onclick="irAZona('senescyt')" title="Enfocar Senescyt y Los Bloques">
            🎓 Senescyt / Bloques
        </button>
        <button class="nav-btn" onclick="irAZona('general')" title="Restablecer vista completa del campus">
            🔭 Vista Campus
        </button>
    </div>

    <!-- LEYENDA VISUAL ACCESIBLE (Encima del minimapa) -->
    <div id="panel-leyenda">
        <div class="leyenda-header" onclick="toggleLeyenda()">
            <span>📋 Simbología Humanista</span>
            <span id="leyenda-icon-toggle">−</span>
        </div>
        <div id="leyenda-body" class="leyenda-content">
            <div class="leyenda-item">
                <span class="leyenda-badge" style="background: rgba(46, 204, 113, 0.4); border: 1px solid #27ae60;"></span>
                <span><b>Zona Segura:</b> Aromaterapia natural y aire limpio</span>
            </div>
            <div class="leyenda-item">
                <span class="leyenda-badge" style="background: #10ac84;"></span>
                <span><b>Cercas Vivas:</b> 3 estratos (Molle, Arrayán, H. Luisa)</span>
            </div>
            <div class="leyenda-item">
                <span class="leyenda-badge" style="background: #0abde3;"></span>
                <span><b>Canales Hídricos:</b> Biocontrol con Libélulas + Bti</span>
            </div>
            <div class="leyenda-item">
                <span class="leyenda-badge" style="background: #1e3799;"></span>
                <span><b>Bio-Monitoreo:</b> Validación continua del confort</span>
            </div>
            <div class="leyenda-item">
                <span class="leyenda-badge" style="background: #e74c3c;"></span>
                <span><b>Hitos de Vida:</b> Residencias, aulas y cultura</span>
            </div>
        </div>
    </div>

    <!-- DASHBOARD FLOTANTE HUMANISTA -->
    <div id="dashboard-flotante">
        <div class="dash-header">
            <div>
                <span style="font-weight: 700; font-size: 14px; letter-spacing: 0.3px;">🌱 Algoritmo Verde YT</span><br>
                <span style="font-size: 11px; opacity: 0.9;">Yachay Open Science Week 2026</span>
            </div>
            <button class="toggle-btn" onclick="toggleDashboard()" title="Minimizar / Expandir panel" id="btn-dash-toggle">−</button>
        </div>
        <div id="dash-content" class="dash-body">
            <p style="margin: 0 0 8px 0; font-size: 11.5px; color: #57606f; line-height: 1.35;">
                <b>Reto 3:</b> Manejo ecológico de arenillas que prioriza la salud, el estudio y la vida al aire libre en Yachay Tech.
            </p>
            <table style="width: 100%; font-size: 11.5px; line-height: 1.65; color: #2f3542; border-collapse: collapse;">
                <tr>
                    <td>👥 <b>Comunidad Protegida:</b></td>
                    <td style="text-align: right; font-weight: 700; color: #1e3799;">~800+ personas</td>
                </tr>
                <tr>
                    <td>🌿 <b>Cercas en 3 Estratos:</b></td>
                    <td style="text-align: right; font-weight: 700; color: #10ac84;">980 m lineales</td>
                </tr>
                <tr>
                    <td>🛡️ <b>Área de Confort:</b></td>
                    <td style="text-align: right; font-weight: 700; color: #009432;">~39,200 m²</td>
                </tr>
                <tr>
                    <td>🌳 <b>Plántulas Repelentes:</b></td>
                    <td style="text-align: right; font-weight: 700; color: #10ac84;">~1,960 plantas</td>
                </tr>
                <tr>
                    <td>🚫 <b>Insecticidas Químicos:</b></td>
                    <td style="text-align: right; font-weight: 700; color: #10ac84;">0% (Cero toxicidad)</td>
                </tr>
                <tr>
                    <td>🦗 <b>Control Biológico:</b></td>
                    <td style="text-align: right; font-weight: 700; color: #0984e3;">Libélulas + Bti</td>
                </tr>
                <tr>
                    <td>🎯 <b>Bio-Monitoreo:</b></td>
                    <td style="text-align: right; font-weight: 700; color: #1e3799;">6 estaciones GPS</td>
                </tr>
                <tr style="border-top: 1px dashed #ced6e0;">
                    <td>📉 <b>Mitigación Picaduras:</b></td>
                    <td style="text-align: right; font-weight: 800; color: #e74c3c; font-size: 12.5px;">82% efectividad</td>
                </tr>
            </table>
            <div style="margin-top: 10px; font-size: 10.5px; color: #747d8c; text-align: center;">
                💡 <i>Usa los botones superiores para recorrer el campus</i>
            </div>
        </div>
    </div>

    <!-- MODAL DE BIENVENIDA Y PROPÓSITO HUMANISTA -->
    <div id="modal-bienvenida" style="display: none;">
        <div class="modal-card">
            <div class="modal-header">
                <h2 style="margin: 0; font-size: 20px; font-weight: 700;">🌱 Algoritmo Verde: Un Campus para Vivir y Estudiar en Paz</h2>
                <div style="font-size: 12px; opacity: 0.95; margin-top: 4px;">
                    Propuesta Multidisciplinar · YOSW 2026 Ideatón (Reto 3 - Control de Arenillas)
                </div>
            </div>
            <div class="modal-body">
                <p style="margin-top: 0; font-size: 14px; color: #1e272e;">
                    <b>¿Por qué existe este proyecto?</b><br>
                    En el campus de Yachay Tech, las picaduras diurnas de arenillas (<i>Simulium</i> spp.) afectan la concentración en clases, el descanso en residencias y el uso de espacios culturales. Nuestra propuesta <b>no es llenar el campus de venenos sintéticos</b>, sino devolverle la armonía al territorio mediante ciencia aplicada, ecología y diseño paisajístico.
                </p>

                <div class="card-pilar">
                    <b style="color: #10ac84; font-size: 13.5px;">👥 Las Personas Primero (Salud y Confort)</b><br>
                    Protegemos a más de 800 residentes, docentes y trabajadores. Eliminamos el uso de pesticidas tóxicos protegiendo el aire que respiran los estudiantes en Las Multis, Los Bloques y aulas.
                </div>

                <div class="card-pilar" style="border-left-color: #3498db;">
                    <b style="color: #2980b9; font-size: 13.5px;">🌿 Naturaleza que Protege (3 Estratos Vegetales)</b><br>
                    980 metros de barreras vivas con especies andinas: <b>Molle</b> (sombra y rompeviento), <b>Arrayán y Romero</b> (bloqueo físico y fragancia relajante) y <b>Hierba Luisa</b> (repelente cítrico basal). Aromaterapia natural que disminuye el estrés académico.
                </div>

                <div class="card-pilar" style="border-left-color: #0abde3;">
                    <b style="color: #0abde3; font-size: 13.5px;">💧 Agua Limpia y Biocontrol Respetuoso</b><br>
                    Los canales de riego que cruzan Yachay alimentan los cultivos de Urcuquí. Nuestro control biológico usa <b>ninfas de libélulas nativas</b> y micro-larvicidas biológicos (Bti) que preservan la calidad del agua para las comunidades vecinas.
                </div>

                <div style="text-align: center; margin-top: 20px;">
                    <button class="modal-btn-close" onclick="toggleModalBienvenida(false)">
                        ✨ ¡Explorar el Campus Protegido!
                    </button>
                </div>
            </div>
        </div>
    </div>

    <!-- JAVASCRIPT DE INTERACTIVIDAD DINÁMICA -->
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

        // 4. Modal de bienvenida
        function toggleModalBienvenida(show) {{
            var modal = document.getElementById('modal-bienvenida');
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

        // Mostrar bienvenida automáticamente cuando la ventana haya cargado
        window.addEventListener('load', function() {{
            setTimeout(function() {{
                toggleModalBienvenida(true);
            }}, 350);
        }});
    </script>
    """

    m.get_root().html.add_child(folium.Element(interfaz_humanista_html))

    output_path = "reto3_Control_Arenillas/mapa_interactivo_control_arenillas.html"
    m.save(output_path)
    print(f"Mapa generado exitosamente con Interfaz Humanista en: {output_path}")

if __name__ == "__main__":
    generar_mapa()
