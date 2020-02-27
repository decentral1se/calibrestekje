"""SQLAlchemy generated Calibre database bindings."""

from sqlalchemy import (
    TIMESTAMP,
    Boolean,
    CheckConstraint,
    Column,
    Float,
    ForeignKey,
    Integer,
    LargeBinary,
    Table,
    Text,
    UniqueConstraint,
    text,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
metadata = Base.metadata

books_authors_link = Table(
    "books_authors_link",
    Base.metadata,
    Column("book", Integer, ForeignKey("books.id"), primary_key=True),
    Column("author", Integer, ForeignKey("authors.id"), primary_key=True),
)

books_tags_link = Table(
    "books_tags_link",
    Base.metadata,
    Column("book", Integer, ForeignKey("books.id"), primary_key=True),
    Column("tag", Integer, ForeignKey("tags.id"), primary_key=True),
)

books_series_link = Table(
    "books_series_link",
    Base.metadata,
    Column("book", Integer, ForeignKey("books.id"), primary_key=True),
    Column("series", Integer, ForeignKey("series.id"), primary_key=True),
)

books_ratings_link = Table(
    "books_ratings_link",
    Base.metadata,
    Column("book", Integer, ForeignKey("books.id"), primary_key=True),
    Column("rating", Integer, ForeignKey("ratings.id"), primary_key=True),
)

books_languages_link = Table(
    "books_languages_link",
    Base.metadata,
    Column("book", Integer, ForeignKey("books.id"), primary_key=True),
    Column("lang_code", Integer, ForeignKey("languages.id"), primary_key=True),
)


books_publishers_link = Table(
    "books_publishers_link",
    Base.metadata,
    Column("book", Integer, ForeignKey("books.id"), primary_key=True),
    Column("publisher", Integer, ForeignKey("publishers.id"), primary_key=True),
)


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False, unique=True)
    sort = Column(Text)
    link = Column(Text, nullable=False, server_default=text('""'))


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False, server_default=text("'Unknown'"))
    sort = Column(Text)
    timestamp = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
    pubdate = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
    series_index = Column(Float, nullable=False, server_default=text("1.0"))
    author_sort = Column(Text)
    isbn = Column(Text, server_default=text('""'))
    lccn = Column(Text, server_default=text('""'))
    path = Column(Text, nullable=False, server_default=text('""'))
    flags = Column(Integer, nullable=False, server_default=text("1"))
    uuid = Column(Text)
    has_cover = Column(Boolean, server_default=text("0"))
    last_modified = Column(
        TIMESTAMP,
        nullable=False,
        server_default=text('"2000-01-01 00:00:00+00:00"'),
    )
    authors = relationship(
        "Author", secondary=books_authors_link, backref="books"
    )
    tags = relationship(
        "Tag", secondary=books_tags_link, backref="books", order_by="Tag.name"
    )
    comments = relationship("Comment", backref="books")
    data = relationship("Datum", backref="books")
    series = relationship(
        "Series", secondary=books_series_link, backref="books"
    )
    ratings = relationship(
        "Rating", secondary=books_ratings_link, backref="books"
    )
    languages = relationship(
        "Language", secondary=books_languages_link, backref="books"
    )
    publishers = relationship(
        "Publisher", secondary=books_publishers_link, backref="books"
    )
    identifiers = relationship("Identifier", backref="books")


class BooksPluginDatum(Base):
    __tablename__ = "books_plugin_data"
    __table_args__ = (UniqueConstraint("book", "name"),)

    id = Column(Integer, primary_key=True)
    book = Column(Integer, ForeignKey("books.id"), nullable=False)
    name = Column(Text, nullable=False)
    val = Column(Text, nullable=False)


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    book = Column(Integer, ForeignKey("books.id"))
    text = Column(Text, nullable=False)


class ConversionOption(Base):
    __tablename__ = "conversion_options"
    __table_args__ = (UniqueConstraint("format", "book"),)

    id = Column(Integer, primary_key=True)
    format = Column(Text, nullable=False)
    book = Column(Integer, ForeignKey("books.id"))
    data = Column(LargeBinary, ForeignKey("data.id"), nullable=False)


class CustomColumn(Base):
    __tablename__ = "custom_columns"

    id = Column(Integer, primary_key=True)
    label = Column(Text, nullable=False, unique=True)
    name = Column(Text, nullable=False)
    datatype = Column(Text, nullable=False)
    mark_for_delete = Column(Boolean, nullable=False, server_default=text("0"))
    editable = Column(Boolean, nullable=False, server_default=text("1"))
    display = Column(Text, nullable=False, server_default=text('"{}"'))
    is_multiple = Column(Boolean, nullable=False, server_default=text("0"))
    normalized = Column(Boolean, nullable=False)


class Datum(Base):
    __tablename__ = "data"
    __table_args__ = (UniqueConstraint("book", "format"),)

    id = Column(Integer, primary_key=True)
    book = Column(Integer, ForeignKey("books.id"), nullable=False)
    format = Column(Text, nullable=False)
    uncompressed_size = Column(Integer, nullable=False)
    name = Column(Text, nullable=False)


class Feed(Base):
    __tablename__ = "feeds"

    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False, unique=True)
    script = Column(Text, nullable=False)


class Identifier(Base):
    __tablename__ = "identifiers"
    __table_args__ = (UniqueConstraint("book", "type"),)

    id = Column(Integer, primary_key=True)
    book = Column(Integer, ForeignKey("books.id"))
    type = Column(Text, nullable=False, server_default=text('"isbn"'))
    val = Column(Text, nullable=False)


class Language(Base):
    __tablename__ = "languages"

    id = Column(Integer, primary_key=True)
    lang_code = Column(Text, nullable=False, unique=True)


class LibraryId(Base):
    __tablename__ = "library_id"

    id = Column(Integer, primary_key=True)
    uuid = Column(Text, nullable=False, unique=True)


class MetadataDirtied(Base):
    __tablename__ = "metadata_dirtied"

    id = Column(Integer, primary_key=True)
    book = Column(Integer, ForeignKey("books.id"), nullable=False, unique=True)


class Preference(Base):
    __tablename__ = "preferences"

    id = Column(Integer, primary_key=True)
    key = Column(Text, nullable=False, unique=True)
    val = Column(Text, nullable=False)


class Publisher(Base):
    __tablename__ = "publishers"

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False, unique=True)
    sort = Column(Text)


class Rating(Base):
    __tablename__ = "ratings"
    __table_args__ = (CheckConstraint("rating > -1 AND rating < 11"),)

    id = Column(Integer, primary_key=True)
    rating = Column(Integer, unique=True)


class Series(Base):
    __tablename__ = "series"

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False, unique=True)
    sort = Column(Text)


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False, unique=True)
