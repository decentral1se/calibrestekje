"""Command-line entrypoint module."""

from argparse import ArgumentParser

# TODO: https://github.com/agronholm/sqlacodegen


def generate_bindings():
    """Spit out generated SQLAlchemy bindings."""
    pass


def entrypoint(args=None):
    """Command-line entry point."""
    parser = ArgumentParser(description="Calibrestekje command-line interface")
    parser.parse_args()
    generate_bindings()


if __name__ == "__main__":
    entrypoint()
