import os
from hw_5.general import FeedMain


class AddNewsFromFile(FeedMain):

    @staticmethod
    def file_data_into_var(part_path: str = "\\hw_6\\",
                           file_name: str = "add_data",
                           file_ext: str = '.txt'):
        file_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")) + \
                    part_path
        with open(file_path + file_name + file_ext,
                  encoding="utf8") as txt_data:
            txt_info = txt_data.read()
        return txt_info

    @staticmethod
    def add_one_or_few_items(data: str, items_qty: int):
        items_list = data.split(sep='\n\n')
        print(items_list)
        for item in items_list[:items_qty]:
            FeedMain.add_data_to_file(data=f'\n{item}\n')

    @staticmethod
    def delete_file(part_path: str = "\\hw_6\\",
                    file_name: str = "add_data",
                    file_ext: str = '.txt'):
        file_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")) + \
                    part_path
        file = file_path + file_name + file_ext
        if os.path.exists(file):
            os.remove(file)
        else:
            print("The file does not exist")


#print(AddNewsFromFile.file_data_into_var())
AddNewsFromFile.add_one_or_few_items(data=AddNewsFromFile.file_data_into_var(), items_qty=2)