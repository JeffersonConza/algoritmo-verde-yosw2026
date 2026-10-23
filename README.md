# Algoritmo Verde YT 🌱🦟
### Yachay Open Science Week 2026 · Ideatón
**Reto 3:** Estrategias Innovadoras para el Control de Arenillas en el Campus de Yachay Tech  
**Institución:** Universidad Yachay Tech — Urcuquí, Imbabura, Ecuador  
**Mentor:** Ing. José Luis Flores M.Sc.  

---

## 🌐🗺️ ¡Explora el Mapa Interactivo en Vivo! (Acceso Directo)

> **¿Escaneaste nuestro Código QR?** Haz clic en el botón inferior para abrir directamente el **Visor Geoespacial Interactivo del Campus Yachay Tech** (Bilingüe `ES/EN`, Modo `Claro/Oscuro`, 286 entidades GIS, 7 tramos de Cercas Vivas y Evidencia de Campo):

<div align="center">

[![🗺️ ABRIR MAPA INTERACTIVO EN VIVO](https://img.shields.io/badge/%F0%9F%97%BA%EF%B8%8F_VER_MAPA_INTERACTIVO_EN_VIVO-Click_Aqu%C3%AD_(Abrir_Visor_Web)-10ac84?style=for-the-badge&logoColor=white)](https://jeffersonconza.github.io/algoritmo-verde-yosw2026/)

### 👉 [**https://jeffersonconza.github.io/algoritmo-verde-yosw2026/**](https://jeffersonconza.github.io/algoritmo-verde-yosw2026/) 👈

[![📄 Documento Técnico](https://img.shields.io/badge/%F0%9F%93%84_Documento_T%C3%A9cnico_APA-Ver_Markdown-1e3799?style=flat-square)](reto3_Control_Arenillas/DOCUMENTO_TECNICO_RETO3_ALGORITMO_VERDE.md)
[![📍 Catálogo GIS (286 Entidades)](https://img.shields.io/badge/%F0%9F%93%8D_Cat%C3%A1logo_GIS_Campus-286_Entidades-0abde3?style=flat-square)](reto3_Control_Arenillas/CATALOGO_PUNTOS_GEOREFERENCIADOS_CAMPUS.md)
[![🧮 Modelo Matemático SLSQP](https://img.shields.io/badge/%F0%9F%A7%AE_Optimizaci%C3%B3n_SLSQP-Python_SciPy-e67e22?style=flat-square)](reto3_Control_Arenillas/modelo_optimizacion_matematica.py)

</div>

---

## 👥 Equipo "Algoritmo Verde YT"

| Integrante | Carrera / Perfil | Rol en el Proyecto |
| :--- | :--- | :--- |
| **Jefferson Conza** | Matemáticas / Computación | **Líder Técnico & Modelado Espacial:** Algoritmos de optimización espacial, dimensionamiento de barreras y análisis de eficacia. |
| **Christopher Picuasi** | Computación | **Desarrollo de Software & Prototipo:** Implementación del visor geoespacial interactivo y visualización de datos. |
| **Francisco Ibujés** | Química | **Investigación Fitoquímica & Repelencia:** Composición de metabolitos secundarios en 3 estratos vegetales y química ambiental. |
| **Luis Collaguazo** | Biomedicina | **Entomología Médica & Salud:** Taxonomía de *Simuliidae*, control biológico por depredadores y análisis de impacto en salud. |

---

## 🎯 Descripción de la Propuesta

El proyecto aborda la problemática de insectos picadores (*Simuliidae* / moscas negras / arenillas) en el campus mediante un **enfoque de Manejo Integrado**, descartando el uso de insecticidas químicos sintéticos por su toxicidad hídrica y priorizando la sostenibilidad ambiental:

1. **Cercas Vivas Repelentes en 3 Estratos (Diseño Paisajístico y Funcional):**
   * **Estrato Alto (3-5 m):** *Schinus molle* (Pimiento nativo) para interceptar corrientes de viento del valle.
   * **Estrato Medio (1.2-2 m):** *Myrcianthes hallii* (Arrayán) y *Rosmarinus officinalis* (Romero) como cortina física a la altura de vuelo del insecto.
   * **Estrato Bajo (0.3-0.8 m):** *Cymbopogon citratus* (Hierba luisa/citronela) emitiendo monoterpenos volátiles (*citronelal, geraniol*) a ras de suelo y márgenes hídricos.
2. **Control Biológico Selectivo:**
   * Fase acuática (larval): Fomento de ninfas de libélula (odonatos nativos) en canales y aplicación microbiológica de *Bacillus thuringiensis israelensis* (Bti).
   * Fase aérea: Refugios para aves insectívoras y murciélagos.
3. **Optimización Matemática Espacial:**
   * Distribución geoespacial óptima de ~980 metros lineales de barreras vivas y 6 estaciones de monitoreo protegiendo las 3 zonas críticas del campus (Multifamiliares, Ingenio Azucarero y Senescyt).

---

## 📂 Estructura del Repositorio

```text
├── index.html                                       # Redirección y cargador para GitHub Pages
├── .nojekyll                                        # Desactiva motor Jekyll en GitHub Pages
├── .github/
│   └── workflows/
│       └── deploy_pages.yml                         # Pipeline CI/CD GitHub Pages
├── 01_Equipo_y_Estrategia/
│   ├── Directrices_Mentor_Jose_Luis_Flores.md       # Acuerdos y directrices del mentor
│   ├── Integrantes_Algoritmo_Verde_YT.md            # Datos institucionales del equipo
│   └── Respaldo_Estrategico_Ideaton_YOSW.md         # Documento maestro de estrategia
├── 02_Correos_y_Comunicaciones/                     # Trazabilidad de correos y WhatsApp
├── 03_Documentos_Congreso/                          # Guías, reglamentos y programa oficial YOSW
├── reto3_Control_Arenillas/                         # Insumos y entregables del Reto 3
│   ├── DOCUMENTO_TECNICO_RETO3_ALGORITMO_VERDE.md  # Documento técnico maestro (APA 7.ª ed.)
│   ├── DECLARACION_USO_IA_ALGORITMO_VERDE.md        # Declaración obligatoria de IA (Sec. 13)
│   ├── CATALOGO_PUNTOS_GEOREFERENCIADOS_CAMPUS.md  # Catálogo oficial de coordenadas y GeoJSON
│   ├── mapa_interactivo_control_arenillas.html     # Prototipo: Visor satelital interactivo bilingüe
│   ├── generar_mapa_interactivo.py                 # Script generador en Folium / Python
│   ├── modelo_optimizacion_matematica.py           # Modelo matemático SLSQP y simulación estocástica
│   ├── api_telemetria.py                           # API REST de telemetría en FastAPI
│   ├── exportar_figuras_tecnicas.py                # Script generador de figuras APA (300 DPI)
│   ├── Figura1_Diagnostico_Espacial_Yachay.png     # Figura 1: Diagnóstico espacial (300 DPI)
│   ├── Figura2_Diseno_Tecnico_Intervencion.png     # Figura 2: Diseño técnico (300 DPI)
│   ├── Figura3_Corte_Transversal_Cercas_3Estratos.png # Figura 3: Corte transversal botánico (300 DPI)
│   ├── Figura4_Curva_Reduccion_BioMonitoreo.png    # Figura 4: Curva reducción telemetría (300 DPI)
│   ├── logo_algoritmo_verde.svg                    # Identidad de marca (Modo Claro)
│   ├── logo_algoritmo_verde_dark.svg               # Identidad de marca (Modo Oscuro)
│   ├── qr_algoritmo_verde.png                      # Código QR de alta resolución para móviles
│   ├── Plantilla Documento Tecnico Reto3...docx    # Plantilla Word oficial para entrega
│   └── Declaracion_Uso_IA.docx                     # Formato Word oficial de declaración IA
├── .gitignore
└── README.md
```

---

## 🚀 Prototipo Interactivo y Despliegue en Línea

El visor geoespacial interactivo cuenta con despliegue continuo en **GitHub Pages**:
🌐 **Enlace Web Oficial:** [https://jeffersonconza.github.io/algoritmo-verde-yosw2026/](https://jeffersonconza.github.io/algoritmo-verde-yosw2026/)

Para visualizarlo de forma local sin conexión:
```bash
# Abrir directamente en el navegador
xdg-open reto3_Control_Arenillas/mapa_interactivo_control_arenillas.html
```
Incluye selector de capas satelitales (Google Satellite, Google Streets, Esri Topo y Esri Dark Mode), polígonos de zonas críticas, trazado del canal larvario, buffers de protección fitoquímica (40 m), red de 6 estaciones de bio-monitoreo telemétrico, selector bilingüe Español/Inglés y código QR integrado.

---

## 📅 Hitos de la Competencia

* **Mentorías oficiales:** Lunes 19 a Jueves 22 de octubre (19:00 - 21:00)
* **Entrega Presentación (PDF):** Viernes 23 de octubre, 10:00
* **Pitch Final (10 min):** Viernes 23 de octubre, 14:00 (Hall Senescyt)
* **Premiación:** Sábado 24 de octubre, 10:00 (Auditorio Principal)
