"""
This is the documentation for database competency.

This is our first time working with databases in python.
"""


import sqlite3


class DBOperations():
    """Interact with a database."""

    def __init__(self):
        """Build database."""
        try:
            self.conn = sqlite3.connect("assignment.sqlite")

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
                print("Error:", e)
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
                    self.cur.execute(sql, data)
                except Exception as e:
                    print("Error:", e)

            self.conn.commit()
        except Exception as e:
            print("Error:", e)

    def printdb(self):
        """Print out contents of datavase."""
        try:
            for row in self.cur.execute("select * from samples"):
                try:
                    print(row)
                except Exception as e:
                    print("Error:", e)
        except Exception as e:
            print("Error:", e)


try:
    weather = {"2018-06-01": {"Max": 12.0,
                              "Min": 5.6,
                              "Mean": 7.1},
               "2018-06-02": {"Max": 22.2,
                              "Min": 11.1,
                              "Mean": 15.5},
               "2018-06-03": {"Max": 31.3,
                              "Min": 29.9,
                              "Mean": 30.0}}

    sample_database = DBOperations()
    sample_database.insert(weather)
    sample_database.printdb()
except Exception as e:
    print("Error:", e)
