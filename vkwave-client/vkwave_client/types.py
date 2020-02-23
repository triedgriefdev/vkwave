import typing

if typing.TYPE_CHECKING:
    from .context import ResultContext
    from .context import RequestContext

ErrorHandlerCallable = typing.Callable[
    [Exception, "ResultContext"], typing.Awaitable[None]
]

MethodName = typing.NewType("MethodName", str)
RequestCallbackCallable = typing.Callable[[MethodName, dict], typing.Awaitable[dict]]
SignalCallbackCallable = typing.Callable[["RequestContext"], typing.Awaitable[None]]
