import os
import pytest
import pandas as pd
from lector_excel import LectorExcel

def crear_excel_simulado(ruta):
    """Crea un archivo Excel simulado con nombres de municipios."""
    df = pd.DataFrame({
        'MUNICIPIO': ['Toledo (Norte)', 'Cuenca - Este', 'Guadalajara, Oeste']
    })

    os.makedirs(os.path.dirname(ruta), exist_ok=True)

    with pd.ExcelWriter(ruta) as writer:
        df.to_excel(writer, sheet_name='2015', index=False)
        df.to_excel(writer, sheet_name='2016', index=False)  # Dos hojas para mostrar que funciona bien la función

def test_importar_y_limpiar_excel():
    archivo_simulado = 'tests/data/fake_test.xlsx'

    # Crear archivo si no existe
    if not os.path.exists(archivo_simulado):
        crear_excel_simulado(archivo_simulado)

    # Usar la clase
    lector = LectorExcel(archivo_simulado, columna_municipio='MUNICIPIO')
    lector.importar_hojas()
    lector.limpiar_y_renombrar()
    dataframes = lector.obtener_dataframes()

    # Verificaciones
    assert isinstance(dataframes, dict)
    assert len(dataframes) >= 2

    for hoja, df in dataframes.items():
        assert 'Municipio' in df.columns
        muestra = df['Municipio'].dropna().astype(str)
        for val in muestra:
            assert all(car not in val for car in [",", "(", ")", "-"])

