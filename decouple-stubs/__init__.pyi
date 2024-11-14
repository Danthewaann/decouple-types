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

_T = TypeVar("_T")

class Config:
    repository: RepositoryEmpty
    def __init__(self, repository: RepositoryEmpty) -> None: ...
    @overload
    def get(
        self,
        option: str,
        default: _T,
        cast: Undefined = ...,
    ) -> _T: ...
    @overload
    def get(
        self,
        option: str,
        cast: _T,
        default: Undefined = ...,
    ) -> _T: ...
    @overload
    def get(
        self,
        option: str,
        cast: _T,
        default: _T,
    ) -> _T: ...
    @overload
    def get(
        self,
        option: str,
        default: Undefined = ...,
        cast: Undefined = ...,
    ) -> str: ...
    @overload
    def __call__(
        self,
        option: str,
        default: _T,
        cast: Undefined = ...,
    ) -> _T: ...
    @overload
    def __call__(
        self,
        option: str,
        cast: _T,
        default: Undefined = ...,
    ) -> _T: ...
    @overload
    def __call__(
        self,
        option: str,
        cast: _T,
        default: _T,
    ) -> _T: ...
    @overload
    def __call__(
        self,
        option: str,
        default: Undefined = ...,
        cast: Undefined = ...,
    ) -> str: ...

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
        default: _T | Undefined,
        cast: Callable[..., _T] | Undefined = ...,
    ) -> _T: ...
    @overload
    def __call__(
        self,
        option: str,
        cast: Callable[..., _T] | Undefined,
        default: _T | Undefined = ...,
    ) -> _T: ...
    @overload
    def __call__(
        self,
        option: str,
        cast: Callable[..., _T],
        default: _T,
    ) -> _T: ...
    @overload
    def __call__(
        self,
        option: str,
        cast: Undefined = ...,
        default: Undefined = ...,
    ) -> str: ...

config: AutoConfig

class Csv(Generic[_T]):
    cast: Callable[..., _T]
    delimiter: str
    strip: str
    post_process: Callable[..., Sequence[_T]]
    @overload
    def __init__(
        self,
        cast: Callable[..., _T],
        delimiter: str = ...,
        strip: str = ...,
        post_process: Callable[..., Sequence[_T]] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        cast: Callable[..., str] = ...,
        delimiter: str = ...,
        strip: str = ...,
        post_process: Callable[..., Sequence[str]] = ...,
    ) -> None: ...
    def __call__(self, value: Any | None) -> Sequence[_T]: ...

class Choices(Generic[_T]):
    flat: list
    cast: Callable[..., _T]
    choices: list
    @overload
    def __init__(
        self,
        cast: Callable[..., _T],
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
    def __call__(self, value: Any) -> _T: ...
