import pandas as pd
from categorizar_ganado import categorizar_ganado

def test_categorizar_ganado():
    # Crear un DataFrame simulado
    df_simulado = pd.DataFrame({
        'Municipio': ['Toledo', 'Toledo', 'Cuenca', 'Guadalajara', 'Toledo', 'Cuenca', 'Cuenca'],
        'ESPECIE': ['BOVINO', 'BOVINO', 'EQUINO', 'GALLINAS', 'PORCINO', 'OVINO', 'CAPRINO'],
        'CLASIF.ZOOTECNICA': [
            'BOVINO REPRODUCCION PARA CARNE',
            'BOVINO REPRODUCCIÓN PARA LECHE',
            'EQUINO DE TRABAJO',
            'PONEDORAS', 
            'CERDOS DE CEBO',
            'OVINO LECHERO',
            'CAPRINO LECHERO'
        ],
        'CENSO': [100, 50, 10, 300, 200, 70, 30]
    })

    resumen = categorizar_ganado(df_simulado)

    # Comprobaciones básicas
    assert isinstance(resumen, pd.DataFrame)
    assert 'CATEGORIA' in resumen.columns
    assert 'CENSO' in resumen.columns
    assert resumen['CENSO'].sum() == df_simulado['CENSO'].sum()

    # Comprobación de asignación de categorías
    categorias_esperadas = set([
        'Vacuno de Carne', 'Vacuno de Leche', 'Caballos, mulas y asnos',
        'Ponedoras y pollos', 'Porcino', 'Ovino', 'Caprino'
    ])
    assert set(resumen['CATEGORIA']).issubset(categorias_esperadas)
