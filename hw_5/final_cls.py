from hw_5.general import NewsName, FeedMain
from hw_5.news import NewsGen
from hw_5.others_news import SellGive
from hw_5.private_ad import PrivateAdGen


class FinalAction:

    def __init__(self):
        self.news = NewsGen(NewsName.NEWS.value)
        self.ad = PrivateAdGen(NewsName.PRIVATE_AD.value)
        self.sell = SellGive(NewsName.SELL_GIVE.value)

    def fill_news_file(self):
        val = FeedMain.choose_news_type()
        if type(val) is str:
            if int(val) == 1:
                self.news.add_news_data_to_file()
            elif int(val) == 2:
                self.ad.add_private_ad_data_to_file()
            else:
                self.sell.add_sell_give_data_to_file()

    def add_one_more_ad(self):
        self.fill_news_file()
        while True:
            val = input("Do you want add data to news paper? (y/n)")
            if val == 'y':
                self.fill_news_file()
            else:
                print("Good lack!")
                break


FinalAction().add_one_more_ad()
