import connexion
import six

from swagger_server.models.image_analysis import ImageAnalysis  # noqa: E501
from swagger_server.models.image_to_analyze import ImageToAnalyze  # noqa: E501
from swagger_server import util


def post_image(body):  # noqa: E501
    """Post an Image to analyze

     # noqa: E501

    :param body: Plain image or image as json object
    :type body: dict | bytes

    :rtype: ImageAnalysis
    """
    if connexion.request.is_json:
        body = ImageToAnalyze.from_dict(connexion.request.get_json())  # noqa: E501

    return ImageAnalysis(5, 0.0)
