# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.image_analysis import ImageAnalysis  # noqa: E501
from swagger_server.models.image_to_analyze import ImageToAnalyze  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_post_image(self):
        """Test case for post_image

        Post an Image to analyze
        """
        body = ImageToAnalyze()
        response = self.client.open(
            '/v1/nosecount',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
