import unittest
from is_likelion import is_likelion

class TestIsLikelion(unittest.TestCase):
    def test_is_likelion(self):
        self.assertTrue(is_likelion('likelion'))
        self.assertTrue(is_likelion('likeLion'))
        self.assertTrue(is_likelion('  LikeliOn  '))
    
    def test_is_korean_likelion(self):
        self.assertTrue(is_likelion('멋쟁이사자처럼'))
        self.assertTrue(is_likelion('    멋쟁이사자처럼    '))
        self.assertTrue(is_likelion('멋쟁이사자처럼    '))
        self.assertTrue(is_likelion('    멋쟁이사자처럼'))
        self.assertFalse(is_likelion('멋쟁이호랑이처럼'))
        self.assertFalse(is_likelion('멋쟁이토끼처럼'))
