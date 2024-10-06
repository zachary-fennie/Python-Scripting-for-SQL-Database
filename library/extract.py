"""
EXTRACT
Extract a dataset from a url
"""

import requests


def extract(
    url="https://github.com/fivethirtyeight/data/blob/e6bbbb2d35310b5c63c2995a0d03d582d0c7b2e6/covid-geography/mmsa-icu-beds.csv",
    file_path="covid-geography/mmsa-icu-beds.csv",
):
    """Extract a url to a file path"""
    print("Extracting data...")
    with requests.get(url, timeout=5) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return file_path
