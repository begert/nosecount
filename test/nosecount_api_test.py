import unittest
import requests


class NosecountApiTest(unittest.TestCase):

    def test_base64(self):
        filename = "tools/example.base64"
        with open(filename, "r") as fid:
            data = fid.read()

        result = requests.post("http://localhost:8000/nosecount",
                               json={"imageData": data})
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.json()["personCount"], 5)
        self.assertGreater(result.json()["accuracy"], 80.0)

    def test_url_png(self):
        result = requests.post("http://localhost:8000/nosecount",
                               json={"imageUrl": "http://localhost:8000/example.png"})
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.json()["personCount"], 5)
        self.assertGreater(result.json()["accuracy"], 80.0)

    def test_url_jpg(self):
        result = requests.post("http://localhost:8000/nosecount",
                               json={"imageUrl": "http://localhost:8000/example.jpg"})
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.json()["personCount"], 5)
        self.assertGreater(result.json()["accuracy"], 80.0)

    def test_url_gif(self):
        result = requests.post("http://localhost:8000/nosecount",
                               json={"imageUrl": "http://localhost:8000/example.gif"})
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.json()["personCount"], 5)
        self.assertGreater(result.json()["accuracy"], 80.0)
