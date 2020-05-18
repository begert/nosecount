from flask import Flask, request, jsonify, send_file
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


def fail(msg):
    return jsonify(error=msg), 400


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
        try:
            img = imread(image_url)
        except (FileNotFoundError, IOError):
            return fail("Could not fetch content at this imageUrl")
        except ValueError as e:
            return fail(str(e))

    elif "imageData" in request.json:
        try:
            image_data = request.json['imageData']
            img = imread(io.BytesIO(base64.b64decode(image_data)))
        except ValueError as e:
            return fail("Could not read base64 imageData. " + str(e))
    else:
        return fail("Either imageUrl or imageData must be provided.")

    try:
        detection = detector.detectObjectsFromImage(
            input_image=img,
            input_type='array',
            output_image_path='output.jpg',
            output_type='file',
            thread_safe=True
        )
    except:
        return fail("Detection failed.")

    counter = 0
    accuracy = 0
    for item in detection:
        if item["name"] == 'person':
            counter += 1
            accuracy += item["percentage_probability"]
    if counter > 0:
        accuracy = accuracy / counter
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


@app.route('/example.png')
def example_img_png():
    return send_file("tools/example.png")


@app.route('/example.jpg')
def example_img_jpg():
    return send_file("tools/example.jpg")


@app.route('/example.gif')
def example_img_gif():
    return send_file("tools/example.gif")


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5777)
