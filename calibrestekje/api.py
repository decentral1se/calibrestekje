"""User facing API."""

from re import IGNORECASE, compile

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from calibrestekje.bindings import *  # noqa


def title_sort(title):
    """Title sorting SQLAlchemy view function."""
    regex = r"^(A|The|An|Der|Die|Das|Den|Ein|Eine|Einen|Dem|Des|Einem|Eines)\s+"
    title_pat = compile(regex, IGNORECASE)
    match = title_pat.search(title)
    if match:
        prep = match.group(1)
        title = title.replace(prep, "") + ", " + prep
    return title.strip()


def init_session(url: str):
    """Initialise a SQLAlchemy session against a Calibre database."""
    engine = create_engine(url)
    session = Session(engine)
    connection = session.connection()
    connection.connection.create_function("title_sort", 1, title_sort)
    return session
