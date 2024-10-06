"""
QUERY
Query the database
"""

import sqlite3


def create():
    """Create function for CRUD"""
    conn = sqlite3.connect("icu.db")
    cursor = conn.cursor()
    # create execution
    cursor.execute(
        "INSERT INTO icuDB (MMSA, total_percent_at_risk, high_risk_per_ICU_bed, high_risk_per_hospital, icu_beds, hospitals, total_at_risk) VALUES('Duham, NC','50%',1947,43787,360,14,667189)"
    )
    conn.close()
    return "Create Success"


def read():
    """Read function for CRUD"""
    conn = sqlite3.connect("icu.db")
    cursor = conn.cursor()
    # read execution
    print("Top 5 rows of the table:")
    cursor.execute("SELECT * FROM icuDB LIMIT 5;")
    conn.close()
    return "Read Success"


def query():
    """Query the database for the test case"""
    print("Querying data...")
    conn = sqlite3.connect("icu.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM icuDB WHERE MMSA = 'Duham, NC';")
    print(cursor.fetchall())
    conn.close()
    return "Query Success"


def update():
    """Update function for CRUD"""
    conn = sqlite3.connect("icu.db")
    cursor = conn.cursor()
    # update execution
    cursor.execute("UPDATE icuDB SET MMSA = 'Durham, NC' WHERE MMSA = 'Duham, NC'")
    conn.close()
    return "Update Success"


def delete():
    """Delete function for CRUD"""
    conn = sqlite3.connect("icu.db")
    cursor = conn.cursor()
    # delete execution
    cursor.execute("DELETE FROM icuDB WHERE MMSA = 'Durham, NC'")
    conn.close()
    return "Delete Success"


def full_crudquery():
    """Run all functions of crud_query.py"""

    # return a dictionary for testing
    return {
        "full_crudquery": [
            create(),
            read(),
            query(),
            update(),
            delete(),
        ]
    }
