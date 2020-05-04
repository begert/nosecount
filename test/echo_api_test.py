import unittest
import requests


class EchoApiTest(unittest.TestCase):

    def test_echo(self):
        result = requests.get("https://nosecount.herokuapp.com/echo?p=value")
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.json()["p"], "value")

    def test_echo_without_p(self):
        result = requests.get("https://nosecount.herokuapp.com/echo")
        self.assertEqual(result.status_code, 200)
        self.assertIsNone(result.json()["p"])