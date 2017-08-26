import os


class DataUtils(object):

    singer_name = "singer_name.txt"
    html_txt = "html.txt "

    def __init__(self, file_name):
        self.file_name = "data/" + file_name
        file_object = open(self.file_name, "r", encoding="utf-8")
        file_object.close()

    def get_data(self):
        file_object = open(self.file_name, "r", encoding="utf-8")
        all_the_text = file_object.readlines()
        file_object.close()
        return all_the_text

    def set_data(self, all_lines):
        file = open(self.file_name, 'w', encoding="utf-8")
        file.writelines(all_lines)
        file.close()

#
# list1 = list(txt_file.get_data())
# for element in txt_file.get_data():
#     print(element.rstrip("\n"))
