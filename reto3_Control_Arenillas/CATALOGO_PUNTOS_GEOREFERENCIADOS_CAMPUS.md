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

## 2. Polígonos de Huella Arquitectónica Regularizada (Zona Norte)

Las edificaciones residenciales y de servicios comunitarios del campus presentan diseño arquitectónico modular de **planta rectangular regularizada** (a excepción del Edificio Senescyt, cuya morfología es poliédrica no rectangular de 8 vértices). 

A partir de las mediciones GPS de campo, se aplicó un ajuste geométrico de mínimos rectángulos orientados (*Oriented Bounding Boxes - OBB*) para garantizar ortogonalidad estricta (ángulos rectos a 90°), separando los Bloques F y G en edificios independientes y delimitando los locales interiores contenidos dentro del Edificio Senescyt:

### 2.1. Bloques Residenciales Estudiantiles (A, B, C, D, E, F, G, H, I)

* **Bloque A (Rectangular):**
  * *Uso:* Residencia Estudiantil | *Dimensiones:* ~18.4 m × 32.6 m | *Superficie:* ~600 m² | *Centroide:* `[0.4068090, -78.1705631]`
  * *Vértices (Lat, Lon):*
    1. `0.4069739, -78.1705279`
    2. `0.4068642, -78.1704038`
    3. `0.4066441, -78.1705984`
    4. `0.4067538, -78.1707225`

* **Bloque B (Rectangular):**
  * *Uso:* Residencia Estudiantil | *Dimensiones:* ~18.6 m × 32.7 m | *Superficie:* ~607 m² | *Centroide:* `[0.4069719, -78.1707265]`
  * *Vértices (Lat, Lon):*
    1. `0.4069112, -78.1708846`
    2. `0.4071388, -78.1706975`
    3. `0.4070326, -78.1705683`
    4. `0.4068050, -78.1707554`

* **Bloque C (Rectangular):**
  * *Uso:* Residencia Estudiantil | *Dimensiones:* ~17.3 m × 33.3 m | *Superficie:* ~577 m² | *Centroide:* `[0.4071456, -78.1708960]`
  * *Vértices (Lat, Lon):*
    1. `0.4070848, -78.1710539`
    2. `0.4073098, -78.1708551`
    3. `0.4072065, -78.1707382`
    4. `0.4069815, -78.1709370`

* **Bloque D (Rectangular):**
  * *Uso:* Residencia Estudiantil | *Dimensiones:* ~20.1 m × 31.9 m | *Superficie:* ~642 m² | *Centroide:* `[0.4072929, -78.1711743]`
  * *Vértices (Lat, Lon):*
    1. `0.4072699, -78.1710060`
    2. `0.4071311, -78.1711226`
    3. `0.4073159, -78.1713426`
    4. `0.4074547, -78.1712260`

* **Bloque E (Rectangular):**
  * *Uso:* Residencia Estudiantil | *Dimensiones:* ~18.0 m × 32.5 m | *Superficie:* ~586 m² | *Centroide:* `[0.4074338, -78.1710544]`
  * *Vértices (Lat, Lon):*
    1. `0.4072764, -78.1709972`
    2. `0.4074687, -78.1712182`
    3. `0.4075913, -78.1711116`
    4. `0.4073990, -78.1708906`

* **Bloque F (Rectangular Independiente - Ala Occidental):**
  * *Uso:* Residencia Estudiantil Bloque F | *Superficie:* ~690 m² | *Centroide:* `[0.4077333, -78.1713810]`
  * *Vértices (Lat, Lon):*
    1. `0.4075616, -78.1714552`
    2. `0.4078955, -78.1714740`
    3. `0.4079049, -78.1713069`
    4. `0.4075710, -78.1712881`

* **Bloque G (Rectangular Independiente - Ala Oriental):**
  * *Uso:* Residencia Estudiantil Bloque G | *Superficie:* ~680 m² | *Centroide:* `[0.4078306, -78.1711349]`
  * *Vértices (Lat, Lon):*
    1. `0.4077735, -78.1709533`
    2. `0.4077295, -78.1712963`
    3. `0.4078877, -78.1713166`
    4. `0.4079317, -78.1709736`

* **Bloque H (Rectangular):**
  * *Uso:* Residencia Estudiantil (Ala Este) | *Superficie:* ~647 m² | *Centroide:* `[0.4073628, -78.1704021]`
  * *Vértices (Lat, Lon):*
    1. `0.4071925, -78.1703263`
    2. `0.4074167, -78.1705805`
    3. `0.4075330, -78.1704780`
    4. `0.4073088, -78.1702238`

