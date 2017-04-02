from unittest import TestCase
from sample_python.code.scraper import Scraper
# import mock
import mongomock


class TestScraper(TestCase):
    def setUp(self):
        self.scraper = Scraper()
        self.scraper.client = mongomock.MongoClient()
        self.scraper.db = self.scraper.client.words_database

    def tearDown(self):
        self.scraper.db.drop_collection('words')

    def test_get_words_list_from_db(self):
        temp_words_list = {"casa": 5, "mesa": 3, "patata": 2}
        self.scraper.db.words.insert_one(temp_words_list)

        received_words_list = self.scraper.get_words_list_from_db()
        self.assertEqual([temp_words_list], received_words_list)
