import unittest
import datetime
from sqlalchemy import Column, String, Integer, Date, DateTime, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import Date as SqlDate, DateTime as SqlDateTime # Per confrontare i tipi di colonna SQLAlchemy specifici

from db.modelli import Base, AnagraficaSoggetto, AnagraficaEnte, Elaborazione, ElaborazioneSoggetto


class TestAnagraficaSoggettoModel(unittest.TestCase):

    def test_table_name(self):
        self.assertEqual(AnagraficaSoggetto.__tablename__, 'tbl_AnagraficaSoggetto')

    def test_inheritance(self):
        self.assertTrue(issubclass(AnagraficaSoggetto, Base))

    def test_columns_exist_and_types(self):
        # Accedi alla colonna tramite __table__.columns
        codice_le_moire_col = AnagraficaSoggetto.__table__.columns['CodiceLeMoire']
        self.assertIsInstance(codice_le_moire_col, Column) # Ora questo test passerà!
        self.assertEqual(codice_le_moire_col.type.python_type, str)
        self.assertTrue(codice_le_moire_col.primary_key)
        self.assertEqual(codice_le_moire_col.type.length, 33)

        data_nascita_col = AnagraficaSoggetto.__table__.columns['DataNascita']
        self.assertIsInstance(data_nascita_col, Column)
        self.assertIsInstance(data_nascita_col.type, SqlDate) # Verifica il tipo SQLAlchemy
        self.assertEqual(data_nascita_col.type.python_type, datetime.date) # Verifica il tipo Python corrispondente

        sesso_col = AnagraficaSoggetto.__table__.columns['Sesso']
        self.assertIsInstance(sesso_col, Column)
        self.assertEqual(sesso_col.type.python_type, str)
        self.assertEqual(sesso_col.type.length, 1)

        relazione_prima_chiave_esterna_col = AnagraficaSoggetto.__table__.columns['RelazionePrimaChiaveEstera']
        self.assertIsInstance(relazione_prima_chiave_esterna_col, Column)
        self.assertEqual(relazione_prima_chiave_esterna_col.type.python_type, int)

    def test_all_columns_defined(self):
        expected_columns = [
            'CodiceLeMoire', 'CodiceArca', 'ChiaveEstera', 'CodiceFiscale',
            'RelazionePrimaChiaveEstera', 'CodStatoRisposta', 'Nome', 'Cognome',
            'CognomeAcquisito', 'NomePadre', 'CognomePadre', 'NomeMadre',
            'CognomeMadre', 'DataNascita', 'Sesso', 'CodiceComuneNascita',
            'NomeComuneNascita', 'ViaResidenza', 'NumCivicoResidenza', 'CittaResidenza',
            'CAPResidenza', 'CodPaeseResidenzaISO316612', 'StatoCivile',
            '_DataVariazioneStatoCivile', 'DataMorte', 'DataArrivo',
            '_DataCreazionePosizione', '_DataAggiornamentoPosizione', '_DataRicezioneMorte'
        ]
        defined_columns = AnagraficaSoggetto.__table__.columns.keys()

        for col_name in expected_columns:
            self.assertIn(col_name, defined_columns, f"Colonna {col_name} non trovata in {defined_columns}")
            # Puoi anche verificare che siano istanze di Column se vuoi, anche se __table__.columns lo garantisce
            self.assertIsInstance(AnagraficaSoggetto.__table__.columns[col_name], Column)


class TestAnagraficaEnteModel(unittest.TestCase):

    def test_table_name(self):
        self.assertEqual(AnagraficaEnte.__tablename__, 'tbl_AnagraficaEnte')

    def test_inheritance(self):
        self.assertTrue(issubclass(AnagraficaEnte, Base))

    def test_columns_exist_and_types(self):
        cod_ente_col = AnagraficaEnte.__table__.columns['CodEnte']
        self.assertIsInstance(cod_ente_col, Column)
        self.assertTrue(cod_ente_col.primary_key)
        self.assertEqual(cod_ente_col.type.python_type, str)
        self.assertEqual(cod_ente_col.type.length, 5)

        cod_belfiore_col = AnagraficaEnte.__table__.columns['CodBelfiore']
        self.assertIsInstance(cod_belfiore_col, Column)
        self.assertFalse(cod_belfiore_col.nullable) # Deve essere NOT NULL
        self.assertEqual(cod_belfiore_col.type.length, 4)


class TestElaborazioneModel(unittest.TestCase):

    def test_table_name(self):
        self.assertEqual(Elaborazione.__tablename__, 'tbl_Elaborazione')

    def test_inheritance(self):
        self.assertTrue(issubclass(Elaborazione, Base))

    def test_composite_primary_key(self):
        pk_columns = [c.name for c in Elaborazione.__table__.primary_key.columns]
        expected_pk = [
            'TipoOperazione', 'TipoScambio', 'PaeseRichiestaScambio316612',
            'PaeseRispostaScambio316612', '_DataTestaFile', 'Progressivo'
        ]
        self.assertSetEqual(set(pk_columns), set(expected_pk)) # Confronta come set per ignorare l'ordine
        self.assertEqual(len(pk_columns), 6)

    def test_columns_exist_and_types(self):
        num_soggetti_col = Elaborazione.__table__.columns['NumSoggetti']
        self.assertIsInstance(num_soggetti_col, Column)
        self.assertEqual(num_soggetti_col.type.python_type, int)

        nome_file_col = Elaborazione.__table__.columns['NomeFile']
        self.assertIsInstance(nome_file_col, Column)
        self.assertEqual(nome_file_col.type.python_type, str)
        self.assertEqual(nome_file_col.type.length, 39)


class TestElaborazioneSoggettoModel(unittest.TestCase):

    def test_table_name(self):
        self.assertEqual(ElaborazioneSoggetto.__tablename__, 'tbl_ElaborazioneSoggetto')

    def test_inheritance(self):
        self.assertTrue(issubclass(ElaborazioneSoggetto, Base))

    def test_composite_primary_key(self):
        pk_columns = [c.name for c in ElaborazioneSoggetto.__table__.primary_key.columns]
        expected_pk = [
            'ChiaveElabSogg', 'TipoOperazione', 'TipoScambio',
            'PaeseRichiestaScambio316612', 'PaeseRispostaScambio316612', '_DataTestaFile'
        ]
        self.assertSetEqual(set(pk_columns), set(expected_pk))
        self.assertEqual(len(pk_columns), 6)

    def test_columns_exist_and_types(self):
        chiave_elab_sogg_col = ElaborazioneSoggetto.__table__.columns['ChiaveElabSogg']
        self.assertIsInstance(chiave_elab_sogg_col, Column)
        self.assertEqual(chiave_elab_sogg_col.type.python_type, int) # BigInteger di solito mappa a int in Python
        self.assertTrue(chiave_elab_sogg_col.primary_key)

        codice_le_moire_col = ElaborazioneSoggetto.__table__.columns['CodiceLeMoire']
        self.assertIsInstance(codice_le_moire_col, Column)
        self.assertFalse(codice_le_moire_col.nullable) # Deve essere NOT NULL
        self.assertEqual(codice_le_moire_col.type.length, 33)

        descrizione_errore_col = ElaborazioneSoggetto.__table__.columns['DescrizioneErrore']
        self.assertIsInstance(descrizione_errore_col, Column)
        self.assertEqual(descrizione_errore_col.type.python_type, str)


if __name__ == '__main__':
    unittest.main()