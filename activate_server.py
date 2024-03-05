from flask import Flask
from threading import Thread

web_app = Flask(__name__)


@web_app.route("/")
def index():
    return "activated"


def start_server():
    web_app.run(host="0.0.0.0", port=8080)


def activate_server():
    server_thread = Thread(target=start_server)
    server_thread.start()
