import unittest

from RomanNumerals import RomanError, romanToArab, arabToRoman, validateArab, validateRoman

class TestArabToRoman(unittest.TestCase):
    def test_arabToRoman_minusless(self):
        self.assertEqual(arabToRoman(36),"XXXVI")
    def test_arabToRoman_minus(self):
        self.assertEqual(arabToRoman(464), "CDLXIV")

def test_arabigo_a_romano_solo_admite_enteros(self):
        with self.assertRaises(TypeError):
            arabToRoman(str)

def test_arabigo_a_romano_solo_enteros_positivos(self):
        with self.assertRaises(ValueError):
            arabToRoman(0)


class RomanosFuncionesAromanoTest(unittest.TestCase):
    def test_romano_a_arabigo_tres_repeticiones_OK(self):
        self.assertEqual(romanToArab('III'), 3)

    def test_romano_a_arabigo_cuatro_repeticiones_ERROR(self):
        with self.assertRaises(RomanError):
            romanToArab('IIII')

    def test_romano_a_arabigo_dos_repeticiones_de_VLD_error(self):
        with self.assertRaises(RomanError):
            romanToArab('VV')
        with self.assertRaises(RomanError):
            romanToArab('LL')
        with self.assertRaises(RomanError):
            romanToArab('DD')

    def test_romano_a_arabigo_VLD_no_resta(self):
        with self.assertRaises(RomanError):
            romanToArab('VX')
        with self.assertRaises(RomanError):
            romanToArab('LC')
        with self.assertRaises(RomanError):
            romanToArab('DM')

    def test_romano_a_arabigo_tras_repeticion_no_se_resta(self):
        with self.assertRaises(RomanError):
            romanToArab('XXL')

        self.assertEqual(romanToArab('XXIII'), 23)

    def test_romano_a_arabigo_restas_prohibidas_si_separacion_alta(self):
        with self.assertRaises(RomanError):
            romanToArab('XM')

    def test_romano_a_arabigo_simbolos_incorrectos(self):
        with self.assertRaises(RomanError):
            romanToArab('IK')
        with self.assertRaises(RomanError):
            romanToArab('KI')
        with self.assertRaises(RomanError):
            romanToArab('K')    