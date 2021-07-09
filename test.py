import unittest
from logic import Logic
# This testfile is for the logic without the UI found in testfile branch of the repository

class Test(unittest.TestCase):
    def test_normal(self):
        g = Logic()
        g.textbox = "1+1"
        self.assertEqual(g.Calculate(), 2 )
    def test_(self):
        g = Logic()
        g.textbox = "1/1"
        self.assertEqual(g.Calculate(), 1 )
    def test_1(self):
        g = Logic()
        g.textbox = "2/1"
        self.assertEqual(g.Calculate(), 2)
    def test_5(self):
        g = Logic()
        g.textbox = "2+ 2+2"
        self.assertEqual(g.Calculate(), 6)
    def test_5312(self):
        g = Logic()
        g.textbox = "2 -5 "
        self.assertEqual(g.Calculate(), -3)
    def test_53(self):
        g = Logic()
        g.textbox = "1+1+1"
        self.assertEqual(g.Calculate(), 3)
    def test_551(self):
        g = Logic()
        g.textbox = "5"
        self.assertEqual(g.Calculate(), 5)
    def test_55315(self):
        g = Logic()
        g.textbox = "5*5"
        self.assertEqual(g.Calculate(), 25)
    def test_553(self):
        g = Logic()
        g.textbox = "6-3"
        self.assertEqual(g.Calculate(), 3)
    def test_5213(self):
        g = Logic()
        g.textbox = "5-5-5"
        self.assertEqual(g.Calculate(), -5)
    def test_673(self):
        g = Logic()
        g.textbox = "9"
        self.assertEqual(g.special1(), 3.0)

    def test_674(self):
        g = Logic()
        g.textbox = "9"
        self.assertEqual(g.special2(), 81.0)


if __name__ == "__main__":
    unittest.main()