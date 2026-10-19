"""
Generador de Figuras Técnicas para el Documento Word (Formato APA 7ma Edición)
Equipo: Algoritmo Verde YT - Reto 3: Control de Arenillas
Calibrado con Hitos Oficiales de Google Maps
"""

import matplotlib.pyplot as plt
import numpy as np

def crear_figura_diagnostico():
    fig, ax = plt.subplots(figsize=(11.5, 7.5), dpi=300)
    
    # Coordenadas relativas en metros desde el centro del campus (Biblioteca Patrimonial)
    # Zona 1: Multifamiliares y Pats (Verde)
    z1_x = [-300, -220, -180, -260, -320, -300]
    z1_y = [-280, -200, -230, -310, -330, -280]
    ax.fill(z1_x, z1_y, color='#2ecc71', alpha=0.35, label='Zona 1: Las Multis y Residencias Patrimoniales')
    ax.plot(z1_x, z1_y, color='#27ae60', lw=2)

    # Zona 2: Ingenio Azucarero (Azul)
    z2_x = [-60, 40, 80, -10, -80, -60]
    z2_y = [-80, -40, 60, 40, -40, -80]
    ax.fill(z2_x, z2_y, color='#3498db', alpha=0.35, label='Zona 2: Ingenio Azucarero y Laboratorios')
    ax.plot(z2_x, z2_y, color='#2980b9', lw=2)

    # Zona 3: Bloques y Senescyt (Rojo/Naranja)
    z3_x = [150, 260, 320, 240, 160, 150]
    z3_y = [140, 200, 160, 80, 100, 140]
    ax.fill(z3_x, z3_y, color='#e74c3c', alpha=0.35, label='Zona 3: Edificio Senescyt y Residencias Los Bloques')
    ax.plot(z3_x, z3_y, color='#c0392b', lw=2)

    # Canal de Riego Principal (Agua corriente - Foco Simuliidae)
    canal_x = np.linspace(-350, 350, 100)
    canal_y = 0.5 * canal_x - 30 + 15 * np.sin(canal_x / 50)
    ax.plot(canal_x, canal_y, color='#0984e3', lw=3, linestyle='--', label='Canal de Riego Principal (Foco Larvario)')

    # Edificaciones sensibles calibradas
    ax.scatter([-240, -280], [-250, -290], color='#27ae60', s=90, marker='s', label='Hitos Z1: Las Multis / Residencias Patrimoniales')
    ax.scatter([0, 20], [0, -30], color='#2980b9', s=90, marker='^', label='Hitos Z2: Biblioteca Patrimonial / Lab. Química')
    ax.scatter([220, 260], [150, 120], color='#c0392b', s=90, marker='o', label='Hitos Z3: Edificio Senescyt / Los Bloques')

    # Título y etiquetas
    ax.set_title("Diagnóstico Espacial de Zonas Críticas y Focos Larvarios (Campus Yachay Tech)\nFigura 1", 
                 fontsize=13, fontweight='bold', pad=15)
    ax.set_xlabel("Distancia relativa Este-Oeste desde Biblioteca (metros)", fontsize=11)
    ax.set_ylabel("Distancia relativa Norte-Sur desde Biblioteca (metros)", fontsize=11)
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), fontsize=9.2, frameon=True)
    
    # Rosa de los vientos (Norte)
    ax.annotate('N', xy=(0.06, 0.92), xytext=(0.06, 0.83),
                arrowprops=dict(facecolor='black', width=2.5, headwidth=8),
                ha='center', va='center', xycoords='axes fraction', fontsize=12, fontweight='bold')

    output_f1 = "reto3_Control_Arenillas/Figura1_Diagnostico_Espacial_Yachay.png"
    plt.savefig(output_f1, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Figura 1 generada en: {output_f1}")

def crear_figura_diseno_tecnico():
    fig, ax = plt.subplots(figsize=(11.5, 7.5), dpi=300)

    # Zonas de fondo
    z1_x = [-300, -220, -180, -260, -320, -300]
    z1_y = [-280, -200, -230, -310, -330, -280]
    ax.fill(z1_x, z1_y, color='#2ecc71', alpha=0.15)
    z2_x = [-60, 40, 80, -10, -80, -60]
    z2_y = [-80, -40, 60, 40, -40, -80]
    ax.fill(z2_x, z2_y, color='#3498db', alpha=0.15)
    z3_x = [150, 260, 320, 240, 160, 150]
    z3_y = [140, 200, 160, 80, 100, 140]
    ax.fill(z3_x, z3_y, color='#e74c3c', alpha=0.15)

    # Canal
    canal_x = np.linspace(-350, 350, 100)
    canal_y = 0.5 * canal_x - 30 + 15 * np.sin(canal_x / 50)
    ax.plot(canal_x, canal_y, color='#0984e3', lw=2, linestyle=':', alpha=0.7, label='Canal Hídrico')

    # Cercas Vivas Multiestrato
    c1_x = [-280, -200, -160]
    c1_y = [-210, -190, -250]
    ax.plot(c1_x, c1_y, color='#16a085', lw=4, solid_capstyle='round', label='Cerca Viva 1 (380m) - Sector Las Multis / Residencias')
    
    c2_x = [-50, 20, 60]
    c2_y = [-50, -10, 30]
    ax.plot(c2_x, c2_y, color='#27ae60', lw=4, solid_capstyle='round', label='Cerca Viva 2 (280m) - Sector Ingenio / Laboratorios')

    c3_x = [160, 220, 290]
    c3_y = [110, 160, 130]
    ax.plot(c3_x, c3_y, color='#2ecc71', lw=4, solid_capstyle='round', label='Cerca Viva 3 (320m) - Sector Edificio Senescyt / Los Bloques')

    # Buffers de amortiguamiento (40m)
    for cx, cy in [(c1_x, c1_y), (c2_x, c2_y), (c3_x, c3_y)]:
        ax.plot(cx, cy, color='#2ecc71', lw=25, alpha=0.22, solid_capstyle='round')

    # Trampas de Monitoreo Biológico
    tx = [-220, -170, 0, 45, 180, 260]
    ty = [-190, -230, -25, 10, 130, 150]
    ax.scatter(tx, ty, color='#2c3e50', s=100, marker='X', zorder=5, label='Estaciones de Trampas Bio-Monitoreo (n=6 GPS)')

    ax.set_title("Diseño Técnico de la Intervención: Distribución de Cercas Vivas y Red de Monitoreo\nFigura 2", 
                 fontsize=13, fontweight='bold', pad=15)
    ax.set_xlabel("Distancia relativa Este-Oeste desde Biblioteca (metros)", fontsize=11)
    ax.set_ylabel("Distancia relativa Norte-Sur desde Biblioteca (metros)", fontsize=11)
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), fontsize=9.2, frameon=True)

    ax.annotate('N', xy=(0.06, 0.92), xytext=(0.06, 0.83),
                arrowprops=dict(facecolor='black', width=2.5, headwidth=8),
                ha='center', va='center', xycoords='axes fraction', fontsize=12, fontweight='bold')

    output_f2 = "reto3_Control_Arenillas/Figura2_Diseno_Tecnico_Intervencion.png"
    plt.savefig(output_f2, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Figura 2 generada en: {output_f2}")

if __name__ == "__main__":
    crear_figura_diagnostico()
    crear_figura_diseno_tecnico()
