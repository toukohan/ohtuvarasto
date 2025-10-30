import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.barasto = Varasto(-2, -2)
        self.tulva = Varasto(10, 100)

    def test_negatiivisella_tilavuudella_nolla(self):
        self.assertAlmostEqual(self.barasto.tilavuus, 0)

    def test_ylimaarainen_saldo_menee_hukkaan(self):
        self.assertAlmostEqual(self.tulva.saldo, 10)

    def test_otetaan_negatiivista(self):
        otto = self.tulva.ota_varastosta(-2)
        self.assertAlmostEqual(otto, 0)

    def test_tayteen_varastoon_ei_tule_lisaa(self):
        self.tulva.lisaa_varastoon(2)

        self.assertAlmostEqual(self.tulva.saldo, 10)

    def test_negatiivisella_saldolla_nolla(self):
        self.assertAlmostEqual(self.barasto.saldo, 0)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)


    def test_lisataan_negatiivista(self):
        edellinen = self.varasto.saldo
        self.varasto.lisaa_varastoon(-2)

        self.assertAlmostEqual(self.varasto.saldo, edellinen)


    def test_varastosta_otetaan_enemman_kuin_saldo(self):
        otto = self.tulva.ota_varastosta(15)

        self.assertAlmostEqual(otto, 10)
        self.assertAlmostEqual(self.tulva.saldo, 0)

    def test_saattaa_tulostaa_oikein(self):
        oikea = "saldo = 10, vielä tilaa 0"

        self.assertEqual(oikea, str(self.tulva))
