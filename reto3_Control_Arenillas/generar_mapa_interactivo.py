"""
Generador del Visor Geoespacial Interactivo - Reto 3: Control de Arenillas
Equipo: Algoritmo Verde YT | Yachay Open Science Week 2026
Calibrado con Coordenadas GPS Oficiales de Google Maps
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
        control_scale=True
    )
    
    # -------------------------------------------------------------
    # CAPAS BASE
    # -------------------------------------------------------------
    # 1. Google Híbrido (Satélite de máxima fidelidad + Vías)
    folium.TileLayer(
        tiles='https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}',
        attr='Google Maps Satellite Hybrid',
        name='Google Satélite Híbrido (Recomendado)',
        overlay=False,
        control=True
    ).add_to(m)

    # 2. Satélite Esri
    folium.TileLayer(
        tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        attr='Esri World Imagery',
        name='Satélite Esri (Alta Resolución)',
        overlay=False,
        control=True
    ).add_to(m)
    
    # 3. OpenStreetMap
    folium.TileLayer(
        tiles='OpenStreetMap',
        name='Mapa Callejero (OSM)',
        overlay=False,
        control=True
    ).add_to(m)

    # -------------------------------------------------------------
    # FEATURE GROUPS (CAPAS TEMÁTICAS)
    # -------------------------------------------------------------
    fg_zonas = folium.FeatureGroup(name="⚠️ Zonas Críticas Oficiales (Calibradas GPS)", show=True)
    fg_edificios = folium.FeatureGroup(name="🏛️ Edificaciones Reales (Google Maps)", show=True)
    fg_canales = folium.FeatureGroup(name="💧 Canales Hídricos y Focos Larvarios (Simuliidae)", show=True)
    fg_biocontrol = folium.FeatureGroup(name="🦗 Control Biológico Acuático (Libélulas + Bti)", show=True)
    fg_cercas = folium.FeatureGroup(name="🌿 Cercas Vivas en 3 Estratos (Algoritmo Verde)", show=True)
    fg_buffer = folium.FeatureGroup(name="🛡️ Cobertura Repelente (Buffer de Monoterpenos)", show=True)
    fg_trampas = folium.FeatureGroup(name="🎯 Red de Trampas de Monitoreo Biológico", show=True)

    # -------------------------------------------------------------
    # 1. POLÍGONOS DE ZONAS CRÍTICAS (CALIBRADOS GPS)
    # -------------------------------------------------------------
    # Zona 1: Multifamiliares y Pats (Sur - Las Multis, Residencias Patrimoniales, Concha Acústica)
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
        color="#2ecc71",
        weight=3,
        fill=True,
        fill_color="#2ecc71",
        fill_opacity=0.25,
        popup=folium.Popup("""
            <div style="font-family: Arial; width: 240px;">
                <h4 style="color: #27ae60; margin: 0 0 5px 0;">Zona 1: Multifamiliares y Pats</h4>
                <b>Hitos GPS:</b> Residencias Patrimoniales (0.4023, -78.1738), Las Multis, Concha Acústica.<br>
                <b>Población:</b> Alta densidad estudiantil.<br>
                <b>Riesgo:</b> Picaduras severas en horas de descanso y tránsito.<br>
                <b>Estrategia:</b> Cerca Viva Multiestrato 1 (380m) + 2 estaciones de monitoreo.
            </div>
        """, max_width=260),
        tooltip="Zona 1: Multifamiliares y Pats (Residencias)"
    ).add_to(fg_zonas)

    # Zona 2: Ingenio Azucarero (Centro - Patrimonio, Biblioteca, Laboratorios, Chimenea)
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
        weight=3,
        fill=True,
        fill_color="#3498db",
        fill_opacity=0.25,
        popup=folium.Popup("""
            <div style="font-family: Arial; width: 240px;">
                <h4 style="color: #2980b9; margin: 0 0 5px 0;">Zona 2: Ingenio Azucarero</h4>
                <b>Hitos GPS:</b> Biblioteca Patrimonial (0.4051, -78.1742), Chimenea Patrimonial, Laboratorios de Carrera.<br>
                <b>Riesgo:</b> Muy alto por cruce de acequias y sombra.<br>
                <b>Estrategia:</b> Cerca Viva Multiestrato 2 (280m) + intervención biológica en canal.
            </div>
        """, max_width=260),
        tooltip="Zona 2: Ingenio Azucarero (Patrimonio / Laboratorios)"
    ).add_to(fg_zonas)

    # Zona 3: Bloques y Senescyt (Noreste - Edificio Senescyt, Los Bloques, Vida Comunitaria)
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
        weight=3,
        fill=True,
        fill_color="#e74c3c",
        fill_opacity=0.25,
        popup=folium.Popup("""
            <div style="font-family: Arial; width: 240px;">
                <h4 style="color: #c0392b; margin: 0 0 5px 0;">Zona 3: Bloques y Senescyt</h4>
                <b>Hitos GPS:</b> Edificio Senescyt (0.4067, -78.1702), Residencias Los Bloques, Vida Comunitaria.<br>
                <b>Riesgo:</b> Exposición diurna en aulas y nocturna en dormitorios.<br>
                <b>Estrategia:</b> Cerca Viva Multiestrato 3 (320m) + 2 estaciones de monitoreo.
            </div>
        """, max_width=260),
        tooltip="Zona 3: Bloques y Senescyt (Aulas / Los Bloques)"
    ).add_to(fg_zonas)

    # -------------------------------------------------------------
    # 2. HITOS Y EDIFICACIONES REALES (EXTRAÍDOS DE GOOGLE MAPS)
    # -------------------------------------------------------------
    hitos_reales = [
        # Zona 1
        ([0.402297, -78.173836], "Residencias Patrimoniales", "home", "green", "Residencias Estudiantiles"),
        ([0.402750, -78.174800], "Las Multis (Residencias)", "home", "green", "Residencias Estudiantiles"),
        ([0.402350, -78.175500], "Concha Acústica Yachay Tech", "music", "darkgreen", "Espacio Cultural al Aire Libre"),
        ([0.402500, -78.171800], "Canchas Deportivas", "futbol-o", "cadetblue", "Recreación Estudiantil"),
        ([0.402550, -78.172800], "Parada Fasta (Arco Pats)", "bus", "gray", "Transporte Universitario"),
        # Zona 2
        ([0.405072, -78.174159], "Biblioteca Patrimonial 'Yachay Tech'", "book", "blue", "Área de Estudio Central"),
        ([0.405320, -78.174000], "Chimenea Ingenio Azucarero", "industry", "purple", "Patrimonio Histórico"),
        ([0.404900, -78.173900], "Laboratorio de Química", "flask", "darkpurple", "Docencia e Investigación"),
        ([0.404780, -78.172450], "Laboratorios de Carrera, Yachay Tech", "cogs", "darkpurple", "Laboratorios Tecnológicos"),
        # Zona 3
        ([0.406691, -78.170214], "Edificio Senescyt (Yachay Tech)", "graduation-cap", "red", "Aulas y Oficinas Docentes"),
        ([0.406950, -78.171150], "Residencias 'Los Bloques'", "bed", "darkred", "Residencias Estudiantiles"),
        ([0.407400, -78.171500], "Promoción de la Vida Comunitaria", "users", "orange", "Bienestar Estudiantil"),
        ([0.406500, -78.170500], "Minimarket Krispan", "shopping-cart", "orange", "Zona de Alimentación y Servicios")
    ]
    for coord, nombre, icono, color, tipo in hitos_reales:
        folium.Marker(
            location=coord,
            icon=folium.Icon(icon=icono, prefix='fa', color=color),
            popup=f"<b>{nombre}</b><br>Tipo: {tipo}<br>GPS: {coord[0]:.6f}, {coord[1]:.6f}",
            tooltip=nombre
        ).add_to(fg_edificios)

    # -------------------------------------------------------------
    # 3. CANALES HÍDRICOS (FOCOS LARVARIOS DE SIMULIIDAE)
    # -------------------------------------------------------------
    # Canal de riego que baja por la franja oriental de la Vía a Yachay
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
        color="#00d2d3",
        weight=5,
        dash_array='8, 8',
        popup="<b>Canal de Riego Principal (Agua Lótica / Corriente):</b> Sustrato rocoso y macrófitas sumergidas donde se fijan las larvas de <i>Simuliidae</i>.",
        tooltip="Canal de Riego Principal (Foco Larvario)"
    ).add_to(fg_canales)

    # Acequia secundaria patrimonial del Ingenio
    acequia_ingenio = [
        [0.4056, -78.1738],
        [0.4050, -78.1732],
        [0.4045, -78.1728]
    ]
    folium.PolyLine(
        locations=acequia_ingenio,
        color="#00d2d3",
        weight=4,
        dash_array='5, 5',
        popup="<b>Acequia de Desvío Patrimonial:</b> Conexión hídrica en sector de laboratorios.",
        tooltip="Acequia Secundaria Ingenio"
    ).add_to(fg_canales)

    # -------------------------------------------------------------
    # 4. CONTROL BIOLÓGICO ACUÁTICO (LIBÉLULAS + Bti)
    # -------------------------------------------------------------
    puntos_biocontrol = [
        ([0.4072, -78.1705], "Bio-Estación Norte (Bti + Nicho Odonatos)", "Canal Senescyt"),
        ([0.4048, -78.1720], "Bio-Estación Central (Monitoreo Macroinvertebrados)", "Canal Laboratorios"),
        ([0.4028, -78.1726], "Bio-Estación Sur (Refugio de Libélulas Nativas)", "Canal Canchas / Pats")
    ]
    for pt, titulo, detalle in puntos_biocontrol:
        folium.CircleMarker(
            location=pt,
            radius=8,
            color="#0984e3",
            fill=True,
            fill_color="#74b9ff",
            fill_opacity=0.9,
            popup=f"<b>{titulo}</b><br>{detalle}<br>• Depredación larval por ninfas de libélula.<br>• Aplicación selectiva de <i>Bacillus thuringiensis israelensis</i> (Bti).",
            tooltip=titulo
        ).add_to(fg_biocontrol)

    # -------------------------------------------------------------
    # 5. CERCAS VIVAS EN 3 ESTRATOS (PROPUESTA ALGORITMO VERDE YT)
    # -------------------------------------------------------------
    # Cerca 1: Sector Las Multis / Residencias Patrimoniales (380m)
    cerca1 = [
        [0.4031, -78.1750],
        [0.4030, -78.1738],
        [0.4024, -78.1730]
    ]
    folium.PolyLine(
        locations=cerca1,
        color="#27ae60",
        weight=6,
        popup=folium.Popup("""
            <div style="font-family: Arial; width: 250px;">
                <h4 style="color: #27ae60; margin: 0 0 5px 0;">🌿 Cerca Viva 1 - Sector Residencial (380m)</h4>
                <b>Estructura en 3 Estratos:</b><br>
                • <b>Alto (3.5-5m):</b> <i>Schinus molle</i> (Pimiento andino nativo) - Rompevientos.<br>
                • <b>Medio (1.2-2m):</b> <i>Myrcianthes hallii</i> (Arrayán) & Romero - Bloqueo de vuelo.<br>
                • <b>Bajo (0.4-0.8m):</b> <i>Cymbopogon citratus</i> (Hierba luisa) - Citronelal basal.<br>
                <b>Eficacia proyectada:</b> ~85% reducción de picaduras.
            </div>
        """, max_width=270),
        tooltip="🌿 Cerca Viva 1: Residencias Las Multis / Patrimoniales (380m)"
    ).add_to(fg_cercas)

    # Cerca 2: Sector Ingenio / Laboratorios (280m)
    cerca2 = [
        [0.4055, -78.1734],
        [0.4048, -78.1728],
        [0.4040, -78.1726]
    ]
    folium.PolyLine(
        locations=cerca2,
        color="#27ae60",
        weight=6,
        popup=folium.Popup("""
            <div style="font-family: Arial; width: 250px;">
                <h4 style="color: #27ae60; margin: 0 0 5px 0;">🌿 Cerca Viva 2 - Sector Ingenio / Laboratorios (280m)</h4>
                <b>Estructura en 3 Estratos:</b><br>
                • <b>Alto:</b> <i>Schinus molle</i>.<br>
                • <b>Medio:</b> <i>Lantana camara</i> y Lavanda.<br>
                • <b>Bajo:</b> <i>Cymbopogon citratus</i>.<br>
                <b>Función:</b> Amortiguamiento entre canal de riego y caminerías de aulas.
            </div>
        """, max_width=270),
        tooltip="🌿 Cerca Viva 2: Ingenio / Laboratorios (280m)"
    ).add_to(fg_cercas)

    # Cerca 3: Sector Edificio Senescyt / Los Bloques (320m)
    cerca3 = [
        [0.4072, -78.1718],
        [0.4066, -78.1710],
        [0.4060, -78.1702]
    ]
    folium.PolyLine(
        locations=cerca3,
        color="#27ae60",
        weight=6,
        popup=folium.Popup("""
            <div style="font-family: Arial; width: 250px;">
                <h4 style="color: #27ae60; margin: 0 0 5px 0;">🌿 Cerca Viva 3 - Sector Senescyt / Los Bloques (320m)</h4>
                <b>Estructura en 3 Estratos:</b><br>
                • <b>Alto:</b> <i>Schinus molle</i>.<br>
                • <b>Medio:</b> <i>Myrcianthes hallii</i> (Arrayán) & Romero.<br>
                • <b>Bajo:</b> <i>Cymbopogon citratus</i>.<br>
                <b>Protección:</b> Complejo habitacional y aulas académicas.
            </div>
        """, max_width=270),
        tooltip="🌿 Cerca Viva 3: Edificio Senescyt / Los Bloques (320m)"
    ).add_to(fg_cercas)

    # -------------------------------------------------------------
    # 6. BUFFERS DE COBERTURA DE MONOTERPENOS REPELENTES (40m)
    # -------------------------------------------------------------
    for c_coords, c_name in [(cerca1, "Buffer Residencias"), (cerca2, "Buffer Ingenio"), (cerca3, "Buffer Senescyt")]:
        folium.PolyLine(
            locations=c_coords,
            color="#2ecc71",
            weight=35,
            opacity=0.25,
            tooltip=f"Área de Amortiguamiento Repelente ({c_name})"
        ).add_to(fg_buffer)

    # -------------------------------------------------------------
    # 7. RED DE TRAMPAS DE MONITOREO BIOLÓGICO (6 ESTACIONES GPS)
    # -------------------------------------------------------------
    trampas_gps = [
        ([0.4024, -78.1730], "T-01: Residencias Patrimoniales / Canchas"),
        ([0.4028, -78.1750], "T-02: Las Multis / Concha Acústica"),
        ([0.4052, -78.1742], "T-03: Biblioteca Patrimonial / Chimenea"),
        ([0.4047, -78.1724], "T-04: Laboratorios de Carrera"),
        ([0.4067, -78.1702], "T-05: Edificio Senescyt (Fachada Sur)"),
        ([0.4070, -78.1714], "T-06: Residencias Los Bloques / Vida Comunitaria")
    ]
    for pt, label in trampas_gps:
        folium.Marker(
            location=pt,
            icon=folium.Icon(icon="crosshairs", prefix="fa", color="darkblue"),
            popup=f"""
                <b>Estación de Bio-Monitoreo</b><br>
                <b>Código:</b> {label}<br>
                <b>Mecanismo:</b> Trampa de silueta + cebo bio-ecológico (ácido L-láctico y fermentación CO2).<br>
                <b>Objetivo:</b> Validación empírica de reducción de picaduras (RF-04).
            """,
            tooltip=label
        ).add_to(fg_trampas)

    # Agregar capas al mapa
    fg_zonas.add_to(m)
    fg_canales.add_to(m)
    fg_biocontrol.add_to(m)
    fg_edificios.add_to(m)
    fg_cercas.add_to(m)
    fg_buffer.add_to(m)
    fg_trampas.add_to(m)

    # Controles de interfaz
    folium.LayerControl(position='topright', collapsed=False).add_to(m)
    plugins.MiniMap(toggle_display=True, position='bottomleft').add_to(m)
    plugins.MeasureControl(position='topleft', primary_length_unit='meters', primary_area_unit='sqmeters').add_to(m)

    # Dashboard flotante
    dashboard_html = """
    <div style="
        position: fixed;
        bottom: 30px;
        right: 30px;
        width: 320px;
        z-index: 9999;
        background: rgba(255, 255, 255, 0.96);
        border: 2px solid #27ae60;
        border-radius: 12px;
        padding: 14px 18px;
        font-family: 'Segoe UI', Arial, sans-serif;
        box-shadow: 0 4px 15px rgba(0,0,0,0.25);
    ">
        <div style="display: flex; align-items: center; margin-bottom: 8px;">
            <div style="width: 14px; height: 14px; border-radius: 50%; background: #27ae60; margin-right: 8px;"></div>
            <h3 style="margin: 0; color: #1e3799; font-size: 15px; font-weight: bold;">Algoritmo Verde YT</h3>
        </div>
        <p style="margin: 0 0 10px 0; font-size: 11px; color: #57606f; line-height: 1.3;">
            <b>YOSW 2026 · Reto 3:</b> Manejo Integrado de Arenillas calibrado con coordenadas satelitales oficiales.
        </p>
        <hr style="border: none; border-top: 1px solid #dfe4ea; margin: 8px 0;">
        <table style="width: 100%; font-size: 11px; line-height: 1.6; color: #2f3542;">
            <tr>
                <td>🌿 <b>Cercas en 3 Estratos:</b></td>
                <td style="text-align: right; font-weight: bold; color: #27ae60;">980 m lineales</td>
            </tr>
            <tr>
                <td>🌱 <b>Plántulas Repelentes:</b></td>
                <td style="text-align: right; font-weight: bold; color: #27ae60;">~1,960 unid.</td>
            </tr>
            <tr>
                <td>🦗 <b>Control Biológico:</b></td>
                <td style="text-align: right; font-weight: bold; color: #0984e3;">Odonatos + Bti</td>
            </tr>
            <tr>
                <td>🎯 <b>Trampas Bio-Monitoreo:</b></td>
                <td style="text-align: right; font-weight: bold; color: #1e3799;">6 estaciones GPS</td>
            </tr>
            <tr>
                <td>🛡️ <b>Área de Protección:</b></td>
                <td style="text-align: right; font-weight: bold; color: #009432;">~39,200 m²</td>
            </tr>
            <tr>
                <td>📉 <b>Mitigación Estimada:</b></td>
                <td style="text-align: right; font-weight: bold; color: #e74c3c;">82% picaduras</td>
            </tr>
        </table>
        <div style="margin-top: 10px; font-size: 10px; color: #747d8c; text-align: center;">
            *Haga clic en las capas para filtrar elementos
        </div>
    </div>
    """
    m.get_root().html.add_child(folium.Element(dashboard_html))

    output_path = "reto3_Control_Arenillas/mapa_interactivo_control_arenillas.html"
    m.save(output_path)
    print(f"Mapa generado exitosamente en: {output_path}")

if __name__ == "__main__":
    generar_mapa()
