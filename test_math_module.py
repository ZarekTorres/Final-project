from math_module import *
from math import pi
import unittest


class MathTest(unittest.TestCase):
    
    def test_area_of_circle(self):
        self.assertEqual(area_of_circle(1), pi)
        self.assertAlmostEqual(area_of_circle(.1), 0.031415926535897934)

        with self.assertRaises(TypeError):
            area_of_circle('z')
        with self.assertRaises(ValueError):
            area_of_circle(-1)
            area_of_square(0)
    
    def test_area_of_rectangle(self):
        self.assertEqual(area_of_rectangle(1, 10), 10)
        self.assertAlmostEqual(area_of_rectangle(1, 1.5), 1.5)
        self.assertAlmostEqual(area_of_rectangle(1.5, 1), 1.5)
        self.assertAlmostEqual(area_of_rectangle(1.5, 1.5), 2.25)

        with self.assertRaises(TypeError):
            area_of_rectangle('z', 1)
            area_of_rectangle('z', '1')
            area_of_rectangle(1, 'z')
            
        with self.assertRaises(ValueError):
            area_of_rectangle(-1, -1)
            area_of_rectangle(-1, 1)
            area_of_rectangle(1, -1)
            
            area_of_rectangle(0, 0)
            area_of_rectangle(0, -1)
            area_of_rectangle(-1, 0)
    
    
    def test_area_of_square(self):
        self.assertEqual(area_of_square(1), 1)
        self.assertAlmostEqual(area_of_square(.1), .01)

        with self.assertRaises(TypeError):
            area_of_square('z')
        with self.assertRaises(ValueError):
            area_of_square(-1)
            area_of_square(0)

    
    def test_area_of_triangle(self):
        self.assertEqual(area_of_triangle(1, 10), 5)
        self.assertAlmostEqual(area_of_triangle(1, 1.5), .75)
        self.assertAlmostEqual(area_of_triangle(1.5, 1), .75)
        self.assertAlmostEqual(area_of_triangle(1.5, 1.5), 1.125)

        with self.assertRaises(TypeError):
            area_of_triangle('z', 1)
            area_of_triangle('z', '1')
            area_of_triangle(1, 'z')
            
        with self.assertRaises(ValueError):
            area_of_triangle(-1, -1)
            area_of_triangle(-1, 1)
            area_of_triangle(1, -1)
            
            area_of_triangle(0, 0)
            area_of_triangle(0, -1)
            area_of_triangle(-1, 0)
    

if __name__ == '__main__':
    unittest.main()
