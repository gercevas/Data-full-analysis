import pandas as pd

class LectorExcel:
    def __init__(self, ruta_archivo, columna_municipio='MUNICIPIO'):
        """
        Inicializa el lector con la ruta del archivo Excel y el nombre original de la columna de municipio.
        
        :Argumento ruta_archivo: Ruta del archivo Excel.
        :Argumento columna_municipio: Nombre de la columna que contiene los municipios a limpiar.
        """
        self.ruta_archivo = ruta_archivo
        self.columna_municipio = columna_municipio
        self.caracteres_reemplazar = [",", "(", ")", "-"]
        self.hojas = []
        self.dataframes = {}

    def importar_hojas(self):
        """
        Lee todas las hojas del archivo Excel y las guarda en un diccionario sin procesar.
        """
        self.hojas = pd.ExcelFile(self.ruta_archivo).sheet_names
        for hoja in self.hojas:
            self.dataframes[hoja] = pd.read_excel(self.ruta_archivo, sheet_name=hoja)

    def limpiar_y_renombrar(self):
        """
        Limpia los nombres de los municipios en cada hoja y renombra la columna a 'Municipio'.
        """
        for hoja, df in self.dataframes.items():
            if self.columna_municipio in df.columns:
                df = df.copy()  # Evita advertencias por SettingWithCopy
                df.rename(columns={self.columna_municipio: 'Municipio'}, inplace=True)
                for caracter in self.caracteres_reemplazar:
                    df['Municipio'] = df['Municipio'].astype(str).str.replace(caracter, "", regex=False)
                self.dataframes[hoja] = df  # Guardar el df limpio

    def obtener_dataframes(self):
        """
        Devuelve el diccionario con los DataFrames procesados.
        """
        return self.dataframes
