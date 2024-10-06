"""
MAIN
"""

from library.extract import extract
from library.transform_load import load
from library.query import query


def main():
    """Main function for the ETL-Query script"""
    # Extract
    extract()

    # Transform and load
    load()

    # Query
    query()


if __name__ == "__main__":
    main()
