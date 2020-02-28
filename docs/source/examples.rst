.. _examples:

********
Examples
********

In order to work with Calibrestkje, you'll need to learn more about
`SQLAlchemy`_. SQLAlchemy is a Python "Object Relational Mapper", meaning that
it can help you write Python programs that interact with a database without
having to write raw database queries (that is often harder to do correctly).
The `querying`_ documentation is particularly useful. The following examples
are laid out in a "cookbook" style. Hopefully there is something useful in here
for you.

.. _SQLAlchemy: https://docs.sqlalchemy.org/en/13/
.. _querying: https://docs.sqlalchemy.org/en/13/orm/tutorial.html#querying

Working with the Calibre database
---------------------------------

Calibrestkje works with the Calibre metadata database. This means, you need to
install `Calibre`_ first on your system. On my Debian operating system , that
means I would run:

.. _Calibre: https://calibre-ebook.com

.. code-block:: bash

   $ sudo apt install -y calibre

And the first time I run Calibre, I would find that a metadata database has
been created in the ``/home/myuser/calibre/`` folder with the name
``metadata.db``. If you've been using Calibre for some time already, then
you'll probably already have this folder and database.

Sometimes it is useful to start from an empty metadata database and this can be
achieved by creating one with the ``calibredb`` command on the command-line. An
example of this would be:

.. code-block:: bash

   $ mkdir mytestcalibredb
   $ calibredb restore_database --really-do-it --with-library mytestcalibredb

Unfortunately, there is no "create new database command" (AFAIK) and therefore
it is required to run this magical incantation that is hard to remember.
Afterwards, you'll have a new ``mytestcalibredb/metadata.db`` file which you
can start to work with.

Please see the :ref:`limitations` documentation for understanding what
Calibrestekje can't do right now.

Initialising a new session
--------------------------

.. code-block:: python

    from calibrestkje import init_session

    sqlite_url = "sqlite:///path_to_my_calibre_metadata.db"
    session = init_session(sqlite_url)

All books without a publisher
-----------------------------

.. code-block:: python

    (session.query(Book)
           .filter(Book.publishers == None))

All books with multiple authors
-------------------------------

.. code-block:: python

    from sqlalchemy.sql.expression import func

    (session.query(Book)
           .join(Book.authors)
           .group_by(Book)
           .having(func.count(Author.id) > 1))

List of all tags that contain some pattern
------------------------------------------

.. code-block:: python

    (session.query(Tag)
           .filter(Tag.name.contains("humanities")))
