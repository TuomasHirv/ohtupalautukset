import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):

    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 5
            if tuote_id == 3:
                return 0
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "piimä", 10)
            if tuote_id == 3:
                return Tuote(3, "jugurtti", 10)


        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote
        self.viitegeneraattori_mock.uusi.return_value = 999
    def test_maksettaessa_ostos_pankin_metodia_tilisiirto_kutsutaan(self):

        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_tilinsiirto_kutsutaan_oikeilla_arvoilla(self):


        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
        kauppa.aloita_asiointi()

        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("Testaaja", 1234567)


        self.pankki_mock.tilisiirto.assert_called_with("Testaaja",999,1234567,"33333-44455",5)

    def test_tilinsiirto_kutsutaan_oikeilla_arvoilla_kaksi_tuotetta(self):


        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
        kauppa.aloita_asiointi()

        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("Testaaja", 1234567)

        
        self.pankki_mock.tilisiirto.assert_called_with("Testaaja",999,1234567,"33333-44455",15)
    
    def test_tilinsiirto_kutsutaan_oikeilla_arvoilla_kaksi_samaa_tuotetta(self):


        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
        kauppa.aloita_asiointi()

        kauppa.lisaa_koriin(2)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("Testaaja", 1234567)

        
        self.pankki_mock.tilisiirto.assert_called_with("Testaaja",999,1234567,"33333-44455",20)


    def test_tilinsiirto_kutsutaan_oikeilla_arvoilla_toinen_tuote_loppu(self):


        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
        kauppa.aloita_asiointi()

        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(3)
        kauppa.tilimaksu("Testaaja", 1234567)

        
        self.pankki_mock.tilisiirto.assert_called_with("Testaaja",999,1234567,"33333-44455",5)

    def test_aloita_asiointi_nollaa_edelliset(self):
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(2)
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)

        kauppa.tilimaksu("Testaaja", 1234567)
        self.pankki_mock.tilisiirto.assert_called_with("Testaaja",999,1234567,"33333-44455",5)
    
    def test_viite_kutsutaan_jokaiselle_tilinsiirrolle(self):
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("Testaaja", 1234567)
        
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("Testaaja", 1234567)

        assert self.viitegeneraattori_mock.uusi.call_count == 2
    
    def test_ostoskorista_poistaminen(self):
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(2)
        kauppa.lisaa_koriin(1)
        kauppa.poista_korista(2)

        kauppa.tilimaksu("Testaaja", 1234567)
        self.pankki_mock.tilisiirto.assert_called_with("Testaaja",999,1234567,"33333-44455",5)