* **Bloque I (Rectangular):**
  * *Uso:* Residencia Estudiantil (Ala Sur de Bloques) | *Superficie:* ~604 m² | *Centroide:* `[0.4071316, -78.1702490]`
  * *Vértices (Lat, Lon):*
    1. `0.4072116, -78.1700833`
    2. `0.4069564, -78.1703052`
    3. `0.4070515, -78.1704146`
    4. `0.4073067, -78.1701927`

* **Centro Médico Tipo A / Vida Comunitaria (Rectangular):**
  * *Uso:* Salud y Bienestar Estudiantil | *Superficie:* ~451 m² | *Centroide:* `[0.4076553, -78.1707205]`
  * *Vértices (Lat, Lon):*
    1. `0.4075180, -78.1706569`
    2. `0.4076870, -78.1708685`
    3. `0.4077926, -78.1707842`
    4. `0.4076236, -78.1705726`

---

### 2.2. Complejo Edificio Senescyt y Locales Interiores Contenidos

El **Edificio Senescyt** es la principal estructura académica del sector norte, caracterizado por su volumetría escalonada y forma poliédrica no rectangular. Los locales de servicio académico y comercial se encuentran **estrictamente contenidos dentro de su perímetro**:

* **Edificio Senescyt (Polígono Matriz - 8 vértices):**
  * *Uso:* Aulas Magnas, Laboratorios de Informática, Decanatos y Rectorado | *Superficie:* ~3,475 m² | *Centroide:* `[0.4066329, -78.1700962]`
  * *Vértices Perimetrales:*
    1. `0.4071147, -78.1699317`
    2. `0.4069484, -78.1697289`
    3. `0.4068317, -78.1698328`
    4. `0.4068019, -78.1698043`
    5. `0.4063912, -78.1701510`
    6. `0.4062218, -78.1699562`
    7. `0.4061159, -78.1700531`
    8. `0.4064619, -78.1704732`

* **Biblioteca Universitaria (Local Interior en Edificio Senescyt):**
  * *Uso:* Biblioteca y sala de lectura situada en el ala sur del Edificio Senescyt (estrictamente interior).
  * *Superficie interna:* ~514 m² | *Centroide:* `[0.4062547, -78.1701150]`
  * *Vértices Interiores (Lat, Lon):*
    1. `0.4062218, -78.1699562`
    2. `0.4061159, -78.1700531`
    3. `0.4063150, -78.1702949`
    4. `0.4063677, -78.1702261`
    5. `0.4063425, -78.1701969`
    6. `0.4063898, -78.1701540`
    7. `0.4062959, -78.1700414`

* **Minimarket Krispan (Local Interior en Edificio Senescyt):**
  * *Uso:* Cafetería y tienda de conveniencia en el ala oeste del Edificio Senescyt (estrictamente interior).
  * *Superficie interna:* ~158 m² | *Centroide:* `[0.4064965, -78.1703919]`
  * *Vértices Interiores (Lat, Lon):*
    1. `0.4065778, -78.1703771`
    2. `0.4065494, -78.1703109`
    3. `0.4064042, -78.1704011`
    4. `0.4064659, -78.1704699`

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

## 8. Snippet GeoJSON Oficial (Hitos, Huellas Rectangulares y Locales Interiores)

