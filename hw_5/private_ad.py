from datetime import datetime
from hw_5.general import FeedMain, NewsName


class PrivateAdGen(FeedMain):

    @staticmethod
    def validation_for_input_date(input_dt):
        try:
            dt = datetime.strptime(input_dt, '%Y-%m-%d')
            return dt
        except ValueError:
            print('Invalid date! Try again')

    @staticmethod
    def is_input_date_over_today(input_dt):
        dt = PrivateAdGen.validation_for_input_date(input_dt=input_dt)
        if type(dt) is datetime:
            if dt > datetime.now():
                return dt
            else:
                print('Input date is smaller then today! Try again')

    @staticmethod
    def find_diff_between_dates(dt_end):
        if type(dt_end) is datetime:
            dt_start = datetime.now()
            return (dt_end - dt_start).days

    def private_ad_string_for_feed(self):
        dt_input = self.is_input_date_over_today(FeedMain.input_expiration_date())
        if type(dt_input) is datetime:
            title = f'\n--PRIVATE AD--'
            private_ad_txt = f'\n{self.input_text_according_to_news_type()}'
            input_dt = f'\nActual until: ' \
                       f'{dt_input.strftime("%Y-%m-%d")}, '
            dt_diff = f'{PrivateAdGen.find_diff_between_dates(dt_end=dt_input)} ' \
                      f'day(s) left\n'
            return title + private_ad_txt + input_dt + dt_diff

    def add_private_ad_data_to_file(self):
        data = self.private_ad_string_for_feed()
        if type(data) is str:
            FeedMain.add_data_to_file(data=data)
