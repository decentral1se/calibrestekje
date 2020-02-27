"""calibrestekje init module."""

from calibrestekje.api import init_session  # noqa
from calibrestekje.bindings import (  # noqa
    Author,
    Book,
    BooksPluginDatum,
    Comment,
    ConversionOption,
    CustomColumn,
    Datum,
    Feed,
    Identifier,
    Language,
    LibraryId,
    MetadataDirtied,
    Preference,
    Publisher,
    Rating,
    Series,
    Tag,
)

try:
    import pkg_resources
except ImportError:
    pass


try:
    __version__ = pkg_resources.get_distribution("calibrestekje").version
except Exception:
    __version__ = "unknown"
