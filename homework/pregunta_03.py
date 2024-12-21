"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd
def pregunta_03():
    df = pd.read_csv('tbl0.tsv', sep='\t')
    contar=df['c1'].value_counts().sort_index()
    return contar
print(pregunta_03())
 
"""
¿Cuál es la cantidad de registros por cada letra de la columna `c1` del
archivo `tbl0.tsv`?

Rta/
c1
A     8
B     7
C     5
D     6
E    14
Name: count, dtype: int64

"""
