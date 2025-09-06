from typing import NoReturn
from .interface import E, F, T, U, Result

class Err(Result[NoReturn, E]):
    """
    Represents a failed operation from a Result returning 
    function containing the value E.

    Success type is NoReturn because an Err cannot (and should not
    be forced to) contain a non-error type.
    """

    def __init__(self, error):
        self._error = error

    def __repr__(self):
        return f'Err({self._error!r})'

    def __eq__(self, o: object):
        if isinstance(o, Err):
            return self._error == o._error
        return False


    def is_ok(self):
        return False

    def is_err(self):
        return True

    def unwrap(self):
        raise self._error

    def expect(self, e):
        raise RuntimeError(f'{e}.\n{self._error!r}')

    def unwrap_err(self):
        return self._error

    def unwrap_or(self, fallback): 
        return fallback

    def map(self, f):
        return self
        
    def map_err(self, f):
        return Err(f(self._error))

    def and_then(self, f):
        return self

    def or_else(self, f):
        return f(self._error)
