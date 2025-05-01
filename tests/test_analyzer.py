import unittest
from helena_core.analyzer import CognitiveCore

# tests/test_analyzer.py


class TestCognitiveCore(unittest.TestCase):
    def setUp(self):
        self.core = CognitiveCore()

    def test_suggest_no_errors(self):
        # Test when there are no errors in memory
        self.core.memory = []
        suggestions = self.core._suggest()
        self.assertEqual(suggestions, [])

    def test_suggest_corridor_width_error(self):
        # Test when there is a corridor width error in memory
        self.core.memory = ["Corredor fora da norma: largura < 1.20m."]
        suggestions = self.core._suggest()
        self.assertIn("Recomenda-se largura mínima de 1.20m para corredores.", suggestions)

    def test_suggest_door_height_error(self):
        # Test when there is a door height error in memory
        self.core.memory = ["Altura da porta abaixo do mínimo: < 2.10m."]
        suggestions = self.core._suggest()
        self.assertIn("Portas devem ter altura mínima de 2.10m.", suggestions)

    def test_suggest_emergency_exit_error(self):
        # Test when there is an emergency exit error in memory
        self.core.memory = ["Ausência de saída de emergência."]
        suggestions = self.core._suggest()
        self.assertIn("Adicionar saída de emergência conforme norma NR-23.", suggestions)

    def test_suggest_multiple_errors(self):
        # Test when there are multiple errors in memory
        self.core.memory = [
            "Corredor fora da norma: largura < 1.20m.",
            "Altura da porta abaixo do mínimo: < 2.10m.",
            "Ausência de saída de emergência."
        ]
        suggestions = self.core._suggest()
        self.assertIn("Recomenda-se largura mínima de 1.20m para corredores.", suggestions)
        self.assertIn("Portas devem ter altura mínima de 2.10m.", suggestions)
        self.assertIn("Adicionar saída de emergência conforme norma NR-23.", suggestions)

    def test_suggest_duplicate_errors(self):
        # Test when there are duplicate errors in memory
        self.core.memory = [
            "Corredor fora da norma: largura < 1.20m.",
            "Corredor fora da norma: largura < 1.20m."
        ]
        suggestions = self.core._suggest()
        self.assertEqual(len(suggestions), 1)
        self.assertIn("Recomenda-se largura mínima de 1.20m para corredores.", suggestions)

if __name__ == "__main__":
    unittest.main()