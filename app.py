from flask import Flask, render_template, request, Response, jsonify
import os

app = Flask(__name__)



if __name__ == '__main__':
    cf_port = os.getenv("PORT")
    if cf_port is None:
        app.run(host='0.0.0.0', port=5000, debug=True)
    else:
        app.run(host='0.0.0.0', port=int(cf_port), debug=True)

