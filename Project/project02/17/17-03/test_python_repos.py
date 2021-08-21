import unittest

from python_repos import request_python_repositories
from python_repos import get_repository_dictionaries


class StatusCodeTest(unittest.TestCase):
    def setUp(self) -> None:
        """
        Send a request to GitHub api and save the response in r attribute.
        Get the 'items' dictionary from response and put it into repo_dicts attribute.
        """
        self.r = request_python_repositories()
        self.repo_dicts = get_repository_dictionaries(self.r)

    def test_status_code(self):
        """Test that we receive a 200 to the sent http request."""
        expected_status_code = 200
        self.assertEqual(self.r.status_code, expected_status_code)

    def test_repository_dictionary_length(self):
        """Test that length of 'items' dictionary in response is 30."""
        expected_length = 30
        self.assertEqual(len(self.repo_dicts), expected_length)


if __name__ == '__main__':
    unittest.main()
