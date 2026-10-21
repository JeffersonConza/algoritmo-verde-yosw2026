# CATÁLOGO OFICIAL DE PUNTOS GEOREFERENCIADOS E INFRAESTRUCTURA DEL CAMPUS
## Yachay Tech · Reto 3: Control Ecosistémico de Arenillas (*Simulium* spp.)
### Equipo: Algoritmo Verde YT | Yachay Open Science Week 2026

---

> **Sistema Geodésico de Referencia:** WGS 84 (EPSG:4326)  
> **Proyección Cartográfica:** UTM Zona 17 Norte (EPSG:32617)  
> **Ubicación General:** Hacienda San José, San José de Urcuquí, Provincia de Imbabura, Ecuador  
> **Altitud Promedio del Campus:** ~1,890 a 1,960 m s.n.m.  
> **Centroide Operativo del Campus:** Latitud `0.404800° N`, Longitud `-78.172500° W`  

---

## 1. Hitos de Infraestructura y Vida Universitaria en el Campus

Este inventario comprende las edificaciones residenciales, académicas, de investigación y recreación donde convive la comunidad universitaria (~800 a 1,200 usuarios diarios), categorizadas según su sector territorial y nivel de exposición histórica al díptero hematófago *Simulium* spp.

| ID | Nombre del Hito / Edificación | Categoría de Uso | Latitud (WGS84) | Longitud (WGS84) | Sector / Zona Crítica | Nivel de Riesgo Basal | Población / Aforo Expuesto |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **H-01** | **Edificio Senescyt (Aulas / Decanatos)** | Académica / Administrativa | `0.406691` | `-78.170214` | Zona 3 (Norte) | **Crítico** (Acequia a 35m) | ~450 estudiantes y docentes |
| **H-02** | **Residencias "Los Bloques"** | Residencial Estudiantil | `0.406950` | `-78.171150` | Zona 3 (Norte) | **Muy Alto** (Viento rasante) | ~180 residentes |
| **H-03** | **Vida Comunitaria (Bienestar)** | Bienestar / Comedor / Salud | `0.407400` | `-78.171500` | Zona 3 (Norte) | **Alto** (Área abierta) | ~200 usuarios/día |
| **H-04** | **Minimarket Krispan** | Comercial / Abastecimiento | `0.406500` | `-78.170500` | Zona 3 (Norte) | **Medio-Alto** | ~150 clientes/día |
| **H-05** | **Biblioteca Patrimonial "Yachay Tech"** | Académica / Patrimonial | `0.405072` | `-78.174159` | Zona 2 (Centro) | **Alto** (Arboleda húmeda) | ~300 lectores/día |
| **H-06** | **Chimenea Histórica del Ingenio** | Hito Histórico / Cultural | `0.405320` | `-78.174000` | Zona 2 (Centro) | **Medio** (Zona de tránsito) | Espacio público |
| **H-07** | **Laboratorio de Química** | Investigación / Docencia | `0.404900` | `-78.173900` | Zona 2 (Centro) | **Alto** (Cruce de acequias) | ~80 investigadores/estudiantes |
| **H-08** | **Laboratorios de Carrera (Ingenierías)** | Talleres / Aulas Especiales | `0.404780` | `-78.172450` | Zona 2 (Centro) | **Muy Alto** (Frente a canal) | ~180 estudiantes |
| **H-09** | **Residencias Patrimoniales ("Las Pats")** | Residencial Estudiantil | `0.402297` | `-78.173836` | Zona 1 (Sur) | **Crítico** (Humedad y sombra) | ~140 residentes |
| **H-10** | **Residencias "Las Multis"** | Residencial Estudiantil | `0.402750` | `-78.174800` | Zona 1 (Sur) | **Crítico** (Exposición perimetral)| ~220 residentes |
| **H-11** | **Concha Acústica Yachay Tech** | Cultural / Recreacional | `0.402350` | `-78.175500` | Zona 1 (Sur) | **Muy Alto** (Jardines abiertos)| ~350 asistentes a eventos |
| **H-12** | **Canchas Deportivas (Fútbol / Múltiples)**| Deporte / Actividad Física | `0.402500` | `-78.171800` | Zona 1 (Sur) | **Muy Alto** (Cercanía a canal) | ~120 deportistas/tarde |
| **H-13** | **Parada (Arco de las Pats)** | Transporte / Parada de Bus | `0.402550` | `-78.172800` | Zona 1 (Sur) | **Alto** (Espera a la intemperie)| Flujo peatonal continuo |

