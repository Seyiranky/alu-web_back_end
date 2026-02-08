#!/usr/bin/env python3
""" Unittest Test client
"""
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Unit tests for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test org method"""
        endpoint = f"https://api.github.com/orgs/{org_name}"
        client = GithubOrgClient(org_name)
        client.org()
        mock_get_json.assert_called_once_with(endpoint)

    @parameterized.expand([
        ("random-url", {"repos_url": "http://some_url.com"})
    ])
    def test_public_repos_url(self, org_name, payload):
        """Test _public_repos_url property"""
        with patch(
            'client.GithubOrgClient.org',
            new_callable=PropertyMock,
            return_value=payload
        ):
            client = GithubOrgClient(org_name)
            self.assertEqual(client._public_repos_url, payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test public_repos method"""
        mock_get_json.return_value = [
            {"name": "Google"},
            {"name": "TT"}
        ]

        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock,
            return_value="http://some_url.com"
        ):
            client = GithubOrgClient("test")
            self.assertEqual(client.public_repos(), ["Google", "TT"])

            mock_get_json.assert_called_once()
    
    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test has_license static method"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


# -------- Integration test payload --------
TEST_PAYLOAD = [
    (
        {"repos_url": "http://example.com/orgs/test/repos"},
        [
            {"name": "repo1", "license": {"key": "apache-2.0"}},
            {"name": "repo2", "license": {"key": "mit"}},
        ],
        ["repo1", "repo2"],
        ["repo1"],
    )
]


@parameterized_class(
    ["org_payload", "repos_payload", "expected_repos", "apache2_repos"],
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient"""

    @classmethod
    def setUpClass(cls):
        cls.get_patcher = patch(
            'requests.get',
            side_effect=[cls.org_payload, cls.repos_payload]
        )
        cls.mocked_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public repos integration"""
        client = GithubOrgClient("test")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public repos filtered by license"""
        client = GithubOrgClient("test")
        self.assertEqual(
            client.public_repos(license="apache-2.0"),
            self.apache2_repos
        )


if __name__ == "__main__":
    unittest.main()
