# Python program to convert csv file to json format
import csv
import json
import sys


class CsvToJson:
    def __init__(self):
        """
        Initialization of the class and reading the csv file
        """
        try:
            # CSV file opening and reading
            self.csv_file = open("data.csv", 'r')
            self.input_file = csv.reader(self.csv_file)
            self.json_out = []
        except exception as e:
            print("CSV  File doesn't exist")
            sys.exit()

    def checking(self, list_dict, name):
        """
        Function to check  whether elements present in json or not
        """
        try:
            if list_dict:
                for element in list_dict:
                    if name in element.values():
                        return True
            return False
        except exception as e:
            print("Some error occurred")
            sys.exit()

    def csv_to_json_conversion(self):
        """
        Function to convert CSV to json
        :return: Json
        """
        try:
            temp_dict = {}
            header = None
            last_element = None
            # Reading csv file column wise
            for idx, element in enumerate(self.input_file):
                # Taking out the header line
                if idx == 0:
                    header = element
                else:
                    # Reading each and every column
                    if any(s.strip() for s in element):
                        # Calling checking function to check if the element is present in Json
                        if self.checking(self.json_out, element[0]):
                            if 'children' in self.json_out[-1].keys():
                                if not self.checking(self.json_out[-1]['children'], element[3]):
                                    last_element = self.json_out[-1]
                                    if 'children' in last_element.keys():
                                        if self.checking(last_element['children'], element[3]):
                                            continue
                                        else:
                                            for col in range(len(element[3:6])):
                                                col = col + 3
                                                row = element[col]
                                                temp_dict[header[col]] = row
                                            last_element['children'].append(temp_dict)
                                            temp_dict = {}
                                    else:
                                        last_element['children'] = []
                                        for ind, row in enumerate(element[3:6]):
                                            ind = ind + 3
                                            temp_dict[header[ind]] = row
                                        last_element['children'].append(temp_dict)
                                        temp_dict = {}
                                if element[6]:
                                    last_element1 = last_element['children'][-1]
                                    if 'children' in last_element1.keys():
                                        if self.checking(last_element1['children'], element[6]):
                                            continue
                                        else:
                                            for col in range(len(element[6:9])):
                                                col = col + 6
                                                row = element[col]
                                                temp_dict[header[col]] = row
                                            last_element1['children'].append(temp_dict)
                                            temp_dict = {}
                                    else:
                                        last_element1['children'] = []
                                        for ind, row in enumerate(element[6:9]):
                                            ind = ind + 6
                                            temp_dict[header[ind]] = row
                                        last_element1['children'].append(temp_dict)
                                        temp_dict = {}
                            else:
                                if element[3]:
                                    last_element = self.json_out[-1]
                                    if 'children' in last_element.keys():
                                        if self.checking(last_element['children'], element[3]):
                                            continue
                                        else:
                                            for col in range(len(element[3:6])):
                                                col = col + 3
                                                row = element[col]
                                                temp_dict[header[col]] = row
                                            element['children'].append(temp_dict)
                                            temp_dict = {}
                                    else:
                                        last_element['children'] = []
                                        for ind, row in enumerate(element[3:6]):
                                            ind = ind + 3
                                            temp_dict[header[ind]] = row
                                        last_element['children'].append(temp_dict)
                                        temp_dict = {}
                        else:
                            if element[0]:
                                for col in range(len(element[:3])):
                                    row = element[col]
                                    temp_dict[header[col]] = row
                                self.json_out.append(temp_dict)
                                temp_dict = {}
            # closing csv file
            self.csv_file.close()
            # writing the output to output file
            with open("output.json", 'w') as json_file:
                json_file.write(json.dumps(self.json_out, indent=3))

        except exception as e:
            print("Some error occurred")
            sys.exit()


# Object creation#
c2j = CsvToJson()
c2j.csv_to_json_conversion()