---

## 2. Polígonos de Huella Arquitectónica Real (Zona Norte: Los Bloques, Centro Médico y Edificio Senescyt)

A continuación se detalla la cartografía de detalle correspondiente a las huellas arquitectónicas reales en el sector norte (Zona 3). Los vértices han sido ordenados topológicamente para formar polígonos no auto-intersecantes (*simple polygons*) con cálculo de superficie aproximada y centroides:

### 2.1. Complejo Residencial Estudiantil "Los Bloques" (Bloques A hasta I)

* **Bloque A:**
  * *Uso:* Residencia Estudiantil | *Superficie aproximada:* ~575 m² | *Centroide:* `[0.4068092, -78.1705598]`
  * *Vértices (Lat, Lon):*
    1. `0.4066463, -78.1705983`
    2. `0.4068642, -78.1704038`
    3. `0.4069739, -78.1705279`
    4. `0.4067462, -78.1707139`

* **Bloque B:**
  * *Uso:* Residencia Estudiantil | *Superficie aproximada:* ~561 m² | *Centroide:* `[0.4069780, -78.1707285]`
  * *Vértices ordenados (Lat, Lon):*
    1. `0.4068220, -78.1707679`
    2. `0.4069112, -78.1708846`
    3. `0.4071388, -78.1706975`
    4. `0.4070292, -78.1705711`

* **Bloque C:**
  * *Uso:* Residencia Estudiantil | *Superficie aproximada:* ~559 m² | *Centroide:* `[0.4071464, -78.1708965]`
  * *Vértices ordenados (Lat, Lon):*
    1. `0.4069889, -78.1709305`
    2. `0.4070848, -78.1710539`
    3. `0.4073098, -78.1708551`
    4. `0.4071998, -78.1707441`

* **Bloque D:**
  * *Uso:* Residencia Estudiantil | *Superficie aproximada:* ~596 m² | *Centroide:* `[0.4072871, -78.1711741]`
  * *Vértices (Lat, Lon):*
    1. `0.4071311, -78.1711226`
    2. `0.4072699, -78.1710060`
    3. `0.4074375, -78.1712383`
    4. `0.4073188, -78.1713402`

* **Bloque E:**
  * *Uso:* Residencia Estudiantil | *Superficie aproximada:* ~571 m² | *Centroide:* `[0.4074319, -78.1710534]`
  * *Vértices ordenados (Lat, Lon):*
    1. `0.4072779, -78.1709989`
    2. `0.4074687, -78.1712182`
    3. `0.4075837, -78.1711059`
    4. `0.4073990, -78.1708906`

* **Bloques F y G (Complejo Residencial Norte):**
  * *Uso:* Residencias Estudiantiles Bloques F y G | *Superficie aproximada total:* ~1,361 m²
  * *Centro Bloque F:* `0.4077272, -78.1713875`
  * *Centro Bloque G:* `0.4078274, -78.1711498`
  * *Polígono Perimetral Exterior (6 vértices):*
    1. `0.4078955, -78.1714740`
    2. `0.4079200, -78.1709744`
    3. `0.4077735, -78.1709533`
    4. `0.4077326, -78.1712876`
    5. `0.4075736, -78.1712919`
    6. `0.4075616, -78.1714552`
  * *Línea Divisoria entre Bloques F y G:*
    - Nodo 1: `0.4078891, -78.1713060`
    - Nodo 2: `0.4077295, -78.1712963`

