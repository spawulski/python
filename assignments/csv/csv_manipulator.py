"""
Documentation for csv assignment.

Manipulate the data within a csv file.
"""

import csv


def csv_reader(file):
    """Import csv file."""
    new_array = []
    try:
        with open(file) as mydata:
            for line in csv.DictReader(mydata):
                new_dict = {}
                try:
                    for k, v in line.items():
                        k = k.lstrip()
                        k = k.replace('"', '')
                        # k = k.replace('“', '')
                        # k = k.replace('”', '')
                        try:
                            if k not in new_dict.keys():
                                print(k)
                                new_dict[k] = float(v) * 2
                        except Exception as e:
                            print("Error: ", e)

                    new_array.append(new_dict)
                except Exception as e:
                    print("Error: ", e)
    except Exception as e:
        print("Error; ", e)

    return new_array


def csv_writer(list):
    """Take in a list of dictionaries and write it to a .csv."""
    try:
        with open('newdata.csv', 'w', newline='') as csvfile:
            fieldnames = ['Temp', 'Press', 'Humidity']
            writer = csv.DictWriter(csvfile, fieldnames)
            writer.writeheader()

            try:
                for line in list:
                    try:
                        writer.writerow(line)
                    except Exception as e:
                        print("Error: ", e)
            except Exception as e:
                print("Error: ", e)

    except Exception as e:
        print("Error; ", e)


test = "test"
print(test)

this_array = csv_reader('mydata.csv')
csv_writer(this_array)
