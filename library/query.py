"""
QUERY
Query the database
"""

import sqlite3


def query():
    """Query the database for the top 5 rows of the table"""
    print("Querying data...")
    conn = sqlite3.connect("icu.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM icuDB")
    print("Top 5 rows of the table:")
    print(cursor.fetchall())
    conn.close()
    return "Success"
