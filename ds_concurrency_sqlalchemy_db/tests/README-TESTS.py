# ─────────────────────────────────────────────────────────────────────────────
# Ejecutar pruebas (unittest)
#
# Descubrimiento estándar (verbose legible):
#   python -m unittest discover -s tests -p "test_*.py" -v
#
# Silenciar warnings y hacer buffer del output (más limpio en CI):
#   python -W ignore -m unittest discover -s tests -p "test_*.py" -b -q
#
# Flags clave:
#   -W ignore  -> oculta warnings de Python
#   -b         -> buffer de stdout/stderr (solo muestra si falla)
#   -v / -q    -> verbose / quiet (usa uno u otro)

# ─────────────────────────────────────────────────────────────────────────────
# Cobertura (coverage)
#
# Ejecutar suite + cobertura:
#   coverage run -m unittest discover -s tests -p "test_*.py"
#
# Reporte con líneas faltantes:
#   coverage report -m
#
# HTML (para inspección visual):
#   coverage html
#   # abre htmlcov/index.html

# ─────────────────────────────────────────────────────────────────────────────
# Convención de nombres de tests
#
# test_<metodo>_<escenario>_<resultado>()
# Ejemplo:
#   test_deposit_positive_amount_increases_balance
#
# Archivos:
#   test_<area>.py  (p.ej., test_strategies.py, test_fs.py)
#   # Mantén nombres cortos y legibles (evita romanizaciones eternas).

# ─────────────────────────────────────────────────────────────────────────────
# Orden/agrupación personalizada (opcional) con TestSuite
#
# import unittest
# from tests.test_strategies import TestStrategies
#
# def suite():
#     s = unittest.TestSuite()
#     s.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestStrategies))
#     return s
#
# if __name__ == "__main__":
#     unittest.TextTestRunner(verbosity=2).run(suite())

# ─────────────────────────────────────────────────────────────────────────────
# setUp/tearDown mínimos (ejemplo de patrón para FS temporal)
#
# import tempfile
# import unittest
#
# class TestStrategies(unittest.TestCase):
#     def setUp(self):
#         self._tmp = tempfile.TemporaryDirectory()
#         self.rootpath = self._tmp.name
#         # prepara doubles/mocks aquí si aplica (p.ej., MemoryFS)
#
#     def tearDown(self):
#         self._tmp.cleanup()
#
#     def test_example(self):
#         # Arrange-Act-Assert claro y corto
#         self.assertTrue(True)

# ─────────────────────────────────────────────────────────────────────────────
# Reglas de oro (corto y útil)
# 1) Tests rápidos, aislados y legibles (AAA).
# 2) Un assert principal por test (o pocos, coherentes).
# 3) Mocks/doubles para I/O y paths; no dependas del entorno real.
# 4) Falla explícita > silencios mágicos (tipos, permisos, no-existencia).
# 5) Mantén contratos (Protocols/ABCs) + estrategias separadas y probadas.
# 6) Sube cobertura donde duele (utils/rutas de error) sin perseguir 100% ciego.
