import unittest

from cfp import openfoodfacts_api, get_cfp, make_response


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
        res1 = make_response(bc1)
        self.assertEqual(res1["value"], 178)
        self.assertEqual(res1["unit"], "g")
        # self.assertEqual(res1["quantity_value"], 100)
        # TODO other barcodes to test


if __name__ == "__main__":
    unittest.main()
