import unittest
import requests


class NosecountApiTest(unittest.TestCase):

    def test_base64(self):
        filename = "../tools/example.base64"
        with open(filename, "r") as fid:
            data = fid.read()

        result = requests.post("https://nosecount.herokuapp.com/nosecount",
                               json={"imageData": data})
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.json()["personCount"], 5)
        self.assertGreater(result.json()["accuracy"], 80.0)


    def test_url_png(self):
        result = requests.post("https://nosecount.herokuapp.com/nosecount",
                               json={"imageUrl": "https://nosecount.herokuapp.com/example.png"})
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.json()["personCount"], 5)
        self.assertGreater(result.json()["accuracy"], 80.0)


    def test_url_jpg(self):
        result = requests.post("https://nosecount.herokuapp.com/nosecount",
                               json={"imageUrl": "https://nosecount.herokuapp.com/example.jpg"})
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.json()["personCount"], 5)
        self.assertGreater(result.json()["accuracy"], 80.0)

def test_url_gif(self):
    result = requests.post("https://nosecount.herokuapp.com/nosecount",
                           json={"imageUrl": "https://nosecount.herokuapp.com/example.gif"})
    self.assertEqual(result.status_code, 200)
    self.assertEqual(result.json()["personCount"], 5)
    self.assertGreater(result.json()["accuracy"], 80.0)