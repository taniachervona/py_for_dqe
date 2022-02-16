from datetime import datetime

from hw_5.general import FeedMain


class PrivateAdGen(FeedMain):

    @staticmethod
    def input_private_ad_text():
        return input("Please, input text of your news: ")

    @staticmethod
    def input_expiration_date():
        return input("Please, input expiration date "
                     "for your private ad in yyyy-mm-dd format: ")

    @staticmethod
    def validation_format_for_input_date():
        input_dt = PrivateAdGen.input_expiration_date()
        try:
            dt = datetime.strptime(input_dt, "%Y-%m-%d")
            return dt
        except ValueError:
            print('Invalid date is entered!')
            PrivateAdGen.input_expiration_date()

    @staticmethod
    def check_input_date_is_above_now(dt: datetime):
        if dt > datetime.now():
            return dt
        else:
            print("Entered data is lower then now! "
                  "Please enter correct data ")
            PrivateAdGen.input_expiration_date()

    @staticmethod
    def find_diff_between_dates(end_dt: datetime):
        dt_end = PrivateAdGen.check_input_date_is_above_now(dt=end_dt)
        dt_start = datetime.now()
        return (dt_end - dt_start).days

    @staticmethod
    def private_ad_string_for_feed():
        dt_input = PrivateAdGen.validation_format_for_input_date()
        title = f'\n--PRIVATE AD--'
        private_ad_txt = f'\n{PrivateAdGen.input_private_ad_text()}'
        input_dt = f'\nActual until: ' \
                   f'{PrivateAdGen.check_input_date_is_above_now(dt=dt_input)}, '
        dt_diff = f'{PrivateAdGen.find_diff_between_dates(end_dt=dt_input)} ' \
                  f'day(s) left'
        return title + private_ad_txt + input_dt + dt_diff

    def add_private_ad_data_to_file(self):
        data = self.private_ad_string_for_feed()
        FeedMain.add_data_to_file(data=data)
