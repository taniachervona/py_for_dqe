import os
from hw_4 import normalize_sentence_including_first_separator
from hw_5.general import FeedMain


class AddNewsFromFile(FeedMain):

    @staticmethod
    def file_data_into_var(part_path: str, file_name: str,
                           file_ext: str):
        file_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")) + \
                    part_path
        with open(file_path + file_name + file_ext,
                  encoding="utf8") as txt_data:
            txt_info = txt_data.read()
        return txt_info

    @staticmethod
    def add_one_or_few_items(items_list: list, items_qty: int):
        for item in items_list[:items_qty]:
            FeedMain.add_data_to_file(data=f'\n{item}\n')
            items_list.remove(item)
        return items_list

    @staticmethod
    def delete_file(part_path: str, file_name: str,
                    file_ext: str):
        file_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")) + \
                    part_path
        file = file_path + file_name + file_ext
        if os.path.exists(file):
            os.remove(file)
        else:
            print("The file does not exist")

    @staticmethod
    def delete_if_file_is_empty(
            items_list: list, part_path: str,
            file_name: str, file_ext: str):
        if len(items_list) == 0:
            AddNewsFromFile.delete_file(
                part_path=part_path, file_name=file_name,
                file_ext=file_ext)

    @staticmethod
    def add_data_to_feed_and_remove_successful_processed_file(
            add_to_feed_qty: int,
            part_path: str = "\\hw_6\\",
            file_name: str = "add_data",
            file_ext: str = '.txt', data_sep: str = '\n\n'):
        data = AddNewsFromFile.file_data_into_var(
            part_path=part_path, file_name=file_name,
            file_ext=file_ext)
        input_list = data.split(sep=data_sep)
        output_list = AddNewsFromFile.add_one_or_few_items(
            items_list=input_list, items_qty=add_to_feed_qty)
        AddNewsFromFile.delete_if_file_is_empty(
            items_list=output_list, part_path=part_path,
            file_name=file_name, file_ext=file_ext)

    @staticmethod
    def normalize_txt_in_file(file_name: str = "news_feed",
                              part_path: str = "\\hw_5\\",
                              file_ext: str = ".txt"):
        data = AddNewsFromFile.file_data_into_var(
            part_path=part_path, file_name=file_name,
            file_ext=file_ext)
        sentence_list = data.split(sep='\n')
        for sentence in sentence_list:
            normalize_sentence_including_first_separator(
                sentence=sentence)


AddNewsFromFile.add_data_to_feed_and_remove_successful_processed_file(add_to_feed_qty=1)
