# Proyecto de Análisis Ganadero y Emisiones a Nivel Municipal

Este proyecto implementa una librería modular y reutilizable en Python para el análisis de censos ganaderos, categorización zootécnica y cálculo automatizado de emisiones a nivel municipal. La estructura del proyecto permite importar múltiples hojas de Excel, procesar la información y generar indicadores medioambientales clave del sector ganadero.

---

## Repositorio

Repositorio público disponible en:  
[https://github.com/gercevas/Data-full-analysis.git]

---

## Instalación

```bash
git clone https://github.com/gercevas/Data-full-analysis.git
cd Data-full-analysis
```

# Crear y activar entorno virtual
```bash
python3 -m venv venv
source venv/bin/activate  # o venv\Scripts\activate en Windows
```
```bash
# Instalar dependencias
pip install -r requirements.txt
```
```bash
# Instalar la librería en modo editable
pip install -e .
```

# Estructura del proyecto

Data-full-analysis/
├── scripts/
│   └── main.py
├── src/
│   └── Hojas_excel/
│       ├── __init__.py
│       ├── lector_excel.py
│       ├── categorizar_ganado.py
│       └── calculo_emisiones.py
├── tests/
│   ├── test_lector_excel.py
│   ├── test_categorizar_ganado.py
│   └── test_calculo_emisiones.py
├── Análisis_completo.md        ← Análisis completo del estudio
├── pytest.ini
├── setup.py
├── requirements.txt
└── README.md

# Funcionalidades principales

1. Lectura automatizada de hojas de Excel

La clase LectorExcel permite importar de forma masiva todas las hojas de un archivo Excel. Cada hoja es almacenada como un DataFrame independiente, facilitando el control de calidad sobre los datos (detección de nulos, ceros, formatos inconsistentes).

```bash
from Hojas_excel.lector_excel import LectorExcel

lector = LectorExcel("data/Cabezas_ganado.xlsx", columna_municipio="MUNICIPIO")
lector.importar_hojas()
lector.limpiar_y_renombrar()
dataframes = lector.obtener_dataframes()
```

2. Categorización ganadera

La función categorizar_ganado() agrupa las explotaciones ganaderas por especie y clasificación zootécnica, permitiendo identificar categorías clave como Vacuno de Carne, Porcino, Ovino, Caprino, etc.

```bash
from Hojas_excel.categorizar_ganado import categorizar_ganado

df_categorizado = categorizar_ganado(df)
```

3. Cálculo de emisiones
A partir de la categorización, calcular_emisiones() estima emisiones de:

CH₄ por fermentación entérica
CH₄ por gestión de estiércol
N₂O en sus distintas fases (sólido, líquido, diaria)
La función permite usar datos reales municipales si se reemplazan los censos por los correspondientes al territorio.

```bash 
from Hojas_excel.calculo_emisiones import calcular_emisiones

df_emisiones = calcular_emisiones(df_categorizado)
```
4. Ejecución completa (main.py)

El script scripts/main.py demuestra todo el flujo de análisis: lectura, categorización, cálculo de emisiones y exportación a CSV.

```bash
python scripts/main.py
```

Esto genera 

```bash
output/resultado_emisiones.csv
```

# Análisis completo del estudio 

El archivo Análisis_completo.md contiene un desarrollo detallado del estudio y es el corazón del proyecto. En él se incluyen:

- Procesos ETL paso a paso
- Creación y justificación de indicadores
- Matrices de correlación y causalidad
- Visualizaciones y exploración estadística
- Interpretación de resultados
- Reflexiones para la toma de decisiones públicas

Aunque los datos reales no se suben por confidencialidad, el archivo .md muestra toda la lógica del análisis con ejemplos simulados reproducibles.Este archivo permite conocer el alcance técnico, analítico y metodológico de la investigación.

# Ejecución de pruebas

Tests unitarios incluidos para verificar cada componente:

```bash
python tests/test_lector_excel.py
python tests/test_categorizar_ganado.py
python tests/test_calculo_emisiones.py
```

o se puede ejecutar todos con:

```bash
pytest
```

#Requisitos

Python 3.6 o superior
pandas
pytest

# Autor

Germán Cevallos
https://github.com/gercevas

# Licencia

Este proyecto está licenciado bajo los términos de la licencia MIT.

