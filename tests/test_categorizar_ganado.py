import os
import sys
import unittest
import pandas as pd


# Añadir el directorio raíz al path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Hojas_excel.categorizar_ganado import categorizar_ganado
class TestCategorizacionGanado(unittest.TestCase):
    """Pruebas para la función categorizar_ganado."""

    def test_categorizacion_correcta(self):
        """Debe asignar correctamente la categoría según especie y clasificación."""
        df = pd.DataFrame({
            'Municipio': ['Toledo', 'Cuenca'],
            'ESPECIE': ['BOVINO', 'PORCINO'],
            'CLASIF.ZOOTECNICA': ['BOVINO REPRODUCCION PARA CARNE', 'CERDOS DE CEBO'],
            'CENSO': [100, 200]
        })

        resultado = categorizar_ganado(df)
        categorias = resultado['CATEGORIA'].tolist()
        self.assertIn('Vacuno de Carne', categorias)
        self.assertIn('Porcino', categorias)

if __name__ == '__main__':
    unittest.main()
