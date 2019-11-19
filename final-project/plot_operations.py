"""
This is the documentation for plot_operations module.

This module builds and shows all graph plots.
By: Stephen Pawulski.
"""

import matplotlib.pyplot as plt
import db_operations


class PlotOperations():
    """Build a graph that appears on screen. By: Stephen Pawulski."""

    months_dict = {1: [], 2: [], 3: [], 4: [], 5: [],
                   6: [], 7: [], 8: [], 9: [], 10: [],
                   11: [], 12: []}

    months_array = []

    def build_plot(self, a, b):
        """Build a plot using data that is passed in. By: Stephen Pawulski."""
        # Instantiate db object
        db = db_operations.DBOperations()
        # Query db for all weather data from year a - year b
        data = db.between(str(a), str(b))

        # Iterate through every line of data returned from db Query
        for item in data:
            # Get number of month from db entry
            month = int(item[0][5:7])
            # If a single digit month, trim off leading 0
            if month < 10:
                month = int(item[0][6:7])

            mean = item[3]

            # If month from db entry matches with month_dict key
            for key in self.months_dict.keys():
                if key == month:
                    # There were a few outliers/bad data that this filters out
                    if mean < 100:
                        # add temperature data for that day to month_dict value
                        self.months_dict[key].append(mean)

        # Iterate through month values
        for month in range(1, 13, 1):
            try:
                # Create an array of arrays for boxplot
                self.months_array.append(self.months_dict[month])
            except Exception as e:
                print("Error: ", e)

        # Set params for boxplot along with data to populate
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.boxplot(self.months_array)
        mtd = "Monthy Temperature Distrubution for: "
        if a == b:
            ax.set_title(mtd + str(a))
        else:
            ax.set_title(mtd + str(a) + " to " + str(b))
        ax.set_xlabel("Month")
        ax.set_ylabel("Temperature (Celcius)")

        plt.show()
