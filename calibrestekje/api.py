"""User facing API."""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from calibrestekje.bindings import *  # noqa


def init_session(url: str):
    """Initialise a SQLAlchemy session against a Calibre database."""
    return Session(create_engine(url))
