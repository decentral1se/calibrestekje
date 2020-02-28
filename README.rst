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

.. image:: https://travis-ci.com/Calibrestekje/calibrestekje.svg?branch=master
   :target: https://travis-ci.com/Calibrestekje/calibrestekje
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
`Calibre`_ metadata database outside the context of the Calibre desktop and web
interfaces. A set of generated `SQLAlchemy`_ bindings (see `sqlacodegen`_ for
more) are provided which allow for the querying of an existing Calibre metadata
database (a file typically called ``metadata.db``). These bindings are more
fine grained than Calibres `database interface`_ and provide access to the
Database table layer.

The idea of a "stekje" (Dutch word meaning "little graft") in the context of
software came out of the discussions at `Relearn`_ around cutting, grafting,
remixing, re-using and misusing software for collective work.

This stekje can be understood as a low level building block for experimenting
with new ways of doing library software. One exciting part about a stekje is
that it is possible that new roots will appear. It is hoped that Calibrestekje
may help new library software take root.

.. _Calibre: https://calibre-ebook.com/
.. _SQLALchemy: https://docs.sqlalchemy.org/
.. _sqlacodegen: https://github.com/agronholm/sqlacodegen
.. _database interface: https://manual.calibre-ebook.com/db_api.html
.. _Relearn: http://relearn.be/2019/

.. _example:

Example
*******

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
