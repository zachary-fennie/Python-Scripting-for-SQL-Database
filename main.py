"""
MAIN
ETL-Query script
"""

from library.extract import extract
from library.transform_load import load
from library.query import query

# Extract
extract()

# Transform and load
load()

# Query
query()
