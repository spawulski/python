"""
This is the documentation for weather_processor module.

This module takes input from users and calls methods from the program.
"""

import db_operations
import plot_operations
import scrape_weather
import datetime


class WeatherProcessor():
    """Collect input from user, show boxplots."""

    def __init__(self):
        """Instantiate the Weather Processor Object."""
        f = '%Y-%m-%d'
        t = '%Y-%m-%d'
        self.db = db_operations.DBOperations()
        date = str(self.db.recent())
        old = str(self.db.oldest())
        date = date[2:12]
        old = old[2:12]
        self.old_year = old[0:4]
        self.recent_year = date[0:4]
        self.recent = datetime.datetime.strptime(date, f).strftime(t)
        self.oldest = datetime.datetime.strptime(old, f).strftime(t)


def menu():
    """Menu for user interaction."""
    print("Please select one of the 2 following options")
    print("1) Download full set of weather data (Slow)")
    print("2) Update dataset with only recent missing data (Fast)")


def year_range():
    """Logic for boxplot year range."""
    years = [0, 0]
    year_1 = 0
    year_2 = 100000000000000000
    while year_1 < int(pro.old_year):  # and year_1 < int(pro.recent_year):
        while True:
            try:
                year_1 = (int(input('Please enter a 4 digit year to start')))
                years[0] = year_1
                break
            except ValueError:
                print('Please enter an integer')

    while year_2 > int(pro.recent_year):  # and year_1 < int(pro.recent_year):
        while True:
            try:
                year_2 = (int(input('Please enter a 4 digit year to end')))
                years[1] = year_2
                if year_2 < year_1:
                    year_2 = 100000000000000
                break
            except ValueError:
                print('Please enter an integer')

    return years


if __name__ == "__main__":
    pro = WeatherProcessor()
    db = db_operations.DBOperations()
    plot = plot_operations.PlotOperations()
    get_data = 0
    # db.update(pro.recent)
    # scrape_weather.scrape_all_weather()
    # plot.build_plot(2003, 2016)

    print("Welcome to the Weather Scraper and BoxPlot visualtion tool!")
    # Prompt to download full set of data, or to Update

    while get_data != 1 and get_data != 2:
        menu()
        while True:
            try:
                get_data = int(input("Enter '1' or '2'\n"))
                break
                print("Test 1")
            except ValueError:
                print('\nEnter only the character 1 or 2, nothing else.\n')

    if get_data == 1:
        scrape_weather.scrape_all_weather()
    elif get_data == 2:
        db.update(pro.recent)

    # Propt for year range for boxplot
    print("Great, now that we have the data, we can show you box plots.")
    print("""The box plot takes the mean temperature from each of the months
             in user submitted year range and puts them into a box plot for
              you.\nYou will now have to enter a starting year and a end
              year.""")
    bet = "Year entered has to be between: "
    print(bet + str(pro.old_year) + " and " + str(pro.recent_year))

    year_range = year_range()
    plot.build_plot(year_range[0], year_range[1])