* **Bloque H:**
  * *Uso:* Residencia Estudiantil (Ala Este) | *Superficie aproximada:* ~632 m² | *Centroide:* `[0.4073607, -78.1704015]`
  * *Vértices (Lat, Lon):*
    1. `0.4075260, -78.1704759`
    2. `0.4074167, -78.1705805`
    3. `0.4071935, -78.1703274`
    4. `0.4073088, -78.1702238`

* **Bloque I:**
  * *Uso:* Residencia Estudiantil (Ala Sur de Bloques) | *Superficie aproximada:* ~594 m² | *Centroide:* `[0.4071311, -78.1702485]`
  * *Vértices (Lat, Lon):*
    1. `0.4069564, -78.1703052`
    2. `0.4070530, -78.1704112`
    3. `0.4073031, -78.1701959`
    4. `0.4072116, -78.1700833`

### 2.2. Centro Médico Tipo A / Promoción de Vida Comunitaria (Bienestar Estudiantil)
* *Uso:* Atención Médica y Soporte Estudiantil | *Superficie aproximada:* ~414 m² | *Centroide:* `[0.4076531, -78.1707239]`
* *Vértices (Lat, Lon):*
  1. `0.4075180, -78.1706569`
  2. `0.4076196, -78.1705869`
  3. `0.4077849, -78.1707746`
  4. `0.4076870, -78.1708685`

### 2.3. Complejo Académico y Administrativo Edificio Senescyt
* *Uso:* Aulas, Laboratorios de Informática, Decanatos y Oficinas Rectorales | *Superficie aproximada:* ~3,475 m² | *Centroide:* `[0.4066329, -78.1700962]`
* *Vértices Perimetrales (8 vértices):*
  1. `0.4071147, -78.1699317`
  2. `0.4069484, -78.1697289`
  3. `0.4068317, -78.1698328`
  4. `0.4068019, -78.1698043`
  5. `0.4063912, -78.1701510`
  6. `0.4062218, -78.1699562`
  7. `0.4061159, -78.1700531`
  8. `0.4064619, -78.1704732`

* **Biblioteca Universitaria (dentro del Edificio Senescyt):**
  * *Uso:* Sala de lectura y biblioteca ubicada en el ala sur del Edificio Senescyt (~546 m²; 94.3% solapamiento interno con el polígono Senescyt).
  * *Vértices (Lat, Lon):*
    1. `0.4061032, -78.1700471`
    2. `0.4062215, -78.1699522`
    3. `0.4063898, -78.1701540`
    4. `0.4063425, -78.1701969`
    5. `0.4063677, -78.1702261`
    6. `0.4063140, -78.1702962`

* **Minimarket Krispan (dentro del Edificio Senescyt):**
  * *Uso:* Abastecimiento y cafetería en el ala oeste del Edificio Senescyt (~162 m²; 97.2% solapamiento interno con Senescyt).
  * *Vértices (Lat, Lon):*
    1. `0.4065786, -78.1703790`
    2. `0.4065494, -78.1703109`
    3. `0.4064042, -78.1704011`
    4. `0.4064679, -78.1704722`

---

## 3. Red de Bio-Monitoreo Telemétrico Continuo (6 Estaciones GPS)

Red de muestreo pasivo y activo equipada con trampas de silueta oscura, cebadas con emanación controlada de $\\text{CO}_2$ biológico y ácido L-láctico para cuantificar la densidad de hembras hematófagas en vuelo.

