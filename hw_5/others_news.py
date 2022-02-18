from hw_5.general import FeedMain, NewsName


class SellGive(FeedMain):

    @staticmethod
    def validation_input_price(price):
        try:
            if int(price) == 0:
                txt = "Product is free!"
            else:
                txt = f"Product price is {str(price)} $"
            return txt
        except ValueError:
            print('Invalid price! Try again')

    def other_news_string_for_feed(self):
        price = SellGive.validation_input_price(FeedMain.input_price())
        if type(price) is str:
            title = f'\n--SELL or GIVE FOR FREE --'
            news_txt = f'\n{self.input_text_according_to_news_type()}'
            is_free = f'\n{price}\n'
            return title + news_txt + is_free

    def add_sell_give_data_to_file(self):
        data = self.other_news_string_for_feed()
        if type(data) is str:
            FeedMain.add_data_to_file(data=data)
