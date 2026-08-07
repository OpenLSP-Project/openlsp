"""
OpenLSP Core Exception Module

Version: 0.4-alpha

Defines OpenLSP specific exceptions.
"""


class OpenLSPError(Exception):
    """
    Base exception for all OpenLSP errors.
    """

    pass


class InvalidMessageError(OpenLSPError):
    """
    Raised when an OpenLSP message is invalid.
    """

    pass


class InvalidSessionError(OpenLSPError):
    """
    Raised when a session operation is invalid.
    """

    pass
