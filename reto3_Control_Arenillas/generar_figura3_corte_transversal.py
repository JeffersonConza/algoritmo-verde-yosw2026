"""
Generador de la Figura 3: Corte Transversal Arquitectónico y Agronómico de Cercas Vivas en 3 Estratos
Equipo: Algoritmo Verde YT - Reto 3: Control de Arenillas (YOSW 2026)
Formato: APA 7ma Edición (300 DPI) - Versión de Alta Precisión Gráfica
"""

import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def generar_figura_3():
    fig, ax = plt.subplots(figsize=(14.5, 8.5), dpi=300)
    
    # Límites del corte transversal
    ax.set_xlim(-2.8, 12.8)
    ax.set_ylim(-1.2, 6.5)
    
    # -------------------------------------------------------------
    # 1. SUELO Y ESTRATIGRAFÍA
    # -------------------------------------------------------------
    # Subsuelo mineral
    ax.fill_between([-2.8, 12.8], -1.2, 0, color='#8d6e63', alpha=0.3, label='_nolegend_')
    # Capa de tierra vegetal / suelo fértil
    ax.fill_between([-2.8, 12.8], -0.25, 0, color='#5d4037', alpha=0.6, label='_nolegend_')
    ax.axhline(0, color='#3e2723', lw=1.8)
    
    # Superficie con césped en campus (x > 7.5)
    ax.fill_between([7.5, 12.8], 0, 0.08, color='#4caf50', alpha=0.8)

    # -------------------------------------------------------------
    # 2. CANAL DE RIEGO (FOCO LARVARIO Y CONTROL BIOLÓGICO)
    # -------------------------------------------------------------
    canal_x = [-2.2, -1.8, 0.1, 0.6]
    canal_y = [0.0, -0.9, -0.9, 0.0]
    ax.fill(canal_x, canal_y, color='#0288d1', alpha=0.6, label='_nolegend_')
    ax.plot(canal_x, canal_y, color='#01579b', lw=2.2)
    
    # Sustrato de piedras en el fondo del canal (sitio de fijación larval)
    for px in [-1.5, -1.2, -0.8, -0.4, -0.1]:
        piedra = patches.Ellipse((px, -0.85), width=0.25, height=0.12, color='#78909c')
        ax.add_patch(piedra)

    # Línea de espejo de agua
    ax.plot([-2.0, 0.45], [-0.15, -0.15], color='#4fc3f7', lw=2.5, linestyle='--')
    
    ax.text(-0.85, -0.5, "Canal de Riego\n(Agua Lótica / Corriente)", 
            color='white', fontweight='bold', fontsize=9.5, ha='center', va='center')
    
    # Control Biológico en Canal
    ax.annotate("Control Biológico Larval:\n• Ninfas de Odonatos (Libélulas)\n• Bio-larvicida selectivo (Bti)",
                xy=(-0.5, -0.2), xytext=(-2.5, 1.2),
                arrowprops=dict(facecolor='#0277bd', edgecolor='none', width=1.8, headwidth=7),
                fontsize=8.8, fontweight='bold', color='#01579b',
                bbox=dict(boxstyle="round,pad=0.4", fc="#e1f5fe", ec="#0288d1", lw=1.2))

    # -------------------------------------------------------------
    # 3. ESTRATO BAJO (HERBÁCEO: 0.4 a 0.8 m) - Cymbopogon citratus
    # -------------------------------------------------------------
    for bx in np.linspace(1.2, 2.5, 8):
        for ang in [-35, -20, -5, 10, 25, 40]:
            rad = np.radians(ang)
            h = 0.65 + 0.08 * np.cos(bx * 3)
            ax.plot([bx, bx + 0.25 * np.sin(rad)], [0, h * np.cos(rad)], 
                    color='#2e7d32', lw=2, alpha=0.85)
    
    ax.annotate("ESTRATO BAJO (0.4 - 0.8 m)\n• Cymbopogon citratus (Hierba luisa)\n• Metabolitos: Citronelal y Geraniol\n• Función: Emisión a ras de suelo y canal",
                xy=(1.85, 0.75), xytext=(0.2, 3.8),
                arrowprops=dict(facecolor='#2e7d32', edgecolor='none', width=1.8, headwidth=7),
                fontsize=8.8, fontweight='bold', color='#1b5e20',
                bbox=dict(boxstyle="round,pad=0.4", fc="#e8f8f5", ec="#2ecc71", lw=1.2))

    # -------------------------------------------------------------
    # 4. ESTRATO MEDIO (ARBUSTIVO: 1.2 a 2.0 m) - Myrcianthes hallii / Romero
    # -------------------------------------------------------------
    for ax_pos in [3.5, 4.4]:
        ax.plot([ax_pos, ax_pos], [0, 0.7], color='#4e342e', lw=5)
        copa = patches.Ellipse((ax_pos, 1.4), width=1.35, height=1.35, 
                               color='#388e3c', alpha=0.85, ec='#1b5e20', lw=1.5)
        ax.add_patch(copa)
        copa_sub = patches.Ellipse((ax_pos - 0.1, 1.5), width=0.85, height=0.75, 
                                   color='#43a047', alpha=0.7)
        ax.add_patch(copa_sub)

    ax.annotate("ESTRATO MEDIO (1.2 - 2.0 m · Hipoalergénico)\n• Myrcianthes hallii + Cedrón/Huacatay (<5 m hab.)\n• Rosmarinus officinalis (solo en talud de canal)\n• Metabolitos: Citral, 1,8-Cineol y Limoneno\n• Función: Barrera física libre de alérgenos",
                xy=(3.8, 2.05), xytext=(1.35, 5.15),
                arrowprops=dict(facecolor='#388e3c', edgecolor='none', width=1.8, headwidth=7),
                fontsize=8.3, fontweight='bold', color='#1b5e20',
                bbox=dict(boxstyle="round,pad=0.4", fc="#edf7ed", ec="#4caf50", lw=1.2))

    # -------------------------------------------------------------
    # 5. ESTRATO SUPERIOR (ARBÓREO: 3.5 a 5.0 m) - Schinus molle
    # -------------------------------------------------------------
    tree_x = 6.2
    ax.plot([tree_x, tree_x], [0, 2.3], color='#3e2723', lw=11, solid_capstyle='round')
    ax.plot([tree_x, tree_x - 0.8], [2.1, 3.2], color='#3e2723', lw=6)
    ax.plot([tree_x, tree_x + 0.9], [2.0, 3.1], color='#3e2723', lw=6)
    
    copa_arbol = patches.Ellipse((tree_x, 3.8), width=3.3, height=2.5, 
                                 color='#1b5e20', alpha=0.8, ec='#0d3b10', lw=2)
    ax.add_patch(copa_arbol)
    copa_arbol2 = patches.Ellipse((tree_x - 0.5, 3.6), width=2.1, height=1.8, 
                                  color='#2e7d32', alpha=0.7)
    ax.add_patch(copa_arbol2)
    copa_arbol3 = patches.Ellipse((tree_x + 0.5, 3.7), width=2.0, height=1.7, 
                                  color='#388e3c', alpha=0.7)
    ax.add_patch(copa_arbol3)

    ax.annotate("ESTRATO SUPERIOR (3.5 - 5.0 m)\n• Schinus molle (Pimiento nativo andino)\n• Metabolitos: α-pineno, β-pineno y limoneno\n• Función: Ruptura de vientos dominantes\ny dispersión aérea de fitoquímicos",
                xy=(6.2, 4.95), xytext=(6.6, 5.4),
                arrowprops=dict(facecolor='#1b5e20', edgecolor='none', width=1.8, headwidth=7),
                fontsize=8.8, fontweight='bold', color='#0d3b10',
                bbox=dict(boxstyle="round,pad=0.4", fc="#e8f5e9", ec="#2e7d32", lw=1.2))

    # -------------------------------------------------------------
    # 6. PLUMA DE DISPERSIÓN DE FITOCOMPUESTOS Y VIENTO
    # -------------------------------------------------------------
    pluma_x = [1.2, 3.2, 5.5, 12.6, 12.6, 6.0, 1.2]
    pluma_y = [0.2, 0.4, 0.5, 0.8, 3.6, 4.8, 0.8]
    ax.fill(pluma_x, pluma_y, color='#00e676', alpha=0.15, label='_nolegend_')
    
    # Flechas de viento dominante
    for vy in [0.9, 2.3]:
        ax.annotate("", xy=(-0.1, vy), xytext=(-2.4, vy),
                    arrowprops=dict(arrowstyle="->", color='#0288d1', lw=2.4, ls='-'))
    
    ax.text(-2.4, 2.6, "Viento Dominante\ndel Valle", 
            color='#01579b', fontsize=8.5, fontweight='bold', ha='left')

    # Cartel de la Pluma Química Repelente
    ax.text(10.2, 3.8, "Cortina Química Repelente\n(Pluma de Monoterpenos)\n[Atenuación continua de insectos]",
            fontsize=8.8, fontweight='bold', color='#00695c', ha='center',
            bbox=dict(boxstyle="round,pad=0.35", fc="#e0f2f1", ec="#009688", lw=1.2))

    # -------------------------------------------------------------
    # 7. ZONA PROTEGIDA: CAMPUS UNIVERSITARIO
    # -------------------------------------------------------------
    # Caminería peatonal / adoquín
    ax.fill_between([8.0, 12.8], 0, 0.08, color='#b0bec5')
    ax.plot([8.0, 12.8], [0.08, 0.08], color='#78909c', lw=1.5)
    
    # Banco de campus y farola / luminaria
    banco = patches.Rectangle((9.4, 0.08), width=1.5, height=0.38, color='#5d4037')
    ax.add_patch(banco)
    respaldo = patches.Rectangle((9.4, 0.46), width=0.15, height=0.35, color='#3e2723')
    ax.add_patch(respaldo)
    
    # Farola de campus
    ax.plot([11.8, 11.8], [0.08, 2.2], color='#37474f', lw=3)
    farola = patches.Circle((11.8, 2.25), radius=0.18, color='#ffd54f', ec='#ffb300', lw=1.5)
    ax.add_patch(farola)
    
    ax.text(10.15, 1.55, "Zona Protegida\n(Campus Yachay Tech)\n• Mitigación global: 82.8% (SLSQP)\n• Confort térmico e hipoalergénico",
            fontsize=9.0, fontweight='bold', color='#1a237e', ha='center',
            bbox=dict(boxstyle="round,pad=0.4", fc="#e8eaf6", ec="#3f51b5", lw=1.2))

    # Arenillas repelidas (Simuliidae)
    for insect_pos in [(0.75, 1.65), (0.95, 2.1), (0.65, 1.25)]:
        ax.plot(insect_pos[0], insect_pos[1], marker='x', markersize=9, color='#d32f2f', mew=2.2)
        ax.annotate("", xy=(insect_pos[0] - 0.35, insect_pos[1] + 0.22), xytext=insect_pos,
                    arrowprops=dict(arrowstyle="->", color='#d32f2f', lw=1.8, ls='--'))
    
    ax.text(0.7, 2.5, "Bloqueo Físico y Repelencia\nde Arenillas (Simuliidae)", 
            color='#b71c1c', fontsize=8.5, fontweight='bold', ha='center')

    # -------------------------------------------------------------
    # 8. EJES Y COTAS ESTÁNDAR APA (SIN SOLAPAMIENTO)
    # -------------------------------------------------------------
    # Ticks limpios y oficiales en el eje Y
    ax.set_yticks([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
    ax.set_yticklabels(['-1.0 m', '0.0 m (Suelo)', '1.0 m', '2.0 m', '3.0 m', '4.0 m', '5.0 m', '6.0 m'], 
                       fontsize=9.5)

    ax.set_title("Corte Transversal Arquitectónico y Agronómico: Estructuración de Cercas Vivas en 3 Estratos y Manejo Integrado\nFigura 3", 
                 fontsize=13, fontweight='bold', pad=15)
    ax.set_xlabel("Distancia transversal desde el canal de riego hacia el campus (metros)", fontsize=11)
    ax.set_ylabel("Altura sobre el nivel del suelo (metros)", fontsize=11)
    ax.grid(True, linestyle=':', alpha=0.4)
    ax.set_axisbelow(True)

    plt.tight_layout()
    output_path = os.path.join(BASE_DIR, "Figura3_Corte_Transversal_Cercas_3Estratos.png")
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Figura 3 generada exitosamente en: {output_path}")

if __name__ == "__main__":
    generar_figura_3()
