"""
This is the documentation for db_operations module.

This module performs all of the nessessary database interatcion.
By: Stephen Pawulski
"""


import sqlite3
import scrape_weather


class DBOperations():
    """Interact with a database. By: Stephen Pawulski."""

    def __init__(self):
        """Build database. By: Stephen Pawulski."""
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
                print("")
        except Exception as e:
            print("Error:", e)

    def insert(self, dict):
        """Insert a dict into the table. By: Stephen Pawulski."""
        try:
            loca = "Winnipeg, MB"
            sql = """insert into samples(date, location, min_temp,
                                         max_temp, avg_temp)
                     values(?,?,?,?,?)"""

            for k, v in dict.items():
                try:
                    data = (k, loca, v['Min'], v['Max'], v['Mean'])
                    if not self.check_if_exist(k):
                        try:
                            self.cur.execute(sql, data)
                            print(k + " added to database")
                        except Exception as e:
                            print("Error:", e)
                    else:
                        print(k + " already exists in the db")
                except Exception as e:
                    print("Error:", e)

            self.conn.commit()
        except Exception as e:
            print("Error:", e)

    def check_if_exist(self, day):
        """
        Check if there is a database entry for specific day.

        By: Stephen Pawulski.
        """
        try:
            result = self.cur.execute("""SELECT date
                                         FROM samples
                                         WHERE date=?""", (day, )).fetchone()
            if result:
                return True
            else:
                return False
        except Exception as e:
            print("Error:", e)

    def printdb(self):
        """Print out contents of database.  By: Stephen Pawulski."""
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
        """
        Get weather data within a range passed in to method.

        By: Stephen Pawulski.
        """
        to_pass = []
        sql = """SELECT date, min_temp, max_temp, avg_temp
                 FROM samples
                 WHERE samples.date between
                 ? AND ?
                 ORDER BY date"""
        data = (a, b)
        try:
            for row in self.cur.execute(sql, data):
                try:
                    to_pass.append(row)
                except Exception as e:
                    print("Error:", e)
        except Exception as e:
            print("Error", e)
        return to_pass

    def recent(self):
        """
        Return only the date of the most recent db entry.

        By: Stephen Pawulski.
        """
        sql = """SELECT date
                 FROM samples
                 ORDER BY date DESC
                 LIMIT 1"""

        try:
            for row in self.cur.execute(sql):
                try:
                    return row
                except Exception as e:
                    print("Error:", e)
        except Exception as e:
            print("Error:", e)

    def oldest(self):
        """
        Return only the date of the most recent db entry.

        By: Stephen Pawulski.
        """
        sql = """SELECT date
                 FROM samples
                 ORDER BY date ASC
                 LIMIT 1"""
        for row in self.cur.execute(sql):
            return row

    def update(self, date):
        """Update db. By: Stephen Pawulski."""
        db = DBOperations()
        db.insert(scrape_weather.recent_weather(date))

    def scrape_all(self):
        """Insert the full scrape into db. By: Stephen Pawulski."""
        db = DBOperations()
        db.insert(scrape_weather.scrape_all_weather())


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
    except Exception as e:
        print("Error:", e)
