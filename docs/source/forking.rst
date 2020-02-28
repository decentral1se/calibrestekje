.. _forking:

*******
Forking
*******

If you're not interested in maintaining compatibility with Calibre and would
like to embark on a new experimental library but do not want to have to
re-invent the database schema, you can get Calibrestekje to output
`SQLAlchemy`_ schemas definition based on Calibre but ones which you can change
yourself. This makes it possible to add new columns and tables to your new
database.

.. _SQLALchemy: https://docs.sqlalchemy.org/

To get started, you would run the following command.

.. code-block:: bash

    $ calibrestekje generate > mynewdb.py

From there, you can tell SQLAlchemy to create a new Sqlite database based on
this schema.

.. code-block:: python

    from mynewdb import Base
    from sqlalchemy import create_engine

    engine = create_engine('sqlite:///mynewdb.db')

    Base.metadata.create_all(engine)

It is then possible to investigate your new database with `sqlitebrowser`_.

.. _sqlitebrowser: https://sqlitebrowser.org/

.. code-block:: bash

    sqlitebrowser mynewdb.db
