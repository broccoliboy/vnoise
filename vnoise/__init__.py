from .vnoise import Noise


def _get_version() -> str:
    from importlib.metadata import version

    return version(__package__ or __name__)


__version__ = _get_version()
