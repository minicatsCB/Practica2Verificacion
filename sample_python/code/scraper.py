from pymongo import MongoClient


class Scraper(object):
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.words_database
        # Collections are created in a lazy way, therefore it is not declared nor initialized here

    def save_word_in_db(self, word_list):
        '''
        Insert the frequence list in the database
        '''
        self.db.words.insert_one(word_list)

    def get_words_list_from_db(self):
        # Retrieve all the word lists excluding the ID attribute
        cursor = self.db.words.find({}, {'_id': False})
        # Save all the documents in the database
        words_list = []
        for record in cursor:
            words_list.append(record)
        return words_list

if __name__ == "__main__":
    s = Scraper()
    # word_list = {"casa": 5, "mesa": 3, "patata": 2}
    # s.save_word_in_db(word_list)
    # print(s.get_words_list_from_db())
    print("Hey!")
