from flask import Flask, request, jsonify
from flasgger import Swagger
from imageai.Detection import ObjectDetection
from imageio import imread
import io
import base64

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.config['SWAGGER'] = {
    'title': "InnT nosecount API",
    'description': "This is the API for nosecount, it processes an image and returns the count of persons (humans) on the image. Humans with two noses are counted double ;).",
    'version': "0.0.2",
    'uiversion': 3
}
app.debug = True

swagger = Swagger(app)

detector = ObjectDetection()
detector.setModelTypeAsTinyYOLOv3()
detector.setModelPath("yolo-tiny.h5")
detector.loadModel()

@app.route('/nosecount', methods=["POST"])
def post_image():
    """
    Post an Image to analyze
    ---
    tags:
      - Image analysis
    consumes:
      - "application/json"
    produces:
      - "application/json"
    parameters:
      - in: "body"
        name: "body"
        description: "Plain image as base64 encoded string (imageData)
        or image as a a publicly accessible URL (imageUrl).
        "
        required: true
        schema:
          type: "object"
          properties:
            imageData:
              type: "string"
            imageUrl:
              type: "string"
    responses:
      200:
        description: "successful operation"
        schema:
          type: "object"
          properties:
            personCount:
              type: "integer"
              format: "int32"
            accuracy:
              type: "number"
              format: "float"
      400:
        description: "Invalid input"
    """

    if "imageUrl" in request.json:
        image_url = request.json['imageUrl']
        img = imread(image_url)
    else:
        image_data = request.json['imageData']
        img = imread(io.BytesIO(base64.b64decode(image_data)))

    detection = detector.detectObjectsFromImage(
        input_image=img,
        input_type='array',
        output_image_path='output.jpg',
        output_type='file',
        thread_safe=True
    )

    counter = 0
    accuracy = 0
    for item in detection:
        if item["name"] == 'person':
            counter += 1
            accuracy += item["percentage_probability"]
    if counter > 0:
        accuracy = accuracy/counter
    else:
        accuracy = 99

    return jsonify(personCount=counter,
                   accuracy=accuracy)


@app.route('/echo')
def echo():
    """
    API route for simple echo
    ---
    tags:
      - Other services
    parameters:
      - name: p
        in: query
        type: string
        required: true
        description: value to echo as json
    responses:
      400:
        description: error
      200:
        description: wrapped parameter p as result
        schema:
          id: Result
          properties:
            p:
              type: string
              description: the param returned
              default: 'NA'
    """

    p = request.args.get("p")

    print("echo: p -", p)

    return jsonify(p=p)


if __name__  == '__main__':
    app.debug = True
    app.run(host="0.0.0.0",port=5777)