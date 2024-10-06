"""
MAIN
"""

from library.extract import extract
from library.transform_load import load
from library.crud_query import full_crudquery


def main_results():
    """Results function for testing main"""
    results = {
        "extract": extract(),
        "transform": load(),
        "full_crudquery": full_crudquery(),
    }
    return results


def main():
    """Main function for the ETL-Query script"""
    # extract
    extract()

    # transform and load
    load()

    # query
    full_crudquery()

    # call results function for testing
    main_results()


if __name__ == "__main__":
    main()
