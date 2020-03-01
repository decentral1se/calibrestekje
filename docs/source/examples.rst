.. _examples:

********
Examples
********

In order to work with Calibrestkje, you'll need to learn more about
`SQLAlchemy`_. SQLAlchemy is a Python "Object Relational Mapper", meaning that
it can help you write Python programs that interact with a database without
having to write raw database queries (that is often harder to do correctly).
The `querying`_ documentation is particularly useful. Please also see the
:ref:`modules_api` documentation for which tables are available for import and
use. The following examples are laid out in a "cookbook" style. Hopefully there
is something useful in here for you.

The bindings are generated from Calibre version ``2.75.1``.

.. _SQLAlchemy: https://docs.sqlalchemy.org/en/13/
.. _querying: https://docs.sqlalchemy.org/en/13/orm/tutorial.html#querying

Working with the Calibre database
---------------------------------

Calibrestkje works with an existing Calibre database. This means, you need to
install `Calibre`_ first on your system. On a Debian operating system , that
means you would run:

.. _Calibre: https://calibre-ebook.com

.. code-block:: bash

   $ sudo apt install -y calibre

The first time that Calibre is run, the database is created in the
``/home/myusername/calibre/`` folder with the name ``metadata.db``.  If you've
been using Calibre for some time already, then you'll probably already have
this folder and database. All your book catalogue information is stored in this
file.

Sometimes it is useful to start from an empty metadata database and this can be
achieved by creating one with the ``calibredb`` command on the command-line. An
example of this would be:

.. code-block:: bash

   $ mkdir mytestcalibredb
   $ calibredb restore_database --really-do-it --with-library mytestcalibredb

Unfortunately, there is no "create new database command" (AFAIK) and therefore
it is required to run this magical incantation that is hard to remember.
Afterwards, you'll have a new ``mytestcalibredb/metadata.db`` empty database
which you can start to work with.

If you want to run Calibre only using this new library, you can do the
following. Otherwise, Calibre will default to the standard database location.

.. code-block:: bash

   $ calibre --with-library mytestcalibredb

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

List of all tags that contain some pattern
------------------------------------------

.. code-block:: python

    (session.query(Tag)
           .filter(Tag.name.contains("humanities")))

Adding a new tag to a book
--------------------------

.. code-block:: python

    tag = Tag(name='getting radical')

    book = session.query(Book).first()
    book.tags.append(tag)

    session.add(book)
    session.commit()

All books with multiple authors
-------------------------------

.. code-block:: python

    from sqlalchemy.sql.expression import func

    (session.query(Book)
           .join(Book.authors)
           .group_by(Book)
           .having(func.count(Author.id) > 1))
