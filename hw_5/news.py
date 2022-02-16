from datetime import datetime

from hw_5.general import FeedMain


class NewsGen(FeedMain):

    @staticmethod
    def input_news_text():
        return input("Please, input text of your news: ")

    @staticmethod
    def input_news_city():
        return input("Please, input your city: ")

    @staticmethod
    def news_string_for_feed():
        title = f'\n--NEWS! NEWS! NEWS!--'
        dt = datetime.now().strftime("%Y-%m-%d %H:%M")
        news_txt = f'\n{NewsGen.input_news_text()}'
        city = f'\nCity: {NewsGen.input_news_city()}, Date: {dt}'
        return title + news_txt + city

    def add_news_data_to_file(self):
        data = self.news_string_for_feed()
        FeedMain.add_data_to_file(data=data)
