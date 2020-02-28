.. _limitations:

***********
Limitations
***********

* Only read-only access to the ``metadata.db`` is available file right now.
  There is some more technical work that needs wrangling before it becomes
  possible to programmatically write new entries to a ``metadata.db`` that is
  managed by Calibre.

* It is not possible to extend the Calibre database schema from within the
  context of Calibrestekje right now. This means you can't easily add a new
  column to the Book table. It is however possible to "fork" the Calibre
  database schema and make your own. This involves more work and it is not
  clear if it is possible to stay compatible with the Calibre database schema
  afterwards. This might be useful if you want to start from scratch but not
  re-invent the database schema. See the :ref:`forking` documentation for more.
