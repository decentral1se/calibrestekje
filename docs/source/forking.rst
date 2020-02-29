.. _forking:

*******
Forking
*******

If you'd like to go beyond Calibre and embark on a new experimental library but
do not want to have to re-invent the database schema, you can get `SQLAlchemy`_
ecosystem tooling to output SQLAlchemy schemas definition based on Calibre but
ones which you can change yourself. This makes it possible to add new columns
and tables to your new database.

.. _SQLALchemy: https://docs.sqlalchemy.org/

To get started, you would run the following commands.

.. code-block:: bash

    $ pip install sqlacodegen
    $ sqlacodegen --noviews "sqlite:///path_to_my_calibre_metadata.db" > mynewdb.py

If you look in ``mynewdb.py``, Sqlacodegen may have included a table called
``t_sqlite_sequence``. You will want to remove this as I've only seen errors
related to this table for some reasons which are not clear now.

Feel free to add, delete and change columns and tables in the ``mynewdb.py``
file! It will be used to generate a brand new Sqlite database in which you have
a free hand to design a model for whatever ideas you might want to work with in
your new library software.

To generate the new Sqlite database, run the following.

.. code-block:: python

    from mynewdb import Base
    from sqlalchemy import create_engine

    engine = create_engine('sqlite:///mynewdb.db')

    Base.metadata.create_all(engine)

As a final check, it is then possible to investigate your new database with
`sqlitebrowser`_ to check that the new database matches what you have defined
in your ``mynewdb.py``.

.. _sqlitebrowser: https://sqlitebrowser.org/

.. code-block:: bash

    sqlitebrowser mynewdb.db
