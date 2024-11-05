#!/usr/bin/env python3
"""
basics of flask
"""

from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def home() -> str:
    """
    home/template pagr
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

