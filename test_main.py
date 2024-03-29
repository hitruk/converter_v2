
import unittest
from main import Model


class TestModel(unittest.TestCase):

    def test_mi_to_km(self):
        model = Model(10)
        mi_to_km = model.mi_to_km()
        self.assertEqual(mi_to_km, 16.09344)

    def test_km_to_mi(self):
        model = Model(10)
        km_to_mi = model.km_to_mi()
        self.assertEqual(km_to_mi, 6.2137119223733395)

    def test_value_with_wrong_type(self):
        model = Model(10)
        with self.assertRaises(TypeError):
            model.value = 'abc'
            model.value = False
