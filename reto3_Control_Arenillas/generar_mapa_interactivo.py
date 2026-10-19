"""
Generador del Visor Geoespacial Interactivo - Reto 3: Control de Arenillas
Equipo: Algoritmo Verde YT
Yachay Open Science Week 2026
"""

import folium
from folium import plugins
import json

def generar_mapa():
    # Coordenadas centrales del campus de Yachay Tech
    center_lat = 0.4050
    center_lon = -78.1750
    
    # Crear el mapa base centrado en Yachay Tech
    m = folium.Map(
        location=[center_lat, center_lon],
        zoom_start=16,
        max_zoom=20,
        control_scale=True
    )
    
    # Capa 1: Satélite de Alta Resolución (Esri World Imagery)
    esri_satellite = folium.TileLayer(
        tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        attr='Esri World Imagery',
        name='Satélite Esri (Alta Resolución)',
        overlay=False,
        control=True
    ).add_to(m)
    
    # Capa 2: OpenStreetMap
    folium.TileLayer(
        tiles='OpenStreetMap',
        name='Mapa Callejero (OSM)',
        overlay=False,
        control=True
    ).add_to(m)
    
    # Capa 3: Google Maps Satellite (Tiles estándar)
    folium.TileLayer(
        tiles='https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}',
        attr='Google Maps Satellite Hybrid',
        name='Google Híbrido (Satélite + Vías)',
        overlay=False,
        control=True
    ).add_to(m)
    
    # ==========================================
    # GRUPOS DE CAPAS INTERACTIVAS
    # ==========================================
    fg_zonas = folium.FeatureGroup(name="⚠️ Zonas Críticas Oficiales (Mapa Corregido)", show=True)
    fg_canales = folium.FeatureGroup(name="💧 Canales de Agua y Focos Larvarios (Simuliidae)", show=True)
    fg_edificios = folium.FeatureGroup(name="🏛️ Edificaciones Vulnerables (Aulas / Dormitorios)", show=True)
    fg_cercas = folium.FeatureGroup(name="🌿 Propuesta: Cercas Vivas Repelentes", show=True)
    fg_trampas = folium.FeatureGroup(name="🎯 Red de Trampas de Monitoreo Biológico", show=True)
    fg_buffer = folium.FeatureGroup(name="🛡️ Cobertura de Protección (Buffer Repelente)", show=True)

    # ------------------------------------------
    # 1. ZONAS CRÍTICAS (Polígonos aproximados al mapa corregido)
    # ------------------------------------------
    # Zona 1: Multifamiliares y Pats (Sur/Suroeste - Residencias estudiantiles)
    poly_z1 = [
        [0.4022, -78.1785],
        [0.4035, -78.1795],
        [0.4045, -78.1788],
        [0.4048, -78.1768],
        [0.4032, -78.1755],
        [0.4020, -78.1765]
    ]
    folium.Polygon(
        locations=poly_z1,
        color="#2ecc71",
        weight=3,
        fill=True,
        fill_color="#2ecc71",
        fill_opacity=0.25,
        popup=folium.Popup("""
            <div style="font-family: Arial; width: 220px;">
                <h4 style="color: #27ae60; margin-bottom: 5px;">Zona 1: Multifamiliares y Pats</h4>
                <b>Categoría:</b> Residencial Estudiantil<br>
                <b>Riesgo:</b> Alto (picaduras matutinas y vespertinas al aire libre).<br>
                <b>Intervención:</b> Barrera perimetral vegetal de amortiguamiento (380 m).
            </div>
        """, max_width=250),
        tooltip="Zona 1: Multifamiliares y Pats"
    ).add_to(fg_zonas)

    # Zona 2: Ingenio Azucarero (Centro - Patrimonio, laboratorios, acequias)
    poly_z2 = [
        [0.4042, -78.1752],
        [0.4058, -78.1758],
        [0.4065, -78.1742],
        [0.4055, -78.1725],
        [0.4040, -78.1732]
    ]
    folium.Polygon(
        locations=poly_z2,
        color="#3498db",
        weight=3,
        fill=True,
        fill_color="#3498db",
        fill_opacity=0.25,
        popup=folium.Popup("""
            <div style="font-family: Arial; width: 220px;">
                <h4 style="color: #2980b9; margin-bottom: 5px;">Zona 2: Ingenio Azucarero</h4>
                <b>Categoría:</b> Académica / Patrimonial<br>
                <b>Riesgo:</b> Muy Alto (proximidad a canales de riego y acequias activas).<br>
                <b>Intervención:</b> Manejo de flujo marginal y cercas vivas en bordes de canal (280 m).
            </div>
        """, max_width=250),
        tooltip="Zona 2: Ingenio Azucarero"
    ).add_to(fg_zonas)

    # Zona 3: Bloques de Aulas y Senescyt (Noreste - Aulas, comedores y laboratorios)
    poly_z3 = [
        [0.4068, -78.1738],
        [0.4082, -78.1742],
        [0.4095, -78.1720],
        [0.4085, -78.1705],
        [0.4065, -78.1718]
    ]
    folium.Polygon(
        locations=poly_z3,
        color="#e74c3c",
        weight=3,
        fill=True,
        fill_color="#e74c3c",
        fill_opacity=0.25,
        popup=folium.Popup("""
            <div style="font-family: Arial; width: 220px;">
                <h4 style="color: #c0392b; margin-bottom: 5px;">Zona 3: Bloques y Senescyt</h4>
                <b>Categoría:</b> Aulas / Administración / Laboratorios<br>
                <b>Riesgo:</b> Alto en horas diurnas por exposición en caminerías y áreas abiertas.<br>
                <b>Intervención:</b> Cordón perimetral de especies aromáticas nativas (320 m).
            </div>
        """, max_width=250),
        tooltip="Zona 3: Bloques y Senescyt"
    ).add_to(fg_zonas)

    # ------------------------------------------
    # 2. CANALES HÍDRICOS Y ACEQUIAS (Focos Larvarios)
    # ------------------------------------------
    # Canal de riego principal que cruza desde la cuenca alta hacia los campos agrícolas
    canal_coords = [
        [0.4098, -78.1765],
        [0.4080, -78.1755],
        [0.4062, -78.1748],
        [0.4048, -78.1740],
        [0.4035, -78.1732],
        [0.4018, -78.1720]
    ]
    folium.PolyLine(
        locations=canal_coords,
        color="#00d2d3",
        weight=5,
        dash_array='8, 8',
        popup="<b>Canal de Riego Principal (Agua Corriente):</b> Foco clave de fijación y eclosión de larvas de <i>Simuliidae</i>.",
        tooltip="Canal de Riego / Acequia (Foco Larvario)"
    ).add_to(fg_canales)

    # Acequia secundaria cerca del Ingenio
    acequia_ingenio = [
        [0.4060, -78.1752],
        [0.4052, -78.1745],
        [0.4045, -78.1742]
    ]
    folium.PolyLine(
        locations=acequia_ingenio,
        color="#00d2d3",
        weight=4,
        dash_array='5, 5',
        popup="<b>Acequia de Desvío Ingenio:</b> Monitoreo de macrófitas acuáticas.",
        tooltip="Acequia Secundaria Ingenio"
    ).add_to(fg_canales)

    # Marcadores en puntos críticos de corriente hídrica
    focos_puntos = [
        ([0.4062, -78.1748], "Foco Larvario Norte - Turbulencia Oxigenada"),
        ([0.4048, -78.1740], "Foco Larvario Central - Conexión Ingenio"),
        ([0.4035, -78.1732], "Foco Larvario Sur - Desagüe Agrícola")
    ]
    for pt, desc in focos_puntos:
        folium.CircleMarker(
            location=pt,
            radius=6,
            color="#0984e3",
            fill=True,
            fill_color="#74b9ff",
            fill_opacity=0.9,
            popup=f"<b>Punto Crítico Hidrológico:</b> {desc}",
            tooltip="Punto crítico de desarrollo larvario"
        ).add_to(fg_canales)

    # ------------------------------------------
    # 3. EDIFICACIONES CLAVE (Del Mapa Georreferencial)
    # ------------------------------------------
    edificios_info = [
        ([0.4030, -78.1775], "Multifamiliares (Bloque A-D)", "home", "green", "Residencias Estudiantiles"),
        ([0.4040, -78.1780], "Pats Residenciales", "home", "green", "Residencias Estudiantiles"),
        ([0.4050, -78.1745], "Aulas Patrimoniales Ingenio", "book", "blue", "Aulas y Talleres"),
        ([0.4055, -78.1735], "Laboratorios Centrales", "flask", "darkpurple", "Investigación"),
        ([0.4075, -78.1725], "Bloques de Aulas Senescyt", "graduation-cap", "red", "Aulas Académicas"),
        ([0.4082, -78.1718], "Comedor / Cafetería Campus", "cutlery", "orange", "Zona de Alimentación"),
        ([0.4046, -78.1738], "Cafetería Ingenio", "coffee", "orange", "Zona de Alimentación")
    ]
    for coord, nombre, icono, color, cat in edificios_info:
        folium.Marker(
            location=coord,
            icon=folium.Icon(icon=icono, prefix='fa', color=color),
            popup=f"<b>{nombre}</b><br>Categoría: {cat}",
            tooltip=nombre
        ).add_to(fg_edificios)

    # ------------------------------------------
    # 4. PROPUESTA: CERCAS VIVAS REPELENTES (Algoritmo Verde YT)
    # ------------------------------------------
    # Cerca 1: Cordón de protección residencial (Multifamiliares y Pats)
    cerca_residencias = [
        [0.4025, -78.1760],
        [0.4036, -78.1752],
        [0.4047, -78.1762]
    ]
    folium.PolyLine(
        locations=cerca_residencias,
        color="#27ae60",
        weight=6,
        popup=folium.Popup("""
            <div style="font-family: Arial; width: 230px;">
                <h4 style="color: #27ae60; margin: 0 0 5px 0;">Cerca Viva 1 - Sector Residencial</h4>
                <b>Longitud:</b> 380 metros lineales.<br>
                <b>Especies:</b> <i>Cymbopogon citratus</i> (Hierba Luisa/Citronela) + <i>Schinus molle</i> (Pimiento nativo).<br>
                <b>Densidad:</b> 2 plántulas / metro.<br>
                <b>Efecto:</b> Bloqueo del viento Este-Oeste con fitocompuestos repelentes volátiles.
            </div>
        """, max_width=250),
        tooltip="🌿 Cerca Viva 1: Sector Residencias (380m)"
    ).add_to(fg_cercas)

    # Cerca 2: Barrera de ribera canal Ingenio
    cerca_ingenio = [
        [0.4061, -78.1744],
        [0.4052, -78.1738],
        [0.4042, -78.1730]
    ]
    folium.PolyLine(
        locations=cerca_ingenio,
        color="#27ae60",
        weight=6,
        popup=folium.Popup("""
            <div style="font-family: Arial; width: 230px;">
                <h4 style="color: #27ae60; margin: 0 0 5px 0;">Cerca Viva 2 - Sector Ingenio</h4>
                <b>Longitud:</b> 280 metros lineales.<br>
                <b>Especies:</b> <i>Lantana camara</i> + <i>Lavandula angustifolia</i>.<br>
                <b>Función:</b> Barrera aromática de transición entre canal y caminerías de aulas.
            </div>
        """, max_width=250),
        tooltip="🌿 Cerca Viva 2: Sector Ingenio (280m)"
    ).add_to(fg_cercas)

    # Cerca 3: Cordón perimetral Senescyt
    cerca_senescyt = [
        [0.4072, -78.1735],
        [0.4085, -78.1730],
        [0.4092, -78.1712]
    ]
    folium.PolyLine(
        locations=cerca_senescyt,
        color="#27ae60",
        weight=6,
        popup=folium.Popup("""
            <div style="font-family: Arial; width: 230px;">
                <h4 style="color: #27ae60; margin: 0 0 5px 0;">Cerca Viva 3 - Sector Senescyt</h4>
                <b>Longitud:</b> 320 metros lineales.<br>
                <b>Especies:</b> <i>Myrcianthes hallii</i> (Arrayán nativo) + <i>Rosmarinus officinalis</i>.<br>
                <b>Función:</b> Protección contra corrientes de aire ascendentes del valle.
            </div>
        """, max_width=250),
        tooltip="🌿 Cerca Viva 3: Sector Senescyt (320m)"
    ).add_to(fg_cercas)

    # ------------------------------------------
    # 5. BUFFERS DE PROTECCIÓN REPELENTE (Área de Amortiguamiento)
    # ------------------------------------------
    # Simulación de buffer de 40m alrededor de las cercas vivas
    for coords, name in [(cerca_residencias, "Buffer Residencial"), (cerca_ingenio, "Buffer Ingenio"), (cerca_senescyt, "Buffer Senescyt")]:
        folium.PolyLine(
            locations=coords,
            color="#2ecc71",
            weight=35,
            opacity=0.25,
            tooltip=f"Área de Amortiguamiento Repelente ({name})"
        ).add_to(fg_buffer)

    # ------------------------------------------
    # 6. RED DE TRAMPAS BIOLÓGICAS DE MONITOREO
    # ------------------------------------------
    trampas_pos = [
        ([0.4038, -78.1750], "T-01: Intersección Pats / Canal"),
        ([0.4028, -78.1758], "T-02: Borde Sur Residencias"),
        ([0.4050, -78.1735], "T-03: Paso Peatonal Central Ingenio"),
        ([0.4058, -78.1742], "T-04: Transición Ingenio-Laboratorios"),
        ([0.4075, -78.1732], "T-05: Entrada Bloques Senescyt"),
        ([0.4088, -78.1722], "T-06: Perímetro Comedor Central")
    ]
    for coord, label in trampas_pos:
        folium.Marker(
            location=coord,
            icon=folium.Icon(icon="crosshairs", prefix="fa", color="darkblue"),
            popup=f"""
                <b>Trampa Ecológica de Monitoreo</b><br>
                <b>Código:</b> {label}<br>
                <b>Atrayente:</b> Cebo bio-ecológico (ácido L-láctico + CO2 por fermentación controlada).<br>
                <b>Función:</b> Cuantificación de densidad de <i>Simuliidae</i> y validación de eficacia (RF-04).
            """,
            tooltip=label
        ).add_to(fg_trampas)

    # Agregar todas las capas al mapa
    fg_zonas.add_to(m)
    fg_canales.add_to(m)
    fg_edificios.add_to(m)
    fg_cercas.add_to(m)
    fg_buffer.add_to(m)
    fg_trampas.add_to(m)

    # Control de Capas
    folium.LayerControl(position='topright', collapsed=False).add_to(m)

    # MiniMap
    plugins.MiniMap(toggle_display=True, position='bottomleft').add_to(m)

    # Medidor de distancia
    plugins.MeasureControl(position='topleft', primary_length_unit='meters', primary_area_unit='sqmeters').add_to(m)

    # Widget / Dashboard Flotante Superior Izquierdo con CSS Personalizado
    dashboard_html = """
    <div style="
        position: fixed;
        bottom: 30px;
        right: 30px;
        width: 310px;
        z-index: 9999;
        background: rgba(255, 255, 255, 0.95);
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
            <b>YOSW 2026 · Reto 3:</b> Control de Arenillas mediante Manejo Integrado y Optimización Espacial.
        </p>
        <hr style="border: none; border-top: 1px solid #dfe4ea; margin: 8px 0;">
        <table style="width: 100%; font-size: 11px; line-height: 1.6; color: #2f3542;">
            <tr>
                <td>🌿 <b>Cercas Vivas:</b></td>
                <td style="text-align: right; font-weight: bold; color: #27ae60;">980 m lineales</td>
            </tr>
            <tr>
                <td>🌱 <b>Plántulas Repelentes:</b></td>
                <td style="text-align: right; font-weight: bold; color: #27ae60;">~1,960 unid.</td>
            </tr>
            <tr>
                <td>🎯 <b>Trampas de Monitoreo:</b></td>
                <td style="text-align: right; font-weight: bold; color: #1e3799;">6 estaciones</td>
            </tr>
            <tr>
                <td>🛡️ <b>Área Protegida:</b></td>
                <td style="text-align: right; font-weight: bold; color: #009432;">~39,200 m²</td>
            </tr>
            <tr>
                <td>📉 <b>Reducción de Riesgo:</b></td>
                <td style="text-align: right; font-weight: bold; color: #e74c3c;">82% estimada</td>
            </tr>
        </table>
        <div style="margin-top: 10px; font-size: 10px; color: #747d8c; text-align: center;">
            *Use el selector superior derecho para filtrar capas
        </div>
    </div>
    """
    m.get_root().html.add_child(folium.Element(dashboard_html))

    output_path = "reto3_Control_Arenillas/mapa_interactivo_control_arenillas.html"
    m.save(output_path)
    print(f"Mapa generado exitosamente en: {output_path}")

if __name__ == "__main__":
    generar_mapa()
