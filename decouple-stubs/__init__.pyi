from configparser import ConfigParser
from io import TextIOWrapper
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Generic,
    Sequence,
    TypeVar,
    overload,
)

if TYPE_CHECKING:
    from sys import _version_info

PYVERSION: _version_info
text_type = str
read_config: Callable[[ConfigParser, TextIOWrapper], None]
DEFAULT_ENCODING: str
TRUE_VALUES: dict[str, str]
FALSE_VALUES: dict[str, str]

def strtobool(value: str | bool) -> bool: ...

class UndefinedValueError(Exception): ...
class Undefined: ...

undefined: Undefined

_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2")

class Config:
    repository: RepositoryEmpty
    def __init__(self, repository: RepositoryEmpty) -> None: ...
    @overload
    def get(
        self,
        option: str,
        cast: Undefined = ...,
        default: Undefined = ...,
    ) -> str: ...
    @overload
    def get(
        self,
        option: str,
        default: _T1,
        cast: Undefined = ...,
    ) -> str | _T1: ...
    @overload
    def get(
        self,
        option: str,
        cast: Callable[..., _T1],
        default: Undefined = ...,
    ) -> _T1: ...
    @overload
    def get(
        self,
        option: str,
        cast: Callable[..., _T1],
        default: _T2 = ...,
    ) -> _T1 | _T2: ...
    @overload
    def __call__(
        self,
        option: str,
        cast: Undefined = ...,
        default: Undefined = ...,
    ) -> str: ...
    @overload
    def __call__(
        self,
        option: str,
        default: _T1,
        cast: Undefined = ...,
    ) -> str | _T1: ...
    @overload
    def __call__(
        self,
        option: str,
        cast: Callable[..., _T1],
        default: Undefined = ...,
    ) -> _T1: ...
    @overload
    def __call__(
        self,
        option: str,
        cast: Callable[..., _T1],
        default: _T2 = ...,
    ) -> _T1 | _T2: ...

class RepositoryEmpty:
    def __init__(self, source: str = ..., encoding=...) -> None: ...
    def __contains__(self, key) -> bool: ...
    def __getitem__(self, key) -> None: ...

class RepositoryIni(RepositoryEmpty):
    SECTION: str
    parser: ConfigParser
    def __init__(self, source: str, encoding: str = ...) -> None: ...
    def __contains__(self, key: str) -> bool: ...
    def __getitem__(self, key: str) -> str: ...

class RepositoryEnv(RepositoryEmpty):
    data: dict[str, str]
    def __init__(self, source: str, encoding: str = ...) -> None: ...
    def __contains__(self, key: str) -> bool: ...
    def __getitem__(self, key: str) -> str: ...

class RepositorySecret(RepositoryEmpty):
    data: dict[str, str]
    def __init__(self, source: str = ...) -> None: ...
    def __contains__(self, key: str) -> bool: ...
    def __getitem__(self, key: str) -> str: ...

class AutoConfig:
    SUPPORTED: dict[str, RepositoryEmpty]
    encoding: str
    search_path: str | None
    config: Config
    def __init__(self, search_path: str | None = ...) -> None: ...
    @overload
    def __call__(
        self,
        option: str,
        cast: Undefined = ...,
        default: Undefined = ...,
    ) -> str: ...
    @overload
    def __call__(
        self,
        option: str,
        default: _T1,
        cast: Undefined = ...,
    ) -> str | _T1: ...
    @overload
    def __call__(
        self,
        option: str,
        cast: Callable[..., _T1],
        default: Undefined = ...,
    ) -> _T1: ...
    @overload
    def __call__(
        self,
        option: str,
        cast: Callable[..., _T1],
        default: _T2 = ...,
    ) -> _T1 | _T2: ...

config: AutoConfig

class Csv(Generic[_T1]):
    cast: Callable[..., _T1]
    delimiter: str
    strip: str
    post_process: Callable[..., Sequence[_T1]]
    @overload
    def __init__(
        self,
        cast: Callable[..., _T1],
        delimiter: str = ...,
        strip: str = ...,
        post_process: Callable[..., Sequence[_T1]] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        cast: Callable[..., str] = ...,
        delimiter: str = ...,
        strip: str = ...,
        post_process: Callable[..., Sequence[str]] = ...,
    ) -> None: ...
    def __call__(self, value: Any | None) -> Sequence[_T1]: ...

class Choices(Generic[_T1]):
    flat: list
    cast: Callable[..., _T1]
    choices: list
    @overload
    def __init__(
        self,
        cast: Callable[..., _T1],
        flat: list | None = ...,
        choices: tuple[str, str] | None = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        flat: list | None = ...,
        cast: Callable[..., str] = ...,
        choices: tuple[str, str] | None = ...,
    ) -> None: ...
    def __call__(self, value: Any) -> _T1: ...
