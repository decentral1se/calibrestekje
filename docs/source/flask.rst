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

And then go ahead and create a ``app.cfg`` file.

.. code-block:: cfg

    CALIBRESTEKJE_SQLITE_URL = "sqlite:///mymetadata.db"

Create your Flask application in an ``app.py``.

.. code-block:: python

    from calibrestekje import Book
    from flask import Flask, jsonify

    from flask_calibrestekje import CalibreStekje

    app = Flask(__name__)
    app.config.from_pyfile("app.cfg")
    db = CalibreStekje(app)

    @app.route("/")
    def home():
        return jsonify({"book-count": db.session.query(Book).count()})

And finally, run your application.

.. code-block:: bash

    $ export FLASK_APP=app.py
    $ flask run
