import unittest
from fall16_q10 import *

class TestEnzyme(unittest.TestCase):
    def test_01(self):
        enzyme1 = Enzyme('Sau3A', 'GATC')
        x = 'The enzyme Sau3A has a recognition sequence of length 4'
        self.assertEqual(str(enzyme1), x)

    def test_02(self):
        strand1 = DNAStrand('AGGCCT')
        enzyme1 = Enzyme('HaeIII', 'GGCC')
        strand1.enzymes.append(enzyme1)
        self.assertEqual(len(strand1.enzymes), 1)

        strand1.add_enzyme('XYZ', 'GGCC')
        self.assertEqual(len(strand1.enzymes), 1)

        strand1.add_enzyme('StuI', 'AGGCCT')
        self.assertEqual(len(strand1.enzymes), 2)
        

unittest.main()
