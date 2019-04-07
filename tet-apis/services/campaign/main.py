#!/usr/bin/env python3
"""
Documentation

See also https://www.python-boilerplate.com/flask
"""
import os
import argparse
from flask import Flask, jsonify
from flask_cors import CORS
from logzero import logger


def create_app(config=None):
    app = Flask(__name__)
    # logzero.logfile("./campaign_service.log", maxBytes=1e6, backupCount=3)

    # See http://flask.pocoo.org/docs/latest/config/
    app.config.update(dict(DEBUG=True))
    app.config.update(config or {})

    # Setup cors headers to allow all domains
    # https://flask-cors.readthedocs.io/en/latest/
    CORS(app)

    # Definition of the routes. Put them into their own file. See also
    # Flask Blueprints: http://flask.pocoo.org/docs/latest/blueprints
    @app.route("/")
    def hello_world():
        logger.info("/")
        return "Hello World"

    @app.route("/foo/<someId>")
    def foo_url_arg(someId):
        logger.info("/foo/%s", someId)
        return jsonify({"echo": someId})

    @app.route("/tet/campaign/")
    def foo_url_arg1():
        logger.info("/tet/campaign/ : triggered")
        details = ["hello","world"]
        logger.info("data called : returned: resp: {}".format(details))
        return jsonify({"resp": details})

    @app.route("/tet/campaign/<someId>")
    def foo_url_arg2(someId):
        logger.info("/tet/campaign/ : triggered")
        details = ["hello","world"]
        logger.info("data called by title : {} : resp: {}".format(someId, details))
        return jsonify({"resp": details})

    return app


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", action="store", default="8000")

    args = parser.parse_args()
    port = int(args.port)
    app = create_app()
    app.run(host="0.0.0.0", port=port)
