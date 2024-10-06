"""
TESTING FOR MAIN
"""

from main import main_results


def test_func():
    """Test function for main"""
    test_dict = main_results()
    assert test_dict["extract"] == "covid-geography/mmsa-icu-beds.csv"
    assert test_dict["transform"] == "icuDB.db"
    print(test_dict["full_crudquery"])  # Specifically print the list of messages
    assert test_dict["full_crudquery"] == [
        "Create Success",
        "Read Success",
        "Query Success",
        "Update Success",
        "Delete Success",
    ]


if __name__ == "__main__":
    test_func()
