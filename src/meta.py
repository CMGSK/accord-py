from abc import ABCMeta

class SealedAccord(ABCMeta):
    """
    Prevent arbitrary inheritance from sealed classes. 
    This implementation allows for only specific, pre-registered subclasses to inherit.
    """
    _allow = set()

    def __new__(mcls, name, bases, namespace, /, **kwargs):
        new = super().__new__(mcls, name, bases, namespace, **kwargs)
        for base in bases:
            if isinstance(base, SealedAccord) and getattr(base, '__sealed__', False):
                if new not in base._allow:
                    raise TypeError('You cannot inherit from a sealed class')
        return new

    def seal(cls, *subcls):
        """Registers allowed subclasses and maks the class as sealed"""
        cls.__sealed__ = True
        for sub in subcls:
            cls._allow.add(sub)
        return cls
    