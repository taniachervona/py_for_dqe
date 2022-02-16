import os


class FeedMain:

    @staticmethod
    def input_user_value():
        print("Choose one from list: ", "1. News",
              "2. Private ad", "3. Other one", sep="\n")
        return input("What news type your want to add? ")

    def choose_news_type(self):
        choose = FeedMain.input_user_value()
        if choose.isdigit() is True and int(choose) in [1, 2, 3]:
            return choose
        else:
            print("You enter wrong value. Try again")
            self.choose_news_type()

    @staticmethod
    def add_data_to_file(data: str, file_name: str = "news_feed",
                         part_path: str = "\\hw_5\\",
                         file_ext: str = ".txt"):
        file_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")) + part_path
        with open(file_path + file_name + file_ext,
                  mode='a', encoding="utf8") as txt_data:
            return txt_data.write(data)

FeedMain().choose_news_type()