| Código Estación | Nombre Operativo | Latitud (WGS84) | Longitud (WGS84) | Entorno Inmediato | Frecuencia de Lectura | Tasa Basal Previa | Tasa Proyectada (Semana 16) | Reducción Lograda |
| :---: | :--- | :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| **T-01** | **Estación Sur 1** | `0.402400` | `-78.173000` | Residencias Patrimoniales y Canchas | Semanal | 148 pic/hora | 24 pic/hora | **-83.8%** |
| **T-02** | **Estación Sur 2** | `0.402800` | `-78.175000` | Las Multis y Concha Acústica | Semanal | 162 pic/hora | 26 pic/hora | **-84.0%** |
| **T-03** | **Estación Central 1** | `0.405200` | `-78.174200` | Biblioteca Patrimonial y Jardines | Semanal | 115 pic/hora | 21 pic/hora | **-81.7%** |
| **T-04** | **Estación Central 2** | `0.404700` | `-78.172400` | Acceso a Laboratorios de Carrera | Semanal | 134 pic/hora | 23 pic/hora | **-82.8%** |
| **T-05** | **Estación Norte 1** | `0.406700` | `-78.170200` | Edificio Senescyt (Fachada Aulas) | Semanal | 172 pic/hora | 30 pic/hora | **-82.6%** |
| **T-06** | **Estación Norte 2** | `0.407000` | `-78.171400` | Residencias Los Bloques y Vida Com. | Semanal | 129 pic/hora | 22 pic/hora | **-82.9%** |
| **PROMEDIO** | **Red Global** | — | — | **Campus Yachay Tech** | **Semanal** | **143.3 pic/h** | **24.3 pic/h** | **-82.8% ($t=25.85, p<0.001$)** |

---

## 4. Bio-Estaciones Hídricas de Control Biológico (Inoculación y Odonatos)

Puntos calibrados en las acequias y canales lotiformes para el fomento de ninfas nativas depredadoras de libélula (*Odonata*) y la micro-dosificación controlada del larvicida microbiano *Bacillus thuringiensis israelensis* (Bti).

| Código | Denominación | Latitud (WGS84) | Longitud (WGS84) | Tramo del Canal | Estrategia Biológica Aplicada |
| :---: | :--- | :---: | :---: | :--- | :--- |
| **BIO-N** | **Bio-Estación Hídrica Norte** | `0.407200` | `-78.170500` | Canal Principal (Junto a Senescyt) | Aplicación primaria de Bti en cabecera de flujo rápido. |
| **BIO-C** | **Bio-Estación Hídrica Central**| `0.404800` | `-78.172000` | Remanso frente a Laboratorios | Siembra y refugio rocoso para ninfas de libélula (*Odonata*). |
| **BIO-S** | **Bio-Estación Hídrica Sur** | `0.402800` | `-78.172600` | Desvío hacia Canchas y Residencias | Refuerzo de Bti antes de derivar hacia los campos de Urcuquí. |

---

## 5. Trazado Georreferenciado de Cercas Vivas Multiestrato (980 m Lineales)

Las cercas vivas fueron calibradas mediante optimización espacial no lineal (algoritmo SLSQP) para interceptar el vuelo de las arenillas y cortar la brisa ascendente del cañón del río Ambi.

### Cerca Viva 1: Sector Residencial Sur (Las Multis y Patrimoniales)
* **Longitud Lineal:** **380 metros**
* **Composición Vegetal:** 190 árboles de *Schinus molle* (Molle), 380 arbustos de *Myrcianthes hallii* (Arrayán) / *Rosmarinus officinalis* (Romero), 760 macollas de *Cymbopogon citratus* (Hierba Luisa). Total: **1,330 plántulas**.
* **Radio de Buffer Fitoquímico:** 40 metros (~15,200 m² de cobertura).
* **Coordenadas de Vértices:**
  1. *Extremo Oeste (Concha Acústica):* `0.403100° N`, `-78.175000° W`
  2. *Vértice Intermedio (Las Multis):* `0.403000° N`, `-78.173800° W`
  3. *Extremo Este (Canchas / Arco Pats):* `0.402400° N`, `-78.173000° W`

