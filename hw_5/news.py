from datetime import datetime
from hw_5.general import FeedMain


class NewsGen(FeedMain):

    def news_string_for_feed(self):
        title = f'\n--NEWS! NEWS! NEWS!--'
        dt = datetime.now().strftime("%Y-%m-%d %H:%M")
        news_txt = f'\n{self.input_text_according_to_news_type()}'
        city = f'\nCity: {NewsGen.input_news_city()}, Date: {dt}\n'
        return title + news_txt + city

    def add_news_data_to_file(self):
        data = self.news_string_for_feed()
        if type(data) is str:
            FeedMain.add_data_to_file(data=data)
