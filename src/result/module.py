from ..meta import SealedAccord
from .interface import Result
from .ok import Ok
from .err import Err

Result = Result.seal(Ok, Err)