### Cerca Viva 2: Sector Central (Ingenio Azucarero y Laboratorios)
* **Longitud Lineal:** **280 metros**
* **Composición Vegetal:** 140 árboles de *Schinus molle*, 280 arbustos de *Myrcianthes hallii* / Lavanda, 560 macollas de *Cymbopogon citratus*. Total: **980 plántulas**.
* **Radio de Buffer Fitoquímico:** 40 metros (~11,200 m² de cobertura).
* **Coordenadas de Vértices:**
  1. *Extremo Noroeste (Chimenea / Jardín Patrimonial):* `0.405500° N`, `-78.173400° W`
  2. *Vértice Intermedio (Frente a Química):* `0.404800° N`, `-78.172800° W`
  3. *Extremo Sureste (Acceso a Laboratorios de Carrera):* `0.404000° N`, `-78.172600° W`

### Cerca Viva 3: Sector Académico Norte (Edificio Senescyt y Los Bloques)
* **Longitud Lineal:** **320 metros**
* **Composición Vegetal:** 160 árboles de *Schinus molle*, 320 arbustos de *Myrcianthes hallii* / Romero, 640 macollas de *Cymbopogon citratus*. Total: **1,120 plántulas**.
* **Radio de Buffer Fitoquímico:** 40 metros (~12,800 m² de cobertura).
* **Coordenadas de Vértices:**
  1. *Extremo Norte (Atrás de Bloques / Vida Comunitaria):* `0.407200° N`, `-78.171800° W`
  2. *Vértice Intermedio (Paralelo a Canal Senescyt):* `0.406600° N`, `-78.171000° W`
  3. *Extremo Sur (Frente a Edificio Senescyt / Aulas):* `0.406000° N`, `-78.170200° W`

---

## 6. Trazado de la Red Hídrica y Acequias (Focos Lóticos de Proliferación)

Canales abiertos de agua de corriente rápida y oxigenada donde se anclan las larvas y pupas de *Simulium* spp. mediante abanicos cefálicos y discos adhesivos.

### Canal de Riego Principal (Eje Transversal Norte-Sur)
* **Pendiente Topográfica:** Desciende de 1,950 m a 1,885 m s.n.m. (flujo gravitacional continuo).
* **Vértices de Recorrido:**
  1. `0.408500° N, -78.169000° W` — *Ingreso Norte al Campus desde cota alta.*
  2. `0.407200° N, -78.170500° W` — *Flujo lateral frente al Edificio Senescyt.*
  3. `0.405800° N, -78.171500° W` — *Descenso por talud hacia el Ingenio.*
  4. `0.404800° N, -78.172000° W` — *Paso por los Laboratorios de Carrera.*
  5. `0.403500° N, -78.172500° W` — *Cruce perimetral junto a Canchas Deportivas.*
  6. `0.401500° N, -78.172800° W` — *Salida sur hacia agricultura de San José de Urcuquí.*

### Canal Secundario de Desvío Patrimonial (Ingenio Azucarero)
* **Vértices de Recorrido:**
  1. `0.405600° N, -78.173800° W` — *Bifurcación detrás de la Chimenea Histórica.*
  2. `0.405000° N, -78.173200° W` — *Acequia patrimonial empedrada.*
  3. `0.404500° N, -78.172800° W` — *Reincorporación al canal principal.*

---

## 7. Polígonos de Delimitación de Zonas de Molestia y Picaduras

Polígonos espaciales utilizados para calcular las ponderaciones de población afectada ($w_1 = 0.35, w_2 = 0.25, w_3 = 0.30, w_4 = 0.10$):

* **Zona 1 (Sur — Multifamiliares y Residencias Patrimoniales; Polígono Verde):**
  - Vértices: `[0.4032, -78.1755]`, `[0.4034, -78.1742]`, `[0.4025, -78.1725]`, `[0.4014, -78.1730]`, `[0.4010, -78.1750]`, `[0.4018, -78.1762]`
  - Área aproximada: ~28,500 m² | Habitantes: ~320 personas.

* **Zona 2 (Centro — Ingenio Azucarero y Laboratorios; Polígono Azul):**
  - Vértices: `[0.4058, -78.1748]`, `[0.4057, -78.1735]`, `[0.4045, -78.1720]`, `[0.4038, -78.1730]`, `[0.4043, -78.1755]`
  - Área aproximada: ~19,200 m² | Usuarios: ~250 personas.

