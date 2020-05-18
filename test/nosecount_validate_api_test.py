import unittest
import requests


class NoseCountValidateApiTest(unittest.TestCase):

    def test_no_image(self):
        result = requests.post("http://localhost:8000/nosecount", json={"nothing": "there"})
        self.assertEqual(result.status_code, 400)
        self.assertEqual(result.json()["error"], "Either imageUrl or imageData must be provided.")

    def test_url_bad(self):
        result = requests.post("http://localhost:8000/nosecount", json={"imageUrl": "this is a bad url"})
        self.assertEqual(result.status_code, 400)
        self.assertEqual(result.json()["error"], "Could not fetch content at this imageUrl")

    def test_url_not_accessible(self):
        result = requests.post("http://localhost:8000/nosecount", json={"imageUrl": "http://www.doesnotexist.ch/really_not"})
        self.assertEqual(result.status_code, 400)
        self.assertEqual(result.json()["error"], "Could not fetch content at this imageUrl")

    def test_url_not_an_image(self):
        result = requests.post("http://localhost:8000/nosecount", json={"imageUrl": "https://www.google.com"})
        self.assertEqual(result.status_code, 400)
        self.assertEqual(result.json()["error"], "Could not find a format to read the specified file in single-image mode")

    def test_data_not_base64(self):
        result = requests.post("http://localhost:8000/nosecount", json={"imageData": "thisIsNotBase64"})
        self.assertEqual(result.status_code, 400)
        self.assertEqual(result.json()["error"], "Could not read base64 imageData. Incorrect padding")

    def test_data_not_an_image(self):
        result = requests.post("http://localhost:8000/nosecount", json={"imageData": "aGFsbG8K"})
        self.assertEqual(result.status_code, 400)
        self.assertEqual(result.json()["error"], "Could not read base64 imageData. Could not find a format to read the specified file in single-image mode")
