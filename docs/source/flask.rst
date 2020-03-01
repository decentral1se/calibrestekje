.. _flasking:

**************
Use with Flask
**************

A `flask`_ extension is also provided so it's easy to get started with
developing new web interfaces with calibrestekje. In order to get started
you'll need to install the extension.

.. _flask: https://flask.palletsprojects.com

.. code-block:: bash

    $ pip install flask-calibrestekje

And then go ahead and create a ``flaskconfig.cfg`` file.

.. code-block:: config

    CALIBRESTEKJE_SQLITE_URL = "sqlite:///mymetadata.db"

And then finally, create your Flask application.

.. code-block:: python

    from calibrestekje import Book
    from flask import Flask, jsonify

    from flask_calibrestekje import CalibreStekje

    app = Flask(__name__)
    app.config.from_pyfile("config.cfg")
    db = CalibreStekje(app)

    @app.route("/")
    def home():
        return jsonify({"book-count": db.session.query(Book).count()})
