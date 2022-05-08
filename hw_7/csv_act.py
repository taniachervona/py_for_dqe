import csv
import os


class CSVFileAct:

    def __init__(self, csv_file_name: str = 'word_count',
                 csv_file_path: str = '\\hw_7\\'):
        self.file_name = csv_file_name
        self.part_path = csv_file_path

    def find_word_qty_in_txt_file(self, part_path: str = '\\hw_5\\',
                                  file_name: str = 'news_feed',
                                  file_ext: str = '.txt'):
        file_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")) + part_path
        with open(file_path + file_name + file_ext, encoding="utf8") as txt_data:
            txt_info = txt_data.read()
            lis = txt_info.split(sep=' ')
            n = 0
            for i in lis:
                n += 1
                if i.find('\n') not in [-1, 0]:
                    n += 1
            return n

    def import_csv(self): # file_name: str):
        data = []
        with open(self.file_name + '.csv', 'r') as scraped:
            reader = csv.reader(scraped)
            for row in reader:
                columns = [row[0], row[1]]
                data.append(columns)
            scraped.close()
        print(data)
        return data

    def create_word_count_csv_file(self, qty: int):
        file_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")) + self.part_path
        el = CSVFileAct().import_csv()
        with open(file_path + self.file_name + '.csv', 'a', encoding="utf-8",
                  newline='') as csv_data:
            csv_list = ['word_count', qty]
            if int(el[-1][-1]) != qty:
                csv.writer(csv_data).writerow(csv_list)
            csv_data.close()

    def count_all_letters(self, part_path: str = '\\hw_5\\',
                                  file_name: str = 'news_feed',
                                  file_ext: str = '.txt'):
        sep_list = ['!', ',', '.', '-', '\n', '\t', ' ']
        count_var = 0
        file_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")) + part_path
        with open(file_path + file_name + file_ext, encoding="utf8") as txt_data:
            txt_info = txt_data.read()
            for j in txt_info:
                if j not in sep_list:
                    var = txt_info.count(j)
                    count_var = count_var + var
        return count_var

qty = CSVFileAct().find_word_qty_in_txt_file()
CSVFileAct().create_word_count_csv_file(qty=qty)

# CSVFileAct.import_csv(file_name='word_count')

print(CSVFileAct().count_all_letters())