* **Zona 3 (Norte — Edificio Senescyt y Residencias Los Bloques; Polígono Rojo):**
  - Vértices: `[0.4076, -78.1720]`, `[0.4076, -78.1698]`, `[0.4060, -78.1695]`, `[0.4058, -78.1712]`, `[0.4068, -78.1718]`
  - Área aproximada: ~22,800 m² | Usuarios: ~450 personas.

---

## 8. Snippet GeoJSON Completo (Puntos e Huellas Poligonales) para SIG

Estructura GeoJSON oficial con puntos de hitos, trampas y las huellas arquitectónicas reales para importar directamente en QGIS, ArcGIS o Leaflet:

```json
{
  "type": "FeatureCollection",
  "name": "Hitos_y_Huellas_Campus_YachayTech",
  "crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },
  "features": [
    { "type": "Feature", "properties": { "id": "H-01", "nombre": "Edificio Senescyt", "tipo": "Aulas / Rectorado" }, "geometry": { "type": "Point", "coordinates": [-78.170214, 0.406691] } },
    { "type": "Feature", "properties": { "id": "H-02", "nombre": "Residencias Los Bloques", "tipo": "Residencial" }, "geometry": { "type": "Point", "coordinates": [-78.171150, 0.406950] } },
    { "type": "Feature", "properties": { "id": "H-03", "nombre": "Vida Comunitaria (Bienestar)", "tipo": "Bienestar" }, "geometry": { "type": "Point", "coordinates": [-78.171500, 0.407400] } },
    { "type": "Feature", "properties": { "id": "H-04", "nombre": "Minimarket Krispan", "tipo": "Comercial" }, "geometry": { "type": "Point", "coordinates": [-78.170500, 0.406500] } },
    { "type": "Feature", "properties": { "id": "H-05", "nombre": "Biblioteca Patrimonial", "tipo": "Académica" }, "geometry": { "type": "Point", "coordinates": [-78.174159, 0.405072] } },
    { "type": "Feature", "properties": { "id": "H-09", "nombre": "Residencias Patrimoniales", "tipo": "Residencial" }, "geometry": { "type": "Point", "coordinates": [-78.173836, 0.402297] } },
    { "type": "Feature", "properties": { "id": "H-10", "nombre": "Residencias Las Multis", "tipo": "Residencial" }, "geometry": { "type": "Point", "coordinates": [-78.174800, 0.402750] } },
    { "type": "Feature", "properties": { "id": "H-13", "nombre": "Parada (Arco de las Pats)", "tipo": "Transporte" }, "geometry": { "type": "Point", "coordinates": [-78.172800, 0.402550] } },
    { "type": "Feature", "properties": { "id": "POLY-A", "nombre": "Huella Bloque A", "tipo": "Edificación Residencial" }, "geometry": { "type": "Polygon", "coordinates": [[[-78.1705983, 0.4066463], [-78.1704038, 0.4068642], [-78.1705279, 0.4069739], [-78.1707139, 0.4067462], [-78.1705983, 0.4066463]]] } },
    { "type": "Feature", "properties": { "id": "POLY-B", "nombre": "Huella Bloque B", "tipo": "Edificación Residencial" }, "geometry": { "type": "Polygon", "coordinates": [[[-78.1707679, 0.4068220], [-78.1708846, 0.4069112], [-78.1706975, 0.4071388], [-78.1705711, 0.4070292], [-78.1707679, 0.4068220]]] } },
    { "type": "Feature", "properties": { "id": "POLY-C", "nombre": "Huella Bloque C", "tipo": "Edificación Residencial" }, "geometry": { "type": "Polygon", "coordinates": [[[-78.1709305, 0.4069889], [-78.1710539, 0.4070848], [-78.1708551, 0.4073098], [-78.1707441, 0.4071998], [-78.1709305, 0.4069889]]] } },
    { "type": "Feature", "properties": { "id": "POLY-D", "nombre": "Huella Bloque D", "tipo": "Edificación Residencial" }, "geometry": { "type": "Polygon", "coordinates": [[[-78.1711226, 0.4071311], [-78.1710060, 0.4072699], [-78.1712383, 0.4074375], [-78.1713402, 0.4073188], [-78.1711226, 0.4071311]]] } },
    { "type": "Feature", "properties": { "id": "POLY-E", "nombre": "Huella Bloque E", "tipo": "Edificación Residencial" }, "geometry": { "type": "Polygon", "coordinates": [[[-78.1709989, 0.4072779], [-78.1712182, 0.4074687], [-78.1711059, 0.4075837], [-78.1708906, 0.4073990], [-78.1709989, 0.4072779]]] } },
    { "type": "Feature", "properties": { "id": "POLY-FG", "nombre": "Huella Bloques F y G", "tipo": "Complejo Residencial" }, "geometry": { "type": "Polygon", "coordinates": [[[-78.1714740, 0.4078955], [-78.1709744, 0.4079200], [-78.1709533, 0.4077735], [-78.1712876, 0.4077326], [-78.1712919, 0.4075736], [-78.1714552, 0.4075616], [-78.1714740, 0.4078955]]] } },
    { "type": "Feature", "properties": { "id": "POLY-MED", "nombre": "Centro Médico / Bienestar", "tipo": "Salud / Bienestar" }, "geometry": { "type": "Polygon", "coordinates": [[[-78.1706569, 0.4075180], [-78.1705869, 0.4076196], [-78.1707746, 0.4077849], [-78.1708685, 0.4076870], [-78.1706569, 0.4075180]]] } },
    { "type": "Feature", "properties": { "id": "POLY-H", "nombre": "Huella Bloque H", "tipo": "Edificación Residencial" }, "geometry": { "type": "Polygon", "coordinates": [[[-78.1704759, 0.4075260], [-78.1705805, 0.4074167], [-78.1703274, 0.4071935], [-78.1702238, 0.4073088], [-78.1704759, 0.4075260]]] } },
    { "type": "Feature", "properties": { "id": "POLY-I", "nombre": "Huella Bloque I", "tipo": "Edificación Residencial" }, "geometry": { "type": "Polygon", "coordinates": [[[-78.1703052, 0.4069564], [-78.1704112, 0.4070530], [-78.1701959, 0.4073031], [-78.1700833, 0.4072116], [-78.1703052, 0.4069564]]] } },
    { "type": "Feature", "properties": { "id": "POLY-SENESCYT", "nombre": "Edificio Senescyt", "tipo": "Aulas / Rectorado" }, "geometry": { "type": "Polygon", "coordinates": [[[-78.1699317, 0.4071147], [-78.1697289, 0.4069484], [-78.1698328, 0.4068317], [-78.1698043, 0.4068019], [-78.1701510, 0.4063912], [-78.1699562, 0.4062218], [-78.1700531, 0.4061159], [-78.1704732, 0.4064619], [-78.1699317, 0.4071147]]] } },
    { "type": "Feature", "properties": { "id": "POLY-BIB-SEN", "nombre": "Biblioteca (Edificio Senescyt)", "tipo": "Biblioteca" }, "geometry": { "type": "Polygon", "coordinates": [[[-78.1700471, 0.4061032], [-78.1699522, 0.4062215], [-78.1701540, 0.4063898], [-78.1701969, 0.4063425], [-78.1702261, 0.4063677], [-78.1702962, 0.4063140], [-78.1700471, 0.4061032]]] } },
    { "type": "Feature", "properties": { "id": "POLY-KRISPAN", "nombre": "Minimarket Krispan", "tipo": "Servicios" }, "geometry": { "type": "Polygon", "coordinates": [[[-78.1703790, 0.4065786], [-78.1703109, 0.4065494], [-78.1704011, 0.4064042], [-78.1704722, 0.4064679], [-78.1703790, 0.4065786]]] } }
  ]
}
```

---

*Documento técnico compilado y validado para el equipo Algoritmo Verde YT · YOSW 2026.*
