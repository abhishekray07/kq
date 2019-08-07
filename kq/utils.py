import dill
import inspect

from typing import (
    ByteString,
    Callable,
    Dict,
    List,
)


def serialize_fn(
    fn: Callable, args: List = [], kwargs: Dict = {}
) -> ByteString:
    """Serialize a function with its arguments."""

    if not inspect.isfunction(fn):
        raise TypeError("Expected a function; Received: {fn}")

    if not isinstance(args, list):
        raise TypeError(f"{args} should be a list. {type(args)}")

    if not isinstance(kwargs, dict):
        raise TypeError(f"{kwargs} should be a dict.")

    return dill.dumps((fn, args, kwargs))


def deserialize_fn(serialized_fn: ByteString) -> (Callable, List, Dict):
    """Deserialize a byte string into the function and its arguments."""
    
    fn, args, kwargs = dill.loads(serialized_fn)
    return fn, args, kwargs

