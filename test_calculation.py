import unittest, calculation

class TestCalculation(unittest.TestCase):
    def test_results(self):
        # Test the result of the calculation
        self.assertAlmostEqual(calculation.calc_monthly_income(60050),5004)
        self.assertAlmostEqual(calculation.calc_monthly_income(120000),10000)
        self.assertAlmostEqual(calculation.calc_monthly_tax(60050),922)
        self.assertAlmostEqual(calculation.calc_monthly_tax(120000),2696)
        self.assertAlmostEqual(calculation.calc_net_income(5004,922),4082)
        self.assertAlmostEqual(calculation.calc_net_income(10000,2696),7304)
        self.assertAlmostEqual(calculation.calc_super(5004,"9%"),450)
        self.assertAlmostEqual(calculation.calc_super(10000,"10%"),1000)

    def test_values(self):
        # Test the value error
        self.assertRaises(ValueError, calculation.calc_monthly_income, -2)
        self.assertRaises(ValueError, calculation.calc_monthly_tax, -2)
        self.assertRaises(ValueError, calculation.calc_net_income, -2, 100)
        self.assertRaises(ValueError, calculation.calc_net_income, 2, -100)
        self.assertRaises(ValueError, calculation.calc_net_income, -2, -100)
        self.assertRaises(ValueError, calculation.calc_super,-2,"10%")

    def test_types(self):
        # Test the type error
        self.assertRaises(TypeError, calculation.calc_monthly_income, 50+32j)
        self.assertRaises(TypeError, calculation.calc_monthly_income, True)
        self.assertRaises(TypeError, calculation.calc_monthly_income, "string_name")
        self.assertRaises(TypeError, calculation.calc_monthly_tax, 50+32j)
        self.assertRaises(TypeError, calculation.calc_monthly_tax, True)
        self.assertRaises(TypeError, calculation.calc_monthly_tax, "string_name")
        self.assertRaises(TypeError, calculation.calc_monthly_tax, 50+32j)
        self.assertRaises(TypeError, calculation.calc_monthly_tax, True)
        self.assertRaises(TypeError, calculation.calc_monthly_tax, "string_name")
