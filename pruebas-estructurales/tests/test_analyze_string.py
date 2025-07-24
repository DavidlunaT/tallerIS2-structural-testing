import unittest
import sys
import os

# Añadir el directorio src al path para poder importar los módulos
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.analyze_string import analyzeString

class TestAnalyzeString(unittest.TestCase):
    """
    Pruebas para la función analyzeString.
    Task A.2: Statement Coverage - Diseñar una suite de pruebas que logre una 
    cobertura del 100% con el mínimo número de casos de prueba posible.
    """
    
    def test_more_uppercase(self):
        """
        Test para el caso donde hay más caracteres en mayúscula.
        Este test cubre:
        - Conteo de mayúsculas, minúsculas, dígitos y caracteres especiales
        - La condición countUpper > countLower es verdadera
        """
        result = analyzeString("ABCdef123!@#")
        self.assertEqual(result, (3, 3, 3, 3, "Balanced"))  # Aquí el resultado es "Balanced"
        
        result = analyzeString("ABCDef12!")
        self.assertEqual(result, (4, 2, 2, 1, "More Uppercase"))
    
    def test_more_lowercase(self):
        """
        Test para el caso donde hay más caracteres en minúscula.
        Este test cubre:
        - La condición countLower > countUpper es verdadera
        """
        result = analyzeString("ABcdef123!@#")
        self.assertEqual(result, (2, 4, 3, 3, "More Lowercase"))
    
    def test_balanced(self):
        """
        Test para el caso donde hay igual número de caracteres en mayúscula y minúscula.
        Este test cubre:
        - La condición else cuando countUpper == countLower
        """
        result = analyzeString("ABcd12!@")
        self.assertEqual(result, (2, 2, 2, 2, "Balanced"))

if __name__ == '__main__':
    unittest.main()