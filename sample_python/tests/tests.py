from unittest import TestCase
from sample_python.code.scraper import Scraper
import mock
from mock import *
import mongomock
import errno

class TestScraper(TestCase):
    def setUp(self):
        self.scraper = Scraper()
        self.scraper.client = mongomock.MongoClient()
        self.scraper.db = self.scraper.client.words_database

    def tearDown(self):
        self.scraper.db.drop_collection('words')

    def test_save_words_in_db_if_not_exists_yet(self):
        self.scraper.exists_in_db = Mock(return_value=True)
        # If we can insert, the returned value from save function must be different from None value
        self.assertIsNotNone(self.scraper.save_words_in_db({"dinero": 1000000}))

    def test_save_words_in_db_if_exists_already(self):
        self.scraper.exists_in_db = Mock(return_value=False)
        self.assertIsNone(self.scraper.save_words_in_db({"dinero": 1000000}))

    def test_get_words_list_from_db(self):
        temp_words_list = {"casa": 5, "mesa": 3, "patata": 2}
        self.scraper.db.words.find = mock.MagicMock(return_value=temp_words_list)
        received_words_list = self.scraper.get_words_list_from_db()
        self.assertEqual(temp_words_list, received_words_list)

    def test_save_words_in_db_is_int(self):
        self.assertEqual(self.scraper.save_words_in_db(3), errno.EINVAL)

    def test_save_words_in_db_is_bool(self):
        self.assertEqual(self.scraper.save_words_in_db(True), errno.EINVAL)

    def test_save_words_in_db_is_string(self):
        self.assertEqual(self.scraper.save_words_in_db("Ordenador"), errno.EINVAL)







