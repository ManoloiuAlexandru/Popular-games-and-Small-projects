import os
import sys
import xmltodict

old_path = sys.path[:]
dir_name = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.sep.join([os.path.dirname(__file__), '..', '..', '..', '..', '..', '..']))
sys.path = old_path


class CompareFile:
    def __init__(self, file_for_compare, file_to_compare):
        self.file_for_compare = file_for_compare
        self.file_to_compare = file_to_compare

    def create_dict_file_for_compare(self):
        try:
            with open(self.file_for_compare, 'r') as output:
                file_content = output.read()
                xml_dict_file_for_compare = xmltodict.parse(file_content)
            return xml_dict_file_for_compare
        except OSError:
            print("Error at opening file")

    def create_dict_file_to_compare(self):
        try:
            with open(self.file_to_compare, 'r') as output:
                file_content = output.read()
                xml_dict_file_to_compare = xmltodict.parse(file_content)
            return xml_dict_file_to_compare
        except OSError:
            print("Error at opening file")

    def get_dict_of_specific_item_from_dict_file_for_compare(self, list_of_depth):
        dict_rez = self.create_dict_file_for_compare()
        for child in list_of_depth:
            dict_rez = dict_rez[child]
        return dict_rez

    def get_dict_of_specific_item_from_dict_file_to_compare(self, list_of_depth):
        dict_rez = self.create_dict_file_to_compare()
        for child in list_of_depth:
            dict_rez = dict_rez[child]
        return dict_rez

    def compare_specific_field(self, list_of_depth, field_to_check, key_for_compare):
        dict_rez_for_compare = self.get_dict_of_specific_item_from_dict_file_for_compare(list_of_depth)
        dict_rez_to_compare = self.get_dict_of_specific_item_from_dict_file_to_compare(list_of_depth)
        dict_rez_for_compare = dict_rez_for_compare[field_to_check]
        dict_rez_to_compare = dict_rez_to_compare[field_to_check]

        for item in dict_rez_for_compare:
            self.find_and_compare_element(item, dict_rez_to_compare, key_for_compare)

    def find_and_compare_element(self, item, dict_of_elements, key_for_compare):
        in_the_list = 0
        for element in dict_of_elements:
            if element[key_for_compare] == item[key_for_compare]:
                in_the_list = 1
                if len(element) >= len(item):
                    for attrib in element:
                        if attrib in item:
                            if item[attrib] == element[attrib]:
                                pass
                            else:
                                print("These difference are in the", self.file_for_compare)
                                print("The attribute ", attrib, "of ", element[key_for_compare], " has other value",
                                      item[attrib])
                        else:
                            print("These difference are in the", self.file_for_compare)
                            print("The attrib", attrib, "of ", element[key_for_compare], " is not in the file")
                else:
                    for attrib in element:
                        if attrib in item:
                            if item[attrib] == element[attrib]:
                                pass
                            else:
                                print("These difference are in the", self.file_to_compare)
                                print("The attribute ", attrib, "of ", element[key_for_compare], " has other value",
                                      item[attrib])
                        else:
                            print("These difference are in the", self.file_to_compare)
                            print("The attrib is not in the file")

        if in_the_list == 0:
            print(item[key_for_compare], " not in")
