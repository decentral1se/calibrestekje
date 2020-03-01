.. _header:

*************
calibrestekje
*************

.. image:: https://img.shields.io/badge/license-GPL-brightgreen.svg
   :target: LICENSE
   :alt: Repository license

.. image:: https://badge.fury.io/py/calibrestekje.svg
   :target: https://badge.fury.io/py/calibrestekje
   :alt: PyPI package

.. image:: https://travis-ci.com/decentral1se/calibrestekje.svg?branch=master
   :target: https://travis-ci.com/decentral1se/calibrestekje
   :alt: Travis CI result

.. image:: https://readthedocs.org/projects/calibrestekje/badge/?version=latest
   :target: https://calibrestekje.readthedocs.io/en/latest/
   :alt: Documentation status

.. image:: http://img.shields.io/liberapay/patrons/decentral1se.svg?logo=liberapay
   :target: https://liberapay.com/decentral1se
   :alt: Support badge

.. _introduction:

Library prototyping based on Calibre
------------------------------------

Calibrestekje is a Python library which provides a way to work with the
`Calibre`_ database outside the context of the Calibre desktop and web
interfaces.

Generated `SQLAlchemy`_ database bindings (see `sqlacodegen`_ for more)
are provided which allow for read/write access to an existing Calibre
database. These bindings are more fine grained than Calibres `database
interface`_ and provide direct access to the Database table layer. The
bindings are generated from Calibre version ``2.75.1``.

A `flask`_ extension is also provided for getting started with web prototyping.
Please see `flask-calibrestekje`_ and `the flask usage documentation`_ for
more.

.. _Calibre: https://calibre-ebook.com/
.. _SQLALchemy: https://docs.sqlalchemy.org/
.. _sqlacodegen: https://github.com/agronholm/sqlacodegen
.. _database interface: https://manual.calibre-ebook.com/db_api.html
.. _flask: https://flask.palletsprojects.com/
.. _flask-calibrestekje: https://github.com/decentral1se/flask-calibrestekje
.. _the flask usage documentation: https://calibrestekje.readthedocs.io/en/latest/flask.html

.. _example:

Quick Example
*************

.. code-block:: python

    from calibrestekje import Book, Publisher, init_session

    session = init_session("sqlite:///mymetadata.db")

    publisher = (session.query(Publisher)
                        .filter(Publisher.name == "MIT Press").one())

    books = (session.query(Book)
                    .filter(Book.publishers.contains(publisher)))

    print(f"Books published by MIT Press: {books.count()}")

.. _documentation:

Documentation
*************

* https://calibrestekje.readthedocs.io/

Mirroring
*********

* `hack.decentral1.se/decentral1se/calibrestekje`_

.. _hack.decentral1.se/decentral1se/calibrestekje: https://hack.decentral1.se/decentral1se/calibrestekje/
