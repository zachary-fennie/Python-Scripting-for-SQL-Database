"""
MAIN
"""

from library.extract import extract
from library.transform_load import load
from library.query import query


def main_results():
    """Results function for testing main"""
    results = {"extract": extract(), "transform": load(), "query": query()}
    return results


def main():
    """Main function for the ETL-Query script"""
    # extract
    extract()

    # transform and load
    load()

    # query
    query()

    # call results function for testing
    main_results()


if __name__ == "__main__":
    main()
