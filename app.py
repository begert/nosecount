from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.debug = True

swagger = Swagger(app)

@app.route('/echo')
def echo():
    """
    API rout for simple echo
    ---
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