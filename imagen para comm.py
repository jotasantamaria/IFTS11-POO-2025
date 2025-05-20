import os
os.system ('clear') # esto es un método de una clase! los métodos viven dentro de los objetos

from graphviz import Digraph

dot = Digraph(comment='Modelo de Comunicación de Berlo')
dot.attr(rankdir='LR')  # Orientación horizontal

# Fuente
dot.node('A', 'Lucas (Comedor)\nHabilidades: limitada experiencia\nen comunicación formal', shape='box', style='filled', fillcolor='lightgoldenrod1')

# Mensaje
dot.node('B', '[MENSAJE]\nPedido de leche mezclado con otros datos\n(audio de WhatsApp)', shape='box', style='filled', fillcolor='lightgoldenrodyellow')

# Canal
dot.node('C', 'CANAL\nWhatsApp\n(inadecuado para registros formales)', shape='box', style='filled', fillcolor='lightyellow')

# Receptor
dot.node('D', '[RECEPTOR]\nAndrés (Logística)\nHabilidades: acostumbrado a procesos formales', shape='box', style='filled', fillcolor='lightblue')

# Feedback
dot.node('E', 'FEEDBACK:\n"No recibí ese pedido"\n(conflicto operativo)', shape='note', style='filled', fillcolor='mistyrose')

# Ruidos
dot.node('F', '[RUIDOS]\n- Técnico: Audio no registrable\n- Semántico: Mensaje poco estructurado\n- Psicológico: Estrés por urgencia', shape='note', style='filled', fillcolor='salmon1')

# Conexiones principales
dot.edge('A', 'B')
dot.edge('B', 'C')
dot.edge('C', 'D')
dot.edge('D', 'E', label='↩ Feedback')
dot.edge('F', 'B', style='dashed', label='Interferencia')

# Exportar como imagen
dot.render('modelo_berlo_lucas_andres_horizontal', format='png', cleanup=True)
