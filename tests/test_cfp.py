import unittest

from cfp import openfoodfacts_api, get_cfp, make_response, build_weight, change_units


class TestCFP(unittest.TestCase):

    def test_openfoodfacts_api(self):
        res1 = openfoodfacts_api("")
        self.assertEqual(res1["code"], None)

        res2 = openfoodfacts_api("3265776634553")
        self.assertEqual(res2["code"], "3265776634553")
        self.assertEqual(res2["status"], 1)
        self.assertEqual(res2["product"]["product_name"], "Fromage Frais")

        res3 = openfoodfacts_api("3265776634")
        self.assertEqual(res3["code"], "3265776634")
        self.assertEqual(res3["status"], 0)

    def test_make_response(self):
        test_barcodes = ["3103220009574", "3250391587285", "3017800022016", "9002490100070",
                         "3588570001995"]

        bc1 = "3700214611548"
        bc2 = "3033490306014"
        bc3 = "3229820795676"
        res1 = make_response(bc1)
        res2 = make_response(bc2)
        res3 = make_response(bc3)
        self.assertAlmostEqual(res1["CFPDensity"], 2.6188, 4)
        self.assertEqual(res1["CFPUnit"], "g")
        self.assertEqual(res2["CFPDensity"] / 2, res2["TotalCFP"])
        self.assertEqual(res2["weight"], 500)
        self.assertEqual(res2["weightUnit"], "g")
        self.assertEqual(res3["weight"], 250)
        self.assertEqual(res3["weightUnit"], "g")

    def test_build_weight(self):
        test1 = build_weight("557g")
        test2 = build_weight("32 KG")
        test3 = build_weight(" 4,5 L")

        self.assertEqual(test1["weight"], 557)
        self.assertEqual(test1["weightUnit"], 'g')
        self.assertEqual(test2["weight"], 32)
        self.assertEqual(test2["weightUnit"], 'kg')
        self.assertEqual(test3["weight"], 4.5)
        self.assertEqual(test3["weightUnit"], 'l')


if __name__ == "__main__":
    unittest.main()
