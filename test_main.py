"""
TESTING FOR MAIN
"""

import unittest
from unittest.mock import patch
from main import main


class TestMainFunction(unittest.TestCase):
    """Object for testing main with unittest"""

    @patch("library.extract.extract")
    @patch("library.transform_load.load")
    @patch("library.query.query")
    def test_main(self, mock_query, mock_load, mock_extract):
        """Test the main function calls."""
        main()

        # Assert that each function was called once
        mock_extract.assert_called_once()
        mock_load.assert_called_once()
        mock_query.assert_called_once()


if __name__ == "__main__":
    unittest.main()
