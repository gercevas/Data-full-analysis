import os
import sys
import unittest
import pandas as pd

# Añadir el directorio raíz al path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Hojas_excel.lector_excel import LectorExcel

class TestLectorExcel(unittest.TestCase):
    """Pruebas para la clase LectorExcel."""

    def setUp(self):
        """Crear un archivo simulado antes de cada test."""
        self.archivo = 'tests/data/fake_test.xlsx'
        df = pd.DataFrame({'MUNICIPIO': ['Toledo (Norte)', 'Cuenca - Este', 'Guadalajara, Oeste']})
        os.makedirs(os.path.dirname(self.archivo), exist_ok=True)
        with pd.ExcelWriter(self.archivo) as writer:
            df.to_excel(writer, sheet_name='2015', index=False)
            df.to_excel(writer, sheet_name='2016', index=False)

    def test_importar_y_limpiar(self):
        """Debe importar las hojas y limpiar los nombres de municipios."""
        lector = LectorExcel(self.archivo, columna_municipio='MUNICIPIO')
        lector.importar_hojas()
        lector.limpiar_y_renombrar()

        hojas = lector.hojas
        dfs = lector.dataframes

        self.assertIn('2015', hojas)
        df = dfs['2015']
        self.assertIn('Municipio', df.columns)
        for municipio in df['Municipio']:
            self.assertNotRegex(municipio, r'[(),-]')

if __name__ == '__main__':
    unittest.main()
