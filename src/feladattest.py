import feladat
import unittest

class TestKereso(unittest.TestCase):

    def test_false(self):
        self.assertFalse(feladat.parkereso(["Barnabás", "István", "Dávid", "Dani", "Béla"], ["Bernadett", "Mónika", "Lili", "Lea"]), "Nincs leelenőrizve, hogy különböző hosszúságúak-e a listák")
        self.assertFalse(feladat.parkereso([],[],), "Nincs leelenőrizve, hogy különböző hosszúságúak-e a listák")
        
    def test_output(self):
        self.assertEqual(feladat.parkereso(["Barnabás", "István", "Dávid", "Dani", "Béla"], ["Bernadett", "Mónika", "Lili", "Lea", "Anikó"]), {"Barnabás": "Bernadett", "Dani": "Lili", "István": "Mónika", "Dávid": "Anikó", "Béla": "Lea"}, "Várt kimenet:" + str({"Barnabás": "Bernadett", "Dani": "Lili", "István": "Mónika", "Dávid": "Anikó", "Béla": "Lea"}) + "Kapott kimenet:" + str(feladat.parkereso(["Barnabás", "István", "Dávid", "Dani", "Béla"], ["Bernadett", "Mónika", "Lili", "Lea", "Anikó"])))
        self.assertEqual(feladat.parkereso(["Barnabás"], ["Bernadett"]), {"Barnabás": "Bernadett"}, "Várt kimenet:" + str({"Barnabás": "Bernadett"}) + "Kapott kimenet:" + str(feladat.parkereso(["Barnabás"], ["Bernadett"])))
        self.assertEqual(feladat.parkereso(["Barnabás", "István"], ["Anikó", "Lea"]), {"Barnabás": "Anikó", "István": "Lea"}, "Várt kimenet:" + str({"Barnabás": "Anikó", "István": "Lea"}) + "Kapott kimenet:" + str(feladat.parkereso(["Barnabás", "István"], ["Anikó", "Lea"])))
        self.assertEqual(feladat.parkereso(["István", "Barnabás", "Dani"], ["Mónika", "Lili", "Bernadett"]), {"Barnabás": "Bernadett", "Dani": "Lili", "István":"Mónika"}), "Várt kimenet:" + str({"István": "Mónika", "Barnabás": "Bernadett", "Dani": "Lili"}) + "Kapott kimenet:" + str(feladat.parkereso(["István", "Barnabás", "Dani"], ["Mónika", "Lili", "Bernadett"]))