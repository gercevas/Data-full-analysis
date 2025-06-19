import os
import pandas as pd
from src.Hojas_excel.lector_excel import LectorExcel
from src.Hojas_excel.categorizar_ganado import categorizar_ganado
from src.Hojas_excel.calculo_emisiones import calcular_emisiones

def crear_dataframe_simulado():
    """
    Crea un DataFrame con datos simulados para demostrar el análisis completo.
    """
    return pd.DataFrame({
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

def main():
    print("Análisis de datos ganaderos")

    archivo_excel = 'data/Cabezas_ganado.xlsx'

    if os.path.exists(archivo_excel):
        print(f"Leyendo archivo real: {archivo_excel}")
        lector = LectorExcel(archivo_excel, columna_municipio='MUNICIPIO')
        lector.importar_hojas()
        lector.limpiar_y_renombrar()
        dataframes = lector.obtener_dataframes()

        # Combinar TODAS las hojas en un único DataFrame
        df_completo = pd.concat(dataframes.values(), ignore_index=True)
    else:
        print("Archivo Excel no encontrado. Usando datos simulados.")
        df_completo = crear_dataframe_simulado()

    print("Datos de entrada:")
    print(df_completo.head())

    # Paso 2: Categorizar
    df_categorizado = categorizar_ganado(df_completo)
    print("Datos categorizados:")
    print(df_categorizado.head())

    # Paso 3: Calcular emisiones
    df_final = calcular_emisiones(df_categorizado)
    print("Emisiones estimadas:")
    print(df_final[['Municipio', 'CATEGORIA', 'CENSO', 'Fermentacion_enterica', 'Gestion_estiercol', 'NO2_Solido']].head())

    # Guardar resultado
    output_path = 'output/resultado_emisiones.csv'
    os.makedirs('output', exist_ok=True)
    df_final.to_csv(output_path, index=False)
    print(f"Resultado guardado en: {output_path}")

    print("Análisis completado.")

if __name__ == "__main__":
    main()
