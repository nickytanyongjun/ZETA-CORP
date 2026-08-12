"""
ZETA website server
--------------------
A tiny Flask app that just serves the website (templates/index.html).

Run it with:
    python app.py

Then open in a browser:
    http://localhost:5000

To let other devices on your WiFi reach it, use your computer's local IP
instead of "localhost", e.g. http://192.168.1.23:5000
(Find your local IP with `ipconfig` on Windows or `ifconfig`/`ip addr` on
Mac/Linux.)

To change the port, edit PORT below.
"""

from flask import Flask, render_template

app = Flask(__name__)

PORT = 9000  # change this if you want to run on a different port


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    # host='0.0.0.0' makes it reachable from other devices on the same
    # network, not just this computer. Set debug=False when you're done
    # testing / before leaving it running for real use.
    app.run(host='0.0.0.0', port=PORT, debug=True)
