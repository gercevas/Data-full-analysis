import pandas as pd

def categorizar_ganado(df):
    """
    Categoriza las especies y clasificaciones zootécnicas, y agrupa el censo por categoría.

    :param df: DataFrame que debe contener las columnas: ['Municipio', 'ESPECIE', 'CLASIF.ZOOTECNICA', 'CENSO']
    :return: DataFrame agrupado por ['Municipio', 'ESPECIE', 'CATEGORIA'] con la suma de CENSO.
    """
    df = df.copy()
    df['CATEGORIA'] = None

    vacuno_carne = [
        'BOVINO CEBADERO', 'BOVINO REPRODUCCIÓN MIXTA', 'BOVINO REPRODUCCION PARA CARNE',
        'CEBADERO DE CICLO ABIERTO', 'CEBADERO DE CICLO CERRADO',
        'EXPLOTACION DE CABESTROS', 'MATADERO'
    ]

    # Vacuno
    df.loc[(df['ESPECIE'] == 'BOVINO') & (df['CLASIF.ZOOTECNICA'].isin(vacuno_carne)), 'CATEGORIA'] = 'Vacuno de Carne'
    df.loc[(df['ESPECIE'] == 'BOVINO') & (df['CLASIF.ZOOTECNICA'] == 'BOVINO REPRODUCCIÓN PARA LECHE'), 'CATEGORIA'] = 'Vacuno de Leche'

    # Resto de especies
    df.loc[df['ESPECIE'] == 'EQUINO', 'CATEGORIA'] = 'Caballos, mulas y asnos'
    df.loc[df['ESPECIE'] == 'OVINO', 'CATEGORIA'] = 'Ovino'
    df.loc[df['ESPECIE'] == 'CAPRINO', 'CATEGORIA'] = 'Caprino'
    df.loc[df['ESPECIE'] == 'GALLINAS', 'CATEGORIA'] = 'Ponedoras y pollos'
    df.loc[df['ESPECIE'] == 'PAVOS', 'CATEGORIA'] = 'Pavos'
    df.loc[df['ESPECIE'] == 'PORCINO', 'CATEGORIA'] = 'Porcino'

    # Agrupación
    resumen = df.groupby(['Municipio', 'ESPECIE', 'CATEGORIA'])['CENSO'].sum().reset_index()

    return resumen
