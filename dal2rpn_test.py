import unittest
from dal2rpn import convert

class convertTest(unittest.TestCase):
    def testNormal(self):
        self.assertEqual(convert('1 * 2 / ( 2 - 3 )'), '1 2 * 2 3 - /')
    
    def testNoSpace(self):
        self.assertEqual(convert('1+3*4-2'), '1 3 4 * + 2 -')
    
    def testParenthesis(self):
        self.assertEqual(convert('( 1 + 3 ) * 4'), '1 3 + 4 *')
    
    def testNoMatchParenthesis(self):
        self.assertRaises(AssertionError, convert, '1 + 3 ) * 4')
        
    def testInvalidParenthesis(self):
        self.assertRaises(AssertionError, convert, ') 1 + 3 ( * 4')
        
    def testMoreParenthesiss(self):
        self.assertEqual(convert('1 + 2 * 3 +(2 *( 4 + 3) ) * 2' ), 
            '1 2 3 * + 2 4 3 + * 2 * +')
            
    def testMoreConvert(self):
        self.assertEqual(convert(' 1 +2/(2-3) '), convert('1+2/(2-3)'))
        
    def testPower(self):
        self.assertEqual(convert(' 1 * 2^3/(2-3) '), '1 2 3 ^ * 2 3 - /')
        
if __name__ == '__main__':
    unittest.main()