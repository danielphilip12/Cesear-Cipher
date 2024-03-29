import unittest
import Cesear


class TestCesearCipher(unittest.TestCase):

    def test_encrypt(self):
        self.assertEqual(Cesear.encrypt("Hello world", 7), "Olssv dvysk")

        self.assertEqual(Cesear.encrypt("Your Name", 1), "Zpvs Obnf")

        self.assertEqual(Cesear.encrypt("abc", 23), "xyz")

        self.assertEqual(Cesear.encrypt("Hello", 26), "Hello")

    def test_decrypt(self):
        x = Cesear.encrypt("Your Name", 1)
        y = Cesear.encrypt("Hello world", 7)
        z = Cesear.encrypt("abc", 23)
        self.assertEqual(Cesear.decrypt(x, 1), "Your Name")
        self.assertEqual(Cesear.decrypt(y, 7), "Hello world")
        self.assertEqual(Cesear.decrypt(z, 23), "abc")
