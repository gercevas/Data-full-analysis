import pandas as pd

# Factores constantes
FACTOR_EMISION = {
    'Vacuno de Carne': 62.0,
    'Vacuno de Leche': 124.8,
    'Ovino': 7.6,
    'Porcino': 0.9,
    'Caprino': 9.2,
    'Caballos, mulas y asnos': 11.7,
    'Ponedoras y pollos': 0.0,
    'Pavos': 0.0
}

VS = {
    'Vacuno de Leche': 5.18,
    'Vacuno de Carne': 2.93,
    'Ovino': 0.38,
    'Porcino': 0.34,
    'Caprino': 0.37,
    'Caballos, mulas y asnos': 2.63,
    'Ponedoras y pollos': 0.02,
    'Pavos': 0.07
}

BO = {
    'Vacuno de Leche': 0.24,
    'Vacuno de Carne': 0.18,
    'Ovino': 0.19,
    'Porcino': 0.45,
    'Caprino': 0.18,
    'Caballos, mulas y asnos': 0.35,
    'Ponedoras y pollos': 0.37,
    'Pavos': 0.36
}

EXCRECION_N = {
    'Vacuno de Leche': 113.32,
    'Vacuno de Carne': 52.17,
    'Ovino': 5.34,
    'Porcino': 10.65,
    'Caprino': 9.30,
    'Caballos, mulas y asnos': 42.47,
    'Ponedoras y pollos': 0.63,
    'Pavos': 1.63
}

def calcular_emisiones(df):
    """
    Calcula las emisiones por fermentación entérica y gestión de estiércol.

    :param df: DataFrame con columnas 'CENSO' y 'CATEGORIA'.
    :return: DataFrame con nuevas columnas de emisiones.
    """
    df = df.copy()

    df['Fermentacion_enterica'] = df['CENSO'] * df['CATEGORIA'].map(FACTOR_EMISION) * 1e-3

    df['Gestion_estiercol'] = (
        df['CENSO'] * df['CATEGORIA'].map(VS) * 365 *
        df['CATEGORIA'].map(BO) * 0.67 * 1e-3
    )

    df['NO2_Solido'] = (
        df['CENSO'] * df['CATEGORIA'].map(EXCRECION_N) * 0.005116 * (44 / 28) * 1e-3
    )

    df['NO2_Liquido'] = (
        df['CENSO'] * df['CATEGORIA'].map(EXCRECION_N) * 0.001559 * (44 / 28) * 1e-3
    )

    df['NO2_Diaria'] = (
        df['CENSO'] * df['CATEGORIA'].map(EXCRECION_N) * 0.000075 * (44 / 28) * 1e-3
    )

    return df
