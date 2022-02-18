import os
from enum import Enum


class NewsName(Enum):

    NEWS = 1
    PRIVATE_AD = 2
    SELL_GIVE = 3


class FeedMain:

    def __init__(self, name: NewsName):
        self.name = name

    @staticmethod
    def input_user_value():
        print("Choose one from list: ", "1. News",
              "2. Private ad", "3. Other one", sep="\n")
        return input("What news type your want to add? "
                     "(Enter only number) ")

    @staticmethod
    def choose_news_type():
        choose = FeedMain.input_user_value()
        if choose.isdigit() is True and int(choose) in [1, 2, 3]:
            return choose
        else:
            print("You enter wrong value. Try again")

    @staticmethod
    def add_data_to_file(data: str, file_name: str = "news_feed",
                         part_path: str = "\\hw_5\\",
                         file_ext: str = ".txt"):
        file_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")) + part_path
        with open(file_path + file_name + file_ext,
                  mode='a', encoding="utf8") as txt_data:
            return txt_data.write(data)

    def input_text_according_to_news_type(self):
        if self.name == NewsName.NEWS.value:
            txt_var = 'news'
        elif self.name == NewsName.PRIVATE_AD.value:
            txt_var = 'private ad'
        elif self.name == NewsName.SELL_GIVE.value:
            txt_var = 'sell or give ad'
        else:
            txt_var = ''
        return input(f"Please, input text of {txt_var}: ")

    @staticmethod
    def input_expiration_date():
        return input("Please, input expiration date "
                     "for your private ad in yyyy-mm-dd format: ")

    @staticmethod
    def input_news_city():
        return input("Please, input your city: ")

    @staticmethod
    def input_your_name():
        return input("Please, input your name: ")

    @staticmethod
    def input_price():
        return input("Please, input price in $ (only int value): ")