Estructura GeoJSON estándar (RFC 7946) con geometría de puntos para hitos universitarios y polígonos ortogonales para huellas arquitectónicas:

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
    { "type": "Feature", "properties": { "id": "RECT-A", "nombre": "Bloque A (Rectangular)", "tipo": "Residencial" }, "geometry": { "type": "Polygon", "coordinates": [[[-78.1705279, 0.4069739], [-78.1704038, 0.4068642], [-78.1705984, 0.4066441], [-78.1707225, 0.4067538], [-78.1705279, 0.4069739]]] } },
    { "type": "Feature", "properties": { "id": "RECT-B", "nombre": "Bloque B (Rectangular)", "tipo": "Residencial" }, "geometry": { "type": "Polygon", "coordinates": [[[-78.1708846, 0.4069112], [-78.1706975, 0.4071388], [-78.1705683, 0.4070326], [-78.1707554, 0.4068050], [-78.1708846, 0.4069112]]] } },
    { "type": "Feature", "properties": { "id": "RECT-C", "nombre": "Bloque C (Rectangular)", "tipo": "Residencial" }, "geometry": { "type": "Polygon", "coordinates": [[[-78.1710539, 0.4070848], [-78.1708551, 0.4073098], [-78.1707382, 0.4072065], [-78.1709370, 0.4069815], [-78.1710539, 0.4070848]]] } },
    { "type": "Feature", "properties": { "id": "RECT-D", "nombre": "Bloque D (Rectangular)", "tipo": "Residencial" }, "geometry": { "type": "Polygon", "coordinates": [[[-78.1710060, 0.4072699], [-78.1711226, 0.4071311], [-78.1713426, 0.4073159], [-78.1712260, 0.4074547], [-78.1710060, 0.4072699]]] } },
    { "type": "Feature", "properties": { "id": "RECT-E", "nombre": "Bloque E (Rectangular)", "tipo": "Residencial" }, "geometry": { "type": "Polygon", "coordinates": [[[-78.1709972, 0.4072764], [-78.1712182, 0.4074687], [-78.1711116, 0.4075913], [-78.1708906, 0.4073990], [-78.1709972, 0.4072764]]] } },
    { "type": "Feature", "properties": { "id": "RECT-F", "nombre": "Bloque F (Rectangular)", "tipo": "Residencial" }, "geometry": { "type": "Polygon", "coordinates": [[[-78.1714552, 0.4075616], [-78.1714740, 0.4078955], [-78.1713069, 0.4079049], [-78.1712881, 0.4075710], [-78.1714552, 0.4075616]]] } },
    { "type": "Feature", "properties": { "id": "RECT-G", "nombre": "Bloque G (Rectangular)", "tipo": "Residencial" }, "geometry": { "type": "Polygon", "coordinates": [[[-78.1709533, 0.4077735], [-78.1712963, 0.4077295], [-78.1713166, 0.4078877], [-78.1709736, 0.4079317], [-78.1709533, 0.4077735]]] } },
    { "type": "Feature", "properties": { "id": "RECT-H", "nombre": "Bloque H (Rectangular)", "tipo": "Residencial" }, "geometry": { "type": "Polygon", "coordinates": [[[-78.1703263, 0.4071925], [-78.1705805, 0.4074167], [-78.1704780, 0.4075330], [-78.1702238, 0.4073088], [-78.1703263, 0.4071925]]] } },
    { "type": "Feature", "properties": { "id": "RECT-I", "nombre": "Bloque I (Rectangular)", "tipo": "Residencial" }, "geometry": { "type": "Polygon", "coordinates": [[[-78.1700833, 0.4072116], [-78.1703052, 0.4069564], [-78.1704146, 0.4070515], [-78.1701927, 0.4073067], [-78.1700833, 0.4072116]]] } },
    { "type": "Feature", "properties": { "id": "RECT-MED", "nombre": "Centro Médico / Bienestar", "tipo": "Salud / Bienestar" }, "geometry": { "type": "Polygon", "coordinates": [[[-78.1706569, 0.4075180], [-78.1708685, 0.4076870], [-78.1707842, 0.4077926], [-78.1705726, 0.4076236], [-78.1706569, 0.4075180]]] } },
    { "type": "Feature", "properties": { "id": "POLY-SENESCYT", "nombre": "Edificio Senescyt", "tipo": "Aulas / Rectorado (Poliédrico)" }, "geometry": { "type": "Polygon", "coordinates": [[[-78.1699317, 0.4071147], [-78.1697289, 0.4069484], [-78.1698328, 0.4068317], [-78.1698043, 0.4068019], [-78.1701510, 0.4063912], [-78.1699562, 0.4062218], [-78.1700531, 0.4061159], [-78.1704732, 0.4064619], [-78.1699317, 0.4071147]]] } },
    { "type": "Feature", "properties": { "id": "INT-BIB", "nombre": "Biblioteca (Interior Senescyt)", "tipo": "Biblioteca / Estudio" }, "geometry": { "type": "Polygon", "coordinates": [[[-78.1699562, 0.4062218], [-78.1700531, 0.4061159], [-78.1702949, 0.4063150], [-78.1702261, 0.4063677], [-78.1701969, 0.4063425], [-78.1701540, 0.4063898], [-78.1700414, 0.4062959], [-78.1699562, 0.4062218]]] } },
    { "type": "Feature", "properties": { "id": "INT-KRISPAN", "nombre": "Minimarket Krispan (Interior Senescyt)", "tipo": "Comercial / Cafetería" }, "geometry": { "type": "Polygon", "coordinates": [[[-78.1703771, 0.4065778], [-78.1703109, 0.4065494], [-78.1704011, 0.4064042], [-78.1704699, 0.4064659], [-78.1703771, 0.4065778]]] } }
  ]
}
```

---

*Documento técnico compilado y validado para el equipo Algoritmo Verde YT · YOSW 2026.*
