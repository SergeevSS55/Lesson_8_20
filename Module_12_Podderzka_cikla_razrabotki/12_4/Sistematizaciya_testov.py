import unittest
import Unit_test

calcST = unittest.TestSuite()
# calcST.addTest(unittest.makeSuite(Unit_test.CalcTest)) рабочий метод, но makeSuite перестанет работать в следующей версии
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(Unit_test.CalcTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcST)