import unittest
import Cesear


class TestCesearCipher(unittest.TestCase):

    def test_encrypt(self):
        self.assertEqual(Cesear.encrypt("Hello world", 7), "olssv dvysk")

        self.assertEqual(Cesear.encrypt("Daniel", 1), "ebojfm")

        self.assertEqual(Cesear.encrypt("abc", 23), "xyz")

    def test_decrypt(self):
        x = Cesear.encrypt("Daniel", 1)
        y = Cesear.encrypt("Hello world", 7)
        z = Cesear.encrypt("abc", 23)
        self.assertEqual(Cesear.decrypt(x, 1), "daniel")
        self.assertEqual(Cesear.decrypt(y, 7), "hello world")
        self.assertEqual(Cesear.decrypt(z, 23), "abc")
