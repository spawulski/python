"""
This is the documentation for plot_operations module.

This module builds and shows all graph plots.
"""

import matplotlib.pyplot as plt
import db_operations


class PlotOperations():
    """Build a graph that appears on screen."""

    months_dict = {1: [], 2: [], 3: [], 4: [], 5: [],
                   6: [], 7: [], 8: [], 9: [], 10: [],
                   11: [], 12: []}

    months_array = []

    def build_plot(self, a, b):
        """Build a plot using data that is passed in."""
        db = db_operations.DBOperations()
        data = db.between(str(a), str(b))

        for item in data:
            month = int(item[0][5:7])
            if month < 10:
                month = int(item[0][6:7])

            mean = item[3]

            for key in self.months_dict.keys():
                if key == month:
                    if mean < 100:
                        self.months_dict[key].append(mean)

        for month in range(1, 13, 1):
            try:
                self.months_array.append(self.months_dict[month])
            except Exception as e:
                print("Error: ", e)

        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.boxplot(self.months_array)
        mtd = "Monthy Temperature Distrubution for: "
        ax.set_title(mtd + str(a) + " to " + str(b))
        ax.set_xlabel("Month")
        ax.set_ylabel("Temperature (Celcius")

        plt.show()


plot = PlotOperations()
plot.build_plot(1996, 2019)
