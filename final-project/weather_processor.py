"""
This is the documentation for weather_processor module.

This module takes input from users and calls methods from the program.
By: Stephen Pawulski.
"""

import db_operations
import plot_operations
import datetime


class WeatherProcessor():
    """Collect input from user, show boxplots. By: Stephen Pawulski."""

    def __init__(self):
        """Instantiate the Weather Processor Object. By: Stephen Pawulski."""
        try:
            f = '%Y-%m-%d'
            t = '%Y-%m-%d'
            self.db = db_operations.DBOperations()
            date = str(self.db.recent())
            old = str(self.db.oldest())
            date = date[2:12]
            old = old[2:12]
            if date.strip() != "ne":
                self.old_year = old[0:4]
                self.recent_year = date[0:4]
                self.recent = datetime.datetime.strptime(date, f).strftime(t)
                self.oldest = datetime.datetime.strptime(old, f).strftime(t)
            else:
                self.old_year = -100
        except Exception as e:
            print("Error:", e)


def set_dates(self):
    """Set begging of data year, and end of data year. By: Stephen Pawulski."""
    try:
        f = '%Y-%m-%d'
        t = '%Y-%m-%d'
        date = str(self.db.recent())
        old = str(self.db.oldest())
        date = date[2:12]
        old = old[2:12]
        self.old_year = old[0:4]
        self.recent_year = date[0:4]
        self.recent = datetime.datetime.strptime(date, f).strftime(t)
        self.oldest = datetime.datetime.strptime(old, f).strftime(t)
    except Exception as e:
        print("Error:", e)


def menu():
    """Menu for user interaction. By: Stephen Pawulski."""
    print("Please select one of the 2 following options")
    print("1) Download full set of weather data (Slow)")
    print("2) Update dataset with only recent missing data (Fast)\n")


def year_prompt(pro):
    """Propt for year range for boxplot. By: Stephen Pawulski."""
    a = " and "
    try:
        n = str(pro.old_year)
        o = str(int(pro.recent_year))  # - 1)
    except Exception as e:
        print("Error:", e)

    print("Great, now that we have the data, we can show you box plots.")
    print("""The box plot takes the mean temperature from each of the months
in user submitted year range and puts them into a box plot for you.
You will now have to enter a starting year and a end year.""")
    be = "Year entered has to be between: "
    try:
        if int(pro.old_year) > 0:
            print(be + n + a + o)
        else:
            set_dates(pro)
            print(be + n + a + o)
    except Exception as e:
        print("Error:", e)

    return year_range()


def make_plot(year_range):
    """Create Box Plot. By: Stephen Pawulski."""
    try:
        plot.build_plot(year_range[0], year_range[1])
    except Exception as e:
        print("Error:", e)


def year_range():
    """Logic for boxplot year range. By: Stephen Pawulski."""
    years = [0, 0]
    year_1 = 0
    year_2 = 100000000000000000
    try:
        yo = int(pro.old_year)
        yr = int(pro.recent_year)
        y2 = 'Please enter year including or later than '
        ped = 'Please enter a 4 digit year\n'
        s = "(Must be at least {})\n".format(pro.old_year)
        t = "(Max value can be {})\n".format(pro.recent_year)
        while year_1 < yo or year_1 > yr:
            while True:
                try:
                    year_1 = (int(input(ped + s)))
                    years[0] = year_1
                    break
                except ValueError:
                    print('Please enter an integer')

        while year_2 > int(pro.recent_year):
            while True:
                try:
                    year_2 = (int(input(y2 + str(year_1) + '\n' + t)))
                    years[1] = year_2
                    if year_2 < year_1:
                        year_2 = 100000000000000
                    print(year_2)
                    break
                except ValueError:
                    print('Please enter an integer')
    except Exception as e:
        print("Error:", e)

    return years


if __name__ == "__main__":
    try:
        pro = WeatherProcessor()
        db = db_operations.DBOperations()
        plot = plot_operations.PlotOperations()
        get_data = 0
        ro = '\nEnter only the character 1 or 2, nothing else.\n'
        no = "Database doesn't exist. Please run full scrape."
        sb = 'Stand by while we scrape all of the weather.'
    except Exception as e:
        print("Error", e)

    print("Welcome to the Weather Scraper and BoxPlot visualtion tool!")
    # Prompt to download full set of data, or to Update

    try:
        while get_data != 1 and get_data != 2:
            menu()
            while True:
                try:
                    get_data = int(input("Enter '1' or '2'\n"))
                    break
                except ValueError:
                    print(ro)

        if get_data == 1:
            print(sb)
            db.scrape_all()
            years = year_prompt(pro)
            make_plot(years)
        elif get_data == 2:
            if int(pro.old_year) > 0:
                db.update(pro.recent)
                years = year_prompt(pro)
                make_plot(years)
            else:
                print(no)
    except Exception as e:
        print("Error:", e)
