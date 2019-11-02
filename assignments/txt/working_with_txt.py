"""
Documentaiton for working with text files.

Read in text file, manipulate text, save text file.
"""


def write_over(string, file):
    """Write over file."""
    try:
        with open(file, 'w') as myfile:
            myfile.write(string)

    except Exception as e:
        print("Error: ", e)


def read_in(file):
    """Read in file."""
    try:
        old = "Aqua"
        new = "Azure #007fff"
        mystring = ''

        with open(file) as myfile:
            try:
                for line in myfile:
                    if line.startswith(old):
                        mystring += new + "\n"
                    else:
                        mystring += line

            except Exception as e:
                print("Error: ", e)

    except Exception as e:
        print("Error: ", e)

    return mystring


try:
    ex = read_in('file.txt')
    write_over(ex, 'file.txt')
except Exception as e:
    print("Error: ", e)
