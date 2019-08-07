import dill
import pytest

from kq.utils import (
    serialize_fn,
    deserialize_fn
)


def dummy_fn(a, b=2):
    return a+b


@pytest.mark.parametrize(
    "args, kwargs", 
    [
        ([1], {"b": 2}), 
        ([0], {"b": -2}), 
        ([-11], {"b": 20})
    ]
)
def test_serialize_fn(args, kwargs):
    ser_fn = serialize_fn(
        dummy_fn, 
        args,
        kwargs
    )

    assert ser_fn == (
        dill.dumps((dummy_fn, args, kwargs))
    )


@pytest.mark.parametrize(
    "args, kwargs", 
    [
        ([1], {"b": 2}), 
        ([0], {"b": -2}), 
        ([-11], {"b": 20})
    ]
)
def test_deserialize_fn(args, kwargs):
    serialized_fn = dill.dumps((dummy_fn, args, kwargs))
    
    assert (
        deserialize_fn(serialized_fn) 
        == 
        dummy_fn, args, kwargs
    )