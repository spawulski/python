"""
Docmentation for MyMath with error handling.

MyMath does some simple mathamatical functions.
"""


class MyMath():
    """Mymath implements some simple math functions."""

    def __init__(self, num_list=[]):
        """Initilize MyMath."""
        try:
            self.num_list = num_list
        except Exception as e:
            print("Error: ", e)

    def max(self, num_list):
        """Take a list of numbers and return the one with highest value."""
        try:
            max = int(num_list[0])

            for number in num_list:
                try:
                    if number > max:
                        max = number
                except Exception as e:
                    print("Error", e)

        except Exception as e:
            print("Error:",  e)

        return max

    def average(self, num_list):
        """Take a list of numbers and find average."""
        try:
            total = 0
            accumulator = 0

            for number in num_list:
                try:
                    total += number
                    accumulator += 1
                except Exception as e:
                    print ("Error: ", e)

            average = total / accumulator
        except Exception as e:
            print("Error: ", e)

        return average

    def stddev(self, num_list):
        """Calculate standard deviation from list of numbers."""
        try:
            mean = self.average(num_list)

            minus_mean = []

            for number in num_list:
                try:
                    minus_mean.append((number - mean) ** 2)
                except Exception as e:
                    print("Error: ", e)

            meany_mean = self.average(minus_mean)

            meany_mean = meany_mean ** .5

        except Exception as e:
            print("Error: ", e)

        return meany_mean


# ***************************************************************
# Main Body
# ***************************************************************

print('Input a series of numbers by')
print('entering a number and pressing enter after')

try:
    cont = ''
    mymath = MyMath()

    while cont != 'n':
        while True:
            try:
                mymath.num_list.append(int(input('Please enter a number: ')))
                break
            except ValueError:
                print('Please enter an integer')

        cont = ''

        while cont != 'n' and cont != 'y':
            cont = input('Would you like to add another number?(y/n)').lower()

    high = 'The number with highest value from your list: '
    av = 'The average value of your list: '
    st = 'The standard deviation value of your list: '

    print('')
    print(high + str(mymath.max(mymath.num_list)))
    print(av + str(mymath.average(mymath.num_list)))
    print(st + str(mymath.stddev(mymath.num_list)))

except Exception as e:
    print("Error: ", e)
