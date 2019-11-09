"""
This is the documentation for db_operations module.

This module performs all of the nessessary database interatcion.
"""


import sqlite3
import scrape_weather


class DBOperations():
    """Interact with a database."""

    def __init__(self):
        """Build database."""
        try:
            self.conn = sqlite3.connect("test.sqlite")

            self.cur = self.conn.cursor()
            try:
                self.cur.execute("""Create table samples
                              (id integer primary key autoincrement not null,
                               date text not null,
                               location text not null,
                               min_temp real not null,
                               max_temp real not null,
                               avg_temp real not null);""")
                print("Table created successfully.")
            except Exception as e:
                print(e)
        except Exception as e:
            print("Error:", e)

    def insert(self, dict):
        """Insert a dict into the table."""
        try:
            loca = "Winnipeg, MB"
            sql = """insert into samples(date, location, min_temp,
                                         max_temp, avg_temp)
                     values(?,?,?,?,?)"""

            for k, v in dict.items():
                try:
                    data = (k, loca, v['Min'], v['Max'], v['Mean'])
                    if not self.check_if_exist(k):
                        self.cur.execute(sql, data)
                    else:
                        print(k + " was not inserted into db")
                except Exception as e:
                    print("Error:", e)

            self.conn.commit()
        except Exception as e:
            print("Error:", e)

    def check_if_exist(self, day):
        """Check if there is a database entry for specific day."""
        # sql = """SELECT id, date, location FROM samples WHERE date=?"""
        # self.cur.execute(sql, (day))

        # result = self.cur.fetchone()
        result = self.cur.execute("""SELECT date
                                     FROM samples
                                     WHERE date=?""", (day, )).fetchone()
        if result:
            print(result)
            print("Date did exist")
            return True
        else:
            print("Date did not exist")
            return False

    def printdb(self):
        """Print out contents of dataBase."""
        try:
            for row in self.cur.execute("""SELECT *
                                           FROM samples
                                           ORDER BY date"""):
                try:
                    print(row)
                except Exception as e:
                    print("Error:", e)
        except Exception as e:
            print("Error:", e)

    def between(self, a, b):
        """Get weather data within a range passed in to method."""
        to_pass = []
        sql = """SELECT date, min_temp, max_temp, avg_temp
                 FROM samples
                 WHERE samples.date between
                 ? AND ?
                 ORDER BY date"""
        data = (a, b)
        try:
            for row in self.cur.execute(sql, data):
                to_pass.append(row)
                # print(row)
        except Exception as e:
            print("Error", e)
        return to_pass

#
#
# This is example of between
#
#
# try:
#    sample_database = DBOperations()
#    sample_database.between('2015', '2020')
# except Exception as e:
#    print("Error", e)


if __name__ == "__main__":
    try:
        try:
            sample_database = DBOperations()
        except Exception as e:
            print("Error:", e)
        try:
            sample_database.insert(scrape_weather.scrape_all_weather())
        except Exception as e:
            print("Error:", e)
        # try:
        # sample_database.printdb()
        # except Exception as e:
        #    print("Error:", e)
    except Exception as e:
        print("Error:", e)
