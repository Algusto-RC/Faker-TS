from typing import Optional, Union
import pytest

from generate_stubs import get_signatures_for_func

def func_with_union_return() -> Optional[Union[str, int]]:
    return "42"

def test_get_signatures_handles_optional_union():
    result = get_signatures_for_func(func_with_union_return, "func_with_union_return", locale=None)
    assert isinstance(result, list)
    assert any("func_with_union_return" in sig[0] for sig in result)

def simple_func(x: int) -> str:
    return str(x)

def test_get_signatures_handles_simple_func():
    result = get_signatures_for_func(simple_func, "simple_func", locale=None)
    assert isinstance(result, list)
    assert any("simple_func" in sig[0] for sig in result)

def func_with_forward_ref() -> "MyCustomType":
    pass

def test_get_signatures_handles_forward_ref():
    result = get_signatures_for_func(func_with_forward_ref, "func_with_forward_ref", locale=None)
    assert isinstance(result, list)
    assert any("func_with_forward_ref" in sig[0] for sig in result